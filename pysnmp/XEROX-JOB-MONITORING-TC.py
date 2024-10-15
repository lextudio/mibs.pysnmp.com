# SNMP MIB module (XEROX-JOB-MONITORING-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-JOB-MONITORING-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:26 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmJobMonTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmJMJobServiceTypeOID(ObjectIdentifier, TextualConvention):
    status = "current"


class XcmJMJobState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              11,
              12,
              13,
              14,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("completed", 17),
          ("created", 3),
          ("held", 12),
          ("interrupted", 8),
          ("other", 1),
          ("paused", 13),
          ("pending", 6),
          ("printing", 18),
          ("processing", 7),
          ("retained", 11),
          ("terminating", 14),
          ("unknown", 2))
    )



class XcmJMJobStateReasons(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmJMJobXStateReasons(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmJMJobX2StateReasons(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmJMDocType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("font", 4),
          ("other", 1),
          ("printable", 3),
          ("resource", 5),
          ("unknown", 2))
    )



class XcmJMDocFileNameType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("fntAutomatic", 3),
          ("fntBindery", 13),
          ("fntCDS", 7),
          ("fntDCE", 6),
          ("fntDECNS", 10),
          ("fntDNS", 9),
          ("fntInternetMail", 11),
          ("fntMVS", 28),
          ("fntNDS", 14),
          ("fntNIS", 8),
          ("fntNT", 27),
          ("fntNetWare", 33),
          ("fntOS2", 25),
          ("fntOS400", 30),
          ("fntPCDOS", 26),
          ("fntPOSIX", 23),
          ("fntUNC", 32),
          ("fntUNIX", 24),
          ("fntURL", 15),
          ("fntVM", 29),
          ("fntVMS", 31),
          ("fntX500", 4),
          ("fntXFN", 5),
          ("fntXNS", 12),
          ("other", 1),
          ("unknown", 2))
    )



class XcmJMDocState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("completed", 6),
          ("other", 1),
          ("pending", 4),
          ("printing", 7),
          ("processing", 5),
          ("transferPending", 3),
          ("unknown", 2))
    )



class XcmJMDocOutputMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class XcmJMGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmJMImpsCountType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              11,
              19,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("blackAndWhiteCount", 5),
          ("fourColorantCount", 24),
          ("fullColorCount", 7),
          ("highlightColorCount", 6),
          ("limitedVisibleColorCount", 19),
          ("oneColorantCount", 21),
          ("oneVisibleColorCount", 11),
          ("other", 1),
          ("threeColorantCount", 23),
          ("totalCount", 4),
          ("twoColorantCount", 22))
    )



class XcmJMMediumType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("coated", 101),
          ("continuousLong", 7),
          ("continuousShort", 8),
          ("coverStock", 16),
          ("drilled", 100),
          ("envelope", 5),
          ("envelopePlain", 6),
          ("envelopeWindow", 12),
          ("heavyWeight", 103),
          ("labels", 11),
          ("letterhead", 15),
          ("multiLayer", 13),
          ("multiPartForm", 10),
          ("other", 1),
          ("prePrinted", 14),
          ("recycled", 102),
          ("stationery", 3),
          ("tabStock", 9),
          ("transparency", 4),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_XcmJobServiceTypesOID_ObjectIdentity = ObjectIdentity
xcmJobServiceTypesOID = _XcmJobServiceTypesOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2)
)
if mibBuilder.loadTexts:
    xcmJobServiceTypesOID.setStatus("current")
_XcmJobServiceScanToFileOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToFileOID = _XcmJobServiceScanToFileOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 1)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToFileOID.setStatus("current")
_XcmJobServiceScanToPrintOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToPrintOID = _XcmJobServiceScanToPrintOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 2)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToPrintOID.setStatus("current")
_XcmJobServiceScanToFaxOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToFaxOID = _XcmJobServiceScanToFaxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 3)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToFaxOID.setStatus("current")
_XcmJobServiceScanToMailListOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToMailListOID = _XcmJobServiceScanToMailListOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 4)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToMailListOID.setStatus("current")
_XcmJobServiceFaxToFileOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFaxToFileOID = _XcmJobServiceFaxToFileOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 5)
)
if mibBuilder.loadTexts:
    xcmJobServiceFaxToFileOID.setStatus("current")
_XcmJobServiceFaxToPrintOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFaxToPrintOID = _XcmJobServiceFaxToPrintOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 6)
)
if mibBuilder.loadTexts:
    xcmJobServiceFaxToPrintOID.setStatus("current")
_XcmJobServiceFaxToMailListOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFaxToMailListOID = _XcmJobServiceFaxToMailListOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 7)
)
if mibBuilder.loadTexts:
    xcmJobServiceFaxToMailListOID.setStatus("current")
_XcmJobServicePrintOID_ObjectIdentity = ObjectIdentity
xcmJobServicePrintOID = _XcmJobServicePrintOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 8)
)
if mibBuilder.loadTexts:
    xcmJobServicePrintOID.setStatus("current")
_XcmJobServiceFileToFaxOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFileToFaxOID = _XcmJobServiceFileToFaxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 9)
)
if mibBuilder.loadTexts:
    xcmJobServiceFileToFaxOID.setStatus("current")
_XcmJobServiceFileToMailListOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFileToMailListOID = _XcmJobServiceFileToMailListOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 10)
)
if mibBuilder.loadTexts:
    xcmJobServiceFileToMailListOID.setStatus("current")
_XcmJobServiceCopyOID_ObjectIdentity = ObjectIdentity
xcmJobServiceCopyOID = _XcmJobServiceCopyOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 11)
)
if mibBuilder.loadTexts:
    xcmJobServiceCopyOID.setStatus("current")
_XcmJobServiceFileToFileOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFileToFileOID = _XcmJobServiceFileToFileOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 12)
)
if mibBuilder.loadTexts:
    xcmJobServiceFileToFileOID.setStatus("current")
