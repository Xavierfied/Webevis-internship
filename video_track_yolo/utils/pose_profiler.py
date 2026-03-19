# import cv2 as cv
#
def draw_pose(self, frame, result):
    ...
#     if result.keypoints is None:
#         return frame
#
#     # loop over each detected person
#     for i, kps in enumerate(result.keypoints.xy):
#         # kps is shape (17, 2) — 17 keypoints, each with x and y
#         conf_scores = result.keypoints.conf[i]   # confidence per keypoint
#
#         # ── draw skeleton lines ─────────────────────────────────────
#         for j, (a, b) in enumerate(SKELETON):
#             # only draw if both keypoints were actually detected
#             if conf_scores[a] > 0.5 and conf_scores[b] > 0.5:
#                 x1, y1 = int(kps[a][0]), int(kps[a][1])
#                 x2, y2 = int(kps[b][0]), int(kps[b][1])
#
#                 cv.line(frame, (x1, y1), (x2, y2), SKELETON_COLORS[j], 2)