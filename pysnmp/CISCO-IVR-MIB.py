# SNMP MIB module (CISCO-IVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IVR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:41 2024
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

(DomainId,
 FcAddressId,
 FcNameId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainId",
    "FcAddressId",
    "FcNameId",
    "VsanIndex")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(FcList,
 ZoneQosPriorityLevel) = mibBuilder.importSymbols(
    "CISCO-ZS-MIB",
    "FcList",
    "ZoneQosPriorityLevel")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371)
)
ciscoIvrMIB.setRevisions(
        ("2005-03-03 00:00",
         "2004-10-27 00:00",
         "2003-11-03 00:00",
         "2003-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CIvrZoneMemberType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("pwwnVsan", 1)
    )



class CIvrAutonomousFabricId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CIvrChecksum(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIvrMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoIvrMIBNotifications = _CiscoIvrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 0)
)
_CiscoIvrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIvrMIBObjects = _CiscoIvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1)
)
_CimIvrConfiguration_ObjectIdentity = ObjectIdentity
cimIvrConfiguration = _CimIvrConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1)
)
_CimIvrGeneric_ObjectIdentity = ObjectIdentity
cimIvrGeneric = _CimIvrGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 1)
)
_CivrFcidNatMode_Type = TruthValue
_CivrFcidNatMode_Object = MibScalar
civrFcidNatMode = _CivrFcidNatMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 1, 1),
    _CivrFcidNatMode_Type()
)
civrFcidNatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrFcidNatMode.setStatus("current")
_CivrVsanTopologyAutoDisc_Type = TruthValue
_CivrVsanTopologyAutoDisc_Object = MibScalar
civrVsanTopologyAutoDisc = _CivrVsanTopologyAutoDisc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 1, 2),
    _CivrVsanTopologyAutoDisc_Type()
)
civrVsanTopologyAutoDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrVsanTopologyAutoDisc.setStatus("current")
_CimIvrZoneset_ObjectIdentity = ObjectIdentity
cimIvrZoneset = _CimIvrZoneset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2)
)


class _CivrZoneSetNumber_Type(Integer32):
    """Custom type civrZoneSetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_CivrZoneSetNumber_Type.__name__ = "Integer32"
_CivrZoneSetNumber_Object = MibScalar
civrZoneSetNumber = _CivrZoneSetNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 1),
    _CivrZoneSetNumber_Type()
)
civrZoneSetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneSetNumber.setStatus("current")
_CivrZoneSetTable_Object = MibTable
civrZoneSetTable = _CivrZoneSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    civrZoneSetTable.setStatus("current")
_CivrZoneSetEntry_Object = MibTableRow
civrZoneSetEntry = _CivrZoneSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2, 1)
)
civrZoneSetEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrZoneSetIndex"),
)
if mibBuilder.loadTexts:
    civrZoneSetEntry.setStatus("current")


class _CivrZoneSetIndex_Type(Unsigned32):
    """Custom type civrZoneSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CivrZoneSetIndex_Type.__name__ = "Unsigned32"
_CivrZoneSetIndex_Object = MibTableColumn
civrZoneSetIndex = _CivrZoneSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2, 1, 1),
    _CivrZoneSetIndex_Type()
)
civrZoneSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrZoneSetIndex.setStatus("current")


class _CivrZoneSetName_Type(SnmpAdminString):
    """Custom type civrZoneSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CivrZoneSetName_Type.__name__ = "SnmpAdminString"
_CivrZoneSetName_Object = MibTableColumn
civrZoneSetName = _CivrZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2, 1, 2),
    _CivrZoneSetName_Type()
)
civrZoneSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneSetName.setStatus("current")


class _CivrZoneSetZoneList_Type(FcList):
    """Custom type civrZoneSetZoneList based on FcList"""
    defaultHexValue = ""


_CivrZoneSetZoneList_Object = MibTableColumn
civrZoneSetZoneList = _CivrZoneSetZoneList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2, 1, 3),
    _CivrZoneSetZoneList_Type()
)
civrZoneSetZoneList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneSetZoneList.setStatus("current")
_CivrZoneSetLastChange_Type = TimeStamp
_CivrZoneSetLastChange_Object = MibTableColumn
civrZoneSetLastChange = _CivrZoneSetLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2, 1, 4),
    _CivrZoneSetLastChange_Type()
)
civrZoneSetLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneSetLastChange.setStatus("current")
_CivrZoneSetChecksum_Type = CIvrChecksum
_CivrZoneSetChecksum_Object = MibTableColumn
civrZoneSetChecksum = _CivrZoneSetChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2, 1, 5),
    _CivrZoneSetChecksum_Type()
)
civrZoneSetChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneSetChecksum.setStatus("current")
_CivrZoneSetRowStatus_Type = RowStatus
_CivrZoneSetRowStatus_Object = MibTableColumn
civrZoneSetRowStatus = _CivrZoneSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 2, 1, 6),
    _CivrZoneSetRowStatus_Type()
)
civrZoneSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneSetRowStatus.setStatus("current")


class _CivrZoneSetActivate_Type(Unsigned32):
    """Custom type civrZoneSetActivate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CivrZoneSetActivate_Type.__name__ = "Unsigned32"
_CivrZoneSetActivate_Object = MibScalar
civrZoneSetActivate = _CivrZoneSetActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 3),
    _CivrZoneSetActivate_Type()
)
civrZoneSetActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrZoneSetActivate.setStatus("current")


class _CivrZoneSetActvatDeactvatResult_Type(Integer32):
    """Custom type civrZoneSetActvatDeactvatResult based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("activateFailureFabric", 17),
          ("activateFailureFabricUnstable", 8),
          ("activateFailureNoMembers", 2),
          ("activateFailureNoPerVsanSucc", 5),
          ("activateFailureNoTopology", 4),
          ("activateFailureNoVsans", 7),
          ("activateFailureNoZoneset", 6),
          ("activateFailureZoneOneorLessMem", 3),
          ("activatePartialSuccessFabric", 19),
          ("activateSuccess", 1),
          ("activating", 13),
          ("activatingAdvertising", 23),
          ("activatingReadyToAdv", 22),
          ("deactivateFailureFabric", 18),
          ("deactivateFailureFabricUnstable", 12),
          ("deactivateFailureNoActiveZs", 10),
          ("deactivateFailureNoPerVsanSucc", 11),
          ("deactivatePartialSuccessFabric", 20),
          ("deactivateSuccess", 9),
          ("deactivateSuccessFcNatShutup13", 16),
          ("deactivating", 14),
          ("deviceCleanupInProgress", 21),
          ("idle", 15))
    )


_CivrZoneSetActvatDeactvatResult_Type.__name__ = "Integer32"
_CivrZoneSetActvatDeactvatResult_Object = MibScalar
civrZoneSetActvatDeactvatResult = _CivrZoneSetActvatDeactvatResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 4),
    _CivrZoneSetActvatDeactvatResult_Type()
)
civrZoneSetActvatDeactvatResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneSetActvatDeactvatResult.setStatus("current")


class _CivrZoneSetDeActivate_Type(Integer32):
    """Custom type civrZoneSetDeActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deactivate", 1),
          ("noop", 2))
    )


_CivrZoneSetDeActivate_Type.__name__ = "Integer32"
_CivrZoneSetDeActivate_Object = MibScalar
civrZoneSetDeActivate = _CivrZoneSetDeActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 5),
    _CivrZoneSetDeActivate_Type()
)
civrZoneSetDeActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrZoneSetDeActivate.setStatus("current")
_CivrZonesetDbChecksum_Type = CIvrChecksum
_CivrZonesetDbChecksum_Object = MibScalar
civrZonesetDbChecksum = _CivrZonesetDbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 6),
    _CivrZonesetDbChecksum_Type()
)
civrZonesetDbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZonesetDbChecksum.setStatus("current")
_CivrActiveZonesetChecksum_Type = CIvrChecksum
_CivrActiveZonesetChecksum_Object = MibScalar
civrActiveZonesetChecksum = _CivrActiveZonesetChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 7),
    _CivrActiveZonesetChecksum_Type()
)
civrActiveZonesetChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrActiveZonesetChecksum.setStatus("current")


class _CivrZoneEnforcedZoneSetName_Type(SnmpAdminString):
    """Custom type civrZoneEnforcedZoneSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CivrZoneEnforcedZoneSetName_Type.__name__ = "SnmpAdminString"
_CivrZoneEnforcedZoneSetName_Object = MibScalar
civrZoneEnforcedZoneSetName = _CivrZoneEnforcedZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 8),
    _CivrZoneEnforcedZoneSetName_Type()
)
civrZoneEnforcedZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneSetName.setStatus("current")
_CivrZoneEnforcedZoneSetZoneList_Type = FcList
_CivrZoneEnforcedZoneSetZoneList_Object = MibScalar
civrZoneEnforcedZoneSetZoneList = _CivrZoneEnforcedZoneSetZoneList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 9),
    _CivrZoneEnforcedZoneSetZoneList_Type()
)
civrZoneEnforcedZoneSetZoneList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneSetZoneList.setStatus("current")
_CivrZoneEnforcedZoneSetActvtTime_Type = TimeStamp
_CivrZoneEnforcedZoneSetActvtTime_Object = MibScalar
civrZoneEnforcedZoneSetActvtTime = _CivrZoneEnforcedZoneSetActvtTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 10),
    _CivrZoneEnforcedZoneSetActvtTime_Type()
)
civrZoneEnforcedZoneSetActvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneSetActvtTime.setStatus("current")


class _CivrZoneCopyZoneSetEnforcdToFull_Type(Integer32):
    """Custom type civrZoneCopyZoneSetEnforcdToFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("noOp", 2))
    )


