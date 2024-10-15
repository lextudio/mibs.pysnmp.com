# SNMP MIB module (CTRON-DECIV-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-DECIV-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:41 2024
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

(nwRtrProtoSuites,) = mibBuilder.importSymbols(
    "ROUTER-OIDS",
    "nwRtrProtoSuites")

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


# MODULE-IDENTITY


# Types definitions



class DecIVAddress(OctetString):
    """Custom type DecIVAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NwDecIVRouter_ObjectIdentity = ObjectIdentity
nwDecIVRouter = _NwDecIVRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3)
)
_NwDecIVMibs_ObjectIdentity = ObjectIdentity
nwDecIVMibs = _NwDecIVMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 1)
)
_NwDecIVMibRevText_Type = DisplayString
_NwDecIVMibRevText_Object = MibScalar
nwDecIVMibRevText = _NwDecIVMibRevText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 1, 1),
    _NwDecIVMibRevText_Type()
)
nwDecIVMibRevText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVMibRevText.setStatus("mandatory")
_NwDecIVComponents_ObjectIdentity = ObjectIdentity
nwDecIVComponents = _NwDecIVComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2)
)
_NwDecIVSystem_ObjectIdentity = ObjectIdentity
nwDecIVSystem = _NwDecIVSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1)
)
_NwDecIVSysConfig_ObjectIdentity = ObjectIdentity
nwDecIVSysConfig = _NwDecIVSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1)
)
_NwDecIVSysRouterId_Type = DecIVAddress
_NwDecIVSysRouterId_Object = MibScalar
nwDecIVSysRouterId = _NwDecIVSysRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 1),
    _NwDecIVSysRouterId_Type()
)
nwDecIVSysRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVSysRouterId.setStatus("mandatory")


class _NwDecIVNodeType_Type(Integer32):
    """Custom type nwDecIVNodeType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("area", 3),
          ("other", 1),
          ("routing-iv", 2))
    )


_NwDecIVNodeType_Type.__name__ = "Integer32"
_NwDecIVNodeType_Object = MibScalar
nwDecIVNodeType = _NwDecIVNodeType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 2),
    _NwDecIVNodeType_Type()
)
nwDecIVNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVNodeType.setStatus("mandatory")


class _NwDecIVMaxNodes_Type(Integer32):
    """Custom type nwDecIVMaxNodes based on Integer32"""
    defaultValue = 1023


_NwDecIVMaxNodes_Object = MibScalar
nwDecIVMaxNodes = _NwDecIVMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 3),
    _NwDecIVMaxNodes_Type()
)
nwDecIVMaxNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxNodes.setStatus("mandatory")


class _NwDecIVMaxBRA_Type(Integer32):
    """Custom type nwDecIVMaxBRA based on Integer32"""
    defaultValue = 16


_NwDecIVMaxBRA_Object = MibScalar
nwDecIVMaxBRA = _NwDecIVMaxBRA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 4),
    _NwDecIVMaxBRA_Type()
)
nwDecIVMaxBRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxBRA.setStatus("mandatory")


class _NwDecIVMaxBEA_Type(Integer32):
    """Custom type nwDecIVMaxBEA based on Integer32"""
    defaultValue = 64


_NwDecIVMaxBEA_Object = MibScalar
nwDecIVMaxBEA = _NwDecIVMaxBEA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 5),
    _NwDecIVMaxBEA_Type()
)
nwDecIVMaxBEA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxBEA.setStatus("mandatory")


class _NwDecIVMaxHops_Type(Integer32):
    """Custom type nwDecIVMaxHops based on Integer32"""
    defaultValue = 30


_NwDecIVMaxHops_Object = MibScalar
nwDecIVMaxHops = _NwDecIVMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 6),
    _NwDecIVMaxHops_Type()
)
nwDecIVMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxHops.setStatus("mandatory")


class _NwDecIVMaxCost_Type(Integer32):
    """Custom type nwDecIVMaxCost based on Integer32"""
    defaultValue = 1022


_NwDecIVMaxCost_Object = MibScalar
nwDecIVMaxCost = _NwDecIVMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 7),
    _NwDecIVMaxCost_Type()
)
nwDecIVMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxCost.setStatus("mandatory")


class _NwDecIVMaxVisits_Type(Integer32):
    """Custom type nwDecIVMaxVisits based on Integer32"""
    defaultValue = 63


_NwDecIVMaxVisits_Object = MibScalar
nwDecIVMaxVisits = _NwDecIVMaxVisits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 8),
    _NwDecIVMaxVisits_Type()
)
nwDecIVMaxVisits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxVisits.setStatus("mandatory")


class _NwDecIVNonBroadcastTimer_Type(TimeTicks):
    """Custom type nwDecIVNonBroadcastTimer based on TimeTicks"""
    defaultValue = 1000


_NwDecIVNonBroadcastTimer_Object = MibScalar
nwDecIVNonBroadcastTimer = _NwDecIVNonBroadcastTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 9),
    _NwDecIVNonBroadcastTimer_Type()
)
nwDecIVNonBroadcastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVNonBroadcastTimer.setStatus("mandatory")


class _NwDecIVBroadcastTimer_Type(TimeTicks):
    """Custom type nwDecIVBroadcastTimer based on TimeTicks"""
    defaultValue = 1000


_NwDecIVBroadcastTimer_Object = MibScalar
nwDecIVBroadcastTimer = _NwDecIVBroadcastTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 10),
    _NwDecIVBroadcastTimer_Type()
)
nwDecIVBroadcastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVBroadcastTimer.setStatus("mandatory")


class _NwDecIVAreas_Type(Integer32):
    """Custom type nwDecIVAreas based on Integer32"""
    defaultValue = 63


_NwDecIVAreas_Object = MibScalar
nwDecIVAreas = _NwDecIVAreas_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 11),
    _NwDecIVAreas_Type()
)
nwDecIVAreas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVAreas.setStatus("mandatory")


class _NwDecIVMaxAreaHops_Type(Integer32):
    """Custom type nwDecIVMaxAreaHops based on Integer32"""
    defaultValue = 30


_NwDecIVMaxAreaHops_Object = MibScalar
nwDecIVMaxAreaHops = _NwDecIVMaxAreaHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 12),
    _NwDecIVMaxAreaHops_Type()
)
nwDecIVMaxAreaHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxAreaHops.setStatus("mandatory")


class _NwDecIVMaxAreaCost_Type(Integer32):
    """Custom type nwDecIVMaxAreaCost based on Integer32"""
    defaultValue = 1022


_NwDecIVMaxAreaCost_Object = MibScalar
nwDecIVMaxAreaCost = _NwDecIVMaxAreaCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 1, 13),
    _NwDecIVMaxAreaCost_Type()
)
nwDecIVMaxAreaCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVMaxAreaCost.setStatus("mandatory")
_NwDecIVSysAdministration_ObjectIdentity = ObjectIdentity
nwDecIVSysAdministration = _NwDecIVSysAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 2)
)


class _NwDecIVSysAdminStatus_Type(Integer32):
    """Custom type nwDecIVSysAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVSysAdminStatus_Type.__name__ = "Integer32"
_NwDecIVSysAdminStatus_Object = MibScalar
nwDecIVSysAdminStatus = _NwDecIVSysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 2, 1),
    _NwDecIVSysAdminStatus_Type()
)
nwDecIVSysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVSysAdminStatus.setStatus("mandatory")


class _NwDecIVSysOperStatus_Type(Integer32):
    """Custom type nwDecIVSysOperStatus based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwDecIVSysOperStatus_Type.__name__ = "Integer32"
_NwDecIVSysOperStatus_Object = MibScalar
nwDecIVSysOperStatus = _NwDecIVSysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 2, 2),
    _NwDecIVSysOperStatus_Type()
)
nwDecIVSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVSysOperStatus.setStatus("mandatory")


class _NwDecIVSysAdminReset_Type(Integer32):
    """Custom type nwDecIVSysAdminReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwDecIVSysAdminReset_Type.__name__ = "Integer32"
_NwDecIVSysAdminReset_Object = MibScalar
nwDecIVSysAdminReset = _NwDecIVSysAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 2, 3),
    _NwDecIVSysAdminReset_Type()
)
nwDecIVSysAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVSysAdminReset.setStatus("mandatory")
_NwDecIVSysOperationalTime_Type = TimeTicks
_NwDecIVSysOperationalTime_Object = MibScalar
nwDecIVSysOperationalTime = _NwDecIVSysOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 2, 4),
    _NwDecIVSysOperationalTime_Type()
)
nwDecIVSysOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVSysOperationalTime.setStatus("mandatory")
_NwDecIVSysVersion_Type = DisplayString
_NwDecIVSysVersion_Object = MibScalar
nwDecIVSysVersion = _NwDecIVSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 1, 2, 5),
    _NwDecIVSysVersion_Type()
)
nwDecIVSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVSysVersion.setStatus("mandatory")
_NwDecIVForwarding_ObjectIdentity = ObjectIdentity
nwDecIVForwarding = _NwDecIVForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2)
)
_NwDecIVFwdSystem_ObjectIdentity = ObjectIdentity
nwDecIVFwdSystem = _NwDecIVFwdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1)
)
_NwDecIVFwdCounters_ObjectIdentity = ObjectIdentity
nwDecIVFwdCounters = _NwDecIVFwdCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1)
)


class _NwDecIVFwdCtrAdminStatus_Type(Integer32):
    """Custom type nwDecIVFwdCtrAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVFwdCtrAdminStatus_Type.__name__ = "Integer32"
_NwDecIVFwdCtrAdminStatus_Object = MibScalar
nwDecIVFwdCtrAdminStatus = _NwDecIVFwdCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 1),
    _NwDecIVFwdCtrAdminStatus_Type()
)
nwDecIVFwdCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrAdminStatus.setStatus("mandatory")


class _NwDecIVFwdCtrReset_Type(Integer32):
    """Custom type nwDecIVFwdCtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwDecIVFwdCtrReset_Type.__name__ = "Integer32"
_NwDecIVFwdCtrReset_Object = MibScalar
nwDecIVFwdCtrReset = _NwDecIVFwdCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 2),
    _NwDecIVFwdCtrReset_Type()
)
nwDecIVFwdCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrReset.setStatus("mandatory")
_NwDecIVFwdCtrOperationalTime_Type = TimeTicks
_NwDecIVFwdCtrOperationalTime_Object = MibScalar
nwDecIVFwdCtrOperationalTime = _NwDecIVFwdCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 3),
    _NwDecIVFwdCtrOperationalTime_Type()
)
nwDecIVFwdCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrOperationalTime.setStatus("mandatory")
_NwDecIVFwdCtrInPkts_Type = Counter32
_NwDecIVFwdCtrInPkts_Object = MibScalar
nwDecIVFwdCtrInPkts = _NwDecIVFwdCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 4),
    _NwDecIVFwdCtrInPkts_Type()
)
nwDecIVFwdCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrInPkts.setStatus("mandatory")
_NwDecIVFwdCtrOutPkts_Type = Counter32
_NwDecIVFwdCtrOutPkts_Object = MibScalar
nwDecIVFwdCtrOutPkts = _NwDecIVFwdCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 5),
    _NwDecIVFwdCtrOutPkts_Type()
)
nwDecIVFwdCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrOutPkts.setStatus("mandatory")
_NwDecIVFwdCtrFwdPkts_Type = Counter32
_NwDecIVFwdCtrFwdPkts_Object = MibScalar
nwDecIVFwdCtrFwdPkts = _NwDecIVFwdCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 6),
    _NwDecIVFwdCtrFwdPkts_Type()
)
nwDecIVFwdCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrFwdPkts.setStatus("mandatory")
_NwDecIVFwdCtrFilteredPkts_Type = Counter32
_NwDecIVFwdCtrFilteredPkts_Object = MibScalar
nwDecIVFwdCtrFilteredPkts = _NwDecIVFwdCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 7),
    _NwDecIVFwdCtrFilteredPkts_Type()
)
nwDecIVFwdCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrFilteredPkts.setStatus("mandatory")
_NwDecIVFwdCtrDiscardPkts_Type = Counter32
_NwDecIVFwdCtrDiscardPkts_Object = MibScalar
nwDecIVFwdCtrDiscardPkts = _NwDecIVFwdCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 8),
    _NwDecIVFwdCtrDiscardPkts_Type()
)
nwDecIVFwdCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrDiscardPkts.setStatus("mandatory")
_NwDecIVFwdCtrAddrErrPkts_Type = Counter32
_NwDecIVFwdCtrAddrErrPkts_Object = MibScalar
nwDecIVFwdCtrAddrErrPkts = _NwDecIVFwdCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 9),
    _NwDecIVFwdCtrAddrErrPkts_Type()
)
nwDecIVFwdCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrAddrErrPkts.setStatus("mandatory")
_NwDecIVFwdCtrLenErrPkts_Type = Counter32
_NwDecIVFwdCtrLenErrPkts_Object = MibScalar
nwDecIVFwdCtrLenErrPkts = _NwDecIVFwdCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 10),
    _NwDecIVFwdCtrLenErrPkts_Type()
)
nwDecIVFwdCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrLenErrPkts.setStatus("mandatory")
_NwDecIVFwdCtrHdrErrPkts_Type = Counter32
_NwDecIVFwdCtrHdrErrPkts_Object = MibScalar
nwDecIVFwdCtrHdrErrPkts = _NwDecIVFwdCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 11),
    _NwDecIVFwdCtrHdrErrPkts_Type()
)
nwDecIVFwdCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrHdrErrPkts.setStatus("mandatory")
_NwDecIVFwdCtrInBytes_Type = Counter32
_NwDecIVFwdCtrInBytes_Object = MibScalar
nwDecIVFwdCtrInBytes = _NwDecIVFwdCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 12),
    _NwDecIVFwdCtrInBytes_Type()
)
nwDecIVFwdCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrInBytes.setStatus("mandatory")
_NwDecIVFwdCtrOutBytes_Type = Counter32
_NwDecIVFwdCtrOutBytes_Object = MibScalar
nwDecIVFwdCtrOutBytes = _NwDecIVFwdCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 13),
    _NwDecIVFwdCtrOutBytes_Type()
)
nwDecIVFwdCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrOutBytes.setStatus("mandatory")
_NwDecIVFwdCtrFwdBytes_Type = Counter32
_NwDecIVFwdCtrFwdBytes_Object = MibScalar
nwDecIVFwdCtrFwdBytes = _NwDecIVFwdCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 14),
    _NwDecIVFwdCtrFwdBytes_Type()
)
nwDecIVFwdCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrFwdBytes.setStatus("mandatory")
_NwDecIVFwdCtrFilteredBytes_Type = Counter32
_NwDecIVFwdCtrFilteredBytes_Object = MibScalar
nwDecIVFwdCtrFilteredBytes = _NwDecIVFwdCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 15),
    _NwDecIVFwdCtrFilteredBytes_Type()
)
nwDecIVFwdCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrFilteredBytes.setStatus("mandatory")
_NwDecIVFwdCtrDiscardBytes_Type = Counter32
_NwDecIVFwdCtrDiscardBytes_Object = MibScalar
nwDecIVFwdCtrDiscardBytes = _NwDecIVFwdCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 16),
    _NwDecIVFwdCtrDiscardBytes_Type()
)
nwDecIVFwdCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrDiscardBytes.setStatus("mandatory")
_NwDecIVFwdCtrHostInPkts_Type = Counter32
_NwDecIVFwdCtrHostInPkts_Object = MibScalar
nwDecIVFwdCtrHostInPkts = _NwDecIVFwdCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 17),
    _NwDecIVFwdCtrHostInPkts_Type()
)
nwDecIVFwdCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrHostInPkts.setStatus("mandatory")
_NwDecIVFwdCtrHostOutPkts_Type = Counter32
_NwDecIVFwdCtrHostOutPkts_Object = MibScalar
nwDecIVFwdCtrHostOutPkts = _NwDecIVFwdCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 18),
    _NwDecIVFwdCtrHostOutPkts_Type()
)
nwDecIVFwdCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrHostOutPkts.setStatus("mandatory")
_NwDecIVFwdCtrHostDiscardPkts_Type = Counter32
_NwDecIVFwdCtrHostDiscardPkts_Object = MibScalar
nwDecIVFwdCtrHostDiscardPkts = _NwDecIVFwdCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 19),
    _NwDecIVFwdCtrHostDiscardPkts_Type()
)
nwDecIVFwdCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrHostDiscardPkts.setStatus("mandatory")
_NwDecIVFwdCtrHostInBytes_Type = Counter32
_NwDecIVFwdCtrHostInBytes_Object = MibScalar
nwDecIVFwdCtrHostInBytes = _NwDecIVFwdCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 20),
    _NwDecIVFwdCtrHostInBytes_Type()
)
nwDecIVFwdCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrHostInBytes.setStatus("mandatory")
_NwDecIVFwdCtrHostOutBytes_Type = Counter32
_NwDecIVFwdCtrHostOutBytes_Object = MibScalar
nwDecIVFwdCtrHostOutBytes = _NwDecIVFwdCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 21),
    _NwDecIVFwdCtrHostOutBytes_Type()
)
nwDecIVFwdCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrHostOutBytes.setStatus("mandatory")
_NwDecIVFwdCtrHostDiscardBytes_Type = Counter32
_NwDecIVFwdCtrHostDiscardBytes_Object = MibScalar
nwDecIVFwdCtrHostDiscardBytes = _NwDecIVFwdCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 1, 1, 22),
    _NwDecIVFwdCtrHostDiscardBytes_Type()
)
nwDecIVFwdCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdCtrHostDiscardBytes.setStatus("mandatory")
_NwDecIVFwdInterfaces_ObjectIdentity = ObjectIdentity
nwDecIVFwdInterfaces = _NwDecIVFwdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2)
)
_NwDecIVFwdIfConfig_ObjectIdentity = ObjectIdentity
nwDecIVFwdIfConfig = _NwDecIVFwdIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1)
)
_NwDecIVFwdIfTable_Object = MibTable
nwDecIVFwdIfTable = _NwDecIVFwdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwDecIVFwdIfTable.setStatus("mandatory")
_NwDecIVFwdIfEntry_Object = MibTableRow
nwDecIVFwdIfEntry = _NwDecIVFwdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1)
)
nwDecIVFwdIfEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVFwdIfIndex"),
)
if mibBuilder.loadTexts:
    nwDecIVFwdIfEntry.setStatus("mandatory")
_NwDecIVFwdIfIndex_Type = Integer32
_NwDecIVFwdIfIndex_Object = MibTableColumn
nwDecIVFwdIfIndex = _NwDecIVFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1),
    _NwDecIVFwdIfIndex_Type()
)
nwDecIVFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfIndex.setStatus("mandatory")


class _NwDecIVFwdIfAdminStatus_Type(Integer32):
    """Custom type nwDecIVFwdIfAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVFwdIfAdminStatus_Type.__name__ = "Integer32"
_NwDecIVFwdIfAdminStatus_Object = MibTableColumn
nwDecIVFwdIfAdminStatus = _NwDecIVFwdIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 2),
    _NwDecIVFwdIfAdminStatus_Type()
)
nwDecIVFwdIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfAdminStatus.setStatus("mandatory")


class _NwDecIVFwdIfOperStatus_Type(Integer32):
    """Custom type nwDecIVFwdIfOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwDecIVFwdIfOperStatus_Type.__name__ = "Integer32"
_NwDecIVFwdIfOperStatus_Object = MibTableColumn
nwDecIVFwdIfOperStatus = _NwDecIVFwdIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 3),
    _NwDecIVFwdIfOperStatus_Type()
)
nwDecIVFwdIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfOperStatus.setStatus("mandatory")
_NwDecIVFwdIfOperationalTime_Type = TimeTicks
_NwDecIVFwdIfOperationalTime_Object = MibTableColumn
nwDecIVFwdIfOperationalTime = _NwDecIVFwdIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 4),
    _NwDecIVFwdIfOperationalTime_Type()
)
nwDecIVFwdIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfOperationalTime.setStatus("mandatory")


class _NwDecIVFwdIfControl_Type(Integer32):
    """Custom type nwDecIVFwdIfControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("other", 1))
    )


_NwDecIVFwdIfControl_Type.__name__ = "Integer32"
_NwDecIVFwdIfControl_Object = MibTableColumn
nwDecIVFwdIfControl = _NwDecIVFwdIfControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 5),
    _NwDecIVFwdIfControl_Type()
)
nwDecIVFwdIfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfControl.setStatus("mandatory")


class _NwDecIVFwdIfMtu_Type(Integer32):
    """Custom type nwDecIVFwdIfMtu based on Integer32"""
    defaultValue = 1500


_NwDecIVFwdIfMtu_Object = MibTableColumn
nwDecIVFwdIfMtu = _NwDecIVFwdIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 6),
    _NwDecIVFwdIfMtu_Type()
)
nwDecIVFwdIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfMtu.setStatus("mandatory")


class _NwDecIVFwdIfForwarding_Type(Integer32):
    """Custom type nwDecIVFwdIfForwarding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVFwdIfForwarding_Type.__name__ = "Integer32"
_NwDecIVFwdIfForwarding_Object = MibTableColumn
nwDecIVFwdIfForwarding = _NwDecIVFwdIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 7),
    _NwDecIVFwdIfForwarding_Type()
)
nwDecIVFwdIfForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfForwarding.setStatus("mandatory")


class _NwDecIVFwdIfFrameType_Type(Integer32):
    """Custom type nwDecIVFwdIfFrameType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              9,
              11,
              14,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 17),
          ("encapenet", 9),
          ("encapenetsnap", 11),
          ("encapfddisnap", 16),
          ("encaptrsnap", 14),
          ("ethernet", 2),
          ("nativewan", 8),
          ("other", 1),
          ("snap", 3))
    )


_NwDecIVFwdIfFrameType_Type.__name__ = "Integer32"
_NwDecIVFwdIfFrameType_Object = MibTableColumn
nwDecIVFwdIfFrameType = _NwDecIVFwdIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 8),
    _NwDecIVFwdIfFrameType_Type()
)
nwDecIVFwdIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfFrameType.setStatus("mandatory")


class _NwDecIVFwdIfAclIdentifier_Type(Integer32):
    """Custom type nwDecIVFwdIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwDecIVFwdIfAclIdentifier_Object = MibTableColumn
nwDecIVFwdIfAclIdentifier = _NwDecIVFwdIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 9),
    _NwDecIVFwdIfAclIdentifier_Type()
)
nwDecIVFwdIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfAclIdentifier.setStatus("mandatory")


class _NwDecIVFwdIfAclStatus_Type(Integer32):
    """Custom type nwDecIVFwdIfAclStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVFwdIfAclStatus_Type.__name__ = "Integer32"
_NwDecIVFwdIfAclStatus_Object = MibTableColumn
nwDecIVFwdIfAclStatus = _NwDecIVFwdIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 10),
    _NwDecIVFwdIfAclStatus_Type()
)
nwDecIVFwdIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfAclStatus.setStatus("mandatory")


class _NwDecIVFwdIfCacheControl_Type(Integer32):
    """Custom type nwDecIVFwdIfCacheControl based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_NwDecIVFwdIfCacheControl_Type.__name__ = "Integer32"
_NwDecIVFwdIfCacheControl_Object = MibTableColumn
nwDecIVFwdIfCacheControl = _NwDecIVFwdIfCacheControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 11),
    _NwDecIVFwdIfCacheControl_Type()
)
nwDecIVFwdIfCacheControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCacheControl.setStatus("mandatory")
_NwDecIVFwdIfCacheEntries_Type = Counter32
_NwDecIVFwdIfCacheEntries_Object = MibTableColumn
nwDecIVFwdIfCacheEntries = _NwDecIVFwdIfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 12),
    _NwDecIVFwdIfCacheEntries_Type()
)
nwDecIVFwdIfCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCacheEntries.setStatus("mandatory")
_NwDecIVFwdIfCacheHits_Type = Counter32
_NwDecIVFwdIfCacheHits_Object = MibTableColumn
nwDecIVFwdIfCacheHits = _NwDecIVFwdIfCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 13),
    _NwDecIVFwdIfCacheHits_Type()
)
nwDecIVFwdIfCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCacheHits.setStatus("mandatory")
_NwDecIVFwdIfCacheMisses_Type = Counter32
_NwDecIVFwdIfCacheMisses_Object = MibTableColumn
nwDecIVFwdIfCacheMisses = _NwDecIVFwdIfCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 14),
    _NwDecIVFwdIfCacheMisses_Type()
)
nwDecIVFwdIfCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCacheMisses.setStatus("mandatory")
_NwDecIVFwdIfCounters_ObjectIdentity = ObjectIdentity
nwDecIVFwdIfCounters = _NwDecIVFwdIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2)
)
_NwDecIVFwdIfCtrTable_Object = MibTable
nwDecIVFwdIfCtrTable = _NwDecIVFwdIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrTable.setStatus("mandatory")
_NwDecIVFwdIfCtrEntry_Object = MibTableRow
nwDecIVFwdIfCtrEntry = _NwDecIVFwdIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1)
)
nwDecIVFwdIfCtrEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVFwdIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrEntry.setStatus("mandatory")
_NwDecIVFwdIfCtrIfIndex_Type = Integer32
_NwDecIVFwdIfCtrIfIndex_Object = MibTableColumn
nwDecIVFwdIfCtrIfIndex = _NwDecIVFwdIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1),
    _NwDecIVFwdIfCtrIfIndex_Type()
)
nwDecIVFwdIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrIfIndex.setStatus("mandatory")


class _NwDecIVFwdIfCtrAdminStatus_Type(Integer32):
    """Custom type nwDecIVFwdIfCtrAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVFwdIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwDecIVFwdIfCtrAdminStatus_Object = MibTableColumn
nwDecIVFwdIfCtrAdminStatus = _NwDecIVFwdIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 2),
    _NwDecIVFwdIfCtrAdminStatus_Type()
)
nwDecIVFwdIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrAdminStatus.setStatus("mandatory")


class _NwDecIVFwdIfCtrReset_Type(Integer32):
    """Custom type nwDecIVFwdIfCtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwDecIVFwdIfCtrReset_Type.__name__ = "Integer32"
_NwDecIVFwdIfCtrReset_Object = MibTableColumn
nwDecIVFwdIfCtrReset = _NwDecIVFwdIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 3),
    _NwDecIVFwdIfCtrReset_Type()
)
nwDecIVFwdIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrReset.setStatus("mandatory")
_NwDecIVFwdIfCtrOperationalTime_Type = TimeTicks
_NwDecIVFwdIfCtrOperationalTime_Object = MibTableColumn
nwDecIVFwdIfCtrOperationalTime = _NwDecIVFwdIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 4),
    _NwDecIVFwdIfCtrOperationalTime_Type()
)
nwDecIVFwdIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrOperationalTime.setStatus("mandatory")
_NwDecIVFwdIfCtrInPkts_Type = Counter32
_NwDecIVFwdIfCtrInPkts_Object = MibTableColumn
nwDecIVFwdIfCtrInPkts = _NwDecIVFwdIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 5),
    _NwDecIVFwdIfCtrInPkts_Type()
)
nwDecIVFwdIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrInPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrOutPkts_Type = Counter32
_NwDecIVFwdIfCtrOutPkts_Object = MibTableColumn
nwDecIVFwdIfCtrOutPkts = _NwDecIVFwdIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 6),
    _NwDecIVFwdIfCtrOutPkts_Type()
)
nwDecIVFwdIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrOutPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrFwdPkts_Type = Counter32
_NwDecIVFwdIfCtrFwdPkts_Object = MibTableColumn
nwDecIVFwdIfCtrFwdPkts = _NwDecIVFwdIfCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 7),
    _NwDecIVFwdIfCtrFwdPkts_Type()
)
nwDecIVFwdIfCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrFwdPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrFilteredPkts_Type = Counter32
_NwDecIVFwdIfCtrFilteredPkts_Object = MibTableColumn
nwDecIVFwdIfCtrFilteredPkts = _NwDecIVFwdIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 8),
    _NwDecIVFwdIfCtrFilteredPkts_Type()
)
nwDecIVFwdIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrFilteredPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrDiscardPkts_Type = Counter32
_NwDecIVFwdIfCtrDiscardPkts_Object = MibTableColumn
nwDecIVFwdIfCtrDiscardPkts = _NwDecIVFwdIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 9),
    _NwDecIVFwdIfCtrDiscardPkts_Type()
)
nwDecIVFwdIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrDiscardPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrAddrErrPkts_Type = Counter32
_NwDecIVFwdIfCtrAddrErrPkts_Object = MibTableColumn
nwDecIVFwdIfCtrAddrErrPkts = _NwDecIVFwdIfCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 10),
    _NwDecIVFwdIfCtrAddrErrPkts_Type()
)
nwDecIVFwdIfCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrAddrErrPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrLenErrPkts_Type = Counter32
_NwDecIVFwdIfCtrLenErrPkts_Object = MibTableColumn
nwDecIVFwdIfCtrLenErrPkts = _NwDecIVFwdIfCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 11),
    _NwDecIVFwdIfCtrLenErrPkts_Type()
)
nwDecIVFwdIfCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrLenErrPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrHdrErrPkts_Type = Counter32
_NwDecIVFwdIfCtrHdrErrPkts_Object = MibTableColumn
nwDecIVFwdIfCtrHdrErrPkts = _NwDecIVFwdIfCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 12),
    _NwDecIVFwdIfCtrHdrErrPkts_Type()
)
nwDecIVFwdIfCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrHdrErrPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrInBytes_Type = Counter32
_NwDecIVFwdIfCtrInBytes_Object = MibTableColumn
nwDecIVFwdIfCtrInBytes = _NwDecIVFwdIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 13),
    _NwDecIVFwdIfCtrInBytes_Type()
)
nwDecIVFwdIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrInBytes.setStatus("mandatory")
_NwDecIVFwdIfCtrOutBytes_Type = Counter32
_NwDecIVFwdIfCtrOutBytes_Object = MibTableColumn
nwDecIVFwdIfCtrOutBytes = _NwDecIVFwdIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 14),
    _NwDecIVFwdIfCtrOutBytes_Type()
)
nwDecIVFwdIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrOutBytes.setStatus("mandatory")
_NwDecIVFwdIfCtrFwdBytes_Type = Counter32
_NwDecIVFwdIfCtrFwdBytes_Object = MibTableColumn
nwDecIVFwdIfCtrFwdBytes = _NwDecIVFwdIfCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 15),
    _NwDecIVFwdIfCtrFwdBytes_Type()
)
nwDecIVFwdIfCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrFwdBytes.setStatus("mandatory")
_NwDecIVFwdIfCtrFilteredBytes_Type = Counter32
_NwDecIVFwdIfCtrFilteredBytes_Object = MibTableColumn
nwDecIVFwdIfCtrFilteredBytes = _NwDecIVFwdIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 16),
    _NwDecIVFwdIfCtrFilteredBytes_Type()
)
nwDecIVFwdIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrFilteredBytes.setStatus("mandatory")
_NwDecIVFwdIfCtrDiscardBytes_Type = Counter32
_NwDecIVFwdIfCtrDiscardBytes_Object = MibTableColumn
nwDecIVFwdIfCtrDiscardBytes = _NwDecIVFwdIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 17),
    _NwDecIVFwdIfCtrDiscardBytes_Type()
)
nwDecIVFwdIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrDiscardBytes.setStatus("mandatory")
_NwDecIVFwdIfCtrHostInPkts_Type = Counter32
_NwDecIVFwdIfCtrHostInPkts_Object = MibTableColumn
nwDecIVFwdIfCtrHostInPkts = _NwDecIVFwdIfCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 18),
    _NwDecIVFwdIfCtrHostInPkts_Type()
)
nwDecIVFwdIfCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrHostInPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrHostOutPkts_Type = Counter32
_NwDecIVFwdIfCtrHostOutPkts_Object = MibTableColumn
nwDecIVFwdIfCtrHostOutPkts = _NwDecIVFwdIfCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 19),
    _NwDecIVFwdIfCtrHostOutPkts_Type()
)
nwDecIVFwdIfCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrHostOutPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrHostDiscardPkts_Type = Counter32
_NwDecIVFwdIfCtrHostDiscardPkts_Object = MibTableColumn
nwDecIVFwdIfCtrHostDiscardPkts = _NwDecIVFwdIfCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 20),
    _NwDecIVFwdIfCtrHostDiscardPkts_Type()
)
nwDecIVFwdIfCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrHostDiscardPkts.setStatus("mandatory")
_NwDecIVFwdIfCtrHostInBytes_Type = Counter32
_NwDecIVFwdIfCtrHostInBytes_Object = MibTableColumn
nwDecIVFwdIfCtrHostInBytes = _NwDecIVFwdIfCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 21),
    _NwDecIVFwdIfCtrHostInBytes_Type()
)
nwDecIVFwdIfCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrHostInBytes.setStatus("mandatory")
_NwDecIVFwdIfCtrHostOutBytes_Type = Counter32
_NwDecIVFwdIfCtrHostOutBytes_Object = MibTableColumn
nwDecIVFwdIfCtrHostOutBytes = _NwDecIVFwdIfCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 22),
    _NwDecIVFwdIfCtrHostOutBytes_Type()
)
nwDecIVFwdIfCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrHostOutBytes.setStatus("mandatory")
_NwDecIVFwdIfCtrHostDiscardBytes_Type = Counter32
_NwDecIVFwdIfCtrHostDiscardBytes_Object = MibTableColumn
nwDecIVFwdIfCtrHostDiscardBytes = _NwDecIVFwdIfCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 23),
    _NwDecIVFwdIfCtrHostDiscardBytes_Type()
)
nwDecIVFwdIfCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFwdIfCtrHostDiscardBytes.setStatus("mandatory")
_NwDecIVTopology_ObjectIdentity = ObjectIdentity
nwDecIVTopology = _NwDecIVTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4)
)
_NwDecIVDistanceVector_ObjectIdentity = ObjectIdentity
nwDecIVDistanceVector = _NwDecIVDistanceVector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1)
)
_NwDecIVProto_ObjectIdentity = ObjectIdentity
nwDecIVProto = _NwDecIVProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1)
)
_NwDecIVProtoSystem_ObjectIdentity = ObjectIdentity
nwDecIVProtoSystem = _NwDecIVProtoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1)
)
_NwDecIVProtoConfig_ObjectIdentity = ObjectIdentity
nwDecIVProtoConfig = _NwDecIVProtoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1)
)


class _NwDecIVProtoAdminStatus_Type(Integer32):
    """Custom type nwDecIVProtoAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoAdminStatus_Type.__name__ = "Integer32"
_NwDecIVProtoAdminStatus_Object = MibScalar
nwDecIVProtoAdminStatus = _NwDecIVProtoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 1),
    _NwDecIVProtoAdminStatus_Type()
)
nwDecIVProtoAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoAdminStatus.setStatus("mandatory")


class _NwDecIVProtoOperStatus_Type(Integer32):
    """Custom type nwDecIVProtoOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwDecIVProtoOperStatus_Type.__name__ = "Integer32"
_NwDecIVProtoOperStatus_Object = MibScalar
nwDecIVProtoOperStatus = _NwDecIVProtoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 2),
    _NwDecIVProtoOperStatus_Type()
)
nwDecIVProtoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoOperStatus.setStatus("mandatory")


class _NwDecIVProtoAdminReset_Type(Integer32):
    """Custom type nwDecIVProtoAdminReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwDecIVProtoAdminReset_Type.__name__ = "Integer32"
_NwDecIVProtoAdminReset_Object = MibScalar
nwDecIVProtoAdminReset = _NwDecIVProtoAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 3),
    _NwDecIVProtoAdminReset_Type()
)
nwDecIVProtoAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoAdminReset.setStatus("mandatory")
_NwDecIVProtoOperationalTime_Type = TimeTicks
_NwDecIVProtoOperationalTime_Object = MibScalar
nwDecIVProtoOperationalTime = _NwDecIVProtoOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 4),
    _NwDecIVProtoOperationalTime_Type()
)
nwDecIVProtoOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoOperationalTime.setStatus("mandatory")
_NwDecIVProtoVersion_Type = DisplayString
_NwDecIVProtoVersion_Object = MibScalar
nwDecIVProtoVersion = _NwDecIVProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 5),
    _NwDecIVProtoVersion_Type()
)
nwDecIVProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoVersion.setStatus("mandatory")


class _NwDecIVProtoStackSize_Type(Integer32):
    """Custom type nwDecIVProtoStackSize based on Integer32"""
    defaultValue = 4096


_NwDecIVProtoStackSize_Object = MibScalar
nwDecIVProtoStackSize = _NwDecIVProtoStackSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 6),
    _NwDecIVProtoStackSize_Type()
)
nwDecIVProtoStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoStackSize.setStatus("mandatory")


class _NwDecIVProtoThreadPriority_Type(Integer32):
    """Custom type nwDecIVProtoThreadPriority based on Integer32"""
    defaultValue = 127


_NwDecIVProtoThreadPriority_Object = MibScalar
nwDecIVProtoThreadPriority = _NwDecIVProtoThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 7),
    _NwDecIVProtoThreadPriority_Type()
)
nwDecIVProtoThreadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoThreadPriority.setStatus("mandatory")


class _NwDecIVProtoDatabaseThreshold_Type(Integer32):
    """Custom type nwDecIVProtoDatabaseThreshold based on Integer32"""
    defaultValue = 2000


_NwDecIVProtoDatabaseThreshold_Object = MibScalar
nwDecIVProtoDatabaseThreshold = _NwDecIVProtoDatabaseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 8),
    _NwDecIVProtoDatabaseThreshold_Type()
)
nwDecIVProtoDatabaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoDatabaseThreshold.setStatus("mandatory")


class _NwDecIVProtoAgeOut_Type(Integer32):
    """Custom type nwDecIVProtoAgeOut based on Integer32"""
    defaultValue = 180


_NwDecIVProtoAgeOut_Object = MibScalar
nwDecIVProtoAgeOut = _NwDecIVProtoAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 9),
    _NwDecIVProtoAgeOut_Type()
)
nwDecIVProtoAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoAgeOut.setStatus("mandatory")


class _NwDecIVProtoHoldDown_Type(Integer32):
    """Custom type nwDecIVProtoHoldDown based on Integer32"""
    defaultValue = 120


_NwDecIVProtoHoldDown_Object = MibScalar
nwDecIVProtoHoldDown = _NwDecIVProtoHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 1, 10),
    _NwDecIVProtoHoldDown_Type()
)
nwDecIVProtoHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoHoldDown.setStatus("mandatory")
_NwDecIVProtoCounters_ObjectIdentity = ObjectIdentity
nwDecIVProtoCounters = _NwDecIVProtoCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2)
)


class _NwDecIVProtoCtrAdminStatus_Type(Integer32):
    """Custom type nwDecIVProtoCtrAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoCtrAdminStatus_Type.__name__ = "Integer32"
_NwDecIVProtoCtrAdminStatus_Object = MibScalar
nwDecIVProtoCtrAdminStatus = _NwDecIVProtoCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 1),
    _NwDecIVProtoCtrAdminStatus_Type()
)
nwDecIVProtoCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrAdminStatus.setStatus("mandatory")


class _NwDecIVProtoCtrReset_Type(Integer32):
    """Custom type nwDecIVProtoCtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwDecIVProtoCtrReset_Type.__name__ = "Integer32"
_NwDecIVProtoCtrReset_Object = MibScalar
nwDecIVProtoCtrReset = _NwDecIVProtoCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 2),
    _NwDecIVProtoCtrReset_Type()
)
nwDecIVProtoCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrReset.setStatus("mandatory")
_NwDecIVProtoCtrOperationalTime_Type = TimeTicks
_NwDecIVProtoCtrOperationalTime_Object = MibScalar
nwDecIVProtoCtrOperationalTime = _NwDecIVProtoCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 3),
    _NwDecIVProtoCtrOperationalTime_Type()
)
nwDecIVProtoCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrOperationalTime.setStatus("mandatory")
_NwDecIVProtoCtrInPkts_Type = Counter32
_NwDecIVProtoCtrInPkts_Object = MibScalar
nwDecIVProtoCtrInPkts = _NwDecIVProtoCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 4),
    _NwDecIVProtoCtrInPkts_Type()
)
nwDecIVProtoCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrInPkts.setStatus("mandatory")
_NwDecIVProtoCtrOutPkts_Type = Counter32
_NwDecIVProtoCtrOutPkts_Object = MibScalar
nwDecIVProtoCtrOutPkts = _NwDecIVProtoCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 5),
    _NwDecIVProtoCtrOutPkts_Type()
)
nwDecIVProtoCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrOutPkts.setStatus("mandatory")
_NwDecIVProtoCtrFilteredPkts_Type = Counter32
_NwDecIVProtoCtrFilteredPkts_Object = MibScalar
nwDecIVProtoCtrFilteredPkts = _NwDecIVProtoCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 6),
    _NwDecIVProtoCtrFilteredPkts_Type()
)
nwDecIVProtoCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrFilteredPkts.setStatus("mandatory")
_NwDecIVProtoCtrDiscardPkts_Type = Counter32
_NwDecIVProtoCtrDiscardPkts_Object = MibScalar
nwDecIVProtoCtrDiscardPkts = _NwDecIVProtoCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 7),
    _NwDecIVProtoCtrDiscardPkts_Type()
)
nwDecIVProtoCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrDiscardPkts.setStatus("mandatory")
_NwDecIVProtoCtrInBytes_Type = Counter32
_NwDecIVProtoCtrInBytes_Object = MibScalar
nwDecIVProtoCtrInBytes = _NwDecIVProtoCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 8),
    _NwDecIVProtoCtrInBytes_Type()
)
nwDecIVProtoCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrInBytes.setStatus("mandatory")
_NwDecIVProtoCtrOutBytes_Type = Counter32
_NwDecIVProtoCtrOutBytes_Object = MibScalar
nwDecIVProtoCtrOutBytes = _NwDecIVProtoCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 9),
    _NwDecIVProtoCtrOutBytes_Type()
)
nwDecIVProtoCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrOutBytes.setStatus("mandatory")
_NwDecIVProtoCtrFilteredBytes_Type = Counter32
_NwDecIVProtoCtrFilteredBytes_Object = MibScalar
nwDecIVProtoCtrFilteredBytes = _NwDecIVProtoCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 10),
    _NwDecIVProtoCtrFilteredBytes_Type()
)
nwDecIVProtoCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrFilteredBytes.setStatus("mandatory")
_NwDecIVProtoCtrDiscardBytes_Type = Counter32
_NwDecIVProtoCtrDiscardBytes_Object = MibScalar
nwDecIVProtoCtrDiscardBytes = _NwDecIVProtoCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 1, 2, 11),
    _NwDecIVProtoCtrDiscardBytes_Type()
)
nwDecIVProtoCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoCtrDiscardBytes.setStatus("mandatory")
_NwDecIVProtoInterface_ObjectIdentity = ObjectIdentity
nwDecIVProtoInterface = _NwDecIVProtoInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2)
)
_NwDecIVProtoIfConfig_ObjectIdentity = ObjectIdentity
nwDecIVProtoIfConfig = _NwDecIVProtoIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1)
)
_NwDecIVProtoIfTable_Object = MibTable
nwDecIVProtoIfTable = _NwDecIVProtoIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwDecIVProtoIfTable.setStatus("mandatory")
_NwDecIVProtoIfEntry_Object = MibTableRow
nwDecIVProtoIfEntry = _NwDecIVProtoIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1)
)
nwDecIVProtoIfEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVProtoIfIndex"),
)
if mibBuilder.loadTexts:
    nwDecIVProtoIfEntry.setStatus("mandatory")
_NwDecIVProtoIfIndex_Type = Integer32
_NwDecIVProtoIfIndex_Object = MibTableColumn
nwDecIVProtoIfIndex = _NwDecIVProtoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 1),
    _NwDecIVProtoIfIndex_Type()
)
nwDecIVProtoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfIndex.setStatus("mandatory")


class _NwDecIVProtoIfAdminStatus_Type(Integer32):
    """Custom type nwDecIVProtoIfAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoIfAdminStatus_Type.__name__ = "Integer32"
_NwDecIVProtoIfAdminStatus_Object = MibTableColumn
nwDecIVProtoIfAdminStatus = _NwDecIVProtoIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 2),
    _NwDecIVProtoIfAdminStatus_Type()
)
nwDecIVProtoIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfAdminStatus.setStatus("mandatory")


class _NwDecIVProtoIfOperStatus_Type(Integer32):
    """Custom type nwDecIVProtoIfOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwDecIVProtoIfOperStatus_Type.__name__ = "Integer32"
_NwDecIVProtoIfOperStatus_Object = MibTableColumn
nwDecIVProtoIfOperStatus = _NwDecIVProtoIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 3),
    _NwDecIVProtoIfOperStatus_Type()
)
nwDecIVProtoIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfOperStatus.setStatus("mandatory")
_NwDecIVProtoIfOperationalTime_Type = TimeTicks
_NwDecIVProtoIfOperationalTime_Object = MibTableColumn
nwDecIVProtoIfOperationalTime = _NwDecIVProtoIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 4),
    _NwDecIVProtoIfOperationalTime_Type()
)
nwDecIVProtoIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfOperationalTime.setStatus("mandatory")


class _NwDecIVProtoIfVersion_Type(Integer32):
    """Custom type nwDecIVProtoIfVersion based on Integer32"""
    defaultValue = 3


_NwDecIVProtoIfVersion_Object = MibTableColumn
nwDecIVProtoIfVersion = _NwDecIVProtoIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 5),
    _NwDecIVProtoIfVersion_Type()
)
nwDecIVProtoIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfVersion.setStatus("mandatory")


class _NwDecIVProtoIfAdvertisement_Type(Integer32):
    """Custom type nwDecIVProtoIfAdvertisement based on Integer32"""
    defaultValue = 40


_NwDecIVProtoIfAdvertisement_Object = MibTableColumn
nwDecIVProtoIfAdvertisement = _NwDecIVProtoIfAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 6),
    _NwDecIVProtoIfAdvertisement_Type()
)
nwDecIVProtoIfAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfAdvertisement.setStatus("mandatory")


class _NwDecIVProtoIfFloodDelay_Type(Integer32):
    """Custom type nwDecIVProtoIfFloodDelay based on Integer32"""
    defaultValue = 2


_NwDecIVProtoIfFloodDelay_Object = MibTableColumn
nwDecIVProtoIfFloodDelay = _NwDecIVProtoIfFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 7),
    _NwDecIVProtoIfFloodDelay_Type()
)
nwDecIVProtoIfFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfFloodDelay.setStatus("mandatory")


class _NwDecIVProtoIfRequestDelay_Type(Integer32):
    """Custom type nwDecIVProtoIfRequestDelay based on Integer32"""
    defaultValue = 0


_NwDecIVProtoIfRequestDelay_Object = MibTableColumn
nwDecIVProtoIfRequestDelay = _NwDecIVProtoIfRequestDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 8),
    _NwDecIVProtoIfRequestDelay_Type()
)
nwDecIVProtoIfRequestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfRequestDelay.setStatus("mandatory")


class _NwDecIVProtoIfPriority_Type(Integer32):
    """Custom type nwDecIVProtoIfPriority based on Integer32"""
    defaultValue = 64


_NwDecIVProtoIfPriority_Object = MibTableColumn
nwDecIVProtoIfPriority = _NwDecIVProtoIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 9),
    _NwDecIVProtoIfPriority_Type()
)
nwDecIVProtoIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfPriority.setStatus("mandatory")


class _NwDecIVProtoIfHelloTimer_Type(Integer32):
    """Custom type nwDecIVProtoIfHelloTimer based on Integer32"""
    defaultValue = 15


_NwDecIVProtoIfHelloTimer_Object = MibTableColumn
nwDecIVProtoIfHelloTimer = _NwDecIVProtoIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 10),
    _NwDecIVProtoIfHelloTimer_Type()
)
nwDecIVProtoIfHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfHelloTimer.setStatus("mandatory")


class _NwDecIVProtoIfSplitHorizon_Type(Integer32):
    """Custom type nwDecIVProtoIfSplitHorizon based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoIfSplitHorizon_Type.__name__ = "Integer32"
_NwDecIVProtoIfSplitHorizon_Object = MibTableColumn
nwDecIVProtoIfSplitHorizon = _NwDecIVProtoIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 11),
    _NwDecIVProtoIfSplitHorizon_Type()
)
nwDecIVProtoIfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfSplitHorizon.setStatus("mandatory")


class _NwDecIVProtoIfPoisonReverse_Type(Integer32):
    """Custom type nwDecIVProtoIfPoisonReverse based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoIfPoisonReverse_Type.__name__ = "Integer32"
_NwDecIVProtoIfPoisonReverse_Object = MibTableColumn
nwDecIVProtoIfPoisonReverse = _NwDecIVProtoIfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 12),
    _NwDecIVProtoIfPoisonReverse_Type()
)
nwDecIVProtoIfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfPoisonReverse.setStatus("mandatory")


class _NwDecIVProtoIfSnooping_Type(Integer32):
    """Custom type nwDecIVProtoIfSnooping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoIfSnooping_Type.__name__ = "Integer32"
_NwDecIVProtoIfSnooping_Object = MibTableColumn
nwDecIVProtoIfSnooping = _NwDecIVProtoIfSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 13),
    _NwDecIVProtoIfSnooping_Type()
)
nwDecIVProtoIfSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfSnooping.setStatus("mandatory")


class _NwDecIVProtoIfType_Type(Integer32):
    """Custom type nwDecIVProtoIfType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bma", 2),
          ("nbma", 3),
          ("other", 1))
    )


_NwDecIVProtoIfType_Type.__name__ = "Integer32"
_NwDecIVProtoIfType_Object = MibTableColumn
nwDecIVProtoIfType = _NwDecIVProtoIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 14),
    _NwDecIVProtoIfType_Type()
)
nwDecIVProtoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfType.setStatus("mandatory")


class _NwDecIVProtoIfXmitCost_Type(Integer32):
    """Custom type nwDecIVProtoIfXmitCost based on Integer32"""
    defaultValue = 1


_NwDecIVProtoIfXmitCost_Object = MibTableColumn
nwDecIVProtoIfXmitCost = _NwDecIVProtoIfXmitCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 15),
    _NwDecIVProtoIfXmitCost_Type()
)
nwDecIVProtoIfXmitCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfXmitCost.setStatus("mandatory")


class _NwDecIVProtoIfAclIdentifier_Type(Integer32):
    """Custom type nwDecIVProtoIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwDecIVProtoIfAclIdentifier_Object = MibTableColumn
nwDecIVProtoIfAclIdentifier = _NwDecIVProtoIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 16),
    _NwDecIVProtoIfAclIdentifier_Type()
)
nwDecIVProtoIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfAclIdentifier.setStatus("mandatory")


class _NwDecIVProtoIfAclStatus_Type(Integer32):
    """Custom type nwDecIVProtoIfAclStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoIfAclStatus_Type.__name__ = "Integer32"
_NwDecIVProtoIfAclStatus_Object = MibTableColumn
nwDecIVProtoIfAclStatus = _NwDecIVProtoIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 1, 1, 1, 17),
    _NwDecIVProtoIfAclStatus_Type()
)
nwDecIVProtoIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfAclStatus.setStatus("mandatory")
_NwDecIVProtoIfCounters_ObjectIdentity = ObjectIdentity
nwDecIVProtoIfCounters = _NwDecIVProtoIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2)
)
_NwDecIVProtoIfCtrTable_Object = MibTable
nwDecIVProtoIfCtrTable = _NwDecIVProtoIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrTable.setStatus("mandatory")
_NwDecIVProtoIfCtrEntry_Object = MibTableRow
nwDecIVProtoIfCtrEntry = _NwDecIVProtoIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1)
)
nwDecIVProtoIfCtrEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVProtoIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrEntry.setStatus("mandatory")
_NwDecIVProtoIfCtrIfIndex_Type = Integer32
_NwDecIVProtoIfCtrIfIndex_Object = MibTableColumn
nwDecIVProtoIfCtrIfIndex = _NwDecIVProtoIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 1),
    _NwDecIVProtoIfCtrIfIndex_Type()
)
nwDecIVProtoIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrIfIndex.setStatus("mandatory")


class _NwDecIVProtoIfCtrAdminStatus_Type(Integer32):
    """Custom type nwDecIVProtoIfCtrAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVProtoIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwDecIVProtoIfCtrAdminStatus_Object = MibTableColumn
nwDecIVProtoIfCtrAdminStatus = _NwDecIVProtoIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 2),
    _NwDecIVProtoIfCtrAdminStatus_Type()
)
nwDecIVProtoIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrAdminStatus.setStatus("mandatory")


class _NwDecIVProtoIfCtrReset_Type(Integer32):
    """Custom type nwDecIVProtoIfCtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwDecIVProtoIfCtrReset_Type.__name__ = "Integer32"
_NwDecIVProtoIfCtrReset_Object = MibTableColumn
nwDecIVProtoIfCtrReset = _NwDecIVProtoIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 3),
    _NwDecIVProtoIfCtrReset_Type()
)
nwDecIVProtoIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrReset.setStatus("mandatory")
_NwDecIVProtoIfCtrOperationalTime_Type = TimeTicks
_NwDecIVProtoIfCtrOperationalTime_Object = MibTableColumn
nwDecIVProtoIfCtrOperationalTime = _NwDecIVProtoIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 4),
    _NwDecIVProtoIfCtrOperationalTime_Type()
)
nwDecIVProtoIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrOperationalTime.setStatus("mandatory")
_NwDecIVProtoIfCtrInPkts_Type = Counter32
_NwDecIVProtoIfCtrInPkts_Object = MibTableColumn
nwDecIVProtoIfCtrInPkts = _NwDecIVProtoIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 5),
    _NwDecIVProtoIfCtrInPkts_Type()
)
nwDecIVProtoIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrInPkts.setStatus("mandatory")
_NwDecIVProtoIfCtrOutPkts_Type = Counter32
_NwDecIVProtoIfCtrOutPkts_Object = MibTableColumn
nwDecIVProtoIfCtrOutPkts = _NwDecIVProtoIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 6),
    _NwDecIVProtoIfCtrOutPkts_Type()
)
nwDecIVProtoIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrOutPkts.setStatus("mandatory")
_NwDecIVProtoIfCtrFilteredPkts_Type = Counter32
_NwDecIVProtoIfCtrFilteredPkts_Object = MibTableColumn
nwDecIVProtoIfCtrFilteredPkts = _NwDecIVProtoIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 7),
    _NwDecIVProtoIfCtrFilteredPkts_Type()
)
nwDecIVProtoIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrFilteredPkts.setStatus("mandatory")
_NwDecIVProtoIfCtrDiscardPkts_Type = Counter32
_NwDecIVProtoIfCtrDiscardPkts_Object = MibTableColumn
nwDecIVProtoIfCtrDiscardPkts = _NwDecIVProtoIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 8),
    _NwDecIVProtoIfCtrDiscardPkts_Type()
)
nwDecIVProtoIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrDiscardPkts.setStatus("mandatory")
_NwDecIVProtoIfCtrInBytes_Type = Counter32
_NwDecIVProtoIfCtrInBytes_Object = MibTableColumn
nwDecIVProtoIfCtrInBytes = _NwDecIVProtoIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 9),
    _NwDecIVProtoIfCtrInBytes_Type()
)
nwDecIVProtoIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrInBytes.setStatus("mandatory")
_NwDecIVProtoIfCtrOutBytes_Type = Counter32
_NwDecIVProtoIfCtrOutBytes_Object = MibTableColumn
nwDecIVProtoIfCtrOutBytes = _NwDecIVProtoIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 10),
    _NwDecIVProtoIfCtrOutBytes_Type()
)
nwDecIVProtoIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrOutBytes.setStatus("mandatory")
_NwDecIVProtoIfCtrFilteredBytes_Type = Counter32
_NwDecIVProtoIfCtrFilteredBytes_Object = MibTableColumn
nwDecIVProtoIfCtrFilteredBytes = _NwDecIVProtoIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 11),
    _NwDecIVProtoIfCtrFilteredBytes_Type()
)
nwDecIVProtoIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrFilteredBytes.setStatus("mandatory")
_NwDecIVProtoIfCtrDiscardBytes_Type = Counter32
_NwDecIVProtoIfCtrDiscardBytes_Object = MibTableColumn
nwDecIVProtoIfCtrDiscardBytes = _NwDecIVProtoIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 1, 1, 2, 2, 1, 1, 12),
    _NwDecIVProtoIfCtrDiscardBytes_Type()
)
nwDecIVProtoIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVProtoIfCtrDiscardBytes.setStatus("mandatory")
_NwDecIVLinkState_ObjectIdentity = ObjectIdentity
nwDecIVLinkState = _NwDecIVLinkState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 4, 2)
)
_NwDecIVFib_ObjectIdentity = ObjectIdentity
nwDecIVFib = _NwDecIVFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 5)
)
_NwDecIVFibTable_Object = MibTable
nwDecIVFibTable = _NwDecIVFibTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    nwDecIVFibTable.setStatus("mandatory")
_NwDecIVFibEntry_Object = MibTableRow
nwDecIVFibEntry = _NwDecIVFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 5, 1, 1)
)
nwDecIVFibEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVFibNodeId"),
)
if mibBuilder.loadTexts:
    nwDecIVFibEntry.setStatus("mandatory")
_NwDecIVFibNodeId_Type = DecIVAddress
_NwDecIVFibNodeId_Object = MibTableColumn
nwDecIVFibNodeId = _NwDecIVFibNodeId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 5, 1, 1, 1),
    _NwDecIVFibNodeId_Type()
)
nwDecIVFibNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVFibNodeId.setStatus("mandatory")
_NwDecIVFibNextHopNodeId_Type = DecIVAddress
_NwDecIVFibNextHopNodeId_Object = MibTableColumn
nwDecIVFibNextHopNodeId = _NwDecIVFibNextHopNodeId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 5, 1, 1, 2),
    _NwDecIVFibNextHopNodeId_Type()
)
nwDecIVFibNextHopNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFibNextHopNodeId.setStatus("mandatory")


class _NwDecIVFibNextHopIf_Type(Integer32):
    """Custom type nwDecIVFibNextHopIf based on Integer32"""
    defaultValue = 0


_NwDecIVFibNextHopIf_Object = MibTableColumn
nwDecIVFibNextHopIf = _NwDecIVFibNextHopIf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 5, 1, 1, 3),
    _NwDecIVFibNextHopIf_Type()
)
nwDecIVFibNextHopIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFibNextHopIf.setStatus("mandatory")


class _NwDecIVFibRouteType_Type(Integer32):
    """Custom type nwDecIVFibRouteType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("direct", 3),
          ("invalid", 2),
          ("other", 1),
          ("remote", 4))
    )


_NwDecIVFibRouteType_Type.__name__ = "Integer32"
_NwDecIVFibRouteType_Object = MibTableColumn
nwDecIVFibRouteType = _NwDecIVFibRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 5, 1, 1, 4),
    _NwDecIVFibRouteType_Type()
)
nwDecIVFibRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVFibRouteType.setStatus("mandatory")
_NwDecIVEndSystems_ObjectIdentity = ObjectIdentity
nwDecIVEndSystems = _NwDecIVEndSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6)
)
_NwDecIVHostsSystem_ObjectIdentity = ObjectIdentity
nwDecIVHostsSystem = _NwDecIVHostsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 1)
)
_NwDecIVHostsInterfaces_ObjectIdentity = ObjectIdentity
nwDecIVHostsInterfaces = _NwDecIVHostsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 2)
)
_NwDecIVHostsToMedia_ObjectIdentity = ObjectIdentity
nwDecIVHostsToMedia = _NwDecIVHostsToMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3)
)
_NwDecIVHostMapTable_Object = MibTable
nwDecIVHostMapTable = _NwDecIVHostMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    nwDecIVHostMapTable.setStatus("mandatory")
_NwDecIVHostMapEntry_Object = MibTableRow
nwDecIVHostMapEntry = _NwDecIVHostMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1, 1)
)
nwDecIVHostMapEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVHostMapIfIndex"),
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVHostMapDecIVAddr"),
)
if mibBuilder.loadTexts:
    nwDecIVHostMapEntry.setStatus("mandatory")
_NwDecIVHostMapIfIndex_Type = Integer32
_NwDecIVHostMapIfIndex_Object = MibTableColumn
nwDecIVHostMapIfIndex = _NwDecIVHostMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1, 1, 1),
    _NwDecIVHostMapIfIndex_Type()
)
nwDecIVHostMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVHostMapIfIndex.setStatus("mandatory")
_NwDecIVHostMapDecIVAddr_Type = DecIVAddress
_NwDecIVHostMapDecIVAddr_Object = MibTableColumn
nwDecIVHostMapDecIVAddr = _NwDecIVHostMapDecIVAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1, 1, 2),
    _NwDecIVHostMapDecIVAddr_Type()
)
nwDecIVHostMapDecIVAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVHostMapDecIVAddr.setStatus("mandatory")


class _NwDecIVHostMapType_Type(Integer32):
    """Custom type nwDecIVHostMapType based on Integer32"""
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
        *(("dynamic", 3),
          ("inactive", 5),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_NwDecIVHostMapType_Type.__name__ = "Integer32"
_NwDecIVHostMapType_Object = MibTableColumn
nwDecIVHostMapType = _NwDecIVHostMapType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1, 1, 3),
    _NwDecIVHostMapType_Type()
)
nwDecIVHostMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVHostMapType.setStatus("mandatory")
_NwDecIVHostMapCircuitID_Type = Integer32
_NwDecIVHostMapCircuitID_Object = MibTableColumn
nwDecIVHostMapCircuitID = _NwDecIVHostMapCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1, 1, 4),
    _NwDecIVHostMapCircuitID_Type()
)
nwDecIVHostMapCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVHostMapCircuitID.setStatus("mandatory")


class _NwDecIVHostMapFraming_Type(Integer32):
    """Custom type nwDecIVHostMapFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              9,
              11,
              14,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 17),
          ("encapenet", 9),
          ("encapenetsnap", 11),
          ("encapfddisnap", 16),
          ("encaptrsnap", 14),
          ("ethernet", 2),
          ("nativewan", 8),
          ("other", 1),
          ("snap", 3))
    )


_NwDecIVHostMapFraming_Type.__name__ = "Integer32"
_NwDecIVHostMapFraming_Object = MibTableColumn
nwDecIVHostMapFraming = _NwDecIVHostMapFraming_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1, 1, 5),
    _NwDecIVHostMapFraming_Type()
)
nwDecIVHostMapFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVHostMapFraming.setStatus("mandatory")
_NwDecIVHostMapPortNumber_Type = Integer32
_NwDecIVHostMapPortNumber_Object = MibTableColumn
nwDecIVHostMapPortNumber = _NwDecIVHostMapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 6, 3, 1, 1, 6),
    _NwDecIVHostMapPortNumber_Type()
)
nwDecIVHostMapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVHostMapPortNumber.setStatus("mandatory")
_NwDecIVAccessControl_ObjectIdentity = ObjectIdentity
nwDecIVAccessControl = _NwDecIVAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7)
)
_NwDecIVAclValidEntries_Type = Gauge32
_NwDecIVAclValidEntries_Object = MibScalar
nwDecIVAclValidEntries = _NwDecIVAclValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 1),
    _NwDecIVAclValidEntries_Type()
)
nwDecIVAclValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVAclValidEntries.setStatus("mandatory")
_NwDecIVAclTable_Object = MibTable
nwDecIVAclTable = _NwDecIVAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    nwDecIVAclTable.setStatus("mandatory")
_NwDecIVAclEntry_Object = MibTableRow
nwDecIVAclEntry = _NwDecIVAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2, 1)
)
nwDecIVAclEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVAclIdentifier"),
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVAclSequence"),
)
if mibBuilder.loadTexts:
    nwDecIVAclEntry.setStatus("mandatory")
_NwDecIVAclIdentifier_Type = Integer32
_NwDecIVAclIdentifier_Object = MibTableColumn
nwDecIVAclIdentifier = _NwDecIVAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2, 1, 1),
    _NwDecIVAclIdentifier_Type()
)
nwDecIVAclIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVAclIdentifier.setStatus("mandatory")
_NwDecIVAclSequence_Type = Integer32
_NwDecIVAclSequence_Object = MibTableColumn
nwDecIVAclSequence = _NwDecIVAclSequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2, 1, 2),
    _NwDecIVAclSequence_Type()
)
nwDecIVAclSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVAclSequence.setStatus("mandatory")


class _NwDecIVAclPermission_Type(Integer32):
    """Custom type nwDecIVAclPermission based on Integer32"""
    defaultValue = 3

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
        *(("deny", 4),
          ("deny-bidirectional", 6),
          ("invalid", 2),
          ("other", 1),
          ("permit", 3),
          ("permit-bidirectional", 5))
    )


_NwDecIVAclPermission_Type.__name__ = "Integer32"
_NwDecIVAclPermission_Object = MibTableColumn
nwDecIVAclPermission = _NwDecIVAclPermission_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2, 1, 3),
    _NwDecIVAclPermission_Type()
)
nwDecIVAclPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVAclPermission.setStatus("mandatory")
_NwDecIVAclMatches_Type = Counter32
_NwDecIVAclMatches_Object = MibTableColumn
nwDecIVAclMatches = _NwDecIVAclMatches_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2, 1, 4),
    _NwDecIVAclMatches_Type()
)
nwDecIVAclMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVAclMatches.setStatus("mandatory")
_NwDecIVAclDestAddress_Type = DecIVAddress
_NwDecIVAclDestAddress_Object = MibTableColumn
nwDecIVAclDestAddress = _NwDecIVAclDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2, 1, 5),
    _NwDecIVAclDestAddress_Type()
)
nwDecIVAclDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVAclDestAddress.setStatus("mandatory")
_NwDecIVAclSrcAddress_Type = DecIVAddress
_NwDecIVAclSrcAddress_Object = MibTableColumn
nwDecIVAclSrcAddress = _NwDecIVAclSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 7, 2, 1, 6),
    _NwDecIVAclSrcAddress_Type()
)
nwDecIVAclSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVAclSrcAddress.setStatus("mandatory")
_NwDecIVFilters_ObjectIdentity = ObjectIdentity
nwDecIVFilters = _NwDecIVFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 8)
)
_NwDecIVRedirector_ObjectIdentity = ObjectIdentity
nwDecIVRedirector = _NwDecIVRedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 9)
)
_NwDecIVEvent_ObjectIdentity = ObjectIdentity
nwDecIVEvent = _NwDecIVEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10)
)
_NwDecIVEventLogConfig_ObjectIdentity = ObjectIdentity
nwDecIVEventLogConfig = _NwDecIVEventLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 1)
)


class _NwDecIVEventAdminStatus_Type(Integer32):
    """Custom type nwDecIVEventAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVEventAdminStatus_Type.__name__ = "Integer32"
_NwDecIVEventAdminStatus_Object = MibScalar
nwDecIVEventAdminStatus = _NwDecIVEventAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 1, 1),
    _NwDecIVEventAdminStatus_Type()
)
nwDecIVEventAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVEventAdminStatus.setStatus("mandatory")


class _NwDecIVEventMaxEntries_Type(Integer32):
    """Custom type nwDecIVEventMaxEntries based on Integer32"""
    defaultValue = 100


_NwDecIVEventMaxEntries_Object = MibScalar
nwDecIVEventMaxEntries = _NwDecIVEventMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 1, 2),
    _NwDecIVEventMaxEntries_Type()
)
nwDecIVEventMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVEventMaxEntries.setStatus("mandatory")


class _NwDecIVEventTraceAll_Type(Integer32):
    """Custom type nwDecIVEventTraceAll based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwDecIVEventTraceAll_Type.__name__ = "Integer32"
_NwDecIVEventTraceAll_Object = MibScalar
nwDecIVEventTraceAll = _NwDecIVEventTraceAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 1, 3),
    _NwDecIVEventTraceAll_Type()
)
nwDecIVEventTraceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVEventTraceAll.setStatus("mandatory")
_NwDecIVEventLogFilterTable_ObjectIdentity = ObjectIdentity
nwDecIVEventLogFilterTable = _NwDecIVEventLogFilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2)
)
_NwDecIVEventFilterTable_Object = MibTable
nwDecIVEventFilterTable = _NwDecIVEventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    nwDecIVEventFilterTable.setStatus("mandatory")
_NwDecIVEventFilterEntry_Object = MibTableRow
nwDecIVEventFilterEntry = _NwDecIVEventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1, 1)
)
nwDecIVEventFilterEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVEventFltrProtocol"),
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVEventFltrIfNum"),
)
if mibBuilder.loadTexts:
    nwDecIVEventFilterEntry.setStatus("mandatory")
_NwDecIVEventFltrProtocol_Type = Integer32
_NwDecIVEventFltrProtocol_Object = MibTableColumn
nwDecIVEventFltrProtocol = _NwDecIVEventFltrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1, 1, 1),
    _NwDecIVEventFltrProtocol_Type()
)
nwDecIVEventFltrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventFltrProtocol.setStatus("mandatory")
_NwDecIVEventFltrIfNum_Type = Integer32
_NwDecIVEventFltrIfNum_Object = MibTableColumn
nwDecIVEventFltrIfNum = _NwDecIVEventFltrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1, 1, 2),
    _NwDecIVEventFltrIfNum_Type()
)
nwDecIVEventFltrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventFltrIfNum.setStatus("mandatory")


class _NwDecIVEventFltrControl_Type(Integer32):
    """Custom type nwDecIVEventFltrControl based on Integer32"""
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
        *(("add", 3),
          ("delete", 2),
          ("other", 1))
    )


_NwDecIVEventFltrControl_Type.__name__ = "Integer32"
_NwDecIVEventFltrControl_Object = MibTableColumn
nwDecIVEventFltrControl = _NwDecIVEventFltrControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1, 1, 3),
    _NwDecIVEventFltrControl_Type()
)
nwDecIVEventFltrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVEventFltrControl.setStatus("mandatory")


