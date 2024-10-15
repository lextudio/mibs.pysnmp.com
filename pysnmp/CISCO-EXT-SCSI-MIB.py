# SNMP MIB module (CISCO-EXT-SCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-EXT-SCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:04 2024
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

(ScsiIndexValue,
 ciscoScsiDscLunEntry,
 ciscoScsiDscTgtEntry,
 ciscoScsiInstanceEntry) = mibBuilder.importSymbols(
    "CISCO-SCSI-MIB",
    "ScsiIndexValue",
    "ciscoScsiDscLunEntry",
    "ciscoScsiDscTgtEntry",
    "ciscoScsiInstanceEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DomainId,
 FcAddressId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainId",
    "FcAddressId",
    "VsanIndex")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

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
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoExtScsiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299)
)
ciscoExtScsiMIB.setRevisions(
        ("2004-03-14 00:00",
         "2003-11-28 00:00",
         "2003-01-28 00:00",
         "2002-10-10 00:00",
         "2002-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LunDiscOS(Integer32, TextualConvention):
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
        *(("aix", 2),
          ("all", 6),
          ("hpux", 5),
          ("linux", 4),
          ("solaris", 3),
          ("windows", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoExtScsiMIBObjects_ObjectIdentity = ObjectIdentity
ciscoExtScsiMIBObjects = _CiscoExtScsiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1)
)
_CiscoExtScsiConfiguration_ObjectIdentity = ObjectIdentity
ciscoExtScsiConfiguration = _CiscoExtScsiConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1)
)
_CiscoExtScsiGenInstanceTable_Object = MibTable
ciscoExtScsiGenInstanceTable = _CiscoExtScsiGenInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoExtScsiGenInstanceTable.setStatus("current")
_CiscoExtScsiGenInstanceEntry_Object = MibTableRow
ciscoExtScsiGenInstanceEntry = _CiscoExtScsiGenInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoExtScsiGenInstanceEntry.setStatus("current")


class _CiscoExtScsiDiskGrpId_Type(OctetString):
    """Custom type ciscoExtScsiDiskGrpId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(64, 64),
    )


_CiscoExtScsiDiskGrpId_Type.__name__ = "OctetString"
_CiscoExtScsiDiskGrpId_Object = MibTableColumn
ciscoExtScsiDiskGrpId = _CiscoExtScsiDiskGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1, 1, 1),
    _CiscoExtScsiDiskGrpId_Type()
)
ciscoExtScsiDiskGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiDiskGrpId.setStatus("current")


class _CiscoExtScsiLineCardOrSup_Type(Unsigned32):
    """Custom type ciscoExtScsiLineCardOrSup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoExtScsiLineCardOrSup_Type.__name__ = "Unsigned32"
_CiscoExtScsiLineCardOrSup_Object = MibTableColumn
ciscoExtScsiLineCardOrSup = _CiscoExtScsiLineCardOrSup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1, 1, 2),
    _CiscoExtScsiLineCardOrSup_Type()
)
ciscoExtScsiLineCardOrSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiLineCardOrSup.setStatus("current")
_CiscoExtScsiLunDiscSpinLock_Type = TestAndIncr
_CiscoExtScsiLunDiscSpinLock_Object = MibScalar
ciscoExtScsiLunDiscSpinLock = _CiscoExtScsiLunDiscSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 2),
    _CiscoExtScsiLunDiscSpinLock_Type()
)
ciscoExtScsiLunDiscSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoExtScsiLunDiscSpinLock.setStatus("current")


class _CiscoExtScsiStartLunDisc_Type(Integer32):
    """Custom type ciscoExtScsiStartLunDisc based on Integer32"""
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
        *(("noop", 4),
          ("startDiscovery", 1),
          ("startLocalDiscovery", 2),
          ("startPartialDiscovery", 5),
          ("startPortBasedDiscovery", 6),
          ("startRemoteDiscovery", 3))
    )


_CiscoExtScsiStartLunDisc_Type.__name__ = "Integer32"
_CiscoExtScsiStartLunDisc_Object = MibScalar
ciscoExtScsiStartLunDisc = _CiscoExtScsiStartLunDisc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 3),
    _CiscoExtScsiStartLunDisc_Type()
)
ciscoExtScsiStartLunDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoExtScsiStartLunDisc.setStatus("current")


class _CiscoExtScsiLunDiscStatus_Type(Integer32):
    """Custom type ciscoExtScsiLunDiscStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 2),
          ("failure", 3),
          ("inProgress", 1))
    )


_CiscoExtScsiLunDiscStatus_Type.__name__ = "Integer32"
_CiscoExtScsiLunDiscStatus_Object = MibScalar
ciscoExtScsiLunDiscStatus = _CiscoExtScsiLunDiscStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 4),
    _CiscoExtScsiLunDiscStatus_Type()
)
ciscoExtScsiLunDiscStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiLunDiscStatus.setStatus("current")
_CiscoExtScsiLunDiscCompleteTime_Type = TimeStamp
_CiscoExtScsiLunDiscCompleteTime_Object = MibScalar
ciscoExtScsiLunDiscCompleteTime = _CiscoExtScsiLunDiscCompleteTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 5),
    _CiscoExtScsiLunDiscCompleteTime_Type()
)
ciscoExtScsiLunDiscCompleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiLunDiscCompleteTime.setStatus("current")
_CiscoExtScsiIntrDiscTgtTable_Object = MibTable
ciscoExtScsiIntrDiscTgtTable = _CiscoExtScsiIntrDiscTgtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtTable.setStatus("current")
_CiscoExtScsiIntrDiscTgtEntry_Object = MibTableRow
ciscoExtScsiIntrDiscTgtEntry = _CiscoExtScsiIntrDiscTgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtEntry.setStatus("current")
_CiscoExtScsiIntrDiscTgtVsanId_Type = VsanIndex
_CiscoExtScsiIntrDiscTgtVsanId_Object = MibTableColumn
ciscoExtScsiIntrDiscTgtVsanId = _CiscoExtScsiIntrDiscTgtVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 1),
    _CiscoExtScsiIntrDiscTgtVsanId_Type()
)
ciscoExtScsiIntrDiscTgtVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtVsanId.setStatus("current")
_CiscoExtScsiIntrDiscTgtDevType_Type = Unsigned32
_CiscoExtScsiIntrDiscTgtDevType_Object = MibTableColumn
ciscoExtScsiIntrDiscTgtDevType = _CiscoExtScsiIntrDiscTgtDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 2),
    _CiscoExtScsiIntrDiscTgtDevType_Type()
)
ciscoExtScsiIntrDiscTgtDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtDevType.setStatus("current")


class _CiscoExtScsiIntrDiscTgtVendorId_Type(OctetString):
    """Custom type ciscoExtScsiIntrDiscTgtVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CiscoExtScsiIntrDiscTgtVendorId_Type.__name__ = "OctetString"
_CiscoExtScsiIntrDiscTgtVendorId_Object = MibTableColumn
ciscoExtScsiIntrDiscTgtVendorId = _CiscoExtScsiIntrDiscTgtVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 3),
    _CiscoExtScsiIntrDiscTgtVendorId_Type()
)
ciscoExtScsiIntrDiscTgtVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtVendorId.setStatus("current")


class _CiscoExtScsiIntrDiscTgtProductId_Type(OctetString):
    """Custom type ciscoExtScsiIntrDiscTgtProductId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CiscoExtScsiIntrDiscTgtProductId_Type.__name__ = "OctetString"
_CiscoExtScsiIntrDiscTgtProductId_Object = MibTableColumn
ciscoExtScsiIntrDiscTgtProductId = _CiscoExtScsiIntrDiscTgtProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 4),
    _CiscoExtScsiIntrDiscTgtProductId_Type()
)
ciscoExtScsiIntrDiscTgtProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtProductId.setStatus("current")


class _CiscoExtScsiIntrDiscTgtRevLevel_Type(OctetString):
    """Custom type ciscoExtScsiIntrDiscTgtRevLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoExtScsiIntrDiscTgtRevLevel_Type.__name__ = "OctetString"