_CivrZoneCopyZoneSetEnforcdToFull_Type.__name__ = "Integer32"
_CivrZoneCopyZoneSetEnforcdToFull_Object = MibScalar
civrZoneCopyZoneSetEnforcdToFull = _CivrZoneCopyZoneSetEnforcdToFull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 11),
    _CivrZoneCopyZoneSetEnforcdToFull_Type()
)
civrZoneCopyZoneSetEnforcdToFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrZoneCopyZoneSetEnforcdToFull.setStatus("current")


class _CivrZoneClearFullZoneDb_Type(Integer32):
    """Custom type civrZoneClearFullZoneDb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_CivrZoneClearFullZoneDb_Type.__name__ = "Integer32"
_CivrZoneClearFullZoneDb_Object = MibScalar
civrZoneClearFullZoneDb = _CivrZoneClearFullZoneDb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 12),
    _CivrZoneClearFullZoneDb_Type()
)
civrZoneClearFullZoneDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrZoneClearFullZoneDb.setStatus("current")
_CivrZonesetActivateForce_Type = TruthValue
_CivrZonesetActivateForce_Object = MibScalar
civrZonesetActivateForce = _CivrZonesetActivateForce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 13),
    _CivrZonesetActivateForce_Type()
)
civrZonesetActivateForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrZonesetActivateForce.setStatus("current")
_CivrZoneSetTableNextIndex_Type = Unsigned32
_CivrZoneSetTableNextIndex_Object = MibScalar
civrZoneSetTableNextIndex = _CivrZoneSetTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 2, 14),
    _CivrZoneSetTableNextIndex_Type()
)
civrZoneSetTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneSetTableNextIndex.setStatus("current")
_CimIvrZone_ObjectIdentity = ObjectIdentity
cimIvrZone = _CimIvrZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3)
)


class _CivrZoneNumber_Type(Integer32):
    """Custom type civrZoneNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CivrZoneNumber_Type.__name__ = "Integer32"
_CivrZoneNumber_Object = MibScalar
civrZoneNumber = _CivrZoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 1),
    _CivrZoneNumber_Type()
)
civrZoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneNumber.setStatus("current")
_CivrZoneTable_Object = MibTable
civrZoneTable = _CivrZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    civrZoneTable.setStatus("current")
_CivrZoneEntry_Object = MibTableRow
civrZoneEntry = _CivrZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1)
)
civrZoneEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrZoneIndex"),
)
if mibBuilder.loadTexts:
    civrZoneEntry.setStatus("current")


class _CivrZoneIndex_Type(Unsigned32):
    """Custom type civrZoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CivrZoneIndex_Type.__name__ = "Unsigned32"
_CivrZoneIndex_Object = MibTableColumn
civrZoneIndex = _CivrZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1, 1),
    _CivrZoneIndex_Type()
)
civrZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrZoneIndex.setStatus("current")


class _CivrZoneName_Type(SnmpAdminString):
    """Custom type civrZoneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 58),
    )


_CivrZoneName_Type.__name__ = "SnmpAdminString"
_CivrZoneName_Object = MibTableColumn
civrZoneName = _CivrZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1, 2),
    _CivrZoneName_Type()
)
civrZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneName.setStatus("current")


class _CivrZoneMemberList_Type(FcList):
    """Custom type civrZoneMemberList based on FcList"""
    defaultHexValue = ""


_CivrZoneMemberList_Object = MibTableColumn
civrZoneMemberList = _CivrZoneMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1, 3),
    _CivrZoneMemberList_Type()
)
civrZoneMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneMemberList.setStatus("current")
_CivrZoneLastChange_Type = TimeStamp
_CivrZoneLastChange_Object = MibTableColumn
civrZoneLastChange = _CivrZoneLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1, 5),
    _CivrZoneLastChange_Type()
)
civrZoneLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneLastChange.setStatus("current")
_CivrZoneRowStatus_Type = RowStatus
_CivrZoneRowStatus_Object = MibTableColumn
civrZoneRowStatus = _CivrZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1, 6),
    _CivrZoneRowStatus_Type()
)
civrZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneRowStatus.setStatus("current")
_CivrZoneReadOnly_Type = TruthValue
_CivrZoneReadOnly_Object = MibTableColumn
civrZoneReadOnly = _CivrZoneReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1, 7),
    _CivrZoneReadOnly_Type()
)
civrZoneReadOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneReadOnly.setStatus("current")
_CivrZoneQosPriority_Type = ZoneQosPriorityLevel
_CivrZoneQosPriority_Object = MibTableColumn
civrZoneQosPriority = _CivrZoneQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 2, 1, 8),
    _CivrZoneQosPriority_Type()
)
civrZoneQosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneQosPriority.setStatus("current")


class _CivrZoneEnforcedZoneNumber_Type(Integer32):
    """Custom type civrZoneEnforcedZoneNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_CivrZoneEnforcedZoneNumber_Type.__name__ = "Integer32"
_CivrZoneEnforcedZoneNumber_Object = MibScalar
civrZoneEnforcedZoneNumber = _CivrZoneEnforcedZoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 3),
    _CivrZoneEnforcedZoneNumber_Type()
)
civrZoneEnforcedZoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneNumber.setStatus("current")
_CivrZoneEnforcedZoneTable_Object = MibTable
civrZoneEnforcedZoneTable = _CivrZoneEnforcedZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneTable.setStatus("current")
_CivrZoneEnforcedZoneEntry_Object = MibTableRow
civrZoneEnforcedZoneEntry = _CivrZoneEnforcedZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 4, 1)
)
civrZoneEnforcedZoneEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrZoneIndex"),
)
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneEntry.setStatus("current")


class _CivrZoneEnforcedZoneName_Type(SnmpAdminString):
    """Custom type civrZoneEnforcedZoneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 58),
    )


_CivrZoneEnforcedZoneName_Type.__name__ = "SnmpAdminString"
_CivrZoneEnforcedZoneName_Object = MibTableColumn
civrZoneEnforcedZoneName = _CivrZoneEnforcedZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 4, 1, 1),
    _CivrZoneEnforcedZoneName_Type()
)
civrZoneEnforcedZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneName.setStatus("current")
_CivrZoneEnforcedZoneMemberList_Type = FcList
_CivrZoneEnforcedZoneMemberList_Object = MibTableColumn
civrZoneEnforcedZoneMemberList = _CivrZoneEnforcedZoneMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 4, 1, 2),
    _CivrZoneEnforcedZoneMemberList_Type()
)
civrZoneEnforcedZoneMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberList.setStatus("current")
_CivrZoneEnforcedZoneReadOnly_Type = TruthValue
_CivrZoneEnforcedZoneReadOnly_Object = MibTableColumn
civrZoneEnforcedZoneReadOnly = _CivrZoneEnforcedZoneReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 4, 1, 3),
    _CivrZoneEnforcedZoneReadOnly_Type()
)
civrZoneEnforcedZoneReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneReadOnly.setStatus("current")
_CivrZoneEnforcedZoneQosPriority_Type = ZoneQosPriorityLevel
_CivrZoneEnforcedZoneQosPriority_Object = MibTableColumn
civrZoneEnforcedZoneQosPriority = _CivrZoneEnforcedZoneQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 4, 1, 4),
    _CivrZoneEnforcedZoneQosPriority_Type()
)
civrZoneEnforcedZoneQosPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneQosPriority.setStatus("current")
_CivrZoneTableNextIndex_Type = Unsigned32
_CivrZoneTableNextIndex_Object = MibScalar
civrZoneTableNextIndex = _CivrZoneTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 3, 5),
    _CivrZoneTableNextIndex_Type()
)
civrZoneTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneTableNextIndex.setStatus("current")
_CimIvrZoneMember_ObjectIdentity = ObjectIdentity
cimIvrZoneMember = _CimIvrZoneMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4)
)


class _CivrZoneMemberNumber_Type(Integer32):
    """Custom type civrZoneMemberNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_CivrZoneMemberNumber_Type.__name__ = "Integer32"
_CivrZoneMemberNumber_Object = MibScalar
civrZoneMemberNumber = _CivrZoneMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 1),
    _CivrZoneMemberNumber_Type()
)
civrZoneMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneMemberNumber.setStatus("current")
_CivrZoneMemberTable_Object = MibTable
civrZoneMemberTable = _CivrZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    civrZoneMemberTable.setStatus("current")
_CivrZoneMemberEntry_Object = MibTableRow
civrZoneMemberEntry = _CivrZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1)
)
civrZoneMemberEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrZoneMemberParentIndex"),
    (0, "CISCO-IVR-MIB", "civrZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    civrZoneMemberEntry.setStatus("current")


class _CivrZoneMemberParentIndex_Type(Unsigned32):
    """Custom type civrZoneMemberParentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CivrZoneMemberParentIndex_Type.__name__ = "Unsigned32"
_CivrZoneMemberParentIndex_Object = MibTableColumn
civrZoneMemberParentIndex = _CivrZoneMemberParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 1),
    _CivrZoneMemberParentIndex_Type()
)
civrZoneMemberParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrZoneMemberParentIndex.setStatus("current")


class _CivrZoneMemberIndex_Type(Unsigned32):
    """Custom type civrZoneMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CivrZoneMemberIndex_Type.__name__ = "Unsigned32"
_CivrZoneMemberIndex_Object = MibTableColumn
civrZoneMemberIndex = _CivrZoneMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 2),
    _CivrZoneMemberIndex_Type()
)
civrZoneMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrZoneMemberIndex.setStatus("current")
_CivrZoneMemberType_Type = CIvrZoneMemberType
_CivrZoneMemberType_Object = MibTableColumn
civrZoneMemberType = _CivrZoneMemberType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 3),
    _CivrZoneMemberType_Type()
)
civrZoneMemberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneMemberType.setStatus("current")
_CivrZoneMemberID_Type = OctetString
_CivrZoneMemberID_Object = MibTableColumn
civrZoneMemberID = _CivrZoneMemberID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 4),
    _CivrZoneMemberID_Type()
)
civrZoneMemberID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneMemberID.setStatus("current")


class _CivrZoneMemberAFId_Type(CIvrAutonomousFabricId):
    """Custom type civrZoneMemberAFId based on CIvrAutonomousFabricId"""
    defaultValue = 1


_CivrZoneMemberAFId_Object = MibTableColumn
civrZoneMemberAFId = _CivrZoneMemberAFId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 5),
    _CivrZoneMemberAFId_Type()
)
civrZoneMemberAFId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneMemberAFId.setStatus("current")
_CivrZoneMemberVsan_Type = VsanIndex
_CivrZoneMemberVsan_Object = MibTableColumn
civrZoneMemberVsan = _CivrZoneMemberVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 6),
    _CivrZoneMemberVsan_Type()
)
civrZoneMemberVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneMemberVsan.setStatus("current")
_CivrZoneMemberRowStatus_Type = RowStatus
_CivrZoneMemberRowStatus_Object = MibTableColumn
civrZoneMemberRowStatus = _CivrZoneMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 7),
    _CivrZoneMemberRowStatus_Type()
)
civrZoneMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneMemberRowStatus.setStatus("current")


class _CivrZoneMemberLunID_Type(OctetString):
    """Custom type civrZoneMemberLunID based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_CivrZoneMemberLunID_Type.__name__ = "OctetString"
_CivrZoneMemberLunID_Object = MibTableColumn
civrZoneMemberLunID = _CivrZoneMemberLunID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 2, 1, 8),
    _CivrZoneMemberLunID_Type()
)
civrZoneMemberLunID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrZoneMemberLunID.setStatus("current")


class _CivrZoneEnforcedZoneMemberNumber_Type(Integer32):
    """Custom type civrZoneEnforcedZoneMemberNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_CivrZoneEnforcedZoneMemberNumber_Type.__name__ = "Integer32"
_CivrZoneEnforcedZoneMemberNumber_Object = MibScalar
civrZoneEnforcedZoneMemberNumber = _CivrZoneEnforcedZoneMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 3),
    _CivrZoneEnforcedZoneMemberNumber_Type()
)
civrZoneEnforcedZoneMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberNumber.setStatus("current")
_CivrZoneEnforcedZoneMemberTable_Object = MibTable
civrZoneEnforcedZoneMemberTable = _CivrZoneEnforcedZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberTable.setStatus("current")
_CivrZoneEnforcedZoneMemberEntry_Object = MibTableRow
civrZoneEnforcedZoneMemberEntry = _CivrZoneEnforcedZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 4, 1)
)
civrZoneEnforcedZoneMemberEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrZoneMemberParentIndex"),
    (0, "CISCO-IVR-MIB", "civrZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberEntry.setStatus("current")
_CivrZoneEnforcedZoneMemberType_Type = CIvrZoneMemberType
_CivrZoneEnforcedZoneMemberType_Object = MibTableColumn
civrZoneEnforcedZoneMemberType = _CivrZoneEnforcedZoneMemberType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 4, 1, 2),
    _CivrZoneEnforcedZoneMemberType_Type()
)
civrZoneEnforcedZoneMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberType.setStatus("current")
_CivrZoneEnforcedZoneMemberID_Type = OctetString
_CivrZoneEnforcedZoneMemberID_Object = MibTableColumn
civrZoneEnforcedZoneMemberID = _CivrZoneEnforcedZoneMemberID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 4, 1, 3),
    _CivrZoneEnforcedZoneMemberID_Type()
)
civrZoneEnforcedZoneMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberID.setStatus("current")
_CivrZoneEnforcedZoneMemberAFId_Type = CIvrAutonomousFabricId
_CivrZoneEnforcedZoneMemberAFId_Object = MibTableColumn
civrZoneEnforcedZoneMemberAFId = _CivrZoneEnforcedZoneMemberAFId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 4, 1, 4),
    _CivrZoneEnforcedZoneMemberAFId_Type()
)
civrZoneEnforcedZoneMemberAFId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberAFId.setStatus("current")
_CivrZoneEnforcedZoneMemberVsan_Type = VsanIndex
_CivrZoneEnforcedZoneMemberVsan_Object = MibTableColumn
civrZoneEnforcedZoneMemberVsan = _CivrZoneEnforcedZoneMemberVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 4, 1, 5),
    _CivrZoneEnforcedZoneMemberVsan_Type()
)
civrZoneEnforcedZoneMemberVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberVsan.setStatus("current")


class _CivrZoneEnforcedZoneMemberLunID_Type(OctetString):
    """Custom type civrZoneEnforcedZoneMemberLunID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_CivrZoneEnforcedZoneMemberLunID_Type.__name__ = "OctetString"
_CivrZoneEnforcedZoneMemberLunID_Object = MibTableColumn
civrZoneEnforcedZoneMemberLunID = _CivrZoneEnforcedZoneMemberLunID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 4, 4, 1, 6),
    _CivrZoneEnforcedZoneMemberLunID_Type()
)
civrZoneEnforcedZoneMemberLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneEnforcedZoneMemberLunID.setStatus("current")
_CimIvrTopology_ObjectIdentity = ObjectIdentity
cimIvrTopology = _CimIvrTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5)
)
_CivrTopologyConfiguredChecksum_Type = CIvrChecksum
_CivrTopologyConfiguredChecksum_Object = MibScalar
civrTopologyConfiguredChecksum = _CivrTopologyConfiguredChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 1),
    _CivrTopologyConfiguredChecksum_Type()
)
civrTopologyConfiguredChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyConfiguredChecksum.setStatus("current")
_CivrTopologyConfigTable_Object = MibTable
civrTopologyConfigTable = _CivrTopologyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    civrTopologyConfigTable.setStatus("current")
_CivrTopologyConfigEntry_Object = MibTableRow
civrTopologyConfigEntry = _CivrTopologyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 2, 1)
)
civrTopologyConfigEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrTopologyConfigAutoFabricId"),
    (0, "CISCO-IVR-MIB", "civrTopologyConfigSwitchWwn"),
)
if mibBuilder.loadTexts:
    civrTopologyConfigEntry.setStatus("current")
_CivrTopologyConfigSwitchWwn_Type = FcNameId
_CivrTopologyConfigSwitchWwn_Object = MibTableColumn
civrTopologyConfigSwitchWwn = _CivrTopologyConfigSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 2, 1, 1),
    _CivrTopologyConfigSwitchWwn_Type()
)
civrTopologyConfigSwitchWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyConfigSwitchWwn.setStatus("current")
_CivrTopologyConfigAutoFabricId_Type = CIvrAutonomousFabricId
_CivrTopologyConfigAutoFabricId_Object = MibTableColumn
civrTopologyConfigAutoFabricId = _CivrTopologyConfigAutoFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 2, 1, 2),
    _CivrTopologyConfigAutoFabricId_Type()
)
civrTopologyConfigAutoFabricId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyConfigAutoFabricId.setStatus("current")


class _CivrTopologyConfigSwitchVsan2k_Type(FcList):
    """Custom type civrTopologyConfigSwitchVsan2k based on FcList"""
    defaultHexValue = ""


_CivrTopologyConfigSwitchVsan2k_Object = MibTableColumn
civrTopologyConfigSwitchVsan2k = _CivrTopologyConfigSwitchVsan2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 2, 1, 3),
    _CivrTopologyConfigSwitchVsan2k_Type()
)
civrTopologyConfigSwitchVsan2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyConfigSwitchVsan2k.setStatus("current")


class _CivrTopologyConfigSwitchVsan4k_Type(FcList):
    """Custom type civrTopologyConfigSwitchVsan4k based on FcList"""
    defaultHexValue = ""


_CivrTopologyConfigSwitchVsan4k_Object = MibTableColumn
civrTopologyConfigSwitchVsan4k = _CivrTopologyConfigSwitchVsan4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 2, 1, 4),
    _CivrTopologyConfigSwitchVsan4k_Type()
)
civrTopologyConfigSwitchVsan4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyConfigSwitchVsan4k.setStatus("current")
_CivrTopologyConfigRowStatus_Type = RowStatus
_CivrTopologyConfigRowStatus_Object = MibTableColumn
civrTopologyConfigRowStatus = _CivrTopologyConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 2, 1, 5),
    _CivrTopologyConfigRowStatus_Type()
)
civrTopologyConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyConfigRowStatus.setStatus("current")


class _CivrTopologyActivate_Type(Integer32):
    """Custom type civrTopologyActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("noOp", 2))
    )


_CivrTopologyActivate_Type.__name__ = "Integer32"
_CivrTopologyActivate_Object = MibScalar
civrTopologyActivate = _CivrTopologyActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 3),
    _CivrTopologyActivate_Type()
)
civrTopologyActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrTopologyActivate.setStatus("current")
_CivrTopologyActivateTime_Type = TimeStamp
_CivrTopologyActivateTime_Object = MibScalar
civrTopologyActivateTime = _CivrTopologyActivateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 4),
    _CivrTopologyActivateTime_Type()
)
civrTopologyActivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyActivateTime.setStatus("current")


class _CivrTopologyCopyActiveToConfig_Type(Integer32):
    """Custom type civrTopologyCopyActiveToConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("noOp", 2))
    )


_CivrTopologyCopyActiveToConfig_Type.__name__ = "Integer32"
_CivrTopologyCopyActiveToConfig_Object = MibScalar
civrTopologyCopyActiveToConfig = _CivrTopologyCopyActiveToConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 5),
    _CivrTopologyCopyActiveToConfig_Type()
)
civrTopologyCopyActiveToConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrTopologyCopyActiveToConfig.setStatus("current")


class _CivrTopologyClearConfigured_Type(Integer32):
    """Custom type civrTopologyClearConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_CivrTopologyClearConfigured_Type.__name__ = "Integer32"
_CivrTopologyClearConfigured_Object = MibScalar
civrTopologyClearConfigured = _CivrTopologyClearConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 6),
    _CivrTopologyClearConfigured_Type()
)
civrTopologyClearConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrTopologyClearConfigured.setStatus("current")
_CivrTopologyActiveChecksum_Type = CIvrChecksum
_CivrTopologyActiveChecksum_Object = MibScalar
civrTopologyActiveChecksum = _CivrTopologyActiveChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 7),
    _CivrTopologyActiveChecksum_Type()
)
civrTopologyActiveChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyActiveChecksum.setStatus("current")
_CivrTopologyActiveTable_Object = MibTable
civrTopologyActiveTable = _CivrTopologyActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    civrTopologyActiveTable.setStatus("current")
_CivrTopologyActiveEntry_Object = MibTableRow
civrTopologyActiveEntry = _CivrTopologyActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 8, 1)
)
civrTopologyActiveEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrTopologyActiveAutoFabricId"),
    (0, "CISCO-IVR-MIB", "civrTopologyActiveSwitchWwn"),
)
if mibBuilder.loadTexts:
    civrTopologyActiveEntry.setStatus("current")
_CivrTopologyActiveSwitchWwn_Type = FcNameId
_CivrTopologyActiveSwitchWwn_Object = MibTableColumn
civrTopologyActiveSwitchWwn = _CivrTopologyActiveSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 8, 1, 1),
    _CivrTopologyActiveSwitchWwn_Type()
)
civrTopologyActiveSwitchWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyActiveSwitchWwn.setStatus("current")
_CivrTopologyActiveAutoFabricId_Type = CIvrAutonomousFabricId
_CivrTopologyActiveAutoFabricId_Object = MibTableColumn
civrTopologyActiveAutoFabricId = _CivrTopologyActiveAutoFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 8, 1, 2),
    _CivrTopologyActiveAutoFabricId_Type()
)
civrTopologyActiveAutoFabricId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyActiveAutoFabricId.setStatus("current")


class _CivrTopologyActiveSwitchVsan2k_Type(FcList):
    """Custom type civrTopologyActiveSwitchVsan2k based on FcList"""
    defaultHexValue = ""


_CivrTopologyActiveSwitchVsan2k_Object = MibTableColumn
civrTopologyActiveSwitchVsan2k = _CivrTopologyActiveSwitchVsan2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 8, 1, 3),
    _CivrTopologyActiveSwitchVsan2k_Type()
)
civrTopologyActiveSwitchVsan2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyActiveSwitchVsan2k.setStatus("current")


class _CivrTopologyActiveSwitchVsan4k_Type(FcList):
    """Custom type civrTopologyActiveSwitchVsan4k based on FcList"""
    defaultHexValue = ""


_CivrTopologyActiveSwitchVsan4k_Object = MibTableColumn
civrTopologyActiveSwitchVsan4k = _CivrTopologyActiveSwitchVsan4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 8, 1, 4),
    _CivrTopologyActiveSwitchVsan4k_Type()
)
civrTopologyActiveSwitchVsan4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyActiveSwitchVsan4k.setStatus("current")
_CivrTopologyActive_Type = TruthValue
_CivrTopologyActive_Object = MibScalar
civrTopologyActive = _CivrTopologyActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 9),
    _CivrTopologyActive_Type()
)
civrTopologyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyActive.setStatus("current")
_CivrTopologyAfidConfigChecksum_Type = CIvrChecksum
_CivrTopologyAfidConfigChecksum_Object = MibScalar
civrTopologyAfidConfigChecksum = _CivrTopologyAfidConfigChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 10),
    _CivrTopologyAfidConfigChecksum_Type()
)
civrTopologyAfidConfigChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyAfidConfigChecksum.setStatus("current")
_CivrTopologyAfidConfTable_Object = MibTable
civrTopologyAfidConfTable = _CivrTopologyAfidConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 11)
)
if mibBuilder.loadTexts:
    civrTopologyAfidConfTable.setStatus("current")
_CivrTopologyAfidConfEntry_Object = MibTableRow
civrTopologyAfidConfEntry = _CivrTopologyAfidConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 11, 1)
)
civrTopologyAfidConfEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrTopologyAfidConfSwitchWwn"),
    (0, "CISCO-IVR-MIB", "civrTopologyAfidConfId"),
)
if mibBuilder.loadTexts:
    civrTopologyAfidConfEntry.setStatus("current")
_CivrTopologyAfidConfSwitchWwn_Type = FcNameId
_CivrTopologyAfidConfSwitchWwn_Object = MibTableColumn
civrTopologyAfidConfSwitchWwn = _CivrTopologyAfidConfSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 11, 1, 1),
    _CivrTopologyAfidConfSwitchWwn_Type()
)
civrTopologyAfidConfSwitchWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyAfidConfSwitchWwn.setStatus("current")
_CivrTopologyAfidConfId_Type = CIvrAutonomousFabricId
_CivrTopologyAfidConfId_Object = MibTableColumn
civrTopologyAfidConfId = _CivrTopologyAfidConfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 11, 1, 2),
    _CivrTopologyAfidConfId_Type()
)
civrTopologyAfidConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyAfidConfId.setStatus("current")


class _CivrTopologyAfidConfSwitchVsan2k_Type(FcList):
    """Custom type civrTopologyAfidConfSwitchVsan2k based on FcList"""
    defaultHexValue = ""


_CivrTopologyAfidConfSwitchVsan2k_Object = MibTableColumn
civrTopologyAfidConfSwitchVsan2k = _CivrTopologyAfidConfSwitchVsan2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 11, 1, 3),
    _CivrTopologyAfidConfSwitchVsan2k_Type()
)
civrTopologyAfidConfSwitchVsan2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyAfidConfSwitchVsan2k.setStatus("current")


class _CivrTopologyAfidConfSwitchVsan4k_Type(FcList):
    """Custom type civrTopologyAfidConfSwitchVsan4k based on FcList"""
    defaultHexValue = ""


_CivrTopologyAfidConfSwitchVsan4k_Object = MibTableColumn
civrTopologyAfidConfSwitchVsan4k = _CivrTopologyAfidConfSwitchVsan4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 11, 1, 4),
    _CivrTopologyAfidConfSwitchVsan4k_Type()
)
civrTopologyAfidConfSwitchVsan4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyAfidConfSwitchVsan4k.setStatus("current")
_CivrTopologyAfidConfRowStatus_Type = RowStatus
_CivrTopologyAfidConfRowStatus_Object = MibTableColumn
civrTopologyAfidConfRowStatus = _CivrTopologyAfidConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 11, 1, 5),
    _CivrTopologyAfidConfRowStatus_Type()
)
civrTopologyAfidConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyAfidConfRowStatus.setStatus("current")
_CivrTopologyDefaultAfidChecksum_Type = CIvrChecksum
_CivrTopologyDefaultAfidChecksum_Object = MibScalar
civrTopologyDefaultAfidChecksum = _CivrTopologyDefaultAfidChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 12),
    _CivrTopologyDefaultAfidChecksum_Type()
)
civrTopologyDefaultAfidChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrTopologyDefaultAfidChecksum.setStatus("current")
_CivrTopologyDefaultAfidTable_Object = MibTable
civrTopologyDefaultAfidTable = _CivrTopologyDefaultAfidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 13)
)
if mibBuilder.loadTexts:
    civrTopologyDefaultAfidTable.setStatus("current")
_CivrTopologyDefaultAfidEntry_Object = MibTableRow
civrTopologyDefaultAfidEntry = _CivrTopologyDefaultAfidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 13, 1)
)
civrTopologyDefaultAfidEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrTopologyDefaultAfidSwitchWwn"),
)
if mibBuilder.loadTexts:
    civrTopologyDefaultAfidEntry.setStatus("current")
_CivrTopologyDefaultAfidSwitchWwn_Type = FcNameId
_CivrTopologyDefaultAfidSwitchWwn_Object = MibTableColumn
civrTopologyDefaultAfidSwitchWwn = _CivrTopologyDefaultAfidSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 13, 1, 1),
    _CivrTopologyDefaultAfidSwitchWwn_Type()
)
civrTopologyDefaultAfidSwitchWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyDefaultAfidSwitchWwn.setStatus("current")


class _CivrTopologyDefaultAfidId_Type(CIvrAutonomousFabricId):
    """Custom type civrTopologyDefaultAfidId based on CIvrAutonomousFabricId"""
    defaultValue = 1


_CivrTopologyDefaultAfidId_Object = MibTableColumn
civrTopologyDefaultAfidId = _CivrTopologyDefaultAfidId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 13, 1, 2),
    _CivrTopologyDefaultAfidId_Type()
)
civrTopologyDefaultAfidId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyDefaultAfidId.setStatus("current")
_CivrTopologyDefaultAfidStatus_Type = RowStatus
_CivrTopologyDefaultAfidStatus_Object = MibTableColumn
civrTopologyDefaultAfidStatus = _CivrTopologyDefaultAfidStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 13, 1, 3),
    _CivrTopologyDefaultAfidStatus_Type()
)
civrTopologyDefaultAfidStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyDefaultAfidStatus.setStatus("current")
_CivrTopologyIvrSrvGrpTable_Object = MibTable
civrTopologyIvrSrvGrpTable = _CivrTopologyIvrSrvGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 14)
)
if mibBuilder.loadTexts:
    civrTopologyIvrSrvGrpTable.setStatus("current")
_CivrTopologyIvrSrvGrpEntry_Object = MibTableRow
civrTopologyIvrSrvGrpEntry = _CivrTopologyIvrSrvGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 14, 1)
)
civrTopologyIvrSrvGrpEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrTopologyIvrSrvGrpName"),
    (0, "CISCO-IVR-MIB", "civrTopologyAfidConfId"),
)
if mibBuilder.loadTexts:
    civrTopologyIvrSrvGrpEntry.setStatus("current")


class _CivrTopologyIvrSrvGrpName_Type(SnmpAdminString):
    """Custom type civrTopologyIvrSrvGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CivrTopologyIvrSrvGrpName_Type.__name__ = "SnmpAdminString"