class _NwDecIVEventFltrType_Type(Integer32):
    """Custom type nwDecIVEventFltrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("diags", 32),
          ("error", 64),
          ("event", 16),
          ("misc", 1),
          ("rcv", 4),
          ("timer", 2),
          ("xmit", 8))
    )


_NwDecIVEventFltrType_Type.__name__ = "Integer32"
_NwDecIVEventFltrType_Object = MibTableColumn
nwDecIVEventFltrType = _NwDecIVEventFltrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1, 1, 4),
    _NwDecIVEventFltrType_Type()
)
nwDecIVEventFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVEventFltrType.setStatus("mandatory")


class _NwDecIVEventFltrSeverity_Type(Integer32):
    """Custom type nwDecIVEventFltrSeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highest", 1),
          ("highlow", 3),
          ("highmed", 2))
    )


_NwDecIVEventFltrSeverity_Type.__name__ = "Integer32"
_NwDecIVEventFltrSeverity_Object = MibTableColumn
nwDecIVEventFltrSeverity = _NwDecIVEventFltrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1, 1, 5),
    _NwDecIVEventFltrSeverity_Type()
)
nwDecIVEventFltrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVEventFltrSeverity.setStatus("mandatory")


class _NwDecIVEventFltrAction_Type(Integer32):
    """Custom type nwDecIVEventFltrAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("log-trap", 3),
          ("trap", 2))
    )


_NwDecIVEventFltrAction_Type.__name__ = "Integer32"
_NwDecIVEventFltrAction_Object = MibTableColumn
nwDecIVEventFltrAction = _NwDecIVEventFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 2, 1, 1, 6),
    _NwDecIVEventFltrAction_Type()
)
nwDecIVEventFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDecIVEventFltrAction.setStatus("mandatory")
_NwDecIVEventLogTable_ObjectIdentity = ObjectIdentity
nwDecIVEventLogTable = _NwDecIVEventLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3)
)
_NwDecIVEventTable_Object = MibTable
nwDecIVEventTable = _NwDecIVEventTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    nwDecIVEventTable.setStatus("mandatory")
_NwDecIVEventEntry_Object = MibTableRow
nwDecIVEventEntry = _NwDecIVEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1)
)
nwDecIVEventEntry.setIndexNames(
    (0, "CTRON-DECIV-ROUTER-MIB", "nwDecIVEventNumber"),
)
if mibBuilder.loadTexts:
    nwDecIVEventEntry.setStatus("mandatory")
_NwDecIVEventNumber_Type = Integer32
_NwDecIVEventNumber_Object = MibTableColumn
nwDecIVEventNumber = _NwDecIVEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1, 1),
    _NwDecIVEventNumber_Type()
)
nwDecIVEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventNumber.setStatus("mandatory")
_NwDecIVEventTime_Type = TimeTicks
_NwDecIVEventTime_Object = MibTableColumn
nwDecIVEventTime = _NwDecIVEventTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1, 2),
    _NwDecIVEventTime_Type()
)
nwDecIVEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventTime.setStatus("mandatory")


class _NwDecIVEventType_Type(Integer32):
    """Custom type nwDecIVEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("error", 32),
          ("event", 16),
          ("misc", 1),
          ("rcv", 4),
          ("timer", 2),
          ("xmit", 8))
    )


_NwDecIVEventType_Type.__name__ = "Integer32"
_NwDecIVEventType_Object = MibTableColumn
nwDecIVEventType = _NwDecIVEventType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1, 3),
    _NwDecIVEventType_Type()
)
nwDecIVEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventType.setStatus("mandatory")


