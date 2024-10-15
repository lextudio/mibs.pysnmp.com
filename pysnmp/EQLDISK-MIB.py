# SNMP MIB module (EQLDISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLDISK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:02 2024
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

(eqlGroupId,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eqldiskModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 3)
)
eqldiskModule.setRevisions(
        ("2002-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqldiskObjects_ObjectIdentity = ObjectIdentity
eqldiskObjects = _EqldiskObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1)
)
_EqlDiskTable_Object = MibTable
eqlDiskTable = _EqlDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1)
)
if mibBuilder.loadTexts:
    eqlDiskTable.setStatus("current")
_EqlDiskEntry_Object = MibTableRow
eqlDiskEntry = _EqlDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1)
)
eqlDiskEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLDISK-MIB", "eqlDiskIndex"),
)
if mibBuilder.loadTexts:
    eqlDiskEntry.setStatus("current")
_EqlDiskIndex_Type = Integer32
_EqlDiskIndex_Object = MibTableColumn
eqlDiskIndex = _EqlDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 1),
    _EqlDiskIndex_Type()
)
eqlDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDiskIndex.setStatus("current")


class _EqlDiskType_Type(DisplayString):
    """Custom type eqlDiskType based on DisplayString"""
    defaultValue = OctetString("unknown disk type")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlDiskType_Type.__name__ = "DisplayString"
_EqlDiskType_Object = MibTableColumn
eqlDiskType = _EqlDiskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 2),
    _EqlDiskType_Type()
)
eqlDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskType.setStatus("current")


class _EqlDiskModelNumber_Type(DisplayString):
    """Custom type eqlDiskModelNumber based on DisplayString"""
    defaultValue = OctetString("unknown disk model")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EqlDiskModelNumber_Type.__name__ = "DisplayString"
_EqlDiskModelNumber_Object = MibTableColumn
eqlDiskModelNumber = _EqlDiskModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 3),
    _EqlDiskModelNumber_Type()
)
eqlDiskModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskModelNumber.setStatus("current")


class _EqlDiskRevisionNumber_Type(DisplayString):
    """Custom type eqlDiskRevisionNumber based on DisplayString"""
    defaultValue = OctetString("?firmrev")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EqlDiskRevisionNumber_Type.__name__ = "DisplayString"
_EqlDiskRevisionNumber_Object = MibTableColumn
eqlDiskRevisionNumber = _EqlDiskRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 4),
    _EqlDiskRevisionNumber_Type()
)
eqlDiskRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskRevisionNumber.setStatus("current")


class _EqlDiskSerialNumber_Type(DisplayString):
    """Custom type eqlDiskSerialNumber based on DisplayString"""
    defaultValue = OctetString("unknown serial#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EqlDiskSerialNumber_Type.__name__ = "DisplayString"
_EqlDiskSerialNumber_Object = MibTableColumn
eqlDiskSerialNumber = _EqlDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 5),
    _EqlDiskSerialNumber_Type()
)
eqlDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSerialNumber.setStatus("current")
_EqlDiskSize_Type = Integer32
_EqlDiskSize_Object = MibTableColumn
eqlDiskSize = _EqlDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 6),
    _EqlDiskSize_Type()
)
eqlDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSize.setStatus("current")


class _EqlDiskAdminStatus_Type(Integer32):
    """Custom type eqlDiskAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set-disk-off-line", 2),
          ("set-disk-on-line", 1),
          ("set-disk-spare", 3))
    )


_EqlDiskAdminStatus_Type.__name__ = "Integer32"
_EqlDiskAdminStatus_Object = MibTableColumn
eqlDiskAdminStatus = _EqlDiskAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 7),
    _EqlDiskAdminStatus_Type()
)
eqlDiskAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDiskAdminStatus.setStatus("current")


class _EqlDiskStatus_Type(Integer32):
    """Custom type eqlDiskStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("alt-sig", 5),
          ("encrypted", 11),
          ("failed", 3),
          ("history-of-failures", 7),
          ("notApproved", 12),
          ("off-line", 4),
          ("on-line", 1),
          ("preempt-failed", 13),
          ("replacement", 10),
          ("spare", 2),
          ("too-small", 6),
          ("unhealthy", 9),
          ("unsupported-version", 8))
    )


_EqlDiskStatus_Type.__name__ = "Integer32"
_EqlDiskStatus_Object = MibTableColumn
eqlDiskStatus = _EqlDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 8),
    _EqlDiskStatus_Type()
)
eqlDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatus.setStatus("current")
_EqlDiskErrors_Type = Counter32
_EqlDiskErrors_Object = MibTableColumn
eqlDiskErrors = _EqlDiskErrors_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 9),
    _EqlDiskErrors_Type()
)
eqlDiskErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrors.setStatus("current")
_EqlDiskId_Type = Integer32
_EqlDiskId_Object = MibTableColumn
eqlDiskId = _EqlDiskId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 10),
    _EqlDiskId_Type()
)
eqlDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskId.setStatus("current")


class _EqlDiskSlot_Type(Integer32):
    """Custom type eqlDiskSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_EqlDiskSlot_Type.__name__ = "Integer32"
_EqlDiskSlot_Object = MibTableColumn
eqlDiskSlot = _EqlDiskSlot_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 11),
    _EqlDiskSlot_Type()
)
eqlDiskSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSlot.setStatus("current")


class _EqlDiskTypeEnum_Type(Integer32):
    """Custom type eqlDiskTypeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sas", 2),
          ("sas-sed-hdd", 5),
          ("sas-sed-ssd", 6),
          ("sas-ssd", 4),
          ("sata", 1),
          ("sata-ssd", 3),
          ("unknown", 0))
    )


_EqlDiskTypeEnum_Type.__name__ = "Integer32"
_EqlDiskTypeEnum_Object = MibTableColumn
eqlDiskTypeEnum = _EqlDiskTypeEnum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 12),
    _EqlDiskTypeEnum_Type()
)
eqlDiskTypeEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskTypeEnum.setStatus("current")
_EqlDiskRPM_Type = Integer32
_EqlDiskRPM_Object = MibTableColumn
eqlDiskRPM = _EqlDiskRPM_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 13),
    _EqlDiskRPM_Type()
)
eqlDiskRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskRPM.setStatus("current")


class _EqlDiskSectorSize_Type(Integer32):
    """Custom type eqlDiskSectorSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sector-size-4096-bytes", 1),
          ("sector-size-512-bytes", 0),
          ("sector-size-unknown", 2))
    )


_EqlDiskSectorSize_Type.__name__ = "Integer32"
_EqlDiskSectorSize_Object = MibTableColumn
eqlDiskSectorSize = _EqlDiskSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 14),
    _EqlDiskSectorSize_Type()
)
eqlDiskSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSectorSize.setStatus("current")


class _EqlDiskManufacturingInfo_Type(DisplayString):
    """Custom type eqlDiskManufacturingInfo based on DisplayString"""
    defaultValue = OctetString("mfginfo?")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EqlDiskManufacturingInfo_Type.__name__ = "DisplayString"
_EqlDiskManufacturingInfo_Object = MibTableColumn
eqlDiskManufacturingInfo = _EqlDiskManufacturingInfo_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 15),
    _EqlDiskManufacturingInfo_Type()
)
eqlDiskManufacturingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskManufacturingInfo.setStatus("current")


class _EqlDiskPI_Type(Integer32):
    """Custom type eqlDiskPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pi-disabled", 0),
          ("pi-enabled", 1))
    )