_CiscoExtScsiIntrDiscTgtRevLevel_Object = MibTableColumn
ciscoExtScsiIntrDiscTgtRevLevel = _CiscoExtScsiIntrDiscTgtRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 5),
    _CiscoExtScsiIntrDiscTgtRevLevel_Type()
)
ciscoExtScsiIntrDiscTgtRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtRevLevel.setStatus("current")


class _CiscoExtScsiIntrDiscTgtOtherInfo_Type(OctetString):
    """Custom type ciscoExtScsiIntrDiscTgtOtherInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CiscoExtScsiIntrDiscTgtOtherInfo_Type.__name__ = "OctetString"
_CiscoExtScsiIntrDiscTgtOtherInfo_Object = MibTableColumn
ciscoExtScsiIntrDiscTgtOtherInfo = _CiscoExtScsiIntrDiscTgtOtherInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 6),
    _CiscoExtScsiIntrDiscTgtOtherInfo_Type()
)
ciscoExtScsiIntrDiscTgtOtherInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscTgtOtherInfo.setStatus("current")
_CiscoExtScsiIntrDiscLunsTable_Object = MibTable
ciscoExtScsiIntrDiscLunsTable = _CiscoExtScsiIntrDiscLunsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunsTable.setStatus("current")
_CiscoExtScsiIntrDiscLunsEntry_Object = MibTableRow
ciscoExtScsiIntrDiscLunsEntry = _CiscoExtScsiIntrDiscLunsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunsEntry.setStatus("current")
_CiscoExtScsiIntrDiscLunCapacity_Type = Unsigned32
_CiscoExtScsiIntrDiscLunCapacity_Object = MibTableColumn
ciscoExtScsiIntrDiscLunCapacity = _CiscoExtScsiIntrDiscLunCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 1),
    _CiscoExtScsiIntrDiscLunCapacity_Type()
)
ciscoExtScsiIntrDiscLunCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunCapacity.setStatus("current")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunCapacity.setUnits("MBytes")


class _CiscoExtScsiIntrDiscLunNumber_Type(OctetString):
    """Custom type ciscoExtScsiIntrDiscLunNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CiscoExtScsiIntrDiscLunNumber_Type.__name__ = "OctetString"
_CiscoExtScsiIntrDiscLunNumber_Object = MibTableColumn
ciscoExtScsiIntrDiscLunNumber = _CiscoExtScsiIntrDiscLunNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 2),
    _CiscoExtScsiIntrDiscLunNumber_Type()
)
ciscoExtScsiIntrDiscLunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunNumber.setStatus("current")


class _CiscoExtScsiIntrDiscLunSerialNum_Type(OctetString):
    """Custom type ciscoExtScsiIntrDiscLunSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoExtScsiIntrDiscLunSerialNum_Type.__name__ = "OctetString"
_CiscoExtScsiIntrDiscLunSerialNum_Object = MibTableColumn
ciscoExtScsiIntrDiscLunSerialNum = _CiscoExtScsiIntrDiscLunSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 3),
    _CiscoExtScsiIntrDiscLunSerialNum_Type()
)
ciscoExtScsiIntrDiscLunSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunSerialNum.setStatus("current")
_CiscoExtScsiIntrDiscLunOs_Type = LunDiscOS
_CiscoExtScsiIntrDiscLunOs_Object = MibTableColumn
ciscoExtScsiIntrDiscLunOs = _CiscoExtScsiIntrDiscLunOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 4),
    _CiscoExtScsiIntrDiscLunOs_Type()
)
ciscoExtScsiIntrDiscLunOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunOs.setStatus("current")
_CiscoExtScsiIntrDiscLunPortId_Type = FcAddressId
_CiscoExtScsiIntrDiscLunPortId_Object = MibTableColumn
ciscoExtScsiIntrDiscLunPortId = _CiscoExtScsiIntrDiscLunPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 5),
    _CiscoExtScsiIntrDiscLunPortId_Type()
)
ciscoExtScsiIntrDiscLunPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiIntrDiscLunPortId.setStatus("current")


class _CiscoExtScsiNotificationCntl_Type(TruthValue):
    """Custom type ciscoExtScsiNotificationCntl based on TruthValue"""


_CiscoExtScsiNotificationCntl_Object = MibScalar
ciscoExtScsiNotificationCntl = _CiscoExtScsiNotificationCntl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 8),
    _CiscoExtScsiNotificationCntl_Type()
)
ciscoExtScsiNotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoExtScsiNotificationCntl.setStatus("current")
_CiscoExtScsiPartialLunDiscTable_Object = MibTable
ciscoExtScsiPartialLunDiscTable = _CiscoExtScsiPartialLunDiscTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoExtScsiPartialLunDiscTable.setStatus("current")
_CiscoExtScsiPartialLunDiscEntry_Object = MibTableRow
ciscoExtScsiPartialLunDiscEntry = _CiscoExtScsiPartialLunDiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9, 1)
)
ciscoExtScsiPartialLunDiscEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-EXT-SCSI-MIB", "ciscoExtScsiPartialLunDomId"),
)
if mibBuilder.loadTexts:
    ciscoExtScsiPartialLunDiscEntry.setStatus("current")
_CiscoExtScsiPartialLunDomId_Type = DomainId
_CiscoExtScsiPartialLunDomId_Object = MibTableColumn
ciscoExtScsiPartialLunDomId = _CiscoExtScsiPartialLunDomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9, 1, 1),
    _CiscoExtScsiPartialLunDomId_Type()
)
ciscoExtScsiPartialLunDomId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoExtScsiPartialLunDomId.setStatus("current")
_CiscoExtScsiPartialLunRowStatus_Type = RowStatus
_CiscoExtScsiPartialLunRowStatus_Object = MibTableColumn
ciscoExtScsiPartialLunRowStatus = _CiscoExtScsiPartialLunRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9, 1, 2),
    _CiscoExtScsiPartialLunRowStatus_Type()
)
ciscoExtScsiPartialLunRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoExtScsiPartialLunRowStatus.setStatus("current")


class _CiscoExtScsiLunDiscOs_Type(LunDiscOS):
    """Custom type ciscoExtScsiLunDiscOs based on LunDiscOS"""


_CiscoExtScsiLunDiscOs_Object = MibScalar
ciscoExtScsiLunDiscOs = _CiscoExtScsiLunDiscOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 10),
    _CiscoExtScsiLunDiscOs_Type()
)
ciscoExtScsiLunDiscOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoExtScsiLunDiscOs.setStatus("current")


class _CiscoExtScsiLunDiscVsanId_Type(VsanIndex):
    """Custom type ciscoExtScsiLunDiscVsanId based on VsanIndex"""
    defaultValue = 1


_CiscoExtScsiLunDiscVsanId_Object = MibScalar
ciscoExtScsiLunDiscVsanId = _CiscoExtScsiLunDiscVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 11),
    _CiscoExtScsiLunDiscVsanId_Type()
)
ciscoExtScsiLunDiscVsanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoExtScsiLunDiscVsanId.setStatus("current")


class _CiscoExtScsiLunDiscPortId_Type(FcAddressId):
    """Custom type ciscoExtScsiLunDiscPortId based on FcAddressId"""
    defaultHexValue = "000000"


_CiscoExtScsiLunDiscPortId_Object = MibScalar
ciscoExtScsiLunDiscPortId = _CiscoExtScsiLunDiscPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 12),
    _CiscoExtScsiLunDiscPortId_Type()
)
ciscoExtScsiLunDiscPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoExtScsiLunDiscPortId.setStatus("current")
_CiscoExtScsiLunCacheScsiIndex_Type = ScsiIndexValue
_CiscoExtScsiLunCacheScsiIndex_Object = MibScalar
ciscoExtScsiLunCacheScsiIndex = _CiscoExtScsiLunCacheScsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 13),
    _CiscoExtScsiLunCacheScsiIndex_Type()
)
ciscoExtScsiLunCacheScsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiLunCacheScsiIndex.setStatus("current")
_CiscoExtScsiLunCacheDevIndex_Type = ScsiIndexValue
_CiscoExtScsiLunCacheDevIndex_Object = MibScalar
ciscoExtScsiLunCacheDevIndex = _CiscoExtScsiLunCacheDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 14),
    _CiscoExtScsiLunCacheDevIndex_Type()
)
ciscoExtScsiLunCacheDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiLunCacheDevIndex.setStatus("current")
_CiscoExtScsiLunCachePortIndex_Type = ScsiIndexValue
_CiscoExtScsiLunCachePortIndex_Object = MibScalar
ciscoExtScsiLunCachePortIndex = _CiscoExtScsiLunCachePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 15),
    _CiscoExtScsiLunCachePortIndex_Type()
)
ciscoExtScsiLunCachePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiLunCachePortIndex.setStatus("current")
_CiscoExtScsiLunCacheTgtIndex_Type = ScsiIndexValue
_CiscoExtScsiLunCacheTgtIndex_Object = MibScalar
ciscoExtScsiLunCacheTgtIndex = _CiscoExtScsiLunCacheTgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 16),
    _CiscoExtScsiLunCacheTgtIndex_Type()
)
ciscoExtScsiLunCacheTgtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoExtScsiLunCacheTgtIndex.setStatus("current")


class _CiscoExtScsiDiscType_Type(Integer32):
    """Custom type ciscoExtScsiDiscType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("luns", 2),
          ("targets", 1))
    )


