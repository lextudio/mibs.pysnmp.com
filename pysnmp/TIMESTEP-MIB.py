# SNMP MIB module (TIMESTEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMESTEP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:50 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

timestep = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1022)
)
timestep.setRevisions(
        ("1998-10-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PermitGate_ObjectIdentity = ObjectIdentity
permitGate = _PermitGate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 9)
)


class _PermitGateSerialNumber_Type(OctetString):
    """Custom type permitGateSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_PermitGateSerialNumber_Type.__name__ = "OctetString"
_PermitGateSerialNumber_Object = MibScalar
permitGateSerialNumber = _PermitGateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 1),
    _PermitGateSerialNumber_Type()
)
permitGateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateSerialNumber.setStatus("current")


class _PermitGateCpuUtilInst_Type(Integer32):
    """Custom type permitGateCpuUtilInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PermitGateCpuUtilInst_Type.__name__ = "Integer32"
_PermitGateCpuUtilInst_Object = MibScalar
permitGateCpuUtilInst = _PermitGateCpuUtilInst_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 2),
    _PermitGateCpuUtilInst_Type()
)
permitGateCpuUtilInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateCpuUtilInst.setStatus("current")


class _PermitGateCpuUtilAvg1Min_Type(Integer32):
    """Custom type permitGateCpuUtilAvg1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PermitGateCpuUtilAvg1Min_Type.__name__ = "Integer32"
_PermitGateCpuUtilAvg1Min_Object = MibScalar
permitGateCpuUtilAvg1Min = _PermitGateCpuUtilAvg1Min_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 3),
    _PermitGateCpuUtilAvg1Min_Type()
)
permitGateCpuUtilAvg1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateCpuUtilAvg1Min.setStatus("current")


class _PermitGateCpuUtilAvg5Min_Type(Integer32):
    """Custom type permitGateCpuUtilAvg5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PermitGateCpuUtilAvg5Min_Type.__name__ = "Integer32"
_PermitGateCpuUtilAvg5Min_Object = MibScalar
permitGateCpuUtilAvg5Min = _PermitGateCpuUtilAvg5Min_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 4),
    _PermitGateCpuUtilAvg5Min_Type()
)
permitGateCpuUtilAvg5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateCpuUtilAvg5Min.setStatus("current")
_PermitGateLastConfigModifTime_Type = TimeStamp
_PermitGateLastConfigModifTime_Object = MibScalar
permitGateLastConfigModifTime = _PermitGateLastConfigModifTime_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 5),
    _PermitGateLastConfigModifTime_Type()
)
permitGateLastConfigModifTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateLastConfigModifTime.setStatus("current")
_PermitGateTotalRebootNum_Type = Counter32
_PermitGateTotalRebootNum_Object = MibScalar
permitGateTotalRebootNum = _PermitGateTotalRebootNum_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 6),
    _PermitGateTotalRebootNum_Type()
)
permitGateTotalRebootNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateTotalRebootNum.setStatus("current")
_PermitGateTotalVolMemory_Type = Integer32
_PermitGateTotalVolMemory_Object = MibScalar
permitGateTotalVolMemory = _PermitGateTotalVolMemory_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 7),
    _PermitGateTotalVolMemory_Type()
)
permitGateTotalVolMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateTotalVolMemory.setStatus("current")
_PermitGateFreeVolMemory_Type = Integer32
_PermitGateFreeVolMemory_Object = MibScalar
permitGateFreeVolMemory = _PermitGateFreeVolMemory_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 8),
    _PermitGateFreeVolMemory_Type()
)
permitGateFreeVolMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateFreeVolMemory.setStatus("current")


class _PermitGateEncDevStatus_Type(Integer32):
    """Custom type permitGateEncDevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("notApplicable", 2),
          ("up", 0))
    )


_PermitGateEncDevStatus_Type.__name__ = "Integer32"
_PermitGateEncDevStatus_Object = MibScalar
permitGateEncDevStatus = _PermitGateEncDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 9),
    _PermitGateEncDevStatus_Type()
)
permitGateEncDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateEncDevStatus.setStatus("current")


class _PermitGateRandNumGenStatus_Type(Integer32):
    """Custom type permitGateRandNumGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("notApplicable", 2),
          ("up", 0))
    )


