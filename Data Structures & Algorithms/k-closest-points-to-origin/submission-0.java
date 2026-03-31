class DistPoint {
    int distance;
    int[] point;

    public DistPoint(int distance, int[] point) {
        this.distance = distance;
        this.point = point;
    }
}

class DistPointComparator implements Comparator<DistPoint> 
{
    @Override
    // Override the compare method to define custom
    // comparison logic
    public int compare(DistPoint dp1, DistPoint dp2)
    {
        // Compare persons based on their ages
        return dp1.distance - dp2.distance;
    }
}

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] ans = new int[k][2];
        PriorityQueue<DistPoint> pq = new PriorityQueue<>(new DistPointComparator());
        for(int i=0; i<points.length; i++) {
            int[] point = points[i];
            int dist = (point[0]*point[0] + point[1]*point[1]);
            DistPoint dp = new DistPoint(dist, point);
            pq.add(dp);
        }

        for(int i=0; i<k; i++) {
            ans[i] = pq.poll().point;
        }

        return ans;
    }
}