_CivrTopologyIvrSrvGrpName_Object = MibTableColumn
civrTopologyIvrSrvGrpName = _CivrTopologyIvrSrvGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 14, 1, 1),
    _CivrTopologyIvrSrvGrpName_Type()
)
civrTopologyIvrSrvGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrTopologyIvrSrvGrpName.setStatus("current")
_CivrTopologyIvrSrvGrpVsan2k_Type = FcList
_CivrTopologyIvrSrvGrpVsan2k_Object = MibTableColumn
civrTopologyIvrSrvGrpVsan2k = _CivrTopologyIvrSrvGrpVsan2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 14, 1, 2),
    _CivrTopologyIvrSrvGrpVsan2k_Type()
)
civrTopologyIvrSrvGrpVsan2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyIvrSrvGrpVsan2k.setStatus("current")
_CivrTopologyIvrSrvGrpVsan4k_Type = FcList
_CivrTopologyIvrSrvGrpVsan4k_Object = MibTableColumn
civrTopologyIvrSrvGrpVsan4k = _CivrTopologyIvrSrvGrpVsan4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 14, 1, 3),
    _CivrTopologyIvrSrvGrpVsan4k_Type()
)
civrTopologyIvrSrvGrpVsan4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyIvrSrvGrpVsan4k.setStatus("current")
_CivrTopologyIvrSrvGrpRowStatus_Type = RowStatus
_CivrTopologyIvrSrvGrpRowStatus_Object = MibTableColumn
civrTopologyIvrSrvGrpRowStatus = _CivrTopologyIvrSrvGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 14, 1, 4),
    _CivrTopologyIvrSrvGrpRowStatus_Type()
)
civrTopologyIvrSrvGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    civrTopologyIvrSrvGrpRowStatus.setStatus("current")


class _CivrTopologyClearAfidConfig_Type(Integer32):
    """Custom type civrTopologyClearAfidConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_CivrTopologyClearAfidConfig_Type.__name__ = "Integer32"
_CivrTopologyClearAfidConfig_Object = MibScalar
civrTopologyClearAfidConfig = _CivrTopologyClearAfidConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 5, 15),
    _CivrTopologyClearAfidConfig_Type()
)
civrTopologyClearAfidConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrTopologyClearAfidConfig.setStatus("current")
_CimIvrVirtualDomains_ObjectIdentity = ObjectIdentity
cimIvrVirtualDomains = _CimIvrVirtualDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 6)
)
_CivrAddIvrVirtualDomainsVsans2k_Type = FcList
_CivrAddIvrVirtualDomainsVsans2k_Object = MibScalar
civrAddIvrVirtualDomainsVsans2k = _CivrAddIvrVirtualDomainsVsans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 6, 1),
    _CivrAddIvrVirtualDomainsVsans2k_Type()
)
civrAddIvrVirtualDomainsVsans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrAddIvrVirtualDomainsVsans2k.setStatus("current")
_CivrAddIvrVirtualDomainsVsans4k_Type = FcList
_CivrAddIvrVirtualDomainsVsans4k_Object = MibScalar
civrAddIvrVirtualDomainsVsans4k = _CivrAddIvrVirtualDomainsVsans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 1, 6, 2),
    _CivrAddIvrVirtualDomainsVsans4k_Type()
)
civrAddIvrVirtualDomainsVsans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    civrAddIvrVirtualDomainsVsans4k.setStatus("current")
_CimIvrStats_ObjectIdentity = ObjectIdentity
cimIvrStats = _CimIvrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2)
)
_CivrZoneSetStatusTable_Object = MibTable
civrZoneSetStatusTable = _CivrZoneSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 1)
)
if mibBuilder.loadTexts:
    civrZoneSetStatusTable.setStatus("current")
_CivrZoneSetStatusEntry_Object = MibTableRow
civrZoneSetStatusEntry = _CivrZoneSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 1, 1)
)
civrZoneSetStatusEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    civrZoneSetStatusEntry.setStatus("current")


class _CivrZoneSetStatus_Type(Integer32):
    """Custom type civrZoneSetStatus based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("activating", 11),
          ("activatingFabricChanging", 13),
          ("activatingWaitForLowestSwwn", 12),
          ("activationFailed", 5),
          ("activationFailedFabricChgFailed", 8),
          ("activationFailedLowestWwnWait", 21),
          ("activationNotInitiated", 7),
          ("active", 2),
          ("deactivating", 14),
          ("deactivatingFabricChanging", 16),
          ("deactivatingWaitForLowestSwwn", 15),
          ("deactivationFailed", 6),
          ("deactivationFailedFabChgFailed", 10),
          ("deactivationFailedLowestWwnWait", 22),
          ("deactivationNotInitiated", 9),
          ("deactive", 3),
          ("defaultZoneDeny", 4),
          ("defaultZonePermit", 17),
          ("defaultZonePermitActZsNoForce", 19),
          ("defaultZonePermitNoForce", 18),
          ("denyNoActiveZoneset", 20),
          ("idle", 1))
    )


_CivrZoneSetStatus_Type.__name__ = "Integer32"
_CivrZoneSetStatus_Object = MibTableColumn
civrZoneSetStatus = _CivrZoneSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 1, 1, 1),
    _CivrZoneSetStatus_Type()
)
civrZoneSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrZoneSetStatus.setStatus("current")
_CivrEnabledDeviceTable_Object = MibTable
civrEnabledDeviceTable = _CivrEnabledDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 2)
)
if mibBuilder.loadTexts:
    civrEnabledDeviceTable.setStatus("current")
_CivrEnabledDeviceEntry_Object = MibTableRow
civrEnabledDeviceEntry = _CivrEnabledDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 2, 1)
)
civrEnabledDeviceEntry.setIndexNames(
    (0, "CISCO-IVR-MIB", "civrEnabledDeviceAutoFabricId"),
    (0, "CISCO-IVR-MIB", "civrEnabledDeviceVsan"),
    (0, "CISCO-IVR-MIB", "civrEnabledDeviceDomainId"),
)
if mibBuilder.loadTexts:
    civrEnabledDeviceEntry.setStatus("current")