_PermitGateRandNumGenStatus_Type.__name__ = "Integer32"
_PermitGateRandNumGenStatus_Object = MibScalar
permitGateRandNumGenStatus = _PermitGateRandNumGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 10),
    _PermitGateRandNumGenStatus_Type()
)
permitGateRandNumGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateRandNumGenStatus.setStatus("current")
_PermitGateCertExpDate_Type = DateAndTime
_PermitGateCertExpDate_Object = MibScalar
permitGateCertExpDate = _PermitGateCertExpDate_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 11),
    _PermitGateCertExpDate_Type()
)
permitGateCertExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateCertExpDate.setStatus("current")
_PermitGateIfArpTable_Object = MibTable
permitGateIfArpTable = _PermitGateIfArpTable_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 12)
)
if mibBuilder.loadTexts:
    permitGateIfArpTable.setStatus("current")
_PermitGateIfArpEntry_Object = MibTableRow
permitGateIfArpEntry = _PermitGateIfArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 12, 1)
)
permitGateIfArpEntry.setIndexNames(
    (0, "TIMESTEP-MIB", "permitGateIfArpIndex"),
)
if mibBuilder.loadTexts:
    permitGateIfArpEntry.setStatus("current")
_PermitGateIfArpIndex_Type = Integer32
_PermitGateIfArpIndex_Object = MibTableColumn
permitGateIfArpIndex = _PermitGateIfArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 1),
    _PermitGateIfArpIndex_Type()
)
permitGateIfArpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateIfArpIndex.setStatus("current")
_PermitGateIfArpInPkts_Type = Counter32
_PermitGateIfArpInPkts_Object = MibTableColumn
permitGateIfArpInPkts = _PermitGateIfArpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 2),
    _PermitGateIfArpInPkts_Type()
)
permitGateIfArpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateIfArpInPkts.setStatus("current")
_PermitGateIfArpOutPkts_Type = Counter32
_PermitGateIfArpOutPkts_Object = MibTableColumn
permitGateIfArpOutPkts = _PermitGateIfArpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 3),
    _PermitGateIfArpOutPkts_Type()
)
permitGateIfArpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateIfArpOutPkts.setStatus("current")
_PermitGateIfArpInOctets_Type = Counter32
_PermitGateIfArpInOctets_Object = MibTableColumn
permitGateIfArpInOctets = _PermitGateIfArpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 4),
    _PermitGateIfArpInOctets_Type()
)
permitGateIfArpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateIfArpInOctets.setStatus("current")
_PermitGateIfArpOutOctets_Type = Counter32
_PermitGateIfArpOutOctets_Object = MibTableColumn
permitGateIfArpOutOctets = _PermitGateIfArpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 5),
    _PermitGateIfArpOutOctets_Type()
)
permitGateIfArpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permitGateIfArpOutOctets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMESTEP-MIB",
    **{"timestep": timestep,
       "permitGate": permitGate,
       "permitGateSerialNumber": permitGateSerialNumber,
       "permitGateCpuUtilInst": permitGateCpuUtilInst,
       "permitGateCpuUtilAvg1Min": permitGateCpuUtilAvg1Min,
       "permitGateCpuUtilAvg5Min": permitGateCpuUtilAvg5Min,
       "permitGateLastConfigModifTime": permitGateLastConfigModifTime,
       "permitGateTotalRebootNum": permitGateTotalRebootNum,
       "permitGateTotalVolMemory": permitGateTotalVolMemory,
       "permitGateFreeVolMemory": permitGateFreeVolMemory,
       "permitGateEncDevStatus": permitGateEncDevStatus,
       "permitGateRandNumGenStatus": permitGateRandNumGenStatus,
       "permitGateCertExpDate": permitGateCertExpDate,
       "permitGateIfArpTable": permitGateIfArpTable,
       "permitGateIfArpEntry": permitGateIfArpEntry,
       "permitGateIfArpIndex": permitGateIfArpIndex,
       "permitGateIfArpInPkts": permitGateIfArpInPkts,
       "permitGateIfArpOutPkts": permitGateIfArpOutPkts,
       "permitGateIfArpInOctets": permitGateIfArpInOctets,
       "permitGateIfArpOutOctets": permitGateIfArpOutOctets}
)