_XCmJobMonTCDummy_ObjectIdentity = ObjectIdentity
xCmJobMonTCDummy = _XCmJobMonTCDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999)
)
_XCmJobMonTCJobServiceTypeOID_Type = XcmJMJobServiceTypeOID
_XCmJobMonTCJobServiceTypeOID_Object = MibScalar
xCmJobMonTCJobServiceTypeOID = _XCmJobMonTCJobServiceTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 1),
    _XCmJobMonTCJobServiceTypeOID_Type()
)
xCmJobMonTCJobServiceTypeOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobServiceTypeOID.setStatus("current")
_XCmJobMonTCJobState_Type = XcmJMJobState
_XCmJobMonTCJobState_Object = MibScalar
xCmJobMonTCJobState = _XCmJobMonTCJobState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 2),
    _XCmJobMonTCJobState_Type()
)
xCmJobMonTCJobState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobState.setStatus("current")
_XCmJobMonTCJobStateReasons_Type = XcmJMJobStateReasons
_XCmJobMonTCJobStateReasons_Object = MibScalar
xCmJobMonTCJobStateReasons = _XCmJobMonTCJobStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 3),
    _XCmJobMonTCJobStateReasons_Type()
)
xCmJobMonTCJobStateReasons.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobStateReasons.setStatus("current")
_XCmJobMonTCJobXStateReasons_Type = XcmJMJobXStateReasons
_XCmJobMonTCJobXStateReasons_Object = MibScalar
xCmJobMonTCJobXStateReasons = _XCmJobMonTCJobXStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 4),
    _XCmJobMonTCJobXStateReasons_Type()
)
xCmJobMonTCJobXStateReasons.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobXStateReasons.setStatus("current")
_XCmJobMonTCJobX2StateReasons_Type = XcmJMJobX2StateReasons
_XCmJobMonTCJobX2StateReasons_Object = MibScalar
xCmJobMonTCJobX2StateReasons = _XCmJobMonTCJobX2StateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 5),
    _XCmJobMonTCJobX2StateReasons_Type()
)
xCmJobMonTCJobX2StateReasons.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobX2StateReasons.setStatus("current")
_XCmJobMonTCDocType_Type = XcmJMDocType
_XCmJobMonTCDocType_Object = MibScalar
xCmJobMonTCDocType = _XCmJobMonTCDocType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 6),
    _XCmJobMonTCDocType_Type()
)
xCmJobMonTCDocType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocType.setStatus("current")
_XCmJobMonTCDocFileNameType_Type = XcmJMDocFileNameType
_XCmJobMonTCDocFileNameType_Object = MibScalar
xCmJobMonTCDocFileNameType = _XCmJobMonTCDocFileNameType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 7),
    _XCmJobMonTCDocFileNameType_Type()
)
xCmJobMonTCDocFileNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocFileNameType.setStatus("current")
_XCmJobMonTCDocState_Type = XcmJMDocState
_XCmJobMonTCDocState_Object = MibScalar
xCmJobMonTCDocState = _XCmJobMonTCDocState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 8),
    _XCmJobMonTCDocState_Type()
)
xCmJobMonTCDocState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocState.setStatus("current")
_XCmJobMonTCDocOutputMethod_Type = XcmJMDocOutputMethod
_XCmJobMonTCDocOutputMethod_Object = MibScalar
xCmJobMonTCDocOutputMethod = _XCmJobMonTCDocOutputMethod_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 9),
    _XCmJobMonTCDocOutputMethod_Type()
)
xCmJobMonTCDocOutputMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocOutputMethod.setStatus("current")
_XCmJobMonTCGroupSupport_Type = XcmJMGroupSupport
_XCmJobMonTCGroupSupport_Object = MibScalar
xCmJobMonTCGroupSupport = _XCmJobMonTCGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 10),
    _XCmJobMonTCGroupSupport_Type()
)
xCmJobMonTCGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCGroupSupport.setStatus("current")
_XCmJobMonTCImpsCountType_Type = XcmJMImpsCountType
_XCmJobMonTCImpsCountType_Object = MibScalar
xCmJobMonTCImpsCountType = _XCmJobMonTCImpsCountType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 11),
    _XCmJobMonTCImpsCountType_Type()
)
xCmJobMonTCImpsCountType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCImpsCountType.setStatus("current")
_XCmJobMonTCMediumType_Type = XcmJMMediumType
_XCmJobMonTCMediumType_Object = MibScalar
xCmJobMonTCMediumType = _XCmJobMonTCMediumType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 12),
    _XCmJobMonTCMediumType_Type()
)
xCmJobMonTCMediumType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCMediumType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-JOB-MONITORING-TC",
    **{"XcmJMJobServiceTypeOID": XcmJMJobServiceTypeOID,
       "XcmJMJobState": XcmJMJobState,
       "XcmJMJobStateReasons": XcmJMJobStateReasons,
       "XcmJMJobXStateReasons": XcmJMJobXStateReasons,
       "XcmJMJobX2StateReasons": XcmJMJobX2StateReasons,
       "XcmJMDocType": XcmJMDocType,
       "XcmJMDocFileNameType": XcmJMDocFileNameType,
       "XcmJMDocState": XcmJMDocState,
       "XcmJMDocOutputMethod": XcmJMDocOutputMethod,
       "XcmJMGroupSupport": XcmJMGroupSupport,
       "XcmJMImpsCountType": XcmJMImpsCountType,
       "XcmJMMediumType": XcmJMMediumType,
       "xcmJobMonTC": xcmJobMonTC,
       "xcmJobServiceTypesOID": xcmJobServiceTypesOID,
       "xcmJobServiceScanToFileOID": xcmJobServiceScanToFileOID,
       "xcmJobServiceScanToPrintOID": xcmJobServiceScanToPrintOID,
       "xcmJobServiceScanToFaxOID": xcmJobServiceScanToFaxOID,
       "xcmJobServiceScanToMailListOID": xcmJobServiceScanToMailListOID,
       "xcmJobServiceFaxToFileOID": xcmJobServiceFaxToFileOID,
       "xcmJobServiceFaxToPrintOID": xcmJobServiceFaxToPrintOID,
       "xcmJobServiceFaxToMailListOID": xcmJobServiceFaxToMailListOID,
       "xcmJobServicePrintOID": xcmJobServicePrintOID,
       "xcmJobServiceFileToFaxOID": xcmJobServiceFileToFaxOID,
       "xcmJobServiceFileToMailListOID": xcmJobServiceFileToMailListOID,
       "xcmJobServiceCopyOID": xcmJobServiceCopyOID,
       "xcmJobServiceFileToFileOID": xcmJobServiceFileToFileOID,
       "xCmJobMonTCDummy": xCmJobMonTCDummy,
       "xCmJobMonTCJobServiceTypeOID": xCmJobMonTCJobServiceTypeOID,
       "xCmJobMonTCJobState": xCmJobMonTCJobState,
       "xCmJobMonTCJobStateReasons": xCmJobMonTCJobStateReasons,
       "xCmJobMonTCJobXStateReasons": xCmJobMonTCJobXStateReasons,
       "xCmJobMonTCJobX2StateReasons": xCmJobMonTCJobX2StateReasons,
       "xCmJobMonTCDocType": xCmJobMonTCDocType,
       "xCmJobMonTCDocFileNameType": xCmJobMonTCDocFileNameType,
       "xCmJobMonTCDocState": xCmJobMonTCDocState,
       "xCmJobMonTCDocOutputMethod": xCmJobMonTCDocOutputMethod,
       "xCmJobMonTCGroupSupport": xCmJobMonTCGroupSupport,
       "xCmJobMonTCImpsCountType": xCmJobMonTCImpsCountType,
       "xCmJobMonTCMediumType": xCmJobMonTCMediumType}
)