_CivrEnabledDeviceVsan_Type = VsanIndex
_CivrEnabledDeviceVsan_Object = MibTableColumn
civrEnabledDeviceVsan = _CivrEnabledDeviceVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 2, 1, 1),
    _CivrEnabledDeviceVsan_Type()
)
civrEnabledDeviceVsan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrEnabledDeviceVsan.setStatus("current")
_CivrEnabledDeviceAutoFabricId_Type = CIvrAutonomousFabricId
_CivrEnabledDeviceAutoFabricId_Object = MibTableColumn
civrEnabledDeviceAutoFabricId = _CivrEnabledDeviceAutoFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 2, 1, 2),
    _CivrEnabledDeviceAutoFabricId_Type()
)
civrEnabledDeviceAutoFabricId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrEnabledDeviceAutoFabricId.setStatus("current")
_CivrEnabledDeviceDomainId_Type = DomainId
_CivrEnabledDeviceDomainId_Object = MibTableColumn
civrEnabledDeviceDomainId = _CivrEnabledDeviceDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 2, 1, 3),
    _CivrEnabledDeviceDomainId_Type()
)
civrEnabledDeviceDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    civrEnabledDeviceDomainId.setStatus("current")
_CivrEnabledDeviceSwitchWwn_Type = FcNameId
_CivrEnabledDeviceSwitchWwn_Object = MibTableColumn
civrEnabledDeviceSwitchWwn = _CivrEnabledDeviceSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 2, 1, 4),
    _CivrEnabledDeviceSwitchWwn_Type()
)
civrEnabledDeviceSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrEnabledDeviceSwitchWwn.setStatus("current")


class _CivrEnabledDeviceCapability_Type(Bits):
    """Custom type civrEnabledDeviceCapability based on Bits"""
    namedValues = NamedValues(
        ("version1", 0)
    )

_CivrEnabledDeviceCapability_Type.__name__ = "Bits"
_CivrEnabledDeviceCapability_Object = MibTableColumn
civrEnabledDeviceCapability = _CivrEnabledDeviceCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 2, 1, 5),
    _CivrEnabledDeviceCapability_Type()
)
civrEnabledDeviceCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    civrEnabledDeviceCapability.setStatus("current")
_CivrZoneMemberFabricId_Type = FcAddressId
_CivrZoneMemberFabricId_Object = MibScalar
civrZoneMemberFabricId = _CivrZoneMemberFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 3),
    _CivrZoneMemberFabricId_Type()
)
civrZoneMemberFabricId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrZoneMemberFabricId.setStatus("current")
_CivDomainIdConflictVsan_Type = VsanIndex
_CivDomainIdConflictVsan_Object = MibScalar
civDomainIdConflictVsan = _CivDomainIdConflictVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 4),
    _CivDomainIdConflictVsan_Type()
)
civDomainIdConflictVsan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civDomainIdConflictVsan.setStatus("current")
_CivrZoneSetActDeactPartialSucss_Type = TruthValue
_CivrZoneSetActDeactPartialSucss_Object = MibScalar
civrZoneSetActDeactPartialSucss = _CivrZoneSetActDeactPartialSucss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 5),
    _CivrZoneSetActDeactPartialSucss_Type()
)
civrZoneSetActDeactPartialSucss.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrZoneSetActDeactPartialSucss.setStatus("current")
_CivrAfidMisConfigVsan_Type = VsanIndex
_CivrAfidMisConfigVsan_Object = MibScalar
civrAfidMisConfigVsan = _CivrAfidMisConfigVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 6),
    _CivrAfidMisConfigVsan_Type()
)
civrAfidMisConfigVsan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrAfidMisConfigVsan.setStatus("current")
_CivrAfidMisConfigLocalAfid_Type = CIvrAutonomousFabricId
_CivrAfidMisConfigLocalAfid_Object = MibScalar
civrAfidMisConfigLocalAfid = _CivrAfidMisConfigLocalAfid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 7),
    _CivrAfidMisConfigLocalAfid_Type()
)
civrAfidMisConfigLocalAfid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrAfidMisConfigLocalAfid.setStatus("current")
_CivrAfidMisConfigRemoteAfid_Type = CIvrAutonomousFabricId
_CivrAfidMisConfigRemoteAfid_Object = MibScalar
civrAfidMisConfigRemoteAfid = _CivrAfidMisConfigRemoteAfid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 8),
    _CivrAfidMisConfigRemoteAfid_Type()
)
civrAfidMisConfigRemoteAfid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrAfidMisConfigRemoteAfid.setStatus("current")
_CivrAfidMisConfigLocalSWwn_Type = FcNameId
_CivrAfidMisConfigLocalSWwn_Object = MibScalar
civrAfidMisConfigLocalSWwn = _CivrAfidMisConfigLocalSWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 9),
    _CivrAfidMisConfigLocalSWwn_Type()
)
civrAfidMisConfigLocalSWwn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrAfidMisConfigLocalSWwn.setStatus("current")
_CivrAfidMisConfigRemoteSWwn_Type = FcNameId
_CivrAfidMisConfigRemoteSWwn_Object = MibScalar
civrAfidMisConfigRemoteSWwn = _CivrAfidMisConfigRemoteSWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 10),
    _CivrAfidMisConfigRemoteSWwn_Type()
)
civrAfidMisConfigRemoteSWwn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrAfidMisConfigRemoteSWwn.setStatus("current")


