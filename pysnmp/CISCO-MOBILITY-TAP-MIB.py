# SNMP MIB module (CISCO-MOBILITY-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MOBILITY-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:49 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(cTap2MediationContentId,
 cTap2StreamIndex) = mibBuilder.importSymbols(
    "CISCO-TAP2-MIB",
    "cTap2MediationContentId",
    "cTap2StreamIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMobilityTapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 672)
)
ciscoMobilityTapMIB.setRevisions(
        ("2010-06-16 00:00",
         "2010-04-15 00:00",
         "2008-08-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmtapLawfulInterceptID(OctetString, TextualConvention):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 256),
    )



class CmtapSubscriberIDType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("esn", 5),
          ("imsi", 3),
          ("msid", 2),
          ("nai", 4),
          ("servedMdn", 6),
          ("unknown", 1))
    )



class CmtapSubscriberID(OctetString, TextualConvention):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 256),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMobilityTapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMobilityTapMIBNotifs = _CiscoMobilityTapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 0)
)
_CiscoMobilityTapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMobilityTapMIBObjects = _CiscoMobilityTapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1)
)
_CmtapStreamGroup_ObjectIdentity = ObjectIdentity
cmtapStreamGroup = _CmtapStreamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1)
)


class _CmtapStreamCapabilities_Type(Bits):
    """Custom type cmtapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("calledSubscriberID", 2),
          ("esn", 7),
          ("imsi", 5),
          ("interface", 1),
          ("msid", 4),
          ("nai", 6),
          ("nonvolatileStorage", 3),
          ("servedMdn", 8),
          ("tapEnable", 0))
    )

_CmtapStreamCapabilities_Type.__name__ = "Bits"
_CmtapStreamCapabilities_Object = MibScalar
cmtapStreamCapabilities = _CmtapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 1),
    _CmtapStreamCapabilities_Type()
)
cmtapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmtapStreamCapabilities.setStatus("current")
_CmtapStreamTable_Object = MibTable
cmtapStreamTable = _CmtapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmtapStreamTable.setStatus("current")
_CmtapStreamEntry_Object = MibTableRow
cmtapStreamEntry = _CmtapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1)
)
cmtapStreamEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
    (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"),
)
if mibBuilder.loadTexts:
    cmtapStreamEntry.setStatus("current")


class _CmtapStreamCalledSubscriberIDType_Type(CmtapSubscriberIDType):
    """Custom type cmtapStreamCalledSubscriberIDType based on CmtapSubscriberIDType"""


_CmtapStreamCalledSubscriberIDType_Object = MibTableColumn
cmtapStreamCalledSubscriberIDType = _CmtapStreamCalledSubscriberIDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 1),
    _CmtapStreamCalledSubscriberIDType_Type()
)
cmtapStreamCalledSubscriberIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamCalledSubscriberIDType.setStatus("current")
_CmtapStreamCalledSubscriberID_Type = CmtapSubscriberID
_CmtapStreamCalledSubscriberID_Object = MibTableColumn
cmtapStreamCalledSubscriberID = _CmtapStreamCalledSubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 2),
    _CmtapStreamCalledSubscriberID_Type()
)
cmtapStreamCalledSubscriberID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamCalledSubscriberID.setStatus("current")


class _CmtapStreamSubscriberIDType_Type(CmtapSubscriberIDType):
    """Custom type cmtapStreamSubscriberIDType based on CmtapSubscriberIDType"""


_CmtapStreamSubscriberIDType_Object = MibTableColumn
cmtapStreamSubscriberIDType = _CmtapStreamSubscriberIDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 3),
    _CmtapStreamSubscriberIDType_Type()
)
cmtapStreamSubscriberIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamSubscriberIDType.setStatus("current")
_CmtapStreamSubscriberID_Type = CmtapSubscriberID
_CmtapStreamSubscriberID_Object = MibTableColumn
cmtapStreamSubscriberID = _CmtapStreamSubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 4),
    _CmtapStreamSubscriberID_Type()
)
cmtapStreamSubscriberID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamSubscriberID.setStatus("current")


class _CmtapStreamStorageType_Type(StorageType):
    """Custom type cmtapStreamStorageType based on StorageType"""


_CmtapStreamStorageType_Object = MibTableColumn
cmtapStreamStorageType = _CmtapStreamStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 5),
    _CmtapStreamStorageType_Type()
)
cmtapStreamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamStorageType.setStatus("current")
_CmtapStreamStatus_Type = RowStatus
_CmtapStreamStatus_Object = MibTableColumn
cmtapStreamStatus = _CmtapStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 6),
    _CmtapStreamStatus_Type()
)
cmtapStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamStatus.setStatus("current")


class _CmtapStreamLIIdentifier_Type(CmtapLawfulInterceptID):
    """Custom type cmtapStreamLIIdentifier based on CmtapLawfulInterceptID"""
    defaultValue = OctetString("not set")


_CmtapStreamLIIdentifier_Object = MibTableColumn
cmtapStreamLIIdentifier = _CmtapStreamLIIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 7),
    _CmtapStreamLIIdentifier_Type()
)
cmtapStreamLIIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamLIIdentifier.setStatus("current")


class _CmtapStreamLocationInfo_Type(TruthValue):
    """Custom type cmtapStreamLocationInfo based on TruthValue"""


_CmtapStreamLocationInfo_Object = MibTableColumn
cmtapStreamLocationInfo = _CmtapStreamLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 8),
    _CmtapStreamLocationInfo_Type()
)
cmtapStreamLocationInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamLocationInfo.setStatus("current")


class _CmtapStreamInterceptType_Type(Integer32):
    """Custom type cmtapStreamInterceptType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ccOnly", 1),
          ("iriOnly", 2))
    )