_EqlDiskPI_Type.__name__ = "Integer32"
_EqlDiskPI_Object = MibTableColumn
eqlDiskPI = _EqlDiskPI_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 16),
    _EqlDiskPI_Type()
)
eqlDiskPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskPI.setStatus("current")


class _EqlDiskHealth_Type(Integer32):
    """Custom type eqlDiskHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("smart-ok", 1),
          ("smart-status-not-available", 0),
          ("smart-tripped", 2))
    )


_EqlDiskHealth_Type.__name__ = "Integer32"
_EqlDiskHealth_Object = MibTableColumn
eqlDiskHealth = _EqlDiskHealth_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 17),
    _EqlDiskHealth_Type()
)
eqlDiskHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskHealth.setStatus("current")
_EqlDiskStatusTable_Object = MibTable
eqlDiskStatusTable = _EqlDiskStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2)
)
if mibBuilder.loadTexts:
    eqlDiskStatusTable.setStatus("current")
_EqlDiskStatusEntry_Object = MibTableRow
eqlDiskStatusEntry = _EqlDiskStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eqlDiskStatusEntry.setStatus("current")
_EqlDiskStatusXfers_Type = Counter64
_EqlDiskStatusXfers_Object = MibTableColumn
eqlDiskStatusXfers = _EqlDiskStatusXfers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 1),
    _EqlDiskStatusXfers_Type()
)
eqlDiskStatusXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusXfers.setStatus("current")
_EqlDiskStatusBytesRead_Type = Counter64
_EqlDiskStatusBytesRead_Object = MibTableColumn
eqlDiskStatusBytesRead = _EqlDiskStatusBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 2),
    _EqlDiskStatusBytesRead_Type()
)
eqlDiskStatusBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusBytesRead.setStatus("current")
_EqlDiskStatusBytesWritten_Type = Counter64
_EqlDiskStatusBytesWritten_Object = MibTableColumn
eqlDiskStatusBytesWritten = _EqlDiskStatusBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 3),
    _EqlDiskStatusBytesWritten_Type()
)
eqlDiskStatusBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusBytesWritten.setStatus("current")
_EqlDiskStatusBusyTime_Type = Counter64
_EqlDiskStatusBusyTime_Object = MibTableColumn
eqlDiskStatusBusyTime = _EqlDiskStatusBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 4),
    _EqlDiskStatusBusyTime_Type()
)
eqlDiskStatusBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusBusyTime.setStatus("current")
_EqlDiskStatusNumIOs_Type = Counter32
_EqlDiskStatusNumIOs_Object = MibTableColumn
eqlDiskStatusNumIOs = _EqlDiskStatusNumIOs_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 5),
    _EqlDiskStatusNumIOs_Type()
)
eqlDiskStatusNumIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusNumIOs.setStatus("current")
_EqlDiskStatusFailXfers_Type = Counter32
_EqlDiskStatusFailXfers_Object = MibTableColumn
eqlDiskStatusFailXfers = _EqlDiskStatusFailXfers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 6),
    _EqlDiskStatusFailXfers_Type()
)
eqlDiskStatusFailXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusFailXfers.setStatus("current")
_EqlDiskStatusNumResets_Type = Counter32
_EqlDiskStatusNumResets_Object = MibTableColumn
eqlDiskStatusNumResets = _EqlDiskStatusNumResets_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 7),
    _EqlDiskStatusNumResets_Type()
)
eqlDiskStatusNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusNumResets.setStatus("current")
_EqlDiskStatusTotalQD_Type = Counter64
_EqlDiskStatusTotalQD_Object = MibTableColumn
eqlDiskStatusTotalQD = _EqlDiskStatusTotalQD_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 8),
    _EqlDiskStatusTotalQD_Type()
)
eqlDiskStatusTotalQD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusTotalQD.setStatus("current")
_EqlDiskStatusLifetime_Type = Integer32
_EqlDiskStatusLifetime_Object = MibTableColumn
eqlDiskStatusLifetime = _EqlDiskStatusLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 9),
    _EqlDiskStatusLifetime_Type()
)
eqlDiskStatusLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskStatusLifetime.setStatus("current")
_EqlDiskErrorTable_Object = MibTable
eqlDiskErrorTable = _EqlDiskErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3)
)
if mibBuilder.loadTexts:
    eqlDiskErrorTable.setStatus("current")
_EqlDiskErrorEntry_Object = MibTableRow
eqlDiskErrorEntry = _EqlDiskErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eqlDiskErrorEntry.setStatus("current")
_EqlDiskErrorPhyReady_Type = Counter32
_EqlDiskErrorPhyReady_Object = MibTableColumn
eqlDiskErrorPhyReady = _EqlDiskErrorPhyReady_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 1),
    _EqlDiskErrorPhyReady_Type()
)
eqlDiskErrorPhyReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorPhyReady.setStatus("current")
_EqlDiskErrorPhyInternal_Type = Counter32
_EqlDiskErrorPhyInternal_Object = MibTableColumn
eqlDiskErrorPhyInternal = _EqlDiskErrorPhyInternal_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 2),
    _EqlDiskErrorPhyInternal_Type()
)
eqlDiskErrorPhyInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorPhyInternal.setStatus("current")
_EqlDiskErrorCommWake_Type = Counter32
_EqlDiskErrorCommWake_Object = MibTableColumn
eqlDiskErrorCommWake = _EqlDiskErrorCommWake_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 3),
    _EqlDiskErrorCommWake_Type()
)
eqlDiskErrorCommWake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorCommWake.setStatus("current")
_EqlDiskErrorDecode10b8b_Type = Counter32
_EqlDiskErrorDecode10b8b_Object = MibTableColumn
eqlDiskErrorDecode10b8b = _EqlDiskErrorDecode10b8b_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 4),
    _EqlDiskErrorDecode10b8b_Type()
)
eqlDiskErrorDecode10b8b.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorDecode10b8b.setStatus("current")
_EqlDiskErrorDisparity_Type = Counter32
_EqlDiskErrorDisparity_Object = MibTableColumn
eqlDiskErrorDisparity = _EqlDiskErrorDisparity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 5),
    _EqlDiskErrorDisparity_Type()
)
eqlDiskErrorDisparity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorDisparity.setStatus("current")
_EqlDiskErrorCRC_Type = Counter32
_EqlDiskErrorCRC_Object = MibTableColumn
eqlDiskErrorCRC = _EqlDiskErrorCRC_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 6),
    _EqlDiskErrorCRC_Type()
)
eqlDiskErrorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorCRC.setStatus("current")
_EqlDiskErrorHandShake_Type = Counter32
_EqlDiskErrorHandShake_Object = MibTableColumn
eqlDiskErrorHandShake = _EqlDiskErrorHandShake_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 7),
    _EqlDiskErrorHandShake_Type()
)
eqlDiskErrorHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorHandShake.setStatus("current")
_EqlDiskErrorLinkSeq_Type = Counter32
_EqlDiskErrorLinkSeq_Object = MibTableColumn
eqlDiskErrorLinkSeq = _EqlDiskErrorLinkSeq_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 8),
    _EqlDiskErrorLinkSeq_Type()
)
eqlDiskErrorLinkSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorLinkSeq.setStatus("current")
_EqlDiskErrorTransportState_Type = Counter32
_EqlDiskErrorTransportState_Object = MibTableColumn
eqlDiskErrorTransportState = _EqlDiskErrorTransportState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 9),
    _EqlDiskErrorTransportState_Type()
)
eqlDiskErrorTransportState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorTransportState.setStatus("current")
_EqlDiskErrorUnrecFIS_Type = Counter32
_EqlDiskErrorUnrecFIS_Object = MibTableColumn
eqlDiskErrorUnrecFIS = _EqlDiskErrorUnrecFIS_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 10),
    _EqlDiskErrorUnrecFIS_Type()
)
eqlDiskErrorUnrecFIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskErrorUnrecFIS.setStatus("current")
_EqlDiskSmartInfoTable_Object = MibTable
eqlDiskSmartInfoTable = _EqlDiskSmartInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4)
)
if mibBuilder.loadTexts:
    eqlDiskSmartInfoTable.setStatus("current")
_EqlDiskSmartInfoEntry_Object = MibTableRow
eqlDiskSmartInfoEntry = _EqlDiskSmartInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eqlDiskSmartInfoEntry.setStatus("current")
_EqlDiskSmartInfoRawReadErrorRate_Type = Integer32
_EqlDiskSmartInfoRawReadErrorRate_Object = MibTableColumn
eqlDiskSmartInfoRawReadErrorRate = _EqlDiskSmartInfoRawReadErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 1),
    _EqlDiskSmartInfoRawReadErrorRate_Type()
)
eqlDiskSmartInfoRawReadErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoRawReadErrorRate.setStatus("current")
_EqlDiskSmartInfoRawReadErrorRateWorst_Type = Integer32
_EqlDiskSmartInfoRawReadErrorRateWorst_Object = MibTableColumn
eqlDiskSmartInfoRawReadErrorRateWorst = _EqlDiskSmartInfoRawReadErrorRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 2),
    _EqlDiskSmartInfoRawReadErrorRateWorst_Type()
)
eqlDiskSmartInfoRawReadErrorRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoRawReadErrorRateWorst.setStatus("current")
_EqlDiskSmartInfoThroughputPerformance_Type = Integer32
_EqlDiskSmartInfoThroughputPerformance_Object = MibTableColumn
eqlDiskSmartInfoThroughputPerformance = _EqlDiskSmartInfoThroughputPerformance_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 3),
    _EqlDiskSmartInfoThroughputPerformance_Type()
)
eqlDiskSmartInfoThroughputPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoThroughputPerformance.setStatus("current")
_EqlDiskSmartInfoThroughputPerformanceWorst_Type = Integer32
_EqlDiskSmartInfoThroughputPerformanceWorst_Object = MibTableColumn
eqlDiskSmartInfoThroughputPerformanceWorst = _EqlDiskSmartInfoThroughputPerformanceWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 4),
    _EqlDiskSmartInfoThroughputPerformanceWorst_Type()
)
eqlDiskSmartInfoThroughputPerformanceWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoThroughputPerformanceWorst.setStatus("current")
_EqlDiskSmartInfoSpinUpTime_Type = Integer32
_EqlDiskSmartInfoSpinUpTime_Object = MibTableColumn
eqlDiskSmartInfoSpinUpTime = _EqlDiskSmartInfoSpinUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 5),
    _EqlDiskSmartInfoSpinUpTime_Type()
)
eqlDiskSmartInfoSpinUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinUpTime.setStatus("current")
_EqlDiskSmartInfoSpinUpTimeWorst_Type = Integer32
_EqlDiskSmartInfoSpinUpTimeWorst_Object = MibTableColumn
eqlDiskSmartInfoSpinUpTimeWorst = _EqlDiskSmartInfoSpinUpTimeWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 6),
    _EqlDiskSmartInfoSpinUpTimeWorst_Type()
)
eqlDiskSmartInfoSpinUpTimeWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinUpTimeWorst.setStatus("current")
_EqlDiskSmartInfoStartStopCount_Type = Integer32
_EqlDiskSmartInfoStartStopCount_Object = MibTableColumn
eqlDiskSmartInfoStartStopCount = _EqlDiskSmartInfoStartStopCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 7),
    _EqlDiskSmartInfoStartStopCount_Type()
)
eqlDiskSmartInfoStartStopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoStartStopCount.setStatus("current")
_EqlDiskSmartInfoStartStopCountWorst_Type = Integer32
_EqlDiskSmartInfoStartStopCountWorst_Object = MibTableColumn
eqlDiskSmartInfoStartStopCountWorst = _EqlDiskSmartInfoStartStopCountWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 8),
    _EqlDiskSmartInfoStartStopCountWorst_Type()
)
eqlDiskSmartInfoStartStopCountWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoStartStopCountWorst.setStatus("current")
_EqlDiskSmartInfoReallocatedSectorCount_Type = Integer32
_EqlDiskSmartInfoReallocatedSectorCount_Object = MibTableColumn
eqlDiskSmartInfoReallocatedSectorCount = _EqlDiskSmartInfoReallocatedSectorCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 9),
    _EqlDiskSmartInfoReallocatedSectorCount_Type()
)
eqlDiskSmartInfoReallocatedSectorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoReallocatedSectorCount.setStatus("current")
_EqlDiskSmartInfoReallocatedSectorCountWorst_Type = Integer32
_EqlDiskSmartInfoReallocatedSectorCountWorst_Object = MibTableColumn
eqlDiskSmartInfoReallocatedSectorCountWorst = _EqlDiskSmartInfoReallocatedSectorCountWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 10),
    _EqlDiskSmartInfoReallocatedSectorCountWorst_Type()
)
eqlDiskSmartInfoReallocatedSectorCountWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoReallocatedSectorCountWorst.setStatus("current")
_EqlDiskSmartInfoReadChannelMargin_Type = Integer32
_EqlDiskSmartInfoReadChannelMargin_Object = MibTableColumn
eqlDiskSmartInfoReadChannelMargin = _EqlDiskSmartInfoReadChannelMargin_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 11),
    _EqlDiskSmartInfoReadChannelMargin_Type()
)
eqlDiskSmartInfoReadChannelMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoReadChannelMargin.setStatus("current")
_EqlDiskSmartInfoReadChannelMarginWorst_Type = Integer32
_EqlDiskSmartInfoReadChannelMarginWorst_Object = MibTableColumn
eqlDiskSmartInfoReadChannelMarginWorst = _EqlDiskSmartInfoReadChannelMarginWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 12),
    _EqlDiskSmartInfoReadChannelMarginWorst_Type()
)
eqlDiskSmartInfoReadChannelMarginWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoReadChannelMarginWorst.setStatus("current")
_EqlDiskSmartInfoSeekErrorRate_Type = Integer32
_EqlDiskSmartInfoSeekErrorRate_Object = MibTableColumn
eqlDiskSmartInfoSeekErrorRate = _EqlDiskSmartInfoSeekErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 13),
    _EqlDiskSmartInfoSeekErrorRate_Type()
)
eqlDiskSmartInfoSeekErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSeekErrorRate.setStatus("current")
_EqlDiskSmartInfoSeekErrorRateWorst_Type = Integer32
_EqlDiskSmartInfoSeekErrorRateWorst_Object = MibTableColumn
eqlDiskSmartInfoSeekErrorRateWorst = _EqlDiskSmartInfoSeekErrorRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 14),
    _EqlDiskSmartInfoSeekErrorRateWorst_Type()
)
eqlDiskSmartInfoSeekErrorRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSeekErrorRateWorst.setStatus("current")
_EqlDiskSmartInfoSeekPerformance_Type = Integer32
_EqlDiskSmartInfoSeekPerformance_Object = MibTableColumn
eqlDiskSmartInfoSeekPerformance = _EqlDiskSmartInfoSeekPerformance_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 15),
    _EqlDiskSmartInfoSeekPerformance_Type()
)
eqlDiskSmartInfoSeekPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSeekPerformance.setStatus("current")
_EqlDiskSmartInfoSeekPerformanceWorst_Type = Integer32
_EqlDiskSmartInfoSeekPerformanceWorst_Object = MibTableColumn
eqlDiskSmartInfoSeekPerformanceWorst = _EqlDiskSmartInfoSeekPerformanceWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 16),
    _EqlDiskSmartInfoSeekPerformanceWorst_Type()
)
eqlDiskSmartInfoSeekPerformanceWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSeekPerformanceWorst.setStatus("current")
_EqlDiskSmartInfoPowerOnHours_Type = Integer32
_EqlDiskSmartInfoPowerOnHours_Object = MibTableColumn
eqlDiskSmartInfoPowerOnHours = _EqlDiskSmartInfoPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 17),
    _EqlDiskSmartInfoPowerOnHours_Type()
)
eqlDiskSmartInfoPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoPowerOnHours.setStatus("current")
_EqlDiskSmartInfoPowerOnHoursWorst_Type = Integer32
_EqlDiskSmartInfoPowerOnHoursWorst_Object = MibTableColumn
eqlDiskSmartInfoPowerOnHoursWorst = _EqlDiskSmartInfoPowerOnHoursWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 18),
    _EqlDiskSmartInfoPowerOnHoursWorst_Type()
)
eqlDiskSmartInfoPowerOnHoursWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoPowerOnHoursWorst.setStatus("current")
_EqlDiskSmartInfoSpinupRetries_Type = Integer32
_EqlDiskSmartInfoSpinupRetries_Object = MibTableColumn
eqlDiskSmartInfoSpinupRetries = _EqlDiskSmartInfoSpinupRetries_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 19),
    _EqlDiskSmartInfoSpinupRetries_Type()
)
eqlDiskSmartInfoSpinupRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinupRetries.setStatus("current")
_EqlDiskSmartInfoSpinupRetriesWorst_Type = Integer32
_EqlDiskSmartInfoSpinupRetriesWorst_Object = MibTableColumn
eqlDiskSmartInfoSpinupRetriesWorst = _EqlDiskSmartInfoSpinupRetriesWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 20),
    _EqlDiskSmartInfoSpinupRetriesWorst_Type()
)
eqlDiskSmartInfoSpinupRetriesWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinupRetriesWorst.setStatus("current")
_EqlDiskSmartInfoDriveRecalibRetryCount_Type = Integer32
_EqlDiskSmartInfoDriveRecalibRetryCount_Object = MibTableColumn
eqlDiskSmartInfoDriveRecalibRetryCount = _EqlDiskSmartInfoDriveRecalibRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 21),
    _EqlDiskSmartInfoDriveRecalibRetryCount_Type()
)
eqlDiskSmartInfoDriveRecalibRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoDriveRecalibRetryCount.setStatus("current")
_EqlDiskSmartInfoDriveRecalibRetryCountWorst_Type = Integer32
_EqlDiskSmartInfoDriveRecalibRetryCountWorst_Object = MibTableColumn
eqlDiskSmartInfoDriveRecalibRetryCountWorst = _EqlDiskSmartInfoDriveRecalibRetryCountWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 22),
    _EqlDiskSmartInfoDriveRecalibRetryCountWorst_Type()
)
eqlDiskSmartInfoDriveRecalibRetryCountWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoDriveRecalibRetryCountWorst.setStatus("current")
_EqlDiskSmartInfoPowerCycleCount_Type = Integer32
_EqlDiskSmartInfoPowerCycleCount_Object = MibTableColumn
eqlDiskSmartInfoPowerCycleCount = _EqlDiskSmartInfoPowerCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 23),
    _EqlDiskSmartInfoPowerCycleCount_Type()
)
eqlDiskSmartInfoPowerCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoPowerCycleCount.setStatus("current")
_EqlDiskSmartInfoPowerCycleCountWorst_Type = Integer32
_EqlDiskSmartInfoPowerCycleCountWorst_Object = MibTableColumn
eqlDiskSmartInfoPowerCycleCountWorst = _EqlDiskSmartInfoPowerCycleCountWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 24),
    _EqlDiskSmartInfoPowerCycleCountWorst_Type()
)
eqlDiskSmartInfoPowerCycleCountWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoPowerCycleCountWorst.setStatus("current")
_EqlDiskSmartInfoReadSoftErrorRate_Type = Integer32
_EqlDiskSmartInfoReadSoftErrorRate_Object = MibTableColumn
eqlDiskSmartInfoReadSoftErrorRate = _EqlDiskSmartInfoReadSoftErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 25),
    _EqlDiskSmartInfoReadSoftErrorRate_Type()
)
eqlDiskSmartInfoReadSoftErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoReadSoftErrorRate.setStatus("current")
_EqlDiskSmartInfoReadSoftErrorRateWorst_Type = Integer32
_EqlDiskSmartInfoReadSoftErrorRateWorst_Object = MibTableColumn
eqlDiskSmartInfoReadSoftErrorRateWorst = _EqlDiskSmartInfoReadSoftErrorRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 26),
    _EqlDiskSmartInfoReadSoftErrorRateWorst_Type()
)
eqlDiskSmartInfoReadSoftErrorRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoReadSoftErrorRateWorst.setStatus("current")
_EqlDiskSmartInfoEmergencyRetractCycles_Type = Integer32
_EqlDiskSmartInfoEmergencyRetractCycles_Object = MibTableColumn
eqlDiskSmartInfoEmergencyRetractCycles = _EqlDiskSmartInfoEmergencyRetractCycles_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 27),
    _EqlDiskSmartInfoEmergencyRetractCycles_Type()
)
eqlDiskSmartInfoEmergencyRetractCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoEmergencyRetractCycles.setStatus("current")
_EqlDiskSmartInfoEmergencyRetractCyclesWorst_Type = Integer32
_EqlDiskSmartInfoEmergencyRetractCyclesWorst_Object = MibTableColumn
eqlDiskSmartInfoEmergencyRetractCyclesWorst = _EqlDiskSmartInfoEmergencyRetractCyclesWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 28),
    _EqlDiskSmartInfoEmergencyRetractCyclesWorst_Type()
)
eqlDiskSmartInfoEmergencyRetractCyclesWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoEmergencyRetractCyclesWorst.setStatus("current")
_EqlDiskSmartInfoLoadUnloadCycles_Type = Integer32
_EqlDiskSmartInfoLoadUnloadCycles_Object = MibTableColumn
eqlDiskSmartInfoLoadUnloadCycles = _EqlDiskSmartInfoLoadUnloadCycles_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 29),
    _EqlDiskSmartInfoLoadUnloadCycles_Type()
)
eqlDiskSmartInfoLoadUnloadCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoLoadUnloadCycles.setStatus("current")
_EqlDiskSmartInfoLoadUnloadCyclesWorst_Type = Integer32
_EqlDiskSmartInfoLoadUnloadCyclesWorst_Object = MibTableColumn
eqlDiskSmartInfoLoadUnloadCyclesWorst = _EqlDiskSmartInfoLoadUnloadCyclesWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 30),
    _EqlDiskSmartInfoLoadUnloadCyclesWorst_Type()
)
eqlDiskSmartInfoLoadUnloadCyclesWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoLoadUnloadCyclesWorst.setStatus("current")
_EqlDiskSmartInfoHDDTemp_Type = Integer32
_EqlDiskSmartInfoHDDTemp_Object = MibTableColumn
eqlDiskSmartInfoHDDTemp = _EqlDiskSmartInfoHDDTemp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 31),
    _EqlDiskSmartInfoHDDTemp_Type()
)
eqlDiskSmartInfoHDDTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoHDDTemp.setStatus("current")
_EqlDiskSmartInfoHDDTempWorst_Type = Integer32
_EqlDiskSmartInfoHDDTempWorst_Object = MibTableColumn
eqlDiskSmartInfoHDDTempWorst = _EqlDiskSmartInfoHDDTempWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 32),
    _EqlDiskSmartInfoHDDTempWorst_Type()
)
eqlDiskSmartInfoHDDTempWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoHDDTempWorst.setStatus("current")
_EqlDiskSmartInfoOnTheFlyErrorRate_Type = Integer32
_EqlDiskSmartInfoOnTheFlyErrorRate_Object = MibTableColumn
eqlDiskSmartInfoOnTheFlyErrorRate = _EqlDiskSmartInfoOnTheFlyErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 33),
    _EqlDiskSmartInfoOnTheFlyErrorRate_Type()
)
eqlDiskSmartInfoOnTheFlyErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOnTheFlyErrorRate.setStatus("current")
_EqlDiskSmartInfoOnTheFlyErrorRateWorst_Type = Integer32
_EqlDiskSmartInfoOnTheFlyErrorRateWorst_Object = MibTableColumn
eqlDiskSmartInfoOnTheFlyErrorRateWorst = _EqlDiskSmartInfoOnTheFlyErrorRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 34),
    _EqlDiskSmartInfoOnTheFlyErrorRateWorst_Type()
)
eqlDiskSmartInfoOnTheFlyErrorRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOnTheFlyErrorRateWorst.setStatus("current")
_EqlDiskSmartInfoSelfTestReallocSectors_Type = Integer32
_EqlDiskSmartInfoSelfTestReallocSectors_Object = MibTableColumn
eqlDiskSmartInfoSelfTestReallocSectors = _EqlDiskSmartInfoSelfTestReallocSectors_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 35),
    _EqlDiskSmartInfoSelfTestReallocSectors_Type()
)
eqlDiskSmartInfoSelfTestReallocSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSelfTestReallocSectors.setStatus("current")
_EqlDiskSmartInfoSelfTestReallocSectorsWorst_Type = Integer32
_EqlDiskSmartInfoSelfTestReallocSectorsWorst_Object = MibTableColumn
eqlDiskSmartInfoSelfTestReallocSectorsWorst = _EqlDiskSmartInfoSelfTestReallocSectorsWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 36),
    _EqlDiskSmartInfoSelfTestReallocSectorsWorst_Type()
)
eqlDiskSmartInfoSelfTestReallocSectorsWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSelfTestReallocSectorsWorst.setStatus("current")
_EqlDiskSmartInfoPendingDefects_Type = Integer32
_EqlDiskSmartInfoPendingDefects_Object = MibTableColumn
eqlDiskSmartInfoPendingDefects = _EqlDiskSmartInfoPendingDefects_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 37),
    _EqlDiskSmartInfoPendingDefects_Type()
)
eqlDiskSmartInfoPendingDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoPendingDefects.setStatus("current")
_EqlDiskSmartInfoPendingDefectsWorst_Type = Integer32
_EqlDiskSmartInfoPendingDefectsWorst_Object = MibTableColumn
eqlDiskSmartInfoPendingDefectsWorst = _EqlDiskSmartInfoPendingDefectsWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 38),
    _EqlDiskSmartInfoPendingDefectsWorst_Type()
)
eqlDiskSmartInfoPendingDefectsWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoPendingDefectsWorst.setStatus("current")
_EqlDiskSmartInfoOfflineSurfaceScan_Type = Integer32
_EqlDiskSmartInfoOfflineSurfaceScan_Object = MibTableColumn
eqlDiskSmartInfoOfflineSurfaceScan = _EqlDiskSmartInfoOfflineSurfaceScan_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 39),
    _EqlDiskSmartInfoOfflineSurfaceScan_Type()
)
eqlDiskSmartInfoOfflineSurfaceScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOfflineSurfaceScan.setStatus("current")
_EqlDiskSmartInfoOfflineSurfaceScanWorst_Type = Integer32
_EqlDiskSmartInfoOfflineSurfaceScanWorst_Object = MibTableColumn
eqlDiskSmartInfoOfflineSurfaceScanWorst = _EqlDiskSmartInfoOfflineSurfaceScanWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 40),
    _EqlDiskSmartInfoOfflineSurfaceScanWorst_Type()
)
eqlDiskSmartInfoOfflineSurfaceScanWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOfflineSurfaceScanWorst.setStatus("current")
_EqlDiskSmartInfoUltraDMACRCErrorRate_Type = Integer32
_EqlDiskSmartInfoUltraDMACRCErrorRate_Object = MibTableColumn
eqlDiskSmartInfoUltraDMACRCErrorRate = _EqlDiskSmartInfoUltraDMACRCErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 41),
    _EqlDiskSmartInfoUltraDMACRCErrorRate_Type()
)
eqlDiskSmartInfoUltraDMACRCErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoUltraDMACRCErrorRate.setStatus("current")
_EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Type = Integer32
_EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Object = MibTableColumn
eqlDiskSmartInfoUltraDMACRCErrorRateWorst = _EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 42),
    _EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Type()
)
eqlDiskSmartInfoUltraDMACRCErrorRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoUltraDMACRCErrorRateWorst.setStatus("current")
_EqlDiskSmartInfoWritePreampErrors_Type = Integer32
_EqlDiskSmartInfoWritePreampErrors_Object = MibTableColumn
eqlDiskSmartInfoWritePreampErrors = _EqlDiskSmartInfoWritePreampErrors_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 43),
    _EqlDiskSmartInfoWritePreampErrors_Type()
)
eqlDiskSmartInfoWritePreampErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoWritePreampErrors.setStatus("current")
_EqlDiskSmartInfoWritePreampErrorsWorst_Type = Integer32
_EqlDiskSmartInfoWritePreampErrorsWorst_Object = MibTableColumn
eqlDiskSmartInfoWritePreampErrorsWorst = _EqlDiskSmartInfoWritePreampErrorsWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 44),
    _EqlDiskSmartInfoWritePreampErrorsWorst_Type()
)
eqlDiskSmartInfoWritePreampErrorsWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoWritePreampErrorsWorst.setStatus("current")
_EqlDiskSmartInfoOffTrackErrors_Type = Integer32
_EqlDiskSmartInfoOffTrackErrors_Object = MibTableColumn
eqlDiskSmartInfoOffTrackErrors = _EqlDiskSmartInfoOffTrackErrors_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 45),
    _EqlDiskSmartInfoOffTrackErrors_Type()
)
eqlDiskSmartInfoOffTrackErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOffTrackErrors.setStatus("current")
_EqlDiskSmartInfoOffTrackErrorsWorst_Type = Integer32
_EqlDiskSmartInfoOffTrackErrorsWorst_Object = MibTableColumn
eqlDiskSmartInfoOffTrackErrorsWorst = _EqlDiskSmartInfoOffTrackErrorsWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 46),
    _EqlDiskSmartInfoOffTrackErrorsWorst_Type()
)
eqlDiskSmartInfoOffTrackErrorsWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOffTrackErrorsWorst.setStatus("current")
_EqlDiskSmartInfoDAMErrorRate_Type = Integer32
_EqlDiskSmartInfoDAMErrorRate_Object = MibTableColumn
eqlDiskSmartInfoDAMErrorRate = _EqlDiskSmartInfoDAMErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 47),
    _EqlDiskSmartInfoDAMErrorRate_Type()
)
eqlDiskSmartInfoDAMErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoDAMErrorRate.setStatus("current")
_EqlDiskSmartInfoDAMErrorRateWorst_Type = Integer32
_EqlDiskSmartInfoDAMErrorRateWorst_Object = MibTableColumn
eqlDiskSmartInfoDAMErrorRateWorst = _EqlDiskSmartInfoDAMErrorRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 48),
    _EqlDiskSmartInfoDAMErrorRateWorst_Type()
)
eqlDiskSmartInfoDAMErrorRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoDAMErrorRateWorst.setStatus("current")
_EqlDiskSmartInfoECCErrors_Type = Integer32
_EqlDiskSmartInfoECCErrors_Object = MibTableColumn
eqlDiskSmartInfoECCErrors = _EqlDiskSmartInfoECCErrors_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 49),
    _EqlDiskSmartInfoECCErrors_Type()
)
eqlDiskSmartInfoECCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoECCErrors.setStatus("current")
_EqlDiskSmartInfoECCErrorsWorst_Type = Integer32
_EqlDiskSmartInfoECCErrorsWorst_Object = MibTableColumn
eqlDiskSmartInfoECCErrorsWorst = _EqlDiskSmartInfoECCErrorsWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 50),
    _EqlDiskSmartInfoECCErrorsWorst_Type()
)
eqlDiskSmartInfoECCErrorsWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoECCErrorsWorst.setStatus("current")
_EqlDiskSmartInfoSoftECCCorrection_Type = Integer32
_EqlDiskSmartInfoSoftECCCorrection_Object = MibTableColumn
eqlDiskSmartInfoSoftECCCorrection = _EqlDiskSmartInfoSoftECCCorrection_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 51),
    _EqlDiskSmartInfoSoftECCCorrection_Type()
)
eqlDiskSmartInfoSoftECCCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSoftECCCorrection.setStatus("current")
_EqlDiskSmartInfoSoftECCCorrectionWorst_Type = Integer32
_EqlDiskSmartInfoSoftECCCorrectionWorst_Object = MibTableColumn
eqlDiskSmartInfoSoftECCCorrectionWorst = _EqlDiskSmartInfoSoftECCCorrectionWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 52),
    _EqlDiskSmartInfoSoftECCCorrectionWorst_Type()
)
eqlDiskSmartInfoSoftECCCorrectionWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSoftECCCorrectionWorst.setStatus("current")
_EqlDiskSmartInfoThermalAsperityRate_Type = Integer32
_EqlDiskSmartInfoThermalAsperityRate_Object = MibTableColumn
eqlDiskSmartInfoThermalAsperityRate = _EqlDiskSmartInfoThermalAsperityRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 53),
    _EqlDiskSmartInfoThermalAsperityRate_Type()
)
eqlDiskSmartInfoThermalAsperityRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoThermalAsperityRate.setStatus("current")
_EqlDiskSmartInfoThermalAsperityRateWorst_Type = Integer32
_EqlDiskSmartInfoThermalAsperityRateWorst_Object = MibTableColumn
eqlDiskSmartInfoThermalAsperityRateWorst = _EqlDiskSmartInfoThermalAsperityRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 54),
    _EqlDiskSmartInfoThermalAsperityRateWorst_Type()
)
eqlDiskSmartInfoThermalAsperityRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoThermalAsperityRateWorst.setStatus("current")
_EqlDiskSmartInfoSpinHighCount_Type = Integer32
_EqlDiskSmartInfoSpinHighCount_Object = MibTableColumn
eqlDiskSmartInfoSpinHighCount = _EqlDiskSmartInfoSpinHighCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 55),
    _EqlDiskSmartInfoSpinHighCount_Type()
)
eqlDiskSmartInfoSpinHighCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinHighCount.setStatus("current")
_EqlDiskSmartInfoSpinHighCountWorst_Type = Integer32
_EqlDiskSmartInfoSpinHighCountWorst_Object = MibTableColumn
eqlDiskSmartInfoSpinHighCountWorst = _EqlDiskSmartInfoSpinHighCountWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 56),
    _EqlDiskSmartInfoSpinHighCountWorst_Type()
)
eqlDiskSmartInfoSpinHighCountWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinHighCountWorst.setStatus("current")
_EqlDiskSmartInfoSpinBuzz_Type = Integer32
_EqlDiskSmartInfoSpinBuzz_Object = MibTableColumn
eqlDiskSmartInfoSpinBuzz = _EqlDiskSmartInfoSpinBuzz_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 57),
    _EqlDiskSmartInfoSpinBuzz_Type()
)
eqlDiskSmartInfoSpinBuzz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinBuzz.setStatus("current")
_EqlDiskSmartInfoSpinBuzzWorst_Type = Integer32
_EqlDiskSmartInfoSpinBuzzWorst_Object = MibTableColumn
eqlDiskSmartInfoSpinBuzzWorst = _EqlDiskSmartInfoSpinBuzzWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 58),
    _EqlDiskSmartInfoSpinBuzzWorst_Type()
)
eqlDiskSmartInfoSpinBuzzWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoSpinBuzzWorst.setStatus("current")
_EqlDiskSmartInfoOfflineSeekPerformance_Type = Integer32
_EqlDiskSmartInfoOfflineSeekPerformance_Object = MibTableColumn
eqlDiskSmartInfoOfflineSeekPerformance = _EqlDiskSmartInfoOfflineSeekPerformance_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 59),
    _EqlDiskSmartInfoOfflineSeekPerformance_Type()
)
eqlDiskSmartInfoOfflineSeekPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOfflineSeekPerformance.setStatus("current")
_EqlDiskSmartInfoOfflineSeekPerformanceWorst_Type = Integer32
_EqlDiskSmartInfoOfflineSeekPerformanceWorst_Object = MibTableColumn
eqlDiskSmartInfoOfflineSeekPerformanceWorst = _EqlDiskSmartInfoOfflineSeekPerformanceWorst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 60),
    _EqlDiskSmartInfoOfflineSeekPerformanceWorst_Type()
)
eqlDiskSmartInfoOfflineSeekPerformanceWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoOfflineSeekPerformanceWorst.setStatus("current")
_EqlDiskSmartInfoThresholdExceeded_Type = Integer32
_EqlDiskSmartInfoThresholdExceeded_Object = MibTableColumn
eqlDiskSmartInfoThresholdExceeded = _EqlDiskSmartInfoThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 61),
    _EqlDiskSmartInfoThresholdExceeded_Type()
)
eqlDiskSmartInfoThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDiskSmartInfoThresholdExceeded.setStatus("current")
_EqldiskNotifications_ObjectIdentity = ObjectIdentity
eqldiskNotifications = _EqldiskNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 3, 2)
)
_EqldiskMgmtNotifications_ObjectIdentity = ObjectIdentity
eqldiskMgmtNotifications = _EqldiskMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 3, 2, 1)
)
_EqldiskConformance_ObjectIdentity = ObjectIdentity
eqldiskConformance = _EqldiskConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 3, 3)
)
eqlDiskEntry.registerAugmentions(
    ("EQLDISK-MIB",
     "eqlDiskStatusEntry")
)
eqlDiskStatusEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
eqlDiskEntry.registerAugmentions(
    ("EQLDISK-MIB",
     "eqlDiskErrorEntry")
)
eqlDiskErrorEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
eqlDiskEntry.registerAugmentions(
    ("EQLDISK-MIB",
     "eqlDiskSmartInfoEntry")
)
eqlDiskSmartInfoEntry.setIndexNames(*eqlDiskEntry.getIndexNames())

# Managed Objects groups


# Notification objects

eqlDiskStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 3, 2, 1, 1)
)
eqlDiskStatusChange.setObjects(
      *(("EQLDISK-MIB", "eqlDiskStatus"),
        ("EQLDISK-MIB", "eqlDiskSlot"))
)
if mibBuilder.loadTexts:
    eqlDiskStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLDISK-MIB",
    **{"eqldiskModule": eqldiskModule,
       "eqldiskObjects": eqldiskObjects,
       "eqlDiskTable": eqlDiskTable,
       "eqlDiskEntry": eqlDiskEntry,
       "eqlDiskIndex": eqlDiskIndex,
       "eqlDiskType": eqlDiskType,
       "eqlDiskModelNumber": eqlDiskModelNumber,
       "eqlDiskRevisionNumber": eqlDiskRevisionNumber,
       "eqlDiskSerialNumber": eqlDiskSerialNumber,
       "eqlDiskSize": eqlDiskSize,
       "eqlDiskAdminStatus": eqlDiskAdminStatus,
       "eqlDiskStatus": eqlDiskStatus,
       "eqlDiskErrors": eqlDiskErrors,
       "eqlDiskId": eqlDiskId,
       "eqlDiskSlot": eqlDiskSlot,
       "eqlDiskTypeEnum": eqlDiskTypeEnum,
       "eqlDiskRPM": eqlDiskRPM,
       "eqlDiskSectorSize": eqlDiskSectorSize,
       "eqlDiskManufacturingInfo": eqlDiskManufacturingInfo,
       "eqlDiskPI": eqlDiskPI,
       "eqlDiskHealth": eqlDiskHealth,
       "eqlDiskStatusTable": eqlDiskStatusTable,
       "eqlDiskStatusEntry": eqlDiskStatusEntry,
       "eqlDiskStatusXfers": eqlDiskStatusXfers,
       "eqlDiskStatusBytesRead": eqlDiskStatusBytesRead,
       "eqlDiskStatusBytesWritten": eqlDiskStatusBytesWritten,
       "eqlDiskStatusBusyTime": eqlDiskStatusBusyTime,
       "eqlDiskStatusNumIOs": eqlDiskStatusNumIOs,
       "eqlDiskStatusFailXfers": eqlDiskStatusFailXfers,
       "eqlDiskStatusNumResets": eqlDiskStatusNumResets,
       "eqlDiskStatusTotalQD": eqlDiskStatusTotalQD,
       "eqlDiskStatusLifetime": eqlDiskStatusLifetime,
       "eqlDiskErrorTable": eqlDiskErrorTable,
       "eqlDiskErrorEntry": eqlDiskErrorEntry,
       "eqlDiskErrorPhyReady": eqlDiskErrorPhyReady,
       "eqlDiskErrorPhyInternal": eqlDiskErrorPhyInternal,
       "eqlDiskErrorCommWake": eqlDiskErrorCommWake,
       "eqlDiskErrorDecode10b8b": eqlDiskErrorDecode10b8b,
       "eqlDiskErrorDisparity": eqlDiskErrorDisparity,
       "eqlDiskErrorCRC": eqlDiskErrorCRC,
       "eqlDiskErrorHandShake": eqlDiskErrorHandShake,
       "eqlDiskErrorLinkSeq": eqlDiskErrorLinkSeq,
       "eqlDiskErrorTransportState": eqlDiskErrorTransportState,
       "eqlDiskErrorUnrecFIS": eqlDiskErrorUnrecFIS,
       "eqlDiskSmartInfoTable": eqlDiskSmartInfoTable,
       "eqlDiskSmartInfoEntry": eqlDiskSmartInfoEntry,
       "eqlDiskSmartInfoRawReadErrorRate": eqlDiskSmartInfoRawReadErrorRate,
       "eqlDiskSmartInfoRawReadErrorRateWorst": eqlDiskSmartInfoRawReadErrorRateWorst,
       "eqlDiskSmartInfoThroughputPerformance": eqlDiskSmartInfoThroughputPerformance,
       "eqlDiskSmartInfoThroughputPerformanceWorst": eqlDiskSmartInfoThroughputPerformanceWorst,
       "eqlDiskSmartInfoSpinUpTime": eqlDiskSmartInfoSpinUpTime,
       "eqlDiskSmartInfoSpinUpTimeWorst": eqlDiskSmartInfoSpinUpTimeWorst,
       "eqlDiskSmartInfoStartStopCount": eqlDiskSmartInfoStartStopCount,
       "eqlDiskSmartInfoStartStopCountWorst": eqlDiskSmartInfoStartStopCountWorst,
       "eqlDiskSmartInfoReallocatedSectorCount": eqlDiskSmartInfoReallocatedSectorCount,
       "eqlDiskSmartInfoReallocatedSectorCountWorst": eqlDiskSmartInfoReallocatedSectorCountWorst,
       "eqlDiskSmartInfoReadChannelMargin": eqlDiskSmartInfoReadChannelMargin,
       "eqlDiskSmartInfoReadChannelMarginWorst": eqlDiskSmartInfoReadChannelMarginWorst,
       "eqlDiskSmartInfoSeekErrorRate": eqlDiskSmartInfoSeekErrorRate,
       "eqlDiskSmartInfoSeekErrorRateWorst": eqlDiskSmartInfoSeekErrorRateWorst,
       "eqlDiskSmartInfoSeekPerformance": eqlDiskSmartInfoSeekPerformance,
       "eqlDiskSmartInfoSeekPerformanceWorst": eqlDiskSmartInfoSeekPerformanceWorst,
       "eqlDiskSmartInfoPowerOnHours": eqlDiskSmartInfoPowerOnHours,
       "eqlDiskSmartInfoPowerOnHoursWorst": eqlDiskSmartInfoPowerOnHoursWorst,
       "eqlDiskSmartInfoSpinupRetries": eqlDiskSmartInfoSpinupRetries,
       "eqlDiskSmartInfoSpinupRetriesWorst": eqlDiskSmartInfoSpinupRetriesWorst,
       "eqlDiskSmartInfoDriveRecalibRetryCount": eqlDiskSmartInfoDriveRecalibRetryCount,
       "eqlDiskSmartInfoDriveRecalibRetryCountWorst": eqlDiskSmartInfoDriveRecalibRetryCountWorst,
       "eqlDiskSmartInfoPowerCycleCount": eqlDiskSmartInfoPowerCycleCount,
       "eqlDiskSmartInfoPowerCycleCountWorst": eqlDiskSmartInfoPowerCycleCountWorst,
       "eqlDiskSmartInfoReadSoftErrorRate": eqlDiskSmartInfoReadSoftErrorRate,
       "eqlDiskSmartInfoReadSoftErrorRateWorst": eqlDiskSmartInfoReadSoftErrorRateWorst,
       "eqlDiskSmartInfoEmergencyRetractCycles": eqlDiskSmartInfoEmergencyRetractCycles,
       "eqlDiskSmartInfoEmergencyRetractCyclesWorst": eqlDiskSmartInfoEmergencyRetractCyclesWorst,
       "eqlDiskSmartInfoLoadUnloadCycles": eqlDiskSmartInfoLoadUnloadCycles,
       "eqlDiskSmartInfoLoadUnloadCyclesWorst": eqlDiskSmartInfoLoadUnloadCyclesWorst,
       "eqlDiskSmartInfoHDDTemp": eqlDiskSmartInfoHDDTemp,
       "eqlDiskSmartInfoHDDTempWorst": eqlDiskSmartInfoHDDTempWorst,
       "eqlDiskSmartInfoOnTheFlyErrorRate": eqlDiskSmartInfoOnTheFlyErrorRate,
       "eqlDiskSmartInfoOnTheFlyErrorRateWorst": eqlDiskSmartInfoOnTheFlyErrorRateWorst,
       "eqlDiskSmartInfoSelfTestReallocSectors": eqlDiskSmartInfoSelfTestReallocSectors,
       "eqlDiskSmartInfoSelfTestReallocSectorsWorst": eqlDiskSmartInfoSelfTestReallocSectorsWorst,
       "eqlDiskSmartInfoPendingDefects": eqlDiskSmartInfoPendingDefects,
       "eqlDiskSmartInfoPendingDefectsWorst": eqlDiskSmartInfoPendingDefectsWorst,
       "eqlDiskSmartInfoOfflineSurfaceScan": eqlDiskSmartInfoOfflineSurfaceScan,
       "eqlDiskSmartInfoOfflineSurfaceScanWorst": eqlDiskSmartInfoOfflineSurfaceScanWorst,
       "eqlDiskSmartInfoUltraDMACRCErrorRate": eqlDiskSmartInfoUltraDMACRCErrorRate,
       "eqlDiskSmartInfoUltraDMACRCErrorRateWorst": eqlDiskSmartInfoUltraDMACRCErrorRateWorst,
       "eqlDiskSmartInfoWritePreampErrors": eqlDiskSmartInfoWritePreampErrors,
       "eqlDiskSmartInfoWritePreampErrorsWorst": eqlDiskSmartInfoWritePreampErrorsWorst,
       "eqlDiskSmartInfoOffTrackErrors": eqlDiskSmartInfoOffTrackErrors,
       "eqlDiskSmartInfoOffTrackErrorsWorst": eqlDiskSmartInfoOffTrackErrorsWorst,
       "eqlDiskSmartInfoDAMErrorRate": eqlDiskSmartInfoDAMErrorRate,
       "eqlDiskSmartInfoDAMErrorRateWorst": eqlDiskSmartInfoDAMErrorRateWorst,
       "eqlDiskSmartInfoECCErrors": eqlDiskSmartInfoECCErrors,
       "eqlDiskSmartInfoECCErrorsWorst": eqlDiskSmartInfoECCErrorsWorst,
       "eqlDiskSmartInfoSoftECCCorrection": eqlDiskSmartInfoSoftECCCorrection,
       "eqlDiskSmartInfoSoftECCCorrectionWorst": eqlDiskSmartInfoSoftECCCorrectionWorst,
       "eqlDiskSmartInfoThermalAsperityRate": eqlDiskSmartInfoThermalAsperityRate,
       "eqlDiskSmartInfoThermalAsperityRateWorst": eqlDiskSmartInfoThermalAsperityRateWorst,
       "eqlDiskSmartInfoSpinHighCount": eqlDiskSmartInfoSpinHighCount,
       "eqlDiskSmartInfoSpinHighCountWorst": eqlDiskSmartInfoSpinHighCountWorst,
       "eqlDiskSmartInfoSpinBuzz": eqlDiskSmartInfoSpinBuzz,
       "eqlDiskSmartInfoSpinBuzzWorst": eqlDiskSmartInfoSpinBuzzWorst,
       "eqlDiskSmartInfoOfflineSeekPerformance": eqlDiskSmartInfoOfflineSeekPerformance,
       "eqlDiskSmartInfoOfflineSeekPerformanceWorst": eqlDiskSmartInfoOfflineSeekPerformanceWorst,
       "eqlDiskSmartInfoThresholdExceeded": eqlDiskSmartInfoThresholdExceeded,
       "eqldiskNotifications": eqldiskNotifications,
       "eqldiskMgmtNotifications": eqldiskMgmtNotifications,
       "eqlDiskStatusChange": eqlDiskStatusChange,
       "eqldiskConformance": eqldiskConformance}
)