class _NwDecIVEventSeverity_Type(Integer32):
    """Custom type nwDecIVEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highest", 1),
          ("highlow", 3),
          ("highmed", 2))
    )


_NwDecIVEventSeverity_Type.__name__ = "Integer32"
_NwDecIVEventSeverity_Object = MibTableColumn
nwDecIVEventSeverity = _NwDecIVEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1, 4),
    _NwDecIVEventSeverity_Type()
)
nwDecIVEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventSeverity.setStatus("mandatory")
_NwDecIVEventProtocol_Type = Integer32
_NwDecIVEventProtocol_Object = MibTableColumn
nwDecIVEventProtocol = _NwDecIVEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1, 5),
    _NwDecIVEventProtocol_Type()
)
nwDecIVEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventProtocol.setStatus("mandatory")
_NwDecIVEventIfNum_Type = Integer32
_NwDecIVEventIfNum_Object = MibTableColumn
nwDecIVEventIfNum = _NwDecIVEventIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1, 6),
    _NwDecIVEventIfNum_Type()
)
nwDecIVEventIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventIfNum.setStatus("mandatory")
_NwDecIVEventTextString_Type = OctetString
_NwDecIVEventTextString_Object = MibTableColumn
nwDecIVEventTextString = _NwDecIVEventTextString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 10, 3, 1, 1, 7),
    _NwDecIVEventTextString_Type()
)
nwDecIVEventTextString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDecIVEventTextString.setStatus("mandatory")
_NwDecIVWorkGroup_ObjectIdentity = ObjectIdentity
nwDecIVWorkGroup = _NwDecIVWorkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 3, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-DECIV-ROUTER-MIB",
    **{"DecIVAddress": DecIVAddress,
       "nwDecIVRouter": nwDecIVRouter,
       "nwDecIVMibs": nwDecIVMibs,
       "nwDecIVMibRevText": nwDecIVMibRevText,
       "nwDecIVComponents": nwDecIVComponents,
       "nwDecIVSystem": nwDecIVSystem,
       "nwDecIVSysConfig": nwDecIVSysConfig,
       "nwDecIVSysRouterId": nwDecIVSysRouterId,
       "nwDecIVNodeType": nwDecIVNodeType,
       "nwDecIVMaxNodes": nwDecIVMaxNodes,
       "nwDecIVMaxBRA": nwDecIVMaxBRA,
       "nwDecIVMaxBEA": nwDecIVMaxBEA,
       "nwDecIVMaxHops": nwDecIVMaxHops,
       "nwDecIVMaxCost": nwDecIVMaxCost,
       "nwDecIVMaxVisits": nwDecIVMaxVisits,
       "nwDecIVNonBroadcastTimer": nwDecIVNonBroadcastTimer,
       "nwDecIVBroadcastTimer": nwDecIVBroadcastTimer,
       "nwDecIVAreas": nwDecIVAreas,
       "nwDecIVMaxAreaHops": nwDecIVMaxAreaHops,
       "nwDecIVMaxAreaCost": nwDecIVMaxAreaCost,
       "nwDecIVSysAdministration": nwDecIVSysAdministration,
       "nwDecIVSysAdminStatus": nwDecIVSysAdminStatus,
       "nwDecIVSysOperStatus": nwDecIVSysOperStatus,
       "nwDecIVSysAdminReset": nwDecIVSysAdminReset,
       "nwDecIVSysOperationalTime": nwDecIVSysOperationalTime,
       "nwDecIVSysVersion": nwDecIVSysVersion,
       "nwDecIVForwarding": nwDecIVForwarding,
       "nwDecIVFwdSystem": nwDecIVFwdSystem,
       "nwDecIVFwdCounters": nwDecIVFwdCounters,
       "nwDecIVFwdCtrAdminStatus": nwDecIVFwdCtrAdminStatus,
       "nwDecIVFwdCtrReset": nwDecIVFwdCtrReset,
       "nwDecIVFwdCtrOperationalTime": nwDecIVFwdCtrOperationalTime,
       "nwDecIVFwdCtrInPkts": nwDecIVFwdCtrInPkts,
       "nwDecIVFwdCtrOutPkts": nwDecIVFwdCtrOutPkts,
       "nwDecIVFwdCtrFwdPkts": nwDecIVFwdCtrFwdPkts,
       "nwDecIVFwdCtrFilteredPkts": nwDecIVFwdCtrFilteredPkts,
       "nwDecIVFwdCtrDiscardPkts": nwDecIVFwdCtrDiscardPkts,
       "nwDecIVFwdCtrAddrErrPkts": nwDecIVFwdCtrAddrErrPkts,
       "nwDecIVFwdCtrLenErrPkts": nwDecIVFwdCtrLenErrPkts,
       "nwDecIVFwdCtrHdrErrPkts": nwDecIVFwdCtrHdrErrPkts,
       "nwDecIVFwdCtrInBytes": nwDecIVFwdCtrInBytes,
       "nwDecIVFwdCtrOutBytes": nwDecIVFwdCtrOutBytes,
       "nwDecIVFwdCtrFwdBytes": nwDecIVFwdCtrFwdBytes,
       "nwDecIVFwdCtrFilteredBytes": nwDecIVFwdCtrFilteredBytes,
       "nwDecIVFwdCtrDiscardBytes": nwDecIVFwdCtrDiscardBytes,
       "nwDecIVFwdCtrHostInPkts": nwDecIVFwdCtrHostInPkts,
       "nwDecIVFwdCtrHostOutPkts": nwDecIVFwdCtrHostOutPkts,
       "nwDecIVFwdCtrHostDiscardPkts": nwDecIVFwdCtrHostDiscardPkts,
       "nwDecIVFwdCtrHostInBytes": nwDecIVFwdCtrHostInBytes,
       "nwDecIVFwdCtrHostOutBytes": nwDecIVFwdCtrHostOutBytes,
       "nwDecIVFwdCtrHostDiscardBytes": nwDecIVFwdCtrHostDiscardBytes,
       "nwDecIVFwdInterfaces": nwDecIVFwdInterfaces,
       "nwDecIVFwdIfConfig": nwDecIVFwdIfConfig,
       "nwDecIVFwdIfTable": nwDecIVFwdIfTable,
       "nwDecIVFwdIfEntry": nwDecIVFwdIfEntry,
       "nwDecIVFwdIfIndex": nwDecIVFwdIfIndex,
       "nwDecIVFwdIfAdminStatus": nwDecIVFwdIfAdminStatus,
       "nwDecIVFwdIfOperStatus": nwDecIVFwdIfOperStatus,
       "nwDecIVFwdIfOperationalTime": nwDecIVFwdIfOperationalTime,
       "nwDecIVFwdIfControl": nwDecIVFwdIfControl,
       "nwDecIVFwdIfMtu": nwDecIVFwdIfMtu,
       "nwDecIVFwdIfForwarding": nwDecIVFwdIfForwarding,
       "nwDecIVFwdIfFrameType": nwDecIVFwdIfFrameType,
       "nwDecIVFwdIfAclIdentifier": nwDecIVFwdIfAclIdentifier,
       "nwDecIVFwdIfAclStatus": nwDecIVFwdIfAclStatus,
       "nwDecIVFwdIfCacheControl": nwDecIVFwdIfCacheControl,
       "nwDecIVFwdIfCacheEntries": nwDecIVFwdIfCacheEntries,
       "nwDecIVFwdIfCacheHits": nwDecIVFwdIfCacheHits,
       "nwDecIVFwdIfCacheMisses": nwDecIVFwdIfCacheMisses,
       "nwDecIVFwdIfCounters": nwDecIVFwdIfCounters,
       "nwDecIVFwdIfCtrTable": nwDecIVFwdIfCtrTable,
       "nwDecIVFwdIfCtrEntry": nwDecIVFwdIfCtrEntry,
       "nwDecIVFwdIfCtrIfIndex": nwDecIVFwdIfCtrIfIndex,
       "nwDecIVFwdIfCtrAdminStatus": nwDecIVFwdIfCtrAdminStatus,
       "nwDecIVFwdIfCtrReset": nwDecIVFwdIfCtrReset,
       "nwDecIVFwdIfCtrOperationalTime": nwDecIVFwdIfCtrOperationalTime,
       "nwDecIVFwdIfCtrInPkts": nwDecIVFwdIfCtrInPkts,
       "nwDecIVFwdIfCtrOutPkts": nwDecIVFwdIfCtrOutPkts,
       "nwDecIVFwdIfCtrFwdPkts": nwDecIVFwdIfCtrFwdPkts,
       "nwDecIVFwdIfCtrFilteredPkts": nwDecIVFwdIfCtrFilteredPkts,
       "nwDecIVFwdIfCtrDiscardPkts": nwDecIVFwdIfCtrDiscardPkts,
       "nwDecIVFwdIfCtrAddrErrPkts": nwDecIVFwdIfCtrAddrErrPkts,
       "nwDecIVFwdIfCtrLenErrPkts": nwDecIVFwdIfCtrLenErrPkts,
       "nwDecIVFwdIfCtrHdrErrPkts": nwDecIVFwdIfCtrHdrErrPkts,
       "nwDecIVFwdIfCtrInBytes": nwDecIVFwdIfCtrInBytes,
       "nwDecIVFwdIfCtrOutBytes": nwDecIVFwdIfCtrOutBytes,
       "nwDecIVFwdIfCtrFwdBytes": nwDecIVFwdIfCtrFwdBytes,
       "nwDecIVFwdIfCtrFilteredBytes": nwDecIVFwdIfCtrFilteredBytes,
       "nwDecIVFwdIfCtrDiscardBytes": nwDecIVFwdIfCtrDiscardBytes,
       "nwDecIVFwdIfCtrHostInPkts": nwDecIVFwdIfCtrHostInPkts,
       "nwDecIVFwdIfCtrHostOutPkts": nwDecIVFwdIfCtrHostOutPkts,
       "nwDecIVFwdIfCtrHostDiscardPkts": nwDecIVFwdIfCtrHostDiscardPkts,
       "nwDecIVFwdIfCtrHostInBytes": nwDecIVFwdIfCtrHostInBytes,
       "nwDecIVFwdIfCtrHostOutBytes": nwDecIVFwdIfCtrHostOutBytes,
       "nwDecIVFwdIfCtrHostDiscardBytes": nwDecIVFwdIfCtrHostDiscardBytes,
       "nwDecIVTopology": nwDecIVTopology,
       "nwDecIVDistanceVector": nwDecIVDistanceVector,
       "nwDecIVProto": nwDecIVProto,
       "nwDecIVProtoSystem": nwDecIVProtoSystem,
       "nwDecIVProtoConfig": nwDecIVProtoConfig,
       "nwDecIVProtoAdminStatus": nwDecIVProtoAdminStatus,
       "nwDecIVProtoOperStatus": nwDecIVProtoOperStatus,
       "nwDecIVProtoAdminReset": nwDecIVProtoAdminReset,
       "nwDecIVProtoOperationalTime": nwDecIVProtoOperationalTime,
       "nwDecIVProtoVersion": nwDecIVProtoVersion,
       "nwDecIVProtoStackSize": nwDecIVProtoStackSize,
       "nwDecIVProtoThreadPriority": nwDecIVProtoThreadPriority,
       "nwDecIVProtoDatabaseThreshold": nwDecIVProtoDatabaseThreshold,
       "nwDecIVProtoAgeOut": nwDecIVProtoAgeOut,
       "nwDecIVProtoHoldDown": nwDecIVProtoHoldDown,
       "nwDecIVProtoCounters": nwDecIVProtoCounters,
       "nwDecIVProtoCtrAdminStatus": nwDecIVProtoCtrAdminStatus,
       "nwDecIVProtoCtrReset": nwDecIVProtoCtrReset,
       "nwDecIVProtoCtrOperationalTime": nwDecIVProtoCtrOperationalTime,
       "nwDecIVProtoCtrInPkts": nwDecIVProtoCtrInPkts,
       "nwDecIVProtoCtrOutPkts": nwDecIVProtoCtrOutPkts,
       "nwDecIVProtoCtrFilteredPkts": nwDecIVProtoCtrFilteredPkts,
       "nwDecIVProtoCtrDiscardPkts": nwDecIVProtoCtrDiscardPkts,
       "nwDecIVProtoCtrInBytes": nwDecIVProtoCtrInBytes,
       "nwDecIVProtoCtrOutBytes": nwDecIVProtoCtrOutBytes,
       "nwDecIVProtoCtrFilteredBytes": nwDecIVProtoCtrFilteredBytes,
       "nwDecIVProtoCtrDiscardBytes": nwDecIVProtoCtrDiscardBytes,
       "nwDecIVProtoInterface": nwDecIVProtoInterface,
       "nwDecIVProtoIfConfig": nwDecIVProtoIfConfig,
       "nwDecIVProtoIfTable": nwDecIVProtoIfTable,
       "nwDecIVProtoIfEntry": nwDecIVProtoIfEntry,
       "nwDecIVProtoIfIndex": nwDecIVProtoIfIndex,
       "nwDecIVProtoIfAdminStatus": nwDecIVProtoIfAdminStatus,
       "nwDecIVProtoIfOperStatus": nwDecIVProtoIfOperStatus,
       "nwDecIVProtoIfOperationalTime": nwDecIVProtoIfOperationalTime,
       "nwDecIVProtoIfVersion": nwDecIVProtoIfVersion,
       "nwDecIVProtoIfAdvertisement": nwDecIVProtoIfAdvertisement,
       "nwDecIVProtoIfFloodDelay": nwDecIVProtoIfFloodDelay,
       "nwDecIVProtoIfRequestDelay": nwDecIVProtoIfRequestDelay,
       "nwDecIVProtoIfPriority": nwDecIVProtoIfPriority,
       "nwDecIVProtoIfHelloTimer": nwDecIVProtoIfHelloTimer,
       "nwDecIVProtoIfSplitHorizon": nwDecIVProtoIfSplitHorizon,
       "nwDecIVProtoIfPoisonReverse": nwDecIVProtoIfPoisonReverse,
       "nwDecIVProtoIfSnooping": nwDecIVProtoIfSnooping,
       "nwDecIVProtoIfType": nwDecIVProtoIfType,
       "nwDecIVProtoIfXmitCost": nwDecIVProtoIfXmitCost,
       "nwDecIVProtoIfAclIdentifier": nwDecIVProtoIfAclIdentifier,
       "nwDecIVProtoIfAclStatus": nwDecIVProtoIfAclStatus,
       "nwDecIVProtoIfCounters": nwDecIVProtoIfCounters,
       "nwDecIVProtoIfCtrTable": nwDecIVProtoIfCtrTable,
       "nwDecIVProtoIfCtrEntry": nwDecIVProtoIfCtrEntry,
       "nwDecIVProtoIfCtrIfIndex": nwDecIVProtoIfCtrIfIndex,
       "nwDecIVProtoIfCtrAdminStatus": nwDecIVProtoIfCtrAdminStatus,
       "nwDecIVProtoIfCtrReset": nwDecIVProtoIfCtrReset,
       "nwDecIVProtoIfCtrOperationalTime": nwDecIVProtoIfCtrOperationalTime,
       "nwDecIVProtoIfCtrInPkts": nwDecIVProtoIfCtrInPkts,
       "nwDecIVProtoIfCtrOutPkts": nwDecIVProtoIfCtrOutPkts,
       "nwDecIVProtoIfCtrFilteredPkts": nwDecIVProtoIfCtrFilteredPkts,
       "nwDecIVProtoIfCtrDiscardPkts": nwDecIVProtoIfCtrDiscardPkts,
       "nwDecIVProtoIfCtrInBytes": nwDecIVProtoIfCtrInBytes,
       "nwDecIVProtoIfCtrOutBytes": nwDecIVProtoIfCtrOutBytes,
       "nwDecIVProtoIfCtrFilteredBytes": nwDecIVProtoIfCtrFilteredBytes,
       "nwDecIVProtoIfCtrDiscardBytes": nwDecIVProtoIfCtrDiscardBytes,
       "nwDecIVLinkState": nwDecIVLinkState,
       "nwDecIVFib": nwDecIVFib,
       "nwDecIVFibTable": nwDecIVFibTable,
       "nwDecIVFibEntry": nwDecIVFibEntry,
       "nwDecIVFibNodeId": nwDecIVFibNodeId,
       "nwDecIVFibNextHopNodeId": nwDecIVFibNextHopNodeId,
       "nwDecIVFibNextHopIf": nwDecIVFibNextHopIf,
       "nwDecIVFibRouteType": nwDecIVFibRouteType,
       "nwDecIVEndSystems": nwDecIVEndSystems,
       "nwDecIVHostsSystem": nwDecIVHostsSystem,
       "nwDecIVHostsInterfaces": nwDecIVHostsInterfaces,
       "nwDecIVHostsToMedia": nwDecIVHostsToMedia,
       "nwDecIVHostMapTable": nwDecIVHostMapTable,
       "nwDecIVHostMapEntry": nwDecIVHostMapEntry,
       "nwDecIVHostMapIfIndex": nwDecIVHostMapIfIndex,
       "nwDecIVHostMapDecIVAddr": nwDecIVHostMapDecIVAddr,
       "nwDecIVHostMapType": nwDecIVHostMapType,
       "nwDecIVHostMapCircuitID": nwDecIVHostMapCircuitID,
       "nwDecIVHostMapFraming": nwDecIVHostMapFraming,
       "nwDecIVHostMapPortNumber": nwDecIVHostMapPortNumber,
       "nwDecIVAccessControl": nwDecIVAccessControl,
       "nwDecIVAclValidEntries": nwDecIVAclValidEntries,
       "nwDecIVAclTable": nwDecIVAclTable,
       "nwDecIVAclEntry": nwDecIVAclEntry,
       "nwDecIVAclIdentifier": nwDecIVAclIdentifier,
       "nwDecIVAclSequence": nwDecIVAclSequence,
       "nwDecIVAclPermission": nwDecIVAclPermission,
       "nwDecIVAclMatches": nwDecIVAclMatches,
       "nwDecIVAclDestAddress": nwDecIVAclDestAddress,
       "nwDecIVAclSrcAddress": nwDecIVAclSrcAddress,
       "nwDecIVFilters": nwDecIVFilters,
       "nwDecIVRedirector": nwDecIVRedirector,
       "nwDecIVEvent": nwDecIVEvent,
       "nwDecIVEventLogConfig": nwDecIVEventLogConfig,
       "nwDecIVEventAdminStatus": nwDecIVEventAdminStatus,
       "nwDecIVEventMaxEntries": nwDecIVEventMaxEntries,
       "nwDecIVEventTraceAll": nwDecIVEventTraceAll,
       "nwDecIVEventLogFilterTable": nwDecIVEventLogFilterTable,
       "nwDecIVEventFilterTable": nwDecIVEventFilterTable,
       "nwDecIVEventFilterEntry": nwDecIVEventFilterEntry,
       "nwDecIVEventFltrProtocol": nwDecIVEventFltrProtocol,
       "nwDecIVEventFltrIfNum": nwDecIVEventFltrIfNum,
       "nwDecIVEventFltrControl": nwDecIVEventFltrControl,
       "nwDecIVEventFltrType": nwDecIVEventFltrType,
       "nwDecIVEventFltrSeverity": nwDecIVEventFltrSeverity,
       "nwDecIVEventFltrAction": nwDecIVEventFltrAction,
       "nwDecIVEventLogTable": nwDecIVEventLogTable,
       "nwDecIVEventTable": nwDecIVEventTable,
       "nwDecIVEventEntry": nwDecIVEventEntry,
       "nwDecIVEventNumber": nwDecIVEventNumber,
       "nwDecIVEventTime": nwDecIVEventTime,
       "nwDecIVEventType": nwDecIVEventType,
       "nwDecIVEventSeverity": nwDecIVEventSeverity,
       "nwDecIVEventProtocol": nwDecIVEventProtocol,
       "nwDecIVEventIfNum": nwDecIVEventIfNum,
       "nwDecIVEventTextString": nwDecIVEventTextString,
       "nwDecIVWorkGroup": nwDecIVWorkGroup}
)