_CmtapStreamInterceptType_Type.__name__ = "Integer32"
_CmtapStreamInterceptType_Object = MibTableColumn
cmtapStreamInterceptType = _CmtapStreamInterceptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 9),
    _CmtapStreamInterceptType_Type()
)
cmtapStreamInterceptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmtapStreamInterceptType.setStatus("current")
_CiscoMobilityTapMIBConform_ObjectIdentity = ObjectIdentity
ciscoMobilityTapMIBConform = _CiscoMobilityTapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2)
)
_CiscoMobilityTapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMobilityTapMIBCompliances = _CiscoMobilityTapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1)
)
_CiscoMobilityTapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMobilityTapMIBGroups = _CiscoMobilityTapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2)
)

# Managed Objects groups

ciscoMobilityTapCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 1)
)
ciscoMobilityTapCapabilityGroup.setObjects(
    ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCapabilities")
)
if mibBuilder.loadTexts:
    ciscoMobilityTapCapabilityGroup.setStatus("current")

ciscoMobilityTapStreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 2)
)
ciscoMobilityTapStreamGroup.setObjects(
      *(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberIDType"),
        ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberID"),
        ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberIDType"),
        ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberID"),
        ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStorageType"),
        ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStatus"))
)
if mibBuilder.loadTexts:
    ciscoMobilityTapStreamGroup.setStatus("current")

ciscoMobilityTapStreamGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 3)
)
ciscoMobilityTapStreamGroupSup1.setObjects(
      *(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLIIdentifier"),
        ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLocationInfo"),
        ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamInterceptType"))
)
if mibBuilder.loadTexts:
    ciscoMobilityTapStreamGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMobilityTapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMobilityTapMIBCompliance.setStatus(
        "deprecated"
    )

ciscoMobilityTapMIBComplianceRev01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoMobilityTapMIBComplianceRev01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MOBILITY-TAP-MIB",
    **{"CmtapLawfulInterceptID": CmtapLawfulInterceptID,
       "CmtapSubscriberIDType": CmtapSubscriberIDType,
       "CmtapSubscriberID": CmtapSubscriberID,
       "ciscoMobilityTapMIB": ciscoMobilityTapMIB,
       "ciscoMobilityTapMIBNotifs": ciscoMobilityTapMIBNotifs,
       "ciscoMobilityTapMIBObjects": ciscoMobilityTapMIBObjects,
       "cmtapStreamGroup": cmtapStreamGroup,
       "cmtapStreamCapabilities": cmtapStreamCapabilities,
       "cmtapStreamTable": cmtapStreamTable,
       "cmtapStreamEntry": cmtapStreamEntry,
       "cmtapStreamCalledSubscriberIDType": cmtapStreamCalledSubscriberIDType,
       "cmtapStreamCalledSubscriberID": cmtapStreamCalledSubscriberID,
       "cmtapStreamSubscriberIDType": cmtapStreamSubscriberIDType,
       "cmtapStreamSubscriberID": cmtapStreamSubscriberID,
       "cmtapStreamStorageType": cmtapStreamStorageType,
       "cmtapStreamStatus": cmtapStreamStatus,
       "cmtapStreamLIIdentifier": cmtapStreamLIIdentifier,
       "cmtapStreamLocationInfo": cmtapStreamLocationInfo,
       "cmtapStreamInterceptType": cmtapStreamInterceptType,
       "ciscoMobilityTapMIBConform": ciscoMobilityTapMIBConform,
       "ciscoMobilityTapMIBCompliances": ciscoMobilityTapMIBCompliances,
       "ciscoMobilityTapMIBCompliance": ciscoMobilityTapMIBCompliance,
       "ciscoMobilityTapMIBComplianceRev01": ciscoMobilityTapMIBComplianceRev01,
       "ciscoMobilityTapMIBGroups": ciscoMobilityTapMIBGroups,
       "ciscoMobilityTapCapabilityGroup": ciscoMobilityTapCapabilityGroup,
       "ciscoMobilityTapStreamGroup": ciscoMobilityTapStreamGroup,
       "ciscoMobilityTapStreamGroupSup1": ciscoMobilityTapStreamGroupSup1}
)