_CiscoExtScsiDiscType_Type.__name__ = "Integer32"
_CiscoExtScsiDiscType_Object = MibScalar
ciscoExtScsiDiscType = _CiscoExtScsiDiscType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 17),
    _CiscoExtScsiDiscType_Type()
)
ciscoExtScsiDiscType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoExtScsiDiscType.setStatus("current")
_CiscoExtScsiNotification_ObjectIdentity = ObjectIdentity
ciscoExtScsiNotification = _CiscoExtScsiNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 2)
)
_CiscoExtScsiNotifications_ObjectIdentity = ObjectIdentity
ciscoExtScsiNotifications = _CiscoExtScsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 2, 0)
)
_CiscoExtScsiStats_ObjectIdentity = ObjectIdentity
ciscoExtScsiStats = _CiscoExtScsiStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 3)
)
_CiscoExtScsiMIBConformance_ObjectIdentity = ObjectIdentity
ciscoExtScsiMIBConformance = _CiscoExtScsiMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2)
)
_CiscoExtScsiMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoExtScsiMIBCompliances = _CiscoExtScsiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1)
)
_CiscoExtScsiMIBGroups_ObjectIdentity = ObjectIdentity
ciscoExtScsiMIBGroups = _CiscoExtScsiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2)
)
ciscoScsiInstanceEntry.registerAugmentions(
    ("CISCO-EXT-SCSI-MIB",
     "ciscoExtScsiGenInstanceEntry")
)
ciscoExtScsiGenInstanceEntry.setIndexNames(*ciscoScsiInstanceEntry.getIndexNames())
ciscoScsiDscTgtEntry.registerAugmentions(
    ("CISCO-EXT-SCSI-MIB",
     "ciscoExtScsiIntrDiscTgtEntry")
)
ciscoExtScsiIntrDiscTgtEntry.setIndexNames(*ciscoScsiDscTgtEntry.getIndexNames())
ciscoScsiDscLunEntry.registerAugmentions(
    ("CISCO-EXT-SCSI-MIB",
     "ciscoExtScsiIntrDiscLunsEntry")
)
ciscoExtScsiIntrDiscLunsEntry.setIndexNames(*ciscoScsiDscLunEntry.getIndexNames())

# Managed Objects groups

ciscoExtScsiConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 1)
)
ciscoExtScsiConfigGroup.setObjects(
      *(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiskGrpId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLineCardOrSup"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscSpinLock"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiStartLunDisc"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscCompleteTime"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVsanId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtDevType"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVendorId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtProductId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtRevLevel"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtOtherInfo"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunCapacity"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunNumber"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunSerialNum"))
)
if mibBuilder.loadTexts:
    ciscoExtScsiConfigGroup.setStatus("deprecated")

ciscoExtScsiNotifyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 2)
)
ciscoExtScsiNotifyControlGroup.setObjects(
    ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotificationCntl")
)
if mibBuilder.loadTexts:
    ciscoExtScsiNotifyControlGroup.setStatus("current")

ciscoExtScsiPartialDiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 4)
)
ciscoExtScsiPartialDiscGroup.setObjects(
    ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiPartialLunRowStatus")
)
if mibBuilder.loadTexts:
    ciscoExtScsiPartialDiscGroup.setStatus("current")

ciscoExtScsiConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 5)
)
ciscoExtScsiConfigGroup1.setObjects(
      *(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiskGrpId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLineCardOrSup"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscSpinLock"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscOs"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiStartLunDisc"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscCompleteTime"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVsanId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtDevType"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVendorId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtProductId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtRevLevel"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtOtherInfo"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunCapacity"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunNumber"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunSerialNum"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunOs"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscVsanId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscPortId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheScsiIndex"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheDevIndex"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCachePortIndex"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheTgtIndex"))
)
if mibBuilder.loadTexts:
    ciscoExtScsiConfigGroup1.setStatus("deprecated")

ciscoExtScsiConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 6)
)
ciscoExtScsiConfigGroup2.setObjects(
      *(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiskGrpId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLineCardOrSup"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscSpinLock"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscOs"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiStartLunDisc"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscCompleteTime"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVsanId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtDevType"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVendorId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtProductId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtRevLevel"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtOtherInfo"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunCapacity"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunNumber"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunSerialNum"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunOs"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunPortId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscVsanId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscPortId"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheScsiIndex"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheDevIndex"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCachePortIndex"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheTgtIndex"),
        ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiscType"))
)
if mibBuilder.loadTexts:
    ciscoExtScsiConfigGroup2.setStatus("current")


# Notification objects

ciscoExtScsiLunDiscDoneNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 2, 0, 1)
)
ciscoExtScsiLunDiscDoneNotify.setObjects(
    ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus")
)
if mibBuilder.loadTexts:
    ciscoExtScsiLunDiscDoneNotify.setStatus(
        "current"
    )


# Notifications groups

ciscoExtScsiNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 3)
)
ciscoExtScsiNotifyGroup.setObjects(
    ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscDoneNotify")
)
if mibBuilder.loadTexts:
    ciscoExtScsiNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoExtScsiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoExtScsiMIBCompliance.setStatus(
        "deprecated"
    )

ciscoExtScsiMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoExtScsiMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoExtScsiMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoExtScsiMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoExtScsiMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoExtScsiMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-EXT-SCSI-MIB",
    **{"LunDiscOS": LunDiscOS,
       "ciscoExtScsiMIB": ciscoExtScsiMIB,
       "ciscoExtScsiMIBObjects": ciscoExtScsiMIBObjects,
       "ciscoExtScsiConfiguration": ciscoExtScsiConfiguration,
       "ciscoExtScsiGenInstanceTable": ciscoExtScsiGenInstanceTable,
       "ciscoExtScsiGenInstanceEntry": ciscoExtScsiGenInstanceEntry,
       "ciscoExtScsiDiskGrpId": ciscoExtScsiDiskGrpId,
       "ciscoExtScsiLineCardOrSup": ciscoExtScsiLineCardOrSup,
       "ciscoExtScsiLunDiscSpinLock": ciscoExtScsiLunDiscSpinLock,
       "ciscoExtScsiStartLunDisc": ciscoExtScsiStartLunDisc,
       "ciscoExtScsiLunDiscStatus": ciscoExtScsiLunDiscStatus,
       "ciscoExtScsiLunDiscCompleteTime": ciscoExtScsiLunDiscCompleteTime,
       "ciscoExtScsiIntrDiscTgtTable": ciscoExtScsiIntrDiscTgtTable,
       "ciscoExtScsiIntrDiscTgtEntry": ciscoExtScsiIntrDiscTgtEntry,
       "ciscoExtScsiIntrDiscTgtVsanId": ciscoExtScsiIntrDiscTgtVsanId,
       "ciscoExtScsiIntrDiscTgtDevType": ciscoExtScsiIntrDiscTgtDevType,
       "ciscoExtScsiIntrDiscTgtVendorId": ciscoExtScsiIntrDiscTgtVendorId,
       "ciscoExtScsiIntrDiscTgtProductId": ciscoExtScsiIntrDiscTgtProductId,
       "ciscoExtScsiIntrDiscTgtRevLevel": ciscoExtScsiIntrDiscTgtRevLevel,
       "ciscoExtScsiIntrDiscTgtOtherInfo": ciscoExtScsiIntrDiscTgtOtherInfo,
       "ciscoExtScsiIntrDiscLunsTable": ciscoExtScsiIntrDiscLunsTable,
       "ciscoExtScsiIntrDiscLunsEntry": ciscoExtScsiIntrDiscLunsEntry,
       "ciscoExtScsiIntrDiscLunCapacity": ciscoExtScsiIntrDiscLunCapacity,
       "ciscoExtScsiIntrDiscLunNumber": ciscoExtScsiIntrDiscLunNumber,
       "ciscoExtScsiIntrDiscLunSerialNum": ciscoExtScsiIntrDiscLunSerialNum,
       "ciscoExtScsiIntrDiscLunOs": ciscoExtScsiIntrDiscLunOs,
       "ciscoExtScsiIntrDiscLunPortId": ciscoExtScsiIntrDiscLunPortId,
       "ciscoExtScsiNotificationCntl": ciscoExtScsiNotificationCntl,
       "ciscoExtScsiPartialLunDiscTable": ciscoExtScsiPartialLunDiscTable,
       "ciscoExtScsiPartialLunDiscEntry": ciscoExtScsiPartialLunDiscEntry,
       "ciscoExtScsiPartialLunDomId": ciscoExtScsiPartialLunDomId,
       "ciscoExtScsiPartialLunRowStatus": ciscoExtScsiPartialLunRowStatus,
       "ciscoExtScsiLunDiscOs": ciscoExtScsiLunDiscOs,
       "ciscoExtScsiLunDiscVsanId": ciscoExtScsiLunDiscVsanId,
       "ciscoExtScsiLunDiscPortId": ciscoExtScsiLunDiscPortId,
       "ciscoExtScsiLunCacheScsiIndex": ciscoExtScsiLunCacheScsiIndex,
       "ciscoExtScsiLunCacheDevIndex": ciscoExtScsiLunCacheDevIndex,
       "ciscoExtScsiLunCachePortIndex": ciscoExtScsiLunCachePortIndex,
       "ciscoExtScsiLunCacheTgtIndex": ciscoExtScsiLunCacheTgtIndex,
       "ciscoExtScsiDiscType": ciscoExtScsiDiscType,
       "ciscoExtScsiNotification": ciscoExtScsiNotification,
       "ciscoExtScsiNotifications": ciscoExtScsiNotifications,
       "ciscoExtScsiLunDiscDoneNotify": ciscoExtScsiLunDiscDoneNotify,
       "ciscoExtScsiStats": ciscoExtScsiStats,
       "ciscoExtScsiMIBConformance": ciscoExtScsiMIBConformance,
       "ciscoExtScsiMIBCompliances": ciscoExtScsiMIBCompliances,
       "ciscoExtScsiMIBCompliance": ciscoExtScsiMIBCompliance,
       "ciscoExtScsiMIBCompliance2": ciscoExtScsiMIBCompliance2,
       "ciscoExtScsiMIBComplianceRev3": ciscoExtScsiMIBComplianceRev3,
       "ciscoExtScsiMIBComplianceRev4": ciscoExtScsiMIBComplianceRev4,
       "ciscoExtScsiMIBGroups": ciscoExtScsiMIBGroups,
       "ciscoExtScsiConfigGroup": ciscoExtScsiConfigGroup,
       "ciscoExtScsiNotifyControlGroup": ciscoExtScsiNotifyControlGroup,
       "ciscoExtScsiNotifyGroup": ciscoExtScsiNotifyGroup,
       "ciscoExtScsiPartialDiscGroup": ciscoExtScsiPartialDiscGroup,
       "ciscoExtScsiConfigGroup1": ciscoExtScsiConfigGroup1,
       "ciscoExtScsiConfigGroup2": ciscoExtScsiConfigGroup2}
)