class _CivrTopologyMisConfigReason_Type(Integer32):
    """Custom type civrTopologyMisConfigReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("afidMismatch", 2),
          ("unknown", 1))
    )


_CivrTopologyMisConfigReason_Type.__name__ = "Integer32"
_CivrTopologyMisConfigReason_Object = MibScalar
civrTopologyMisConfigReason = _CivrTopologyMisConfigReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 1, 2, 11),
    _CivrTopologyMisConfigReason_Type()
)
civrTopologyMisConfigReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    civrTopologyMisConfigReason.setStatus("current")
_CiscoIvrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIvrMIBConformance = _CiscoIvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2)
)
_CivrZoneServerMIBCompliances_ObjectIdentity = ObjectIdentity
civrZoneServerMIBCompliances = _CivrZoneServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 1)
)
_CivrZoneServerMIBGroups_ObjectIdentity = ObjectIdentity
civrZoneServerMIBGroups = _CivrZoneServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2)
)

# Managed Objects groups

civrZoneConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 1)
)
civrZoneConfigurationGroup.setObjects(
      *(("CISCO-IVR-MIB", "civrZoneSetNumber"),
        ("CISCO-IVR-MIB", "civrZoneSetName"),
        ("CISCO-IVR-MIB", "civrZoneSetZoneList"),
        ("CISCO-IVR-MIB", "civrZoneSetLastChange"),
        ("CISCO-IVR-MIB", "civrZoneSetChecksum"),
        ("CISCO-IVR-MIB", "civrZoneSetRowStatus"),
        ("CISCO-IVR-MIB", "civrZoneSetActivate"),
        ("CISCO-IVR-MIB", "civrZoneSetActvatDeactvatResult"),
        ("CISCO-IVR-MIB", "civrZoneSetDeActivate"),
        ("CISCO-IVR-MIB", "civrZoneNumber"),
        ("CISCO-IVR-MIB", "civrZoneName"),
        ("CISCO-IVR-MIB", "civrZoneMemberList"),
        ("CISCO-IVR-MIB", "civrZoneLastChange"),
        ("CISCO-IVR-MIB", "civrZoneRowStatus"),
        ("CISCO-IVR-MIB", "civrZoneMemberNumber"),
        ("CISCO-IVR-MIB", "civrZoneMemberType"),
        ("CISCO-IVR-MIB", "civrZoneMemberID"),
        ("CISCO-IVR-MIB", "civrZoneMemberAFId"),
        ("CISCO-IVR-MIB", "civrZoneMemberVsan"),
        ("CISCO-IVR-MIB", "civrZonesetDbChecksum"),
        ("CISCO-IVR-MIB", "civrActiveZonesetChecksum"),
        ("CISCO-IVR-MIB", "civrZoneMemberRowStatus"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneSetName"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneSetZoneList"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneSetActvtTime"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneNumber"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneName"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberList"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberNumber"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberType"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberID"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberAFId"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberVsan"),
        ("CISCO-IVR-MIB", "civrZoneCopyZoneSetEnforcdToFull"),
        ("CISCO-IVR-MIB", "civrZoneClearFullZoneDb"),
        ("CISCO-IVR-MIB", "civrZonesetActivateForce"))
)
if mibBuilder.loadTexts:
    civrZoneConfigurationGroup.setStatus("current")

civrTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 2)
)
civrTopologyGroup.setObjects(
      *(("CISCO-IVR-MIB", "civrTopologyConfigSwitchVsan2k"),
        ("CISCO-IVR-MIB", "civrTopologyConfigSwitchVsan4k"),
        ("CISCO-IVR-MIB", "civrTopologyConfigRowStatus"),
        ("CISCO-IVR-MIB", "civrTopologyActiveSwitchVsan2k"),
        ("CISCO-IVR-MIB", "civrTopologyActiveSwitchVsan4k"),
        ("CISCO-IVR-MIB", "civrTopologyConfiguredChecksum"),
        ("CISCO-IVR-MIB", "civrTopologyActiveChecksum"),
        ("CISCO-IVR-MIB", "civrTopologyActivate"),
        ("CISCO-IVR-MIB", "civrTopologyActivateTime"),
        ("CISCO-IVR-MIB", "civrTopologyCopyActiveToConfig"),
        ("CISCO-IVR-MIB", "civrTopologyClearConfigured"),
        ("CISCO-IVR-MIB", "civrTopologyActive"))
)
if mibBuilder.loadTexts:
    civrTopologyGroup.setStatus("current")

civrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 3)
)
civrStatsGroup.setObjects(
      *(("CISCO-IVR-MIB", "civrZoneSetStatus"),
        ("CISCO-IVR-MIB", "civrEnabledDeviceSwitchWwn"),
        ("CISCO-IVR-MIB", "civrEnabledDeviceCapability"),
        ("CISCO-IVR-MIB", "civDomainIdConflictVsan"),
        ("CISCO-IVR-MIB", "civrZoneMemberFabricId"),
        ("CISCO-IVR-MIB", "civrZoneSetActDeactPartialSucss"))
)
if mibBuilder.loadTexts:
    civrStatsGroup.setStatus("current")

civrVirtualDomainsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 5)
)
civrVirtualDomainsGroup.setObjects(
      *(("CISCO-IVR-MIB", "civrAddIvrVirtualDomainsVsans2k"),
        ("CISCO-IVR-MIB", "civrAddIvrVirtualDomainsVsans4k"))
)
if mibBuilder.loadTexts:
    civrVirtualDomainsGroup.setStatus("current")

civrGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 6)
)
civrGenericGroup.setObjects(
      *(("CISCO-IVR-MIB", "civrFcidNatMode"),
        ("CISCO-IVR-MIB", "civrVsanTopologyAutoDisc"))
)
if mibBuilder.loadTexts:
    civrGenericGroup.setStatus("current")

civrTopologyGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 7)
)
civrTopologyGroupRev2.setObjects(
      *(("CISCO-IVR-MIB", "civrTopologyAfidConfSwitchVsan2k"),
        ("CISCO-IVR-MIB", "civrTopologyAfidConfSwitchVsan4k"),
        ("CISCO-IVR-MIB", "civrTopologyAfidConfRowStatus"),
        ("CISCO-IVR-MIB", "civrTopologyDefaultAfidId"),
        ("CISCO-IVR-MIB", "civrTopologyDefaultAfidStatus"),
        ("CISCO-IVR-MIB", "civrTopologyIvrSrvGrpVsan2k"),
        ("CISCO-IVR-MIB", "civrTopologyIvrSrvGrpVsan4k"),
        ("CISCO-IVR-MIB", "civrTopologyIvrSrvGrpRowStatus"),
        ("CISCO-IVR-MIB", "civrTopologyAfidConfigChecksum"),
        ("CISCO-IVR-MIB", "civrTopologyDefaultAfidChecksum"),
        ("CISCO-IVR-MIB", "civrTopologyClearAfidConfig"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigVsan"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigLocalAfid"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigRemoteAfid"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigLocalSWwn"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigRemoteSWwn"),
        ("CISCO-IVR-MIB", "civrTopologyMisConfigReason"))
)
if mibBuilder.loadTexts:
    civrTopologyGroupRev2.setStatus("current")

civrZoneConfigurationGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 8)
)
civrZoneConfigurationGroupRev2.setObjects(
      *(("CISCO-IVR-MIB", "civrZoneReadOnly"),
        ("CISCO-IVR-MIB", "civrZoneQosPriority"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneReadOnly"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneQosPriority"),
        ("CISCO-IVR-MIB", "civrZoneMemberLunID"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberLunID"),
        ("CISCO-IVR-MIB", "civrZoneSetTableNextIndex"),
        ("CISCO-IVR-MIB", "civrZoneTableNextIndex"))
)
if mibBuilder.loadTexts:
    civrZoneConfigurationGroupRev2.setStatus("current")


# Notification objects

civrZoneActivationDoneNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 0, 1)
)
civrZoneActivationDoneNotify.setObjects(
      *(("CISCO-IVR-MIB", "civrZoneSetName"),
        ("CISCO-IVR-MIB", "civrZoneSetActvatDeactvatResult"),
        ("CISCO-IVR-MIB", "civrZoneSetActDeactPartialSucss"))
)
if mibBuilder.loadTexts:
    civrZoneActivationDoneNotify.setStatus(
        "current"
    )

civrZoneDeactivationDoneNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 0, 2)
)
civrZoneDeactivationDoneNotify.setObjects(
      *(("CISCO-IVR-MIB", "civrZoneSetName"),
        ("CISCO-IVR-MIB", "civrZoneSetActvatDeactvatResult"),
        ("CISCO-IVR-MIB", "civrZoneSetActDeactPartialSucss"))
)
if mibBuilder.loadTexts:
    civrZoneDeactivationDoneNotify.setStatus(
        "current"
    )

civrDomainConflictNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 0, 3)
)
civrDomainConflictNotify.setObjects(
      *(("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberID"),
        ("CISCO-IVR-MIB", "civrZoneEnforcedZoneMemberVsan"),
        ("CISCO-IVR-MIB", "civrZoneMemberFabricId"),
        ("CISCO-IVR-MIB", "civDomainIdConflictVsan"))
)
if mibBuilder.loadTexts:
    civrDomainConflictNotify.setStatus(
        "current"
    )

civrAfidConfigNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 0, 4)
)
civrAfidConfigNotify.setObjects(
      *(("CISCO-IVR-MIB", "civrAfidMisConfigLocalAfid"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigRemoteAfid"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigLocalSWwn"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigRemoteSWwn"),
        ("CISCO-IVR-MIB", "civrAfidMisConfigVsan"),
        ("CISCO-IVR-MIB", "civrTopologyMisConfigReason"))
)
if mibBuilder.loadTexts:
    civrAfidConfigNotify.setStatus(
        "current"
    )


# Notifications groups

civrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 4)
)
civrNotificationGroup.setObjects(
      *(("CISCO-IVR-MIB", "civrZoneActivationDoneNotify"),
        ("CISCO-IVR-MIB", "civrZoneDeactivationDoneNotify"),
        ("CISCO-IVR-MIB", "civrDomainConflictNotify"))
)
if mibBuilder.loadTexts:
    civrNotificationGroup.setStatus(
        "current"
    )

civrNotificationGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 2, 9)
)
civrNotificationGroupRev2.setObjects(
    ("CISCO-IVR-MIB", "civrAfidConfigNotify")
)
if mibBuilder.loadTexts:
    civrNotificationGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

civrZoneServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 1, 1)
)
if mibBuilder.loadTexts:
    civrZoneServerMIBCompliance.setStatus(
        "deprecated"
    )

civrZoneServerMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 1, 2)
)
if mibBuilder.loadTexts:
    civrZoneServerMIBComplianceRev1.setStatus(
        "deprecated"
    )

civrZoneServerMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 371, 2, 1, 3)
)
if mibBuilder.loadTexts:
    civrZoneServerMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IVR-MIB",
    **{"CIvrZoneMemberType": CIvrZoneMemberType,
       "CIvrAutonomousFabricId": CIvrAutonomousFabricId,
       "CIvrChecksum": CIvrChecksum,
       "ciscoIvrMIB": ciscoIvrMIB,
       "ciscoIvrMIBNotifications": ciscoIvrMIBNotifications,
       "civrZoneActivationDoneNotify": civrZoneActivationDoneNotify,
       "civrZoneDeactivationDoneNotify": civrZoneDeactivationDoneNotify,
       "civrDomainConflictNotify": civrDomainConflictNotify,
       "civrAfidConfigNotify": civrAfidConfigNotify,
       "ciscoIvrMIBObjects": ciscoIvrMIBObjects,
       "cimIvrConfiguration": cimIvrConfiguration,
       "cimIvrGeneric": cimIvrGeneric,
       "civrFcidNatMode": civrFcidNatMode,
       "civrVsanTopologyAutoDisc": civrVsanTopologyAutoDisc,
       "cimIvrZoneset": cimIvrZoneset,
       "civrZoneSetNumber": civrZoneSetNumber,
       "civrZoneSetTable": civrZoneSetTable,
       "civrZoneSetEntry": civrZoneSetEntry,
       "civrZoneSetIndex": civrZoneSetIndex,
       "civrZoneSetName": civrZoneSetName,
       "civrZoneSetZoneList": civrZoneSetZoneList,
       "civrZoneSetLastChange": civrZoneSetLastChange,
       "civrZoneSetChecksum": civrZoneSetChecksum,
       "civrZoneSetRowStatus": civrZoneSetRowStatus,
       "civrZoneSetActivate": civrZoneSetActivate,
       "civrZoneSetActvatDeactvatResult": civrZoneSetActvatDeactvatResult,
       "civrZoneSetDeActivate": civrZoneSetDeActivate,
       "civrZonesetDbChecksum": civrZonesetDbChecksum,
       "civrActiveZonesetChecksum": civrActiveZonesetChecksum,
       "civrZoneEnforcedZoneSetName": civrZoneEnforcedZoneSetName,
       "civrZoneEnforcedZoneSetZoneList": civrZoneEnforcedZoneSetZoneList,
       "civrZoneEnforcedZoneSetActvtTime": civrZoneEnforcedZoneSetActvtTime,
       "civrZoneCopyZoneSetEnforcdToFull": civrZoneCopyZoneSetEnforcdToFull,
       "civrZoneClearFullZoneDb": civrZoneClearFullZoneDb,
       "civrZonesetActivateForce": civrZonesetActivateForce,
       "civrZoneSetTableNextIndex": civrZoneSetTableNextIndex,
       "cimIvrZone": cimIvrZone,
       "civrZoneNumber": civrZoneNumber,
       "civrZoneTable": civrZoneTable,
       "civrZoneEntry": civrZoneEntry,
       "civrZoneIndex": civrZoneIndex,
       "civrZoneName": civrZoneName,
       "civrZoneMemberList": civrZoneMemberList,
       "civrZoneLastChange": civrZoneLastChange,
       "civrZoneRowStatus": civrZoneRowStatus,
       "civrZoneReadOnly": civrZoneReadOnly,
       "civrZoneQosPriority": civrZoneQosPriority,
       "civrZoneEnforcedZoneNumber": civrZoneEnforcedZoneNumber,
       "civrZoneEnforcedZoneTable": civrZoneEnforcedZoneTable,
       "civrZoneEnforcedZoneEntry": civrZoneEnforcedZoneEntry,
       "civrZoneEnforcedZoneName": civrZoneEnforcedZoneName,
       "civrZoneEnforcedZoneMemberList": civrZoneEnforcedZoneMemberList,
       "civrZoneEnforcedZoneReadOnly": civrZoneEnforcedZoneReadOnly,
       "civrZoneEnforcedZoneQosPriority": civrZoneEnforcedZoneQosPriority,
       "civrZoneTableNextIndex": civrZoneTableNextIndex,
       "cimIvrZoneMember": cimIvrZoneMember,
       "civrZoneMemberNumber": civrZoneMemberNumber,
       "civrZoneMemberTable": civrZoneMemberTable,
       "civrZoneMemberEntry": civrZoneMemberEntry,
       "civrZoneMemberParentIndex": civrZoneMemberParentIndex,
       "civrZoneMemberIndex": civrZoneMemberIndex,
       "civrZoneMemberType": civrZoneMemberType,
       "civrZoneMemberID": civrZoneMemberID,
       "civrZoneMemberAFId": civrZoneMemberAFId,
       "civrZoneMemberVsan": civrZoneMemberVsan,
       "civrZoneMemberRowStatus": civrZoneMemberRowStatus,
       "civrZoneMemberLunID": civrZoneMemberLunID,
       "civrZoneEnforcedZoneMemberNumber": civrZoneEnforcedZoneMemberNumber,
       "civrZoneEnforcedZoneMemberTable": civrZoneEnforcedZoneMemberTable,
       "civrZoneEnforcedZoneMemberEntry": civrZoneEnforcedZoneMemberEntry,
       "civrZoneEnforcedZoneMemberType": civrZoneEnforcedZoneMemberType,
       "civrZoneEnforcedZoneMemberID": civrZoneEnforcedZoneMemberID,
       "civrZoneEnforcedZoneMemberAFId": civrZoneEnforcedZoneMemberAFId,
       "civrZoneEnforcedZoneMemberVsan": civrZoneEnforcedZoneMemberVsan,
       "civrZoneEnforcedZoneMemberLunID": civrZoneEnforcedZoneMemberLunID,
       "cimIvrTopology": cimIvrTopology,
       "civrTopologyConfiguredChecksum": civrTopologyConfiguredChecksum,
       "civrTopologyConfigTable": civrTopologyConfigTable,
       "civrTopologyConfigEntry": civrTopologyConfigEntry,
       "civrTopologyConfigSwitchWwn": civrTopologyConfigSwitchWwn,
       "civrTopologyConfigAutoFabricId": civrTopologyConfigAutoFabricId,
       "civrTopologyConfigSwitchVsan2k": civrTopologyConfigSwitchVsan2k,
       "civrTopologyConfigSwitchVsan4k": civrTopologyConfigSwitchVsan4k,
       "civrTopologyConfigRowStatus": civrTopologyConfigRowStatus,
       "civrTopologyActivate": civrTopologyActivate,
       "civrTopologyActivateTime": civrTopologyActivateTime,
       "civrTopologyCopyActiveToConfig": civrTopologyCopyActiveToConfig,
       "civrTopologyClearConfigured": civrTopologyClearConfigured,
       "civrTopologyActiveChecksum": civrTopologyActiveChecksum,
       "civrTopologyActiveTable": civrTopologyActiveTable,
       "civrTopologyActiveEntry": civrTopologyActiveEntry,
       "civrTopologyActiveSwitchWwn": civrTopologyActiveSwitchWwn,
       "civrTopologyActiveAutoFabricId": civrTopologyActiveAutoFabricId,
       "civrTopologyActiveSwitchVsan2k": civrTopologyActiveSwitchVsan2k,
       "civrTopologyActiveSwitchVsan4k": civrTopologyActiveSwitchVsan4k,
       "civrTopologyActive": civrTopologyActive,
       "civrTopologyAfidConfigChecksum": civrTopologyAfidConfigChecksum,
       "civrTopologyAfidConfTable": civrTopologyAfidConfTable,
       "civrTopologyAfidConfEntry": civrTopologyAfidConfEntry,
       "civrTopologyAfidConfSwitchWwn": civrTopologyAfidConfSwitchWwn,
       "civrTopologyAfidConfId": civrTopologyAfidConfId,
       "civrTopologyAfidConfSwitchVsan2k": civrTopologyAfidConfSwitchVsan2k,
       "civrTopologyAfidConfSwitchVsan4k": civrTopologyAfidConfSwitchVsan4k,
       "civrTopologyAfidConfRowStatus": civrTopologyAfidConfRowStatus,
       "civrTopologyDefaultAfidChecksum": civrTopologyDefaultAfidChecksum,
       "civrTopologyDefaultAfidTable": civrTopologyDefaultAfidTable,
       "civrTopologyDefaultAfidEntry": civrTopologyDefaultAfidEntry,
       "civrTopologyDefaultAfidSwitchWwn": civrTopologyDefaultAfidSwitchWwn,
       "civrTopologyDefaultAfidId": civrTopologyDefaultAfidId,
       "civrTopologyDefaultAfidStatus": civrTopologyDefaultAfidStatus,
       "civrTopologyIvrSrvGrpTable": civrTopologyIvrSrvGrpTable,
       "civrTopologyIvrSrvGrpEntry": civrTopologyIvrSrvGrpEntry,
       "civrTopologyIvrSrvGrpName": civrTopologyIvrSrvGrpName,
       "civrTopologyIvrSrvGrpVsan2k": civrTopologyIvrSrvGrpVsan2k,
       "civrTopologyIvrSrvGrpVsan4k": civrTopologyIvrSrvGrpVsan4k,
       "civrTopologyIvrSrvGrpRowStatus": civrTopologyIvrSrvGrpRowStatus,
       "civrTopologyClearAfidConfig": civrTopologyClearAfidConfig,
       "cimIvrVirtualDomains": cimIvrVirtualDomains,
       "civrAddIvrVirtualDomainsVsans2k": civrAddIvrVirtualDomainsVsans2k,
       "civrAddIvrVirtualDomainsVsans4k": civrAddIvrVirtualDomainsVsans4k,
       "cimIvrStats": cimIvrStats,
       "civrZoneSetStatusTable": civrZoneSetStatusTable,
       "civrZoneSetStatusEntry": civrZoneSetStatusEntry,
       "civrZoneSetStatus": civrZoneSetStatus,
       "civrEnabledDeviceTable": civrEnabledDeviceTable,
       "civrEnabledDeviceEntry": civrEnabledDeviceEntry,
       "civrEnabledDeviceVsan": civrEnabledDeviceVsan,
       "civrEnabledDeviceAutoFabricId": civrEnabledDeviceAutoFabricId,
       "civrEnabledDeviceDomainId": civrEnabledDeviceDomainId,
       "civrEnabledDeviceSwitchWwn": civrEnabledDeviceSwitchWwn,
       "civrEnabledDeviceCapability": civrEnabledDeviceCapability,
       "civrZoneMemberFabricId": civrZoneMemberFabricId,
       "civDomainIdConflictVsan": civDomainIdConflictVsan,
       "civrZoneSetActDeactPartialSucss": civrZoneSetActDeactPartialSucss,
       "civrAfidMisConfigVsan": civrAfidMisConfigVsan,
       "civrAfidMisConfigLocalAfid": civrAfidMisConfigLocalAfid,
       "civrAfidMisConfigRemoteAfid": civrAfidMisConfigRemoteAfid,
       "civrAfidMisConfigLocalSWwn": civrAfidMisConfigLocalSWwn,
       "civrAfidMisConfigRemoteSWwn": civrAfidMisConfigRemoteSWwn,
       "civrTopologyMisConfigReason": civrTopologyMisConfigReason,
       "ciscoIvrMIBConformance": ciscoIvrMIBConformance,
       "civrZoneServerMIBCompliances": civrZoneServerMIBCompliances,
       "civrZoneServerMIBCompliance": civrZoneServerMIBCompliance,
       "civrZoneServerMIBComplianceRev1": civrZoneServerMIBComplianceRev1,
       "civrZoneServerMIBComplianceRev2": civrZoneServerMIBComplianceRev2,
       "civrZoneServerMIBGroups": civrZoneServerMIBGroups,
       "civrZoneConfigurationGroup": civrZoneConfigurationGroup,
       "civrTopologyGroup": civrTopologyGroup,
       "civrStatsGroup": civrStatsGroup,
       "civrNotificationGroup": civrNotificationGroup,
       "civrVirtualDomainsGroup": civrVirtualDomainsGroup,
       "civrGenericGroup": civrGenericGroup,
       "civrTopologyGroupRev2": civrTopologyGroupRev2,
       "civrZoneConfigurationGroupRev2": civrZoneConfigurationGroupRev2,
       "civrNotificationGroupRev2": civrNotificationGroupRev2}
)
