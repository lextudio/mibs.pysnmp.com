# SNMP MIB module (CTRON-IP-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-IP-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:43 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NwIpRouter_ObjectIdentity = ObjectIdentity
nwIpRouter = _NwIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1)
)
_NwIpMibs_ObjectIdentity = ObjectIdentity
nwIpMibs = _NwIpMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 1)
)
_NwIpMibRevText_Type = DisplayString
_NwIpMibRevText_Object = MibScalar
nwIpMibRevText = _NwIpMibRevText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 1, 1),
    _NwIpMibRevText_Type()
)
nwIpMibRevText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpMibRevText.setStatus("mandatory")
_NwIpComponents_ObjectIdentity = ObjectIdentity
nwIpComponents = _NwIpComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2)
)
_NwIpSystem_ObjectIdentity = ObjectIdentity
nwIpSystem = _NwIpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1)
)
_NwIpSysConfig_ObjectIdentity = ObjectIdentity
nwIpSysConfig = _NwIpSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 1)
)
_NwIpSysRouterId_Type = IpAddress
_NwIpSysRouterId_Object = MibScalar
nwIpSysRouterId = _NwIpSysRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 1, 1),
    _NwIpSysRouterId_Type()
)
nwIpSysRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpSysRouterId.setStatus("mandatory")
_NwIpSysAdministration_ObjectIdentity = ObjectIdentity
nwIpSysAdministration = _NwIpSysAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 2)
)


class _NwIpSysAdminStatus_Type(Integer32):
    """Custom type nwIpSysAdminStatus based on Integer32"""
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


_NwIpSysAdminStatus_Type.__name__ = "Integer32"
_NwIpSysAdminStatus_Object = MibScalar
nwIpSysAdminStatus = _NwIpSysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 2, 1),
    _NwIpSysAdminStatus_Type()
)
nwIpSysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpSysAdminStatus.setStatus("mandatory")


class _NwIpSysOperStatus_Type(Integer32):
    """Custom type nwIpSysOperStatus based on Integer32"""
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


_NwIpSysOperStatus_Type.__name__ = "Integer32"
_NwIpSysOperStatus_Object = MibScalar
nwIpSysOperStatus = _NwIpSysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 2, 2),
    _NwIpSysOperStatus_Type()
)
nwIpSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpSysOperStatus.setStatus("mandatory")


class _NwIpSysAdminReset_Type(Integer32):
    """Custom type nwIpSysAdminReset based on Integer32"""
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


_NwIpSysAdminReset_Type.__name__ = "Integer32"
_NwIpSysAdminReset_Object = MibScalar
nwIpSysAdminReset = _NwIpSysAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 2, 3),
    _NwIpSysAdminReset_Type()
)
nwIpSysAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpSysAdminReset.setStatus("mandatory")
_NwIpSysOperationalTime_Type = TimeTicks
_NwIpSysOperationalTime_Object = MibScalar
nwIpSysOperationalTime = _NwIpSysOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 2, 4),
    _NwIpSysOperationalTime_Type()
)
nwIpSysOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpSysOperationalTime.setStatus("mandatory")
_NwIpSysVersion_Type = DisplayString
_NwIpSysVersion_Object = MibScalar
nwIpSysVersion = _NwIpSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 1, 2, 5),
    _NwIpSysVersion_Type()
)
nwIpSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpSysVersion.setStatus("mandatory")
_NwIpForwarding_ObjectIdentity = ObjectIdentity
nwIpForwarding = _NwIpForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2)
)
_NwIpFwdSystem_ObjectIdentity = ObjectIdentity
nwIpFwdSystem = _NwIpFwdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1)
)
_NwIpFwdCounters_ObjectIdentity = ObjectIdentity
nwIpFwdCounters = _NwIpFwdCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1)
)


class _NwIpFwdCtrAdminStatus_Type(Integer32):
    """Custom type nwIpFwdCtrAdminStatus based on Integer32"""
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


_NwIpFwdCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpFwdCtrAdminStatus_Object = MibScalar
nwIpFwdCtrAdminStatus = _NwIpFwdCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 1),
    _NwIpFwdCtrAdminStatus_Type()
)
nwIpFwdCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdCtrAdminStatus.setStatus("mandatory")


class _NwIpFwdCtrReset_Type(Integer32):
    """Custom type nwIpFwdCtrReset based on Integer32"""
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


_NwIpFwdCtrReset_Type.__name__ = "Integer32"
_NwIpFwdCtrReset_Object = MibScalar
nwIpFwdCtrReset = _NwIpFwdCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 2),
    _NwIpFwdCtrReset_Type()
)
nwIpFwdCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdCtrReset.setStatus("mandatory")
_NwIpFwdCtrOperationalTime_Type = TimeTicks
_NwIpFwdCtrOperationalTime_Object = MibScalar
nwIpFwdCtrOperationalTime = _NwIpFwdCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 3),
    _NwIpFwdCtrOperationalTime_Type()
)
nwIpFwdCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrOperationalTime.setStatus("mandatory")
_NwIpFwdCtrInPkts_Type = Counter32
_NwIpFwdCtrInPkts_Object = MibScalar
nwIpFwdCtrInPkts = _NwIpFwdCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 4),
    _NwIpFwdCtrInPkts_Type()
)
nwIpFwdCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrInPkts.setStatus("mandatory")
_NwIpFwdCtrOutPkts_Type = Counter32
_NwIpFwdCtrOutPkts_Object = MibScalar
nwIpFwdCtrOutPkts = _NwIpFwdCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 5),
    _NwIpFwdCtrOutPkts_Type()
)
nwIpFwdCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrOutPkts.setStatus("mandatory")
_NwIpFwdCtrFwdPkts_Type = Counter32
_NwIpFwdCtrFwdPkts_Object = MibScalar
nwIpFwdCtrFwdPkts = _NwIpFwdCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 6),
    _NwIpFwdCtrFwdPkts_Type()
)
nwIpFwdCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrFwdPkts.setStatus("mandatory")
_NwIpFwdCtrFilteredPkts_Type = Counter32
_NwIpFwdCtrFilteredPkts_Object = MibScalar
nwIpFwdCtrFilteredPkts = _NwIpFwdCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 7),
    _NwIpFwdCtrFilteredPkts_Type()
)
nwIpFwdCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrFilteredPkts.setStatus("mandatory")
_NwIpFwdCtrDiscardPkts_Type = Counter32
_NwIpFwdCtrDiscardPkts_Object = MibScalar
nwIpFwdCtrDiscardPkts = _NwIpFwdCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 8),
    _NwIpFwdCtrDiscardPkts_Type()
)
nwIpFwdCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrDiscardPkts.setStatus("mandatory")
_NwIpFwdCtrAddrErrPkts_Type = Counter32
_NwIpFwdCtrAddrErrPkts_Object = MibScalar
nwIpFwdCtrAddrErrPkts = _NwIpFwdCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 9),
    _NwIpFwdCtrAddrErrPkts_Type()
)
nwIpFwdCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrAddrErrPkts.setStatus("mandatory")
_NwIpFwdCtrLenErrPkts_Type = Counter32
_NwIpFwdCtrLenErrPkts_Object = MibScalar
nwIpFwdCtrLenErrPkts = _NwIpFwdCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 10),
    _NwIpFwdCtrLenErrPkts_Type()
)
nwIpFwdCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrLenErrPkts.setStatus("mandatory")
_NwIpFwdCtrHdrErrPkts_Type = Counter32
_NwIpFwdCtrHdrErrPkts_Object = MibScalar
nwIpFwdCtrHdrErrPkts = _NwIpFwdCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 11),
    _NwIpFwdCtrHdrErrPkts_Type()
)
nwIpFwdCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrHdrErrPkts.setStatus("mandatory")
_NwIpFwdCtrInBytes_Type = Counter32
_NwIpFwdCtrInBytes_Object = MibScalar
nwIpFwdCtrInBytes = _NwIpFwdCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 12),
    _NwIpFwdCtrInBytes_Type()
)
nwIpFwdCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrInBytes.setStatus("mandatory")
_NwIpFwdCtrOutBytes_Type = Counter32
_NwIpFwdCtrOutBytes_Object = MibScalar
nwIpFwdCtrOutBytes = _NwIpFwdCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 13),
    _NwIpFwdCtrOutBytes_Type()
)
nwIpFwdCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrOutBytes.setStatus("mandatory")
_NwIpFwdCtrFwdBytes_Type = Counter32
_NwIpFwdCtrFwdBytes_Object = MibScalar
nwIpFwdCtrFwdBytes = _NwIpFwdCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 14),
    _NwIpFwdCtrFwdBytes_Type()
)
nwIpFwdCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrFwdBytes.setStatus("mandatory")
_NwIpFwdCtrFilteredBytes_Type = Counter32
_NwIpFwdCtrFilteredBytes_Object = MibScalar
nwIpFwdCtrFilteredBytes = _NwIpFwdCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 15),
    _NwIpFwdCtrFilteredBytes_Type()
)
nwIpFwdCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrFilteredBytes.setStatus("mandatory")
_NwIpFwdCtrDiscardBytes_Type = Counter32
_NwIpFwdCtrDiscardBytes_Object = MibScalar
nwIpFwdCtrDiscardBytes = _NwIpFwdCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 16),
    _NwIpFwdCtrDiscardBytes_Type()
)
nwIpFwdCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrDiscardBytes.setStatus("mandatory")
_NwIpFwdCtrHostInPkts_Type = Counter32
_NwIpFwdCtrHostInPkts_Object = MibScalar
nwIpFwdCtrHostInPkts = _NwIpFwdCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 17),
    _NwIpFwdCtrHostInPkts_Type()
)
nwIpFwdCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrHostInPkts.setStatus("mandatory")
_NwIpFwdCtrHostOutPkts_Type = Counter32
_NwIpFwdCtrHostOutPkts_Object = MibScalar
nwIpFwdCtrHostOutPkts = _NwIpFwdCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 18),
    _NwIpFwdCtrHostOutPkts_Type()
)
nwIpFwdCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrHostOutPkts.setStatus("mandatory")
_NwIpFwdCtrHostDiscardPkts_Type = Counter32
_NwIpFwdCtrHostDiscardPkts_Object = MibScalar
nwIpFwdCtrHostDiscardPkts = _NwIpFwdCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 19),
    _NwIpFwdCtrHostDiscardPkts_Type()
)
nwIpFwdCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrHostDiscardPkts.setStatus("mandatory")
_NwIpFwdCtrHostInBytes_Type = Counter32
_NwIpFwdCtrHostInBytes_Object = MibScalar
nwIpFwdCtrHostInBytes = _NwIpFwdCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 20),
    _NwIpFwdCtrHostInBytes_Type()
)
nwIpFwdCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrHostInBytes.setStatus("mandatory")
_NwIpFwdCtrHostOutBytes_Type = Counter32
_NwIpFwdCtrHostOutBytes_Object = MibScalar
nwIpFwdCtrHostOutBytes = _NwIpFwdCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 21),
    _NwIpFwdCtrHostOutBytes_Type()
)
nwIpFwdCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrHostOutBytes.setStatus("mandatory")
_NwIpFwdCtrHostDiscardBytes_Type = Counter32
_NwIpFwdCtrHostDiscardBytes_Object = MibScalar
nwIpFwdCtrHostDiscardBytes = _NwIpFwdCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 1, 1, 22),
    _NwIpFwdCtrHostDiscardBytes_Type()
)
nwIpFwdCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdCtrHostDiscardBytes.setStatus("mandatory")
_NwIpFwdInterfaces_ObjectIdentity = ObjectIdentity
nwIpFwdInterfaces = _NwIpFwdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2)
)
_NwIpFwdIfConfig_ObjectIdentity = ObjectIdentity
nwIpFwdIfConfig = _NwIpFwdIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1)
)
_NwIpFwdIfTable_Object = MibTable
nwIpFwdIfTable = _NwIpFwdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpFwdIfTable.setStatus("mandatory")
_NwIpFwdIfEntry_Object = MibTableRow
nwIpFwdIfEntry = _NwIpFwdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1)
)
nwIpFwdIfEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpFwdIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpFwdIfEntry.setStatus("mandatory")
_NwIpFwdIfIndex_Type = Integer32
_NwIpFwdIfIndex_Object = MibTableColumn
nwIpFwdIfIndex = _NwIpFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 1),
    _NwIpFwdIfIndex_Type()
)
nwIpFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfIndex.setStatus("mandatory")


class _NwIpFwdIfAdminStatus_Type(Integer32):
    """Custom type nwIpFwdIfAdminStatus based on Integer32"""
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


_NwIpFwdIfAdminStatus_Type.__name__ = "Integer32"
_NwIpFwdIfAdminStatus_Object = MibTableColumn
nwIpFwdIfAdminStatus = _NwIpFwdIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 2),
    _NwIpFwdIfAdminStatus_Type()
)
nwIpFwdIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfAdminStatus.setStatus("mandatory")


class _NwIpFwdIfOperStatus_Type(Integer32):
    """Custom type nwIpFwdIfOperStatus based on Integer32"""
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


_NwIpFwdIfOperStatus_Type.__name__ = "Integer32"
_NwIpFwdIfOperStatus_Object = MibTableColumn
nwIpFwdIfOperStatus = _NwIpFwdIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 3),
    _NwIpFwdIfOperStatus_Type()
)
nwIpFwdIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfOperStatus.setStatus("mandatory")
_NwIpFwdIfOperationalTime_Type = TimeTicks
_NwIpFwdIfOperationalTime_Object = MibTableColumn
nwIpFwdIfOperationalTime = _NwIpFwdIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 4),
    _NwIpFwdIfOperationalTime_Type()
)
nwIpFwdIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfOperationalTime.setStatus("mandatory")


class _NwIpFwdIfControl_Type(Integer32):
    """Custom type nwIpFwdIfControl based on Integer32"""
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


_NwIpFwdIfControl_Type.__name__ = "Integer32"
_NwIpFwdIfControl_Object = MibTableColumn
nwIpFwdIfControl = _NwIpFwdIfControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 5),
    _NwIpFwdIfControl_Type()
)
nwIpFwdIfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfControl.setStatus("mandatory")


class _NwIpFwdIfMtu_Type(Integer32):
    """Custom type nwIpFwdIfMtu based on Integer32"""
    defaultValue = 1500


_NwIpFwdIfMtu_Object = MibTableColumn
nwIpFwdIfMtu = _NwIpFwdIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 6),
    _NwIpFwdIfMtu_Type()
)
nwIpFwdIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfMtu.setStatus("mandatory")


class _NwIpFwdIfForwarding_Type(Integer32):
    """Custom type nwIpFwdIfForwarding based on Integer32"""
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


_NwIpFwdIfForwarding_Type.__name__ = "Integer32"
_NwIpFwdIfForwarding_Object = MibTableColumn
nwIpFwdIfForwarding = _NwIpFwdIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 7),
    _NwIpFwdIfForwarding_Type()
)
nwIpFwdIfForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfForwarding.setStatus("mandatory")


class _NwIpFwdIfFrameType_Type(Integer32):
    """Custom type nwIpFwdIfFrameType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
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
          ("localtalk", 7),
          ("nativewan", 8),
          ("other", 1),
          ("slip", 5),
          ("snap", 3))
    )


_NwIpFwdIfFrameType_Type.__name__ = "Integer32"
_NwIpFwdIfFrameType_Object = MibTableColumn
nwIpFwdIfFrameType = _NwIpFwdIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 8),
    _NwIpFwdIfFrameType_Type()
)
nwIpFwdIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfFrameType.setStatus("mandatory")


class _NwIpFwdIfAclIdentifier_Type(Integer32):
    """Custom type nwIpFwdIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwIpFwdIfAclIdentifier_Object = MibTableColumn
nwIpFwdIfAclIdentifier = _NwIpFwdIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 9),
    _NwIpFwdIfAclIdentifier_Type()
)
nwIpFwdIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfAclIdentifier.setStatus("mandatory")


class _NwIpFwdIfAclStatus_Type(Integer32):
    """Custom type nwIpFwdIfAclStatus based on Integer32"""
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


_NwIpFwdIfAclStatus_Type.__name__ = "Integer32"
_NwIpFwdIfAclStatus_Object = MibTableColumn
nwIpFwdIfAclStatus = _NwIpFwdIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 10),
    _NwIpFwdIfAclStatus_Type()
)
nwIpFwdIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfAclStatus.setStatus("mandatory")


class _NwIpFwdIfCacheControl_Type(Integer32):
    """Custom type nwIpFwdIfCacheControl based on Integer32"""
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


_NwIpFwdIfCacheControl_Type.__name__ = "Integer32"
_NwIpFwdIfCacheControl_Object = MibTableColumn
nwIpFwdIfCacheControl = _NwIpFwdIfCacheControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 11),
    _NwIpFwdIfCacheControl_Type()
)
nwIpFwdIfCacheControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfCacheControl.setStatus("mandatory")
_NwIpFwdIfCacheEntries_Type = Counter32
_NwIpFwdIfCacheEntries_Object = MibTableColumn
nwIpFwdIfCacheEntries = _NwIpFwdIfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 12),
    _NwIpFwdIfCacheEntries_Type()
)
nwIpFwdIfCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCacheEntries.setStatus("mandatory")
_NwIpFwdIfCacheHits_Type = Counter32
_NwIpFwdIfCacheHits_Object = MibTableColumn
nwIpFwdIfCacheHits = _NwIpFwdIfCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 13),
    _NwIpFwdIfCacheHits_Type()
)
nwIpFwdIfCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCacheHits.setStatus("mandatory")
_NwIpFwdIfCacheMisses_Type = Counter32
_NwIpFwdIfCacheMisses_Object = MibTableColumn
nwIpFwdIfCacheMisses = _NwIpFwdIfCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 1, 1, 14),
    _NwIpFwdIfCacheMisses_Type()
)
nwIpFwdIfCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCacheMisses.setStatus("mandatory")
_NwIpAddressTable_Object = MibTable
nwIpAddressTable = _NwIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nwIpAddressTable.setStatus("mandatory")
_NwIpAddrEntry_Object = MibTableRow
nwIpAddrEntry = _NwIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1)
)
nwIpAddrEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpAddrIfIndex"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpAddrIfAddress"),
)
if mibBuilder.loadTexts:
    nwIpAddrEntry.setStatus("mandatory")
_NwIpAddrIfIndex_Type = Integer32
_NwIpAddrIfIndex_Object = MibTableColumn
nwIpAddrIfIndex = _NwIpAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1, 1),
    _NwIpAddrIfIndex_Type()
)
nwIpAddrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAddrIfIndex.setStatus("mandatory")
_NwIpAddrIfAddress_Type = IpAddress
_NwIpAddrIfAddress_Object = MibTableColumn
nwIpAddrIfAddress = _NwIpAddrIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1, 2),
    _NwIpAddrIfAddress_Type()
)
nwIpAddrIfAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAddrIfAddress.setStatus("mandatory")


class _NwIpAddrIfControl_Type(Integer32):
    """Custom type nwIpAddrIfControl based on Integer32"""
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


_NwIpAddrIfControl_Type.__name__ = "Integer32"
_NwIpAddrIfControl_Object = MibTableColumn
nwIpAddrIfControl = _NwIpAddrIfControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1, 3),
    _NwIpAddrIfControl_Type()
)
nwIpAddrIfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAddrIfControl.setStatus("mandatory")


class _NwIpAddrIfAddrType_Type(Integer32):
    """Custom type nwIpAddrIfAddrType based on Integer32"""
    defaultValue = 2

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
        *(("other", 1),
          ("primary", 2),
          ("secondary", 3),
          ("workgroup", 4))
    )


_NwIpAddrIfAddrType_Type.__name__ = "Integer32"
_NwIpAddrIfAddrType_Object = MibTableColumn
nwIpAddrIfAddrType = _NwIpAddrIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1, 4),
    _NwIpAddrIfAddrType_Type()
)
nwIpAddrIfAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAddrIfAddrType.setStatus("mandatory")
_NwIpAddrIfMask_Type = IpAddress
_NwIpAddrIfMask_Object = MibTableColumn
nwIpAddrIfMask = _NwIpAddrIfMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1, 5),
    _NwIpAddrIfMask_Type()
)
nwIpAddrIfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAddrIfMask.setStatus("mandatory")


class _NwIpAddrIfBcastAddr_Type(Integer32):
    """Custom type nwIpAddrIfBcastAddr based on Integer32"""
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
        *(("ones", 3),
          ("other", 1),
          ("zeros", 2))
    )


_NwIpAddrIfBcastAddr_Type.__name__ = "Integer32"
_NwIpAddrIfBcastAddr_Object = MibTableColumn
nwIpAddrIfBcastAddr = _NwIpAddrIfBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1, 6),
    _NwIpAddrIfBcastAddr_Type()
)
nwIpAddrIfBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAddrIfBcastAddr.setStatus("mandatory")
_NwIpFwdIfCounters_ObjectIdentity = ObjectIdentity
nwIpFwdIfCounters = _NwIpFwdIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2)
)
_NwIpFwdIfCtrTable_Object = MibTable
nwIpFwdIfCtrTable = _NwIpFwdIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpFwdIfCtrTable.setStatus("mandatory")
_NwIpFwdIfCtrEntry_Object = MibTableRow
nwIpFwdIfCtrEntry = _NwIpFwdIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1)
)
nwIpFwdIfCtrEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpFwdIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpFwdIfCtrEntry.setStatus("mandatory")
_NwIpFwdIfCtrIfIndex_Type = Integer32
_NwIpFwdIfCtrIfIndex_Object = MibTableColumn
nwIpFwdIfCtrIfIndex = _NwIpFwdIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 1),
    _NwIpFwdIfCtrIfIndex_Type()
)
nwIpFwdIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrIfIndex.setStatus("mandatory")


class _NwIpFwdIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpFwdIfCtrAdminStatus based on Integer32"""
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


_NwIpFwdIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpFwdIfCtrAdminStatus_Object = MibTableColumn
nwIpFwdIfCtrAdminStatus = _NwIpFwdIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 2),
    _NwIpFwdIfCtrAdminStatus_Type()
)
nwIpFwdIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrAdminStatus.setStatus("mandatory")


class _NwIpFwdIfCtrReset_Type(Integer32):
    """Custom type nwIpFwdIfCtrReset based on Integer32"""
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


_NwIpFwdIfCtrReset_Type.__name__ = "Integer32"
_NwIpFwdIfCtrReset_Object = MibTableColumn
nwIpFwdIfCtrReset = _NwIpFwdIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 3),
    _NwIpFwdIfCtrReset_Type()
)
nwIpFwdIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrReset.setStatus("mandatory")
_NwIpFwdIfCtrOperationalTime_Type = TimeTicks
_NwIpFwdIfCtrOperationalTime_Object = MibTableColumn
nwIpFwdIfCtrOperationalTime = _NwIpFwdIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 4),
    _NwIpFwdIfCtrOperationalTime_Type()
)
nwIpFwdIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrOperationalTime.setStatus("mandatory")
_NwIpFwdIfCtrInPkts_Type = Counter32
_NwIpFwdIfCtrInPkts_Object = MibTableColumn
nwIpFwdIfCtrInPkts = _NwIpFwdIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 5),
    _NwIpFwdIfCtrInPkts_Type()
)
nwIpFwdIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrInPkts.setStatus("mandatory")
_NwIpFwdIfCtrOutPkts_Type = Counter32
_NwIpFwdIfCtrOutPkts_Object = MibTableColumn
nwIpFwdIfCtrOutPkts = _NwIpFwdIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 6),
    _NwIpFwdIfCtrOutPkts_Type()
)
nwIpFwdIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrOutPkts.setStatus("mandatory")
_NwIpFwdIfCtrFwdPkts_Type = Counter32
_NwIpFwdIfCtrFwdPkts_Object = MibTableColumn
nwIpFwdIfCtrFwdPkts = _NwIpFwdIfCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 7),
    _NwIpFwdIfCtrFwdPkts_Type()
)
nwIpFwdIfCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrFwdPkts.setStatus("mandatory")
_NwIpFwdIfCtrFilteredPkts_Type = Counter32
_NwIpFwdIfCtrFilteredPkts_Object = MibTableColumn
nwIpFwdIfCtrFilteredPkts = _NwIpFwdIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 8),
    _NwIpFwdIfCtrFilteredPkts_Type()
)
nwIpFwdIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrFilteredPkts.setStatus("mandatory")
_NwIpFwdIfCtrDiscardPkts_Type = Counter32
_NwIpFwdIfCtrDiscardPkts_Object = MibTableColumn
nwIpFwdIfCtrDiscardPkts = _NwIpFwdIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 9),
    _NwIpFwdIfCtrDiscardPkts_Type()
)
nwIpFwdIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrDiscardPkts.setStatus("mandatory")
_NwIpFwdIfCtrAddrErrPkts_Type = Counter32
_NwIpFwdIfCtrAddrErrPkts_Object = MibTableColumn
nwIpFwdIfCtrAddrErrPkts = _NwIpFwdIfCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 10),
    _NwIpFwdIfCtrAddrErrPkts_Type()
)
nwIpFwdIfCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrAddrErrPkts.setStatus("mandatory")
_NwIpFwdIfCtrLenErrPkts_Type = Counter32
_NwIpFwdIfCtrLenErrPkts_Object = MibTableColumn
nwIpFwdIfCtrLenErrPkts = _NwIpFwdIfCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 11),
    _NwIpFwdIfCtrLenErrPkts_Type()
)
nwIpFwdIfCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrLenErrPkts.setStatus("mandatory")
_NwIpFwdIfCtrHdrErrPkts_Type = Counter32
_NwIpFwdIfCtrHdrErrPkts_Object = MibTableColumn
nwIpFwdIfCtrHdrErrPkts = _NwIpFwdIfCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 12),
    _NwIpFwdIfCtrHdrErrPkts_Type()
)
nwIpFwdIfCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrHdrErrPkts.setStatus("mandatory")
_NwIpFwdIfCtrInBytes_Type = Counter32
_NwIpFwdIfCtrInBytes_Object = MibTableColumn
nwIpFwdIfCtrInBytes = _NwIpFwdIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 13),
    _NwIpFwdIfCtrInBytes_Type()
)
nwIpFwdIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrInBytes.setStatus("mandatory")
_NwIpFwdIfCtrOutBytes_Type = Counter32
_NwIpFwdIfCtrOutBytes_Object = MibTableColumn
nwIpFwdIfCtrOutBytes = _NwIpFwdIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 14),
    _NwIpFwdIfCtrOutBytes_Type()
)
nwIpFwdIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrOutBytes.setStatus("mandatory")
_NwIpFwdIfCtrFwdBytes_Type = Counter32
_NwIpFwdIfCtrFwdBytes_Object = MibTableColumn
nwIpFwdIfCtrFwdBytes = _NwIpFwdIfCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 15),
    _NwIpFwdIfCtrFwdBytes_Type()
)
nwIpFwdIfCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrFwdBytes.setStatus("mandatory")
_NwIpFwdIfCtrFilteredBytes_Type = Counter32
_NwIpFwdIfCtrFilteredBytes_Object = MibTableColumn
nwIpFwdIfCtrFilteredBytes = _NwIpFwdIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 16),
    _NwIpFwdIfCtrFilteredBytes_Type()
)
nwIpFwdIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrFilteredBytes.setStatus("mandatory")
_NwIpFwdIfCtrDiscardBytes_Type = Counter32
_NwIpFwdIfCtrDiscardBytes_Object = MibTableColumn
nwIpFwdIfCtrDiscardBytes = _NwIpFwdIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 17),
    _NwIpFwdIfCtrDiscardBytes_Type()
)
nwIpFwdIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrDiscardBytes.setStatus("mandatory")
_NwIpFwdIfCtrHostInPkts_Type = Counter32
_NwIpFwdIfCtrHostInPkts_Object = MibTableColumn
nwIpFwdIfCtrHostInPkts = _NwIpFwdIfCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 18),
    _NwIpFwdIfCtrHostInPkts_Type()
)
nwIpFwdIfCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrHostInPkts.setStatus("mandatory")
_NwIpFwdIfCtrHostOutPkts_Type = Counter32
_NwIpFwdIfCtrHostOutPkts_Object = MibTableColumn
nwIpFwdIfCtrHostOutPkts = _NwIpFwdIfCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 19),
    _NwIpFwdIfCtrHostOutPkts_Type()
)
nwIpFwdIfCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrHostOutPkts.setStatus("mandatory")
_NwIpFwdIfCtrHostDiscardPkts_Type = Counter32
_NwIpFwdIfCtrHostDiscardPkts_Object = MibTableColumn
nwIpFwdIfCtrHostDiscardPkts = _NwIpFwdIfCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 20),
    _NwIpFwdIfCtrHostDiscardPkts_Type()
)
nwIpFwdIfCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrHostDiscardPkts.setStatus("mandatory")
_NwIpFwdIfCtrHostInBytes_Type = Counter32
_NwIpFwdIfCtrHostInBytes_Object = MibTableColumn
nwIpFwdIfCtrHostInBytes = _NwIpFwdIfCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 21),
    _NwIpFwdIfCtrHostInBytes_Type()
)
nwIpFwdIfCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrHostInBytes.setStatus("mandatory")
_NwIpFwdIfCtrHostOutBytes_Type = Counter32
_NwIpFwdIfCtrHostOutBytes_Object = MibTableColumn
nwIpFwdIfCtrHostOutBytes = _NwIpFwdIfCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 22),
    _NwIpFwdIfCtrHostOutBytes_Type()
)
nwIpFwdIfCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrHostOutBytes.setStatus("mandatory")
_NwIpFwdIfCtrHostDiscardBytes_Type = Counter32
_NwIpFwdIfCtrHostDiscardBytes_Object = MibTableColumn
nwIpFwdIfCtrHostDiscardBytes = _NwIpFwdIfCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 1, 23),
    _NwIpFwdIfCtrHostDiscardBytes_Type()
)
nwIpFwdIfCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpFwdIfCtrHostDiscardBytes.setStatus("mandatory")
_NwIpTopology_ObjectIdentity = ObjectIdentity
nwIpTopology = _NwIpTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4)
)
_NwIpDistanceVector_ObjectIdentity = ObjectIdentity
nwIpDistanceVector = _NwIpDistanceVector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1)
)
_NwIpRip_ObjectIdentity = ObjectIdentity
nwIpRip = _NwIpRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1)
)
_NwIpRipSystem_ObjectIdentity = ObjectIdentity
nwIpRipSystem = _NwIpRipSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1)
)
_NwIpRipConfig_ObjectIdentity = ObjectIdentity
nwIpRipConfig = _NwIpRipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1)
)


class _NwIpRipAdminStatus_Type(Integer32):
    """Custom type nwIpRipAdminStatus based on Integer32"""
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


_NwIpRipAdminStatus_Type.__name__ = "Integer32"
_NwIpRipAdminStatus_Object = MibScalar
nwIpRipAdminStatus = _NwIpRipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 1),
    _NwIpRipAdminStatus_Type()
)
nwIpRipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipAdminStatus.setStatus("mandatory")


class _NwIpRipOperStatus_Type(Integer32):
    """Custom type nwIpRipOperStatus based on Integer32"""
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


_NwIpRipOperStatus_Type.__name__ = "Integer32"
_NwIpRipOperStatus_Object = MibScalar
nwIpRipOperStatus = _NwIpRipOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 2),
    _NwIpRipOperStatus_Type()
)
nwIpRipOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipOperStatus.setStatus("mandatory")


class _NwIpRipAdminReset_Type(Integer32):
    """Custom type nwIpRipAdminReset based on Integer32"""
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


_NwIpRipAdminReset_Type.__name__ = "Integer32"
_NwIpRipAdminReset_Object = MibScalar
nwIpRipAdminReset = _NwIpRipAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 3),
    _NwIpRipAdminReset_Type()
)
nwIpRipAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipAdminReset.setStatus("mandatory")
_NwIpRipOperationalTime_Type = TimeTicks
_NwIpRipOperationalTime_Object = MibScalar
nwIpRipOperationalTime = _NwIpRipOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 4),
    _NwIpRipOperationalTime_Type()
)
nwIpRipOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipOperationalTime.setStatus("mandatory")
_NwIpRipVersion_Type = DisplayString
_NwIpRipVersion_Object = MibScalar
nwIpRipVersion = _NwIpRipVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 5),
    _NwIpRipVersion_Type()
)
nwIpRipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipVersion.setStatus("mandatory")


class _NwIpRipStackSize_Type(Integer32):
    """Custom type nwIpRipStackSize based on Integer32"""
    defaultValue = 4096


_NwIpRipStackSize_Object = MibScalar
nwIpRipStackSize = _NwIpRipStackSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 6),
    _NwIpRipStackSize_Type()
)
nwIpRipStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipStackSize.setStatus("mandatory")


class _NwIpRipThreadPriority_Type(Integer32):
    """Custom type nwIpRipThreadPriority based on Integer32"""
    defaultValue = 127


_NwIpRipThreadPriority_Object = MibScalar
nwIpRipThreadPriority = _NwIpRipThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 7),
    _NwIpRipThreadPriority_Type()
)
nwIpRipThreadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipThreadPriority.setStatus("mandatory")


class _NwIpRipDatabaseThreshold_Type(Integer32):
    """Custom type nwIpRipDatabaseThreshold based on Integer32"""
    defaultValue = 2000


_NwIpRipDatabaseThreshold_Object = MibScalar
nwIpRipDatabaseThreshold = _NwIpRipDatabaseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 8),
    _NwIpRipDatabaseThreshold_Type()
)
nwIpRipDatabaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipDatabaseThreshold.setStatus("mandatory")


class _NwIpRipAgeOut_Type(Integer32):
    """Custom type nwIpRipAgeOut based on Integer32"""
    defaultValue = 210


_NwIpRipAgeOut_Object = MibScalar
nwIpRipAgeOut = _NwIpRipAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 9),
    _NwIpRipAgeOut_Type()
)
nwIpRipAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipAgeOut.setStatus("mandatory")


class _NwIpRipHoldDown_Type(Integer32):
    """Custom type nwIpRipHoldDown based on Integer32"""
    defaultValue = 120


_NwIpRipHoldDown_Object = MibScalar
nwIpRipHoldDown = _NwIpRipHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 1, 10),
    _NwIpRipHoldDown_Type()
)
nwIpRipHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipHoldDown.setStatus("mandatory")
_NwIpRipCounters_ObjectIdentity = ObjectIdentity
nwIpRipCounters = _NwIpRipCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2)
)


class _NwIpRipCtrAdminStatus_Type(Integer32):
    """Custom type nwIpRipCtrAdminStatus based on Integer32"""
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


_NwIpRipCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpRipCtrAdminStatus_Object = MibScalar
nwIpRipCtrAdminStatus = _NwIpRipCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 1),
    _NwIpRipCtrAdminStatus_Type()
)
nwIpRipCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipCtrAdminStatus.setStatus("mandatory")


class _NwIpRipCtrReset_Type(Integer32):
    """Custom type nwIpRipCtrReset based on Integer32"""
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


_NwIpRipCtrReset_Type.__name__ = "Integer32"
_NwIpRipCtrReset_Object = MibScalar
nwIpRipCtrReset = _NwIpRipCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 2),
    _NwIpRipCtrReset_Type()
)
nwIpRipCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipCtrReset.setStatus("mandatory")
_NwIpRipCtrOperationalTime_Type = TimeTicks
_NwIpRipCtrOperationalTime_Object = MibScalar
nwIpRipCtrOperationalTime = _NwIpRipCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 3),
    _NwIpRipCtrOperationalTime_Type()
)
nwIpRipCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrOperationalTime.setStatus("mandatory")
_NwIpRipCtrInPkts_Type = Counter32
_NwIpRipCtrInPkts_Object = MibScalar
nwIpRipCtrInPkts = _NwIpRipCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 4),
    _NwIpRipCtrInPkts_Type()
)
nwIpRipCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrInPkts.setStatus("mandatory")
_NwIpRipCtrOutPkts_Type = Counter32
_NwIpRipCtrOutPkts_Object = MibScalar
nwIpRipCtrOutPkts = _NwIpRipCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 5),
    _NwIpRipCtrOutPkts_Type()
)
nwIpRipCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrOutPkts.setStatus("mandatory")
_NwIpRipCtrFilteredPkts_Type = Counter32
_NwIpRipCtrFilteredPkts_Object = MibScalar
nwIpRipCtrFilteredPkts = _NwIpRipCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 6),
    _NwIpRipCtrFilteredPkts_Type()
)
nwIpRipCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrFilteredPkts.setStatus("mandatory")
_NwIpRipCtrDiscardPkts_Type = Counter32
_NwIpRipCtrDiscardPkts_Object = MibScalar
nwIpRipCtrDiscardPkts = _NwIpRipCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 7),
    _NwIpRipCtrDiscardPkts_Type()
)
nwIpRipCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrDiscardPkts.setStatus("mandatory")
_NwIpRipCtrInBytes_Type = Counter32
_NwIpRipCtrInBytes_Object = MibScalar
nwIpRipCtrInBytes = _NwIpRipCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 8),
    _NwIpRipCtrInBytes_Type()
)
nwIpRipCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrInBytes.setStatus("mandatory")
_NwIpRipCtrOutBytes_Type = Counter32
_NwIpRipCtrOutBytes_Object = MibScalar
nwIpRipCtrOutBytes = _NwIpRipCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 9),
    _NwIpRipCtrOutBytes_Type()
)
nwIpRipCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrOutBytes.setStatus("mandatory")
_NwIpRipCtrFilteredBytes_Type = Counter32
_NwIpRipCtrFilteredBytes_Object = MibScalar
nwIpRipCtrFilteredBytes = _NwIpRipCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 10),
    _NwIpRipCtrFilteredBytes_Type()
)
nwIpRipCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrFilteredBytes.setStatus("mandatory")
_NwIpRipCtrDiscardBytes_Type = Counter32
_NwIpRipCtrDiscardBytes_Object = MibScalar
nwIpRipCtrDiscardBytes = _NwIpRipCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 1, 2, 11),
    _NwIpRipCtrDiscardBytes_Type()
)
nwIpRipCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipCtrDiscardBytes.setStatus("mandatory")
_NwIpRipInterfaces_ObjectIdentity = ObjectIdentity
nwIpRipInterfaces = _NwIpRipInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2)
)
_NwIpRipIfConfig_ObjectIdentity = ObjectIdentity
nwIpRipIfConfig = _NwIpRipIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1)
)
_NwIpRipIfTable_Object = MibTable
nwIpRipIfTable = _NwIpRipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpRipIfTable.setStatus("mandatory")
_NwIpRipIfEntry_Object = MibTableRow
nwIpRipIfEntry = _NwIpRipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1)
)
nwIpRipIfEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpRipIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpRipIfEntry.setStatus("mandatory")
_NwIpRipIfIndex_Type = Integer32
_NwIpRipIfIndex_Object = MibTableColumn
nwIpRipIfIndex = _NwIpRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 1),
    _NwIpRipIfIndex_Type()
)
nwIpRipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfIndex.setStatus("mandatory")


class _NwIpRipIfAdminStatus_Type(Integer32):
    """Custom type nwIpRipIfAdminStatus based on Integer32"""
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


_NwIpRipIfAdminStatus_Type.__name__ = "Integer32"
_NwIpRipIfAdminStatus_Object = MibTableColumn
nwIpRipIfAdminStatus = _NwIpRipIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 2),
    _NwIpRipIfAdminStatus_Type()
)
nwIpRipIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfAdminStatus.setStatus("mandatory")


class _NwIpRipIfOperStatus_Type(Integer32):
    """Custom type nwIpRipIfOperStatus based on Integer32"""
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


_NwIpRipIfOperStatus_Type.__name__ = "Integer32"
_NwIpRipIfOperStatus_Object = MibTableColumn
nwIpRipIfOperStatus = _NwIpRipIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 3),
    _NwIpRipIfOperStatus_Type()
)
nwIpRipIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfOperStatus.setStatus("mandatory")
_NwIpRipIfOperationalTime_Type = TimeTicks
_NwIpRipIfOperationalTime_Object = MibTableColumn
nwIpRipIfOperationalTime = _NwIpRipIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 4),
    _NwIpRipIfOperationalTime_Type()
)
nwIpRipIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfOperationalTime.setStatus("mandatory")


class _NwIpRipIfVersion_Type(Integer32):
    """Custom type nwIpRipIfVersion based on Integer32"""
    defaultValue = 1


_NwIpRipIfVersion_Object = MibTableColumn
nwIpRipIfVersion = _NwIpRipIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 5),
    _NwIpRipIfVersion_Type()
)
nwIpRipIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfVersion.setStatus("mandatory")


class _NwIpRipIfAdvertisement_Type(Integer32):
    """Custom type nwIpRipIfAdvertisement based on Integer32"""
    defaultValue = 30


_NwIpRipIfAdvertisement_Object = MibTableColumn
nwIpRipIfAdvertisement = _NwIpRipIfAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 6),
    _NwIpRipIfAdvertisement_Type()
)
nwIpRipIfAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfAdvertisement.setStatus("mandatory")


class _NwIpRipIfFloodDelay_Type(Integer32):
    """Custom type nwIpRipIfFloodDelay based on Integer32"""
    defaultValue = 2


_NwIpRipIfFloodDelay_Object = MibTableColumn
nwIpRipIfFloodDelay = _NwIpRipIfFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 7),
    _NwIpRipIfFloodDelay_Type()
)
nwIpRipIfFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfFloodDelay.setStatus("mandatory")


class _NwIpRipIfRequestDelay_Type(Integer32):
    """Custom type nwIpRipIfRequestDelay based on Integer32"""
    defaultValue = 0


_NwIpRipIfRequestDelay_Object = MibTableColumn
nwIpRipIfRequestDelay = _NwIpRipIfRequestDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 8),
    _NwIpRipIfRequestDelay_Type()
)
nwIpRipIfRequestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfRequestDelay.setStatus("mandatory")


class _NwIpRipIfPriority_Type(Integer32):
    """Custom type nwIpRipIfPriority based on Integer32"""
    defaultValue = 1


_NwIpRipIfPriority_Object = MibTableColumn
nwIpRipIfPriority = _NwIpRipIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 9),
    _NwIpRipIfPriority_Type()
)
nwIpRipIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfPriority.setStatus("mandatory")


class _NwIpRipIfHelloTimer_Type(Integer32):
    """Custom type nwIpRipIfHelloTimer based on Integer32"""
    defaultValue = 10


_NwIpRipIfHelloTimer_Object = MibTableColumn
nwIpRipIfHelloTimer = _NwIpRipIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 10),
    _NwIpRipIfHelloTimer_Type()
)
nwIpRipIfHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfHelloTimer.setStatus("mandatory")


class _NwIpRipIfSplitHorizon_Type(Integer32):
    """Custom type nwIpRipIfSplitHorizon based on Integer32"""
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


_NwIpRipIfSplitHorizon_Type.__name__ = "Integer32"
_NwIpRipIfSplitHorizon_Object = MibTableColumn
nwIpRipIfSplitHorizon = _NwIpRipIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 11),
    _NwIpRipIfSplitHorizon_Type()
)
nwIpRipIfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfSplitHorizon.setStatus("mandatory")


class _NwIpRipIfPoisonReverse_Type(Integer32):
    """Custom type nwIpRipIfPoisonReverse based on Integer32"""
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


_NwIpRipIfPoisonReverse_Type.__name__ = "Integer32"
_NwIpRipIfPoisonReverse_Object = MibTableColumn
nwIpRipIfPoisonReverse = _NwIpRipIfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 12),
    _NwIpRipIfPoisonReverse_Type()
)
nwIpRipIfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfPoisonReverse.setStatus("mandatory")


class _NwIpRipIfSnooping_Type(Integer32):
    """Custom type nwIpRipIfSnooping based on Integer32"""
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


_NwIpRipIfSnooping_Type.__name__ = "Integer32"
_NwIpRipIfSnooping_Object = MibTableColumn
nwIpRipIfSnooping = _NwIpRipIfSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 13),
    _NwIpRipIfSnooping_Type()
)
nwIpRipIfSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfSnooping.setStatus("mandatory")


class _NwIpRipIfType_Type(Integer32):
    """Custom type nwIpRipIfType based on Integer32"""
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


_NwIpRipIfType_Type.__name__ = "Integer32"
_NwIpRipIfType_Object = MibTableColumn
nwIpRipIfType = _NwIpRipIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 14),
    _NwIpRipIfType_Type()
)
nwIpRipIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfType.setStatus("mandatory")


class _NwIpRipIfXmitCost_Type(Integer32):
    """Custom type nwIpRipIfXmitCost based on Integer32"""
    defaultValue = 0


_NwIpRipIfXmitCost_Object = MibTableColumn
nwIpRipIfXmitCost = _NwIpRipIfXmitCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 15),
    _NwIpRipIfXmitCost_Type()
)
nwIpRipIfXmitCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfXmitCost.setStatus("mandatory")


class _NwIpRipIfAclIdentifier_Type(Integer32):
    """Custom type nwIpRipIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwIpRipIfAclIdentifier_Object = MibTableColumn
nwIpRipIfAclIdentifier = _NwIpRipIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 16),
    _NwIpRipIfAclIdentifier_Type()
)
nwIpRipIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfAclIdentifier.setStatus("mandatory")


class _NwIpRipIfAclStatus_Type(Integer32):
    """Custom type nwIpRipIfAclStatus based on Integer32"""
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


_NwIpRipIfAclStatus_Type.__name__ = "Integer32"
_NwIpRipIfAclStatus_Object = MibTableColumn
nwIpRipIfAclStatus = _NwIpRipIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 1, 1, 1, 17),
    _NwIpRipIfAclStatus_Type()
)
nwIpRipIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfAclStatus.setStatus("mandatory")
_NwIpRipIfCounters_ObjectIdentity = ObjectIdentity
nwIpRipIfCounters = _NwIpRipIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2)
)
_NwIpRipIfCtrTable_Object = MibTable
nwIpRipIfCtrTable = _NwIpRipIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpRipIfCtrTable.setStatus("mandatory")
_NwIpRipIfCtrEntry_Object = MibTableRow
nwIpRipIfCtrEntry = _NwIpRipIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1)
)
nwIpRipIfCtrEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpRipIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpRipIfCtrEntry.setStatus("mandatory")
_NwIpRipIfCtrIfIndex_Type = Integer32
_NwIpRipIfCtrIfIndex_Object = MibTableColumn
nwIpRipIfCtrIfIndex = _NwIpRipIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 1),
    _NwIpRipIfCtrIfIndex_Type()
)
nwIpRipIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrIfIndex.setStatus("mandatory")


class _NwIpRipIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpRipIfCtrAdminStatus based on Integer32"""
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


_NwIpRipIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpRipIfCtrAdminStatus_Object = MibTableColumn
nwIpRipIfCtrAdminStatus = _NwIpRipIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 2),
    _NwIpRipIfCtrAdminStatus_Type()
)
nwIpRipIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfCtrAdminStatus.setStatus("mandatory")


class _NwIpRipIfCtrReset_Type(Integer32):
    """Custom type nwIpRipIfCtrReset based on Integer32"""
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


_NwIpRipIfCtrReset_Type.__name__ = "Integer32"
_NwIpRipIfCtrReset_Object = MibTableColumn
nwIpRipIfCtrReset = _NwIpRipIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 3),
    _NwIpRipIfCtrReset_Type()
)
nwIpRipIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipIfCtrReset.setStatus("mandatory")
_NwIpRipIfCtrOperationalTime_Type = TimeTicks
_NwIpRipIfCtrOperationalTime_Object = MibTableColumn
nwIpRipIfCtrOperationalTime = _NwIpRipIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 4),
    _NwIpRipIfCtrOperationalTime_Type()
)
nwIpRipIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrOperationalTime.setStatus("mandatory")
_NwIpRipIfCtrInPkts_Type = Counter32
_NwIpRipIfCtrInPkts_Object = MibTableColumn
nwIpRipIfCtrInPkts = _NwIpRipIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 5),
    _NwIpRipIfCtrInPkts_Type()
)
nwIpRipIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrInPkts.setStatus("mandatory")
_NwIpRipIfCtrOutPkts_Type = Counter32
_NwIpRipIfCtrOutPkts_Object = MibTableColumn
nwIpRipIfCtrOutPkts = _NwIpRipIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 6),
    _NwIpRipIfCtrOutPkts_Type()
)
nwIpRipIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrOutPkts.setStatus("mandatory")
_NwIpRipIfCtrFilteredPkts_Type = Counter32
_NwIpRipIfCtrFilteredPkts_Object = MibTableColumn
nwIpRipIfCtrFilteredPkts = _NwIpRipIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 7),
    _NwIpRipIfCtrFilteredPkts_Type()
)
nwIpRipIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrFilteredPkts.setStatus("mandatory")
_NwIpRipIfCtrDiscardPkts_Type = Counter32
_NwIpRipIfCtrDiscardPkts_Object = MibTableColumn
nwIpRipIfCtrDiscardPkts = _NwIpRipIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 8),
    _NwIpRipIfCtrDiscardPkts_Type()
)
nwIpRipIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrDiscardPkts.setStatus("mandatory")
_NwIpRipIfCtrInBytes_Type = Counter32
_NwIpRipIfCtrInBytes_Object = MibTableColumn
nwIpRipIfCtrInBytes = _NwIpRipIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 9),
    _NwIpRipIfCtrInBytes_Type()
)
nwIpRipIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrInBytes.setStatus("mandatory")
_NwIpRipIfCtrOutBytes_Type = Counter32
_NwIpRipIfCtrOutBytes_Object = MibTableColumn
nwIpRipIfCtrOutBytes = _NwIpRipIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 10),
    _NwIpRipIfCtrOutBytes_Type()
)
nwIpRipIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrOutBytes.setStatus("mandatory")
_NwIpRipIfCtrFilteredBytes_Type = Counter32
_NwIpRipIfCtrFilteredBytes_Object = MibTableColumn
nwIpRipIfCtrFilteredBytes = _NwIpRipIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 11),
    _NwIpRipIfCtrFilteredBytes_Type()
)
nwIpRipIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrFilteredBytes.setStatus("mandatory")
_NwIpRipIfCtrDiscardBytes_Type = Counter32
_NwIpRipIfCtrDiscardBytes_Object = MibTableColumn
nwIpRipIfCtrDiscardBytes = _NwIpRipIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 2, 2, 1, 1, 12),
    _NwIpRipIfCtrDiscardBytes_Type()
)
nwIpRipIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipIfCtrDiscardBytes.setStatus("mandatory")
_NwIpRipDatabase_ObjectIdentity = ObjectIdentity
nwIpRipDatabase = _NwIpRipDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3)
)
_NwIpRipRouteTable_Object = MibTable
nwIpRipRouteTable = _NwIpRipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nwIpRipRouteTable.setStatus("mandatory")
_NwIpRipRouteEntry_Object = MibTableRow
nwIpRipRouteEntry = _NwIpRipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1)
)
nwIpRipRouteEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpRipRtNetId"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpRipRtIfIndex"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpRipRtSrcNode"),
)
if mibBuilder.loadTexts:
    nwIpRipRouteEntry.setStatus("mandatory")
_NwIpRipRtNetId_Type = IpAddress
_NwIpRipRtNetId_Object = MibTableColumn
nwIpRipRtNetId = _NwIpRipRtNetId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 1),
    _NwIpRipRtNetId_Type()
)
nwIpRipRtNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtNetId.setStatus("mandatory")
_NwIpRipRtIfIndex_Type = Integer32
_NwIpRipRtIfIndex_Object = MibTableColumn
nwIpRipRtIfIndex = _NwIpRipRtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 2),
    _NwIpRipRtIfIndex_Type()
)
nwIpRipRtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtIfIndex.setStatus("mandatory")
_NwIpRipRtSrcNode_Type = IpAddress
_NwIpRipRtSrcNode_Object = MibTableColumn
nwIpRipRtSrcNode = _NwIpRipRtSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 3),
    _NwIpRipRtSrcNode_Type()
)
nwIpRipRtSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtSrcNode.setStatus("mandatory")
_NwIpRipRtMask_Type = IpAddress
_NwIpRipRtMask_Object = MibTableColumn
nwIpRipRtMask = _NwIpRipRtMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 4),
    _NwIpRipRtMask_Type()
)
nwIpRipRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtMask.setStatus("mandatory")
_NwIpRipRtHops_Type = Integer32
_NwIpRipRtHops_Object = MibTableColumn
nwIpRipRtHops = _NwIpRipRtHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 5),
    _NwIpRipRtHops_Type()
)
nwIpRipRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtHops.setStatus("mandatory")
_NwIpRipRtAge_Type = TimeTicks
_NwIpRipRtAge_Object = MibTableColumn
nwIpRipRtAge = _NwIpRipRtAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 6),
    _NwIpRipRtAge_Type()
)
nwIpRipRtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtAge.setStatus("mandatory")


class _NwIpRipRtType_Type(Integer32):
    """Custom type nwIpRipRtType based on Integer32"""
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
        *(("direct", 3),
          ("invalid", 2),
          ("ospf", 6),
          ("other", 1),
          ("remote", 4),
          ("static", 5))
    )


_NwIpRipRtType_Type.__name__ = "Integer32"
_NwIpRipRtType_Object = MibTableColumn
nwIpRipRtType = _NwIpRipRtType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 7),
    _NwIpRipRtType_Type()
)
nwIpRipRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtType.setStatus("mandatory")
_NwIpRipRtFlags_Type = Integer32
_NwIpRipRtFlags_Object = MibTableColumn
nwIpRipRtFlags = _NwIpRipRtFlags_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 3, 1, 1, 8),
    _NwIpRipRtFlags_Type()
)
nwIpRipRtFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRipRtFlags.setStatus("mandatory")
_NwIpRipFilters_ObjectIdentity = ObjectIdentity
nwIpRipFilters = _NwIpRipFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 1, 1, 4)
)
_NwIpLinkState_ObjectIdentity = ObjectIdentity
nwIpLinkState = _NwIpLinkState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2)
)
_NwIpOspf_ObjectIdentity = ObjectIdentity
nwIpOspf = _NwIpOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1)
)
_NwIpOspfSystem_ObjectIdentity = ObjectIdentity
nwIpOspfSystem = _NwIpOspfSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1)
)
_NwIpOspfConfig_ObjectIdentity = ObjectIdentity
nwIpOspfConfig = _NwIpOspfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1)
)


class _NwIpOspfAdminStatus_Type(Integer32):
    """Custom type nwIpOspfAdminStatus based on Integer32"""
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


_NwIpOspfAdminStatus_Type.__name__ = "Integer32"
_NwIpOspfAdminStatus_Object = MibScalar
nwIpOspfAdminStatus = _NwIpOspfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1, 1),
    _NwIpOspfAdminStatus_Type()
)
nwIpOspfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfAdminStatus.setStatus("mandatory")


class _NwIpOspfOperStatus_Type(Integer32):
    """Custom type nwIpOspfOperStatus based on Integer32"""
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


_NwIpOspfOperStatus_Type.__name__ = "Integer32"
_NwIpOspfOperStatus_Object = MibScalar
nwIpOspfOperStatus = _NwIpOspfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1, 2),
    _NwIpOspfOperStatus_Type()
)
nwIpOspfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfOperStatus.setStatus("mandatory")


class _NwIpOspfAdminReset_Type(Integer32):
    """Custom type nwIpOspfAdminReset based on Integer32"""
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


_NwIpOspfAdminReset_Type.__name__ = "Integer32"
_NwIpOspfAdminReset_Object = MibScalar
nwIpOspfAdminReset = _NwIpOspfAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1, 3),
    _NwIpOspfAdminReset_Type()
)
nwIpOspfAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfAdminReset.setStatus("mandatory")
_NwIpOspfOperationalTime_Type = TimeTicks
_NwIpOspfOperationalTime_Object = MibScalar
nwIpOspfOperationalTime = _NwIpOspfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1, 4),
    _NwIpOspfOperationalTime_Type()
)
nwIpOspfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfOperationalTime.setStatus("mandatory")
_NwIpOspfVersion_Type = DisplayString
_NwIpOspfVersion_Object = MibScalar
nwIpOspfVersion = _NwIpOspfVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1, 5),
    _NwIpOspfVersion_Type()
)
nwIpOspfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfVersion.setStatus("mandatory")


class _NwIpOspfStackSize_Type(Integer32):
    """Custom type nwIpOspfStackSize based on Integer32"""
    defaultValue = 50000


_NwIpOspfStackSize_Object = MibScalar
nwIpOspfStackSize = _NwIpOspfStackSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1, 6),
    _NwIpOspfStackSize_Type()
)
nwIpOspfStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfStackSize.setStatus("mandatory")


class _NwIpOspfThreadPriority_Type(Integer32):
    """Custom type nwIpOspfThreadPriority based on Integer32"""
    defaultValue = 127


_NwIpOspfThreadPriority_Object = MibScalar
nwIpOspfThreadPriority = _NwIpOspfThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 1, 7),
    _NwIpOspfThreadPriority_Type()
)
nwIpOspfThreadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfThreadPriority.setStatus("mandatory")
_NwIpOspfCounters_ObjectIdentity = ObjectIdentity
nwIpOspfCounters = _NwIpOspfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2)
)


class _NwIpOspfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpOspfCtrAdminStatus based on Integer32"""
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


_NwIpOspfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpOspfCtrAdminStatus_Object = MibScalar
nwIpOspfCtrAdminStatus = _NwIpOspfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 1),
    _NwIpOspfCtrAdminStatus_Type()
)
nwIpOspfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfCtrAdminStatus.setStatus("mandatory")


class _NwIpOspfCtrReset_Type(Integer32):
    """Custom type nwIpOspfCtrReset based on Integer32"""
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


_NwIpOspfCtrReset_Type.__name__ = "Integer32"
_NwIpOspfCtrReset_Object = MibScalar
nwIpOspfCtrReset = _NwIpOspfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 2),
    _NwIpOspfCtrReset_Type()
)
nwIpOspfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfCtrReset.setStatus("mandatory")
_NwIpOspfCtrOperationalTime_Type = TimeTicks
_NwIpOspfCtrOperationalTime_Object = MibScalar
nwIpOspfCtrOperationalTime = _NwIpOspfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 3),
    _NwIpOspfCtrOperationalTime_Type()
)
nwIpOspfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrOperationalTime.setStatus("mandatory")
_NwIpOspfCtrInPkts_Type = Counter32
_NwIpOspfCtrInPkts_Object = MibScalar
nwIpOspfCtrInPkts = _NwIpOspfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 4),
    _NwIpOspfCtrInPkts_Type()
)
nwIpOspfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrInPkts.setStatus("mandatory")
_NwIpOspfCtrOutPkts_Type = Counter32
_NwIpOspfCtrOutPkts_Object = MibScalar
nwIpOspfCtrOutPkts = _NwIpOspfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 5),
    _NwIpOspfCtrOutPkts_Type()
)
nwIpOspfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrOutPkts.setStatus("mandatory")
_NwIpOspfCtrFilteredPkts_Type = Counter32
_NwIpOspfCtrFilteredPkts_Object = MibScalar
nwIpOspfCtrFilteredPkts = _NwIpOspfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 6),
    _NwIpOspfCtrFilteredPkts_Type()
)
nwIpOspfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrFilteredPkts.setStatus("mandatory")
_NwIpOspfCtrDiscardPkts_Type = Counter32
_NwIpOspfCtrDiscardPkts_Object = MibScalar
nwIpOspfCtrDiscardPkts = _NwIpOspfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 7),
    _NwIpOspfCtrDiscardPkts_Type()
)
nwIpOspfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrDiscardPkts.setStatus("mandatory")
_NwIpOspfCtrInBytes_Type = Counter32
_NwIpOspfCtrInBytes_Object = MibScalar
nwIpOspfCtrInBytes = _NwIpOspfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 8),
    _NwIpOspfCtrInBytes_Type()
)
nwIpOspfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrInBytes.setStatus("mandatory")
_NwIpOspfCtrOutBytes_Type = Counter32
_NwIpOspfCtrOutBytes_Object = MibScalar
nwIpOspfCtrOutBytes = _NwIpOspfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 9),
    _NwIpOspfCtrOutBytes_Type()
)
nwIpOspfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrOutBytes.setStatus("mandatory")
_NwIpOspfCtrFilteredBytes_Type = Counter32
_NwIpOspfCtrFilteredBytes_Object = MibScalar
nwIpOspfCtrFilteredBytes = _NwIpOspfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 10),
    _NwIpOspfCtrFilteredBytes_Type()
)
nwIpOspfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrFilteredBytes.setStatus("mandatory")
_NwIpOspfCtrDiscardBytes_Type = Counter32
_NwIpOspfCtrDiscardBytes_Object = MibScalar
nwIpOspfCtrDiscardBytes = _NwIpOspfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 1, 2, 11),
    _NwIpOspfCtrDiscardBytes_Type()
)
nwIpOspfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfCtrDiscardBytes.setStatus("mandatory")
_NwIpOspfInterfaces_ObjectIdentity = ObjectIdentity
nwIpOspfInterfaces = _NwIpOspfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2)
)
_NwIpOspfIfConfig_ObjectIdentity = ObjectIdentity
nwIpOspfIfConfig = _NwIpOspfIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1)
)
_NwIpOspfIfTable_Object = MibTable
nwIpOspfIfTable = _NwIpOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpOspfIfTable.setStatus("mandatory")
_NwIpOspfIfEntry_Object = MibTableRow
nwIpOspfIfEntry = _NwIpOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1)
)
nwIpOspfIfEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpOspfIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpOspfIfEntry.setStatus("mandatory")
_NwIpOspfIfIndex_Type = Integer32
_NwIpOspfIfIndex_Object = MibTableColumn
nwIpOspfIfIndex = _NwIpOspfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 1),
    _NwIpOspfIfIndex_Type()
)
nwIpOspfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfIndex.setStatus("mandatory")


class _NwIpOspfIfAdminStatus_Type(Integer32):
    """Custom type nwIpOspfIfAdminStatus based on Integer32"""
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


_NwIpOspfIfAdminStatus_Type.__name__ = "Integer32"
_NwIpOspfIfAdminStatus_Object = MibTableColumn
nwIpOspfIfAdminStatus = _NwIpOspfIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 2),
    _NwIpOspfIfAdminStatus_Type()
)
nwIpOspfIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfIfAdminStatus.setStatus("mandatory")


class _NwIpOspfIfOperStatus_Type(Integer32):
    """Custom type nwIpOspfIfOperStatus based on Integer32"""
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


_NwIpOspfIfOperStatus_Type.__name__ = "Integer32"
_NwIpOspfIfOperStatus_Object = MibTableColumn
nwIpOspfIfOperStatus = _NwIpOspfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 3),
    _NwIpOspfIfOperStatus_Type()
)
nwIpOspfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfOperStatus.setStatus("mandatory")
_NwIpOspfIfOperationalTime_Type = TimeTicks
_NwIpOspfIfOperationalTime_Object = MibTableColumn
nwIpOspfIfOperationalTime = _NwIpOspfIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 4),
    _NwIpOspfIfOperationalTime_Type()
)
nwIpOspfIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfOperationalTime.setStatus("mandatory")


class _NwIpOspfIfVersion_Type(Integer32):
    """Custom type nwIpOspfIfVersion based on Integer32"""
    defaultValue = 1


_NwIpOspfIfVersion_Object = MibTableColumn
nwIpOspfIfVersion = _NwIpOspfIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 5),
    _NwIpOspfIfVersion_Type()
)
nwIpOspfIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfIfVersion.setStatus("mandatory")


class _NwIpOspfIfSnooping_Type(Integer32):
    """Custom type nwIpOspfIfSnooping based on Integer32"""
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


_NwIpOspfIfSnooping_Type.__name__ = "Integer32"
_NwIpOspfIfSnooping_Object = MibTableColumn
nwIpOspfIfSnooping = _NwIpOspfIfSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 6),
    _NwIpOspfIfSnooping_Type()
)
nwIpOspfIfSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfIfSnooping.setStatus("mandatory")


class _NwIpOspfIfType_Type(Integer32):
    """Custom type nwIpOspfIfType based on Integer32"""
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


_NwIpOspfIfType_Type.__name__ = "Integer32"
_NwIpOspfIfType_Object = MibTableColumn
nwIpOspfIfType = _NwIpOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 7),
    _NwIpOspfIfType_Type()
)
nwIpOspfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfType.setStatus("mandatory")


class _NwIpOspfIfAclIdentifier_Type(Integer32):
    """Custom type nwIpOspfIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwIpOspfIfAclIdentifier_Object = MibTableColumn
nwIpOspfIfAclIdentifier = _NwIpOspfIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 8),
    _NwIpOspfIfAclIdentifier_Type()
)
nwIpOspfIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfIfAclIdentifier.setStatus("mandatory")


class _NwIpOspfIfAclStatus_Type(Integer32):
    """Custom type nwIpOspfIfAclStatus based on Integer32"""
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


_NwIpOspfIfAclStatus_Type.__name__ = "Integer32"
_NwIpOspfIfAclStatus_Object = MibTableColumn
nwIpOspfIfAclStatus = _NwIpOspfIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 1, 1, 1, 9),
    _NwIpOspfIfAclStatus_Type()
)
nwIpOspfIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfIfAclStatus.setStatus("mandatory")
_NwIpOspfIfCounters_ObjectIdentity = ObjectIdentity
nwIpOspfIfCounters = _NwIpOspfIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2)
)
_NwIpOspfIfCtrTable_Object = MibTable
nwIpOspfIfCtrTable = _NwIpOspfIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpOspfIfCtrTable.setStatus("mandatory")
_NwIpOspfIfCtrEntry_Object = MibTableRow
nwIpOspfIfCtrEntry = _NwIpOspfIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1)
)
nwIpOspfIfCtrEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpOspfIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpOspfIfCtrEntry.setStatus("mandatory")
_NwIpOspfIfCtrIfIndex_Type = Integer32
_NwIpOspfIfCtrIfIndex_Object = MibTableColumn
nwIpOspfIfCtrIfIndex = _NwIpOspfIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 1),
    _NwIpOspfIfCtrIfIndex_Type()
)
nwIpOspfIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrIfIndex.setStatus("mandatory")


class _NwIpOspfIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpOspfIfCtrAdminStatus based on Integer32"""
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


_NwIpOspfIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpOspfIfCtrAdminStatus_Object = MibTableColumn
nwIpOspfIfCtrAdminStatus = _NwIpOspfIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 2),
    _NwIpOspfIfCtrAdminStatus_Type()
)
nwIpOspfIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrAdminStatus.setStatus("mandatory")


class _NwIpOspfIfCtrReset_Type(Integer32):
    """Custom type nwIpOspfIfCtrReset based on Integer32"""
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


_NwIpOspfIfCtrReset_Type.__name__ = "Integer32"
_NwIpOspfIfCtrReset_Object = MibTableColumn
nwIpOspfIfCtrReset = _NwIpOspfIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 3),
    _NwIpOspfIfCtrReset_Type()
)
nwIpOspfIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrReset.setStatus("mandatory")
_NwIpOspfIfCtrOperationalTime_Type = TimeTicks
_NwIpOspfIfCtrOperationalTime_Object = MibTableColumn
nwIpOspfIfCtrOperationalTime = _NwIpOspfIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 4),
    _NwIpOspfIfCtrOperationalTime_Type()
)
nwIpOspfIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrOperationalTime.setStatus("mandatory")
_NwIpOspfIfCtrInPkts_Type = Counter32
_NwIpOspfIfCtrInPkts_Object = MibTableColumn
nwIpOspfIfCtrInPkts = _NwIpOspfIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 5),
    _NwIpOspfIfCtrInPkts_Type()
)
nwIpOspfIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrInPkts.setStatus("mandatory")
_NwIpOspfIfCtrOutPkts_Type = Counter32
_NwIpOspfIfCtrOutPkts_Object = MibTableColumn
nwIpOspfIfCtrOutPkts = _NwIpOspfIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 6),
    _NwIpOspfIfCtrOutPkts_Type()
)
nwIpOspfIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrOutPkts.setStatus("mandatory")
_NwIpOspfIfCtrFilteredPkts_Type = Counter32
_NwIpOspfIfCtrFilteredPkts_Object = MibTableColumn
nwIpOspfIfCtrFilteredPkts = _NwIpOspfIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 7),
    _NwIpOspfIfCtrFilteredPkts_Type()
)
nwIpOspfIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrFilteredPkts.setStatus("mandatory")
_NwIpOspfIfCtrDiscardPkts_Type = Counter32
_NwIpOspfIfCtrDiscardPkts_Object = MibTableColumn
nwIpOspfIfCtrDiscardPkts = _NwIpOspfIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 8),
    _NwIpOspfIfCtrDiscardPkts_Type()
)
nwIpOspfIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrDiscardPkts.setStatus("mandatory")
_NwIpOspfIfCtrInBytes_Type = Counter32
_NwIpOspfIfCtrInBytes_Object = MibTableColumn
nwIpOspfIfCtrInBytes = _NwIpOspfIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 9),
    _NwIpOspfIfCtrInBytes_Type()
)
nwIpOspfIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrInBytes.setStatus("mandatory")
_NwIpOspfIfCtrOutBytes_Type = Counter32
_NwIpOspfIfCtrOutBytes_Object = MibTableColumn
nwIpOspfIfCtrOutBytes = _NwIpOspfIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 10),
    _NwIpOspfIfCtrOutBytes_Type()
)
nwIpOspfIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrOutBytes.setStatus("mandatory")
_NwIpOspfIfCtrFilteredBytes_Type = Counter32
_NwIpOspfIfCtrFilteredBytes_Object = MibTableColumn
nwIpOspfIfCtrFilteredBytes = _NwIpOspfIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 11),
    _NwIpOspfIfCtrFilteredBytes_Type()
)
nwIpOspfIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrFilteredBytes.setStatus("mandatory")
_NwIpOspfIfCtrDiscardBytes_Type = Counter32
_NwIpOspfIfCtrDiscardBytes_Object = MibTableColumn
nwIpOspfIfCtrDiscardBytes = _NwIpOspfIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 2, 2, 1, 1, 12),
    _NwIpOspfIfCtrDiscardBytes_Type()
)
nwIpOspfIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfIfCtrDiscardBytes.setStatus("mandatory")
_NwIpOspfDatabase_ObjectIdentity = ObjectIdentity
nwIpOspfDatabase = _NwIpOspfDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 3)
)
_NwIpOspfFilters_ObjectIdentity = ObjectIdentity
nwIpOspfFilters = _NwIpOspfFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 4, 2, 1, 4)
)
_NwIpFib_ObjectIdentity = ObjectIdentity
nwIpFib = _NwIpFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5)
)
_NwIpFibSystem_ObjectIdentity = ObjectIdentity
nwIpFibSystem = _NwIpFibSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 1)
)


class _NwIpRipRoutePriority_Type(Integer32):
    """Custom type nwIpRipRoutePriority based on Integer32"""
    defaultValue = 16


_NwIpRipRoutePriority_Object = MibScalar
nwIpRipRoutePriority = _NwIpRipRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 1, 1),
    _NwIpRipRoutePriority_Type()
)
nwIpRipRoutePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRipRoutePriority.setStatus("mandatory")


class _NwIpOSPFRoutePriority_Type(Integer32):
    """Custom type nwIpOSPFRoutePriority based on Integer32"""
    defaultValue = 32


_NwIpOSPFRoutePriority_Object = MibScalar
nwIpOSPFRoutePriority = _NwIpOSPFRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 1, 2),
    _NwIpOSPFRoutePriority_Type()
)
nwIpOSPFRoutePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOSPFRoutePriority.setStatus("mandatory")


class _NwIpStaticRoutePriority_Type(Integer32):
    """Custom type nwIpStaticRoutePriority based on Integer32"""
    defaultValue = 48


_NwIpStaticRoutePriority_Object = MibScalar
nwIpStaticRoutePriority = _NwIpStaticRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 1, 3),
    _NwIpStaticRoutePriority_Type()
)
nwIpStaticRoutePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpStaticRoutePriority.setStatus("mandatory")
_NwIpOspfFib_ObjectIdentity = ObjectIdentity
nwIpOspfFib = _NwIpOspfFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2)
)
_NwIpOspfFibControl_ObjectIdentity = ObjectIdentity
nwIpOspfFibControl = _NwIpOspfFibControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 1)
)
_NwIpOspfForward_Type = Integer32
_NwIpOspfForward_Object = MibScalar
nwIpOspfForward = _NwIpOspfForward_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 1, 1),
    _NwIpOspfForward_Type()
)
nwIpOspfForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfForward.setStatus("mandatory")


class _NwIpOspfLeakAllStaticRoutes_Type(Integer32):
    """Custom type nwIpOspfLeakAllStaticRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NwIpOspfLeakAllStaticRoutes_Type.__name__ = "Integer32"
_NwIpOspfLeakAllStaticRoutes_Object = MibScalar
nwIpOspfLeakAllStaticRoutes = _NwIpOspfLeakAllStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 1, 2),
    _NwIpOspfLeakAllStaticRoutes_Type()
)
nwIpOspfLeakAllStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfLeakAllStaticRoutes.setStatus("mandatory")
_NwIpOspfLeakAllRipRoutes_Type = Integer32
_NwIpOspfLeakAllRipRoutes_Object = MibScalar
nwIpOspfLeakAllRipRoutes = _NwIpOspfLeakAllRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 1, 3),
    _NwIpOspfLeakAllRipRoutes_Type()
)
nwIpOspfLeakAllRipRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfLeakAllRipRoutes.setStatus("mandatory")
_NwIpOspfLeakAllBgp4Routes_Type = Integer32
_NwIpOspfLeakAllBgp4Routes_Object = MibScalar
nwIpOspfLeakAllBgp4Routes = _NwIpOspfLeakAllBgp4Routes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 1, 4),
    _NwIpOspfLeakAllBgp4Routes_Type()
)
nwIpOspfLeakAllBgp4Routes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfLeakAllBgp4Routes.setStatus("mandatory")
_NwIpOspfFibEntries_ObjectIdentity = ObjectIdentity
nwIpOspfFibEntries = _NwIpOspfFibEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2)
)
_NwIpOspfStaticTable_Object = MibTable
nwIpOspfStaticTable = _NwIpOspfStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpOspfStaticTable.setStatus("mandatory")
_NwIpOspfStaticEntry_Object = MibTableRow
nwIpOspfStaticEntry = _NwIpOspfStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1, 1)
)
nwIpOspfStaticEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpOspfStaticDest"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpOspfStaticForwardMask"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpOspfStaticNextHop"),
)
if mibBuilder.loadTexts:
    nwIpOspfStaticEntry.setStatus("mandatory")
_NwIpOspfStaticDest_Type = IpAddress
_NwIpOspfStaticDest_Object = MibTableColumn
nwIpOspfStaticDest = _NwIpOspfStaticDest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1, 1, 1),
    _NwIpOspfStaticDest_Type()
)
nwIpOspfStaticDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfStaticDest.setStatus("mandatory")
_NwIpOspfStaticForwardMask_Type = IpAddress
_NwIpOspfStaticForwardMask_Object = MibTableColumn
nwIpOspfStaticForwardMask = _NwIpOspfStaticForwardMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1, 1, 2),
    _NwIpOspfStaticForwardMask_Type()
)
nwIpOspfStaticForwardMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfStaticForwardMask.setStatus("mandatory")
_NwIpOspfStaticNextHop_Type = IpAddress
_NwIpOspfStaticNextHop_Object = MibTableColumn
nwIpOspfStaticNextHop = _NwIpOspfStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1, 1, 3),
    _NwIpOspfStaticNextHop_Type()
)
nwIpOspfStaticNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpOspfStaticNextHop.setStatus("mandatory")
_NwIpOspfStaticMetric_Type = Integer32
_NwIpOspfStaticMetric_Object = MibTableColumn
nwIpOspfStaticMetric = _NwIpOspfStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1, 1, 4),
    _NwIpOspfStaticMetric_Type()
)
nwIpOspfStaticMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfStaticMetric.setStatus("mandatory")
_NwIpOspfStaticMetricType_Type = Integer32
_NwIpOspfStaticMetricType_Object = MibTableColumn
nwIpOspfStaticMetricType = _NwIpOspfStaticMetricType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1, 1, 5),
    _NwIpOspfStaticMetricType_Type()
)
nwIpOspfStaticMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfStaticMetricType.setStatus("mandatory")


class _NwIpOspfStaticStatus_Type(Integer32):
    """Custom type nwIpOspfStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("delete", 3),
          ("inactive", 1))
    )


_NwIpOspfStaticStatus_Type.__name__ = "Integer32"
_NwIpOspfStaticStatus_Object = MibTableColumn
nwIpOspfStaticStatus = _NwIpOspfStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 1, 1, 6),
    _NwIpOspfStaticStatus_Type()
)
nwIpOspfStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpOspfStaticStatus.setStatus("mandatory")
_NwIpOspfDynamicTable_ObjectIdentity = ObjectIdentity
nwIpOspfDynamicTable = _NwIpOspfDynamicTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 2)
)
_NwIpOspfRipTable_ObjectIdentity = ObjectIdentity
nwIpOspfRipTable = _NwIpOspfRipTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 3)
)
_NwIpOspfBgp4Table_ObjectIdentity = ObjectIdentity
nwIpOspfBgp4Table = _NwIpOspfBgp4Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 5, 2, 2, 4)
)
_NwIpEndSystems_ObjectIdentity = ObjectIdentity
nwIpEndSystems = _NwIpEndSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6)
)
_NwIpHostsSystem_ObjectIdentity = ObjectIdentity
nwIpHostsSystem = _NwIpHostsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 1)
)
_NwIpHostsTimeToLive_Type = Integer32
_NwIpHostsTimeToLive_Object = MibScalar
nwIpHostsTimeToLive = _NwIpHostsTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 1, 1),
    _NwIpHostsTimeToLive_Type()
)
nwIpHostsTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostsTimeToLive.setStatus("mandatory")
_NwIpHostsRetryCount_Type = Counter32
_NwIpHostsRetryCount_Object = MibScalar
nwIpHostsRetryCount = _NwIpHostsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 1, 2),
    _NwIpHostsRetryCount_Type()
)
nwIpHostsRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostsRetryCount.setStatus("mandatory")
_NwIpHostsInterfaces_ObjectIdentity = ObjectIdentity
nwIpHostsInterfaces = _NwIpHostsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2)
)
_NwIpHostCtlTable_Object = MibTable
nwIpHostCtlTable = _NwIpHostCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpHostCtlTable.setStatus("mandatory")
_NwIpHostCtlEntry_Object = MibTableRow
nwIpHostCtlEntry = _NwIpHostCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1)
)
nwIpHostCtlEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpHostCtlIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpHostCtlEntry.setStatus("mandatory")
_NwIpHostCtlIfIndex_Type = Integer32
_NwIpHostCtlIfIndex_Object = MibTableColumn
nwIpHostCtlIfIndex = _NwIpHostCtlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 1),
    _NwIpHostCtlIfIndex_Type()
)
nwIpHostCtlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlIfIndex.setStatus("mandatory")


class _NwIpHostCtlAdminStatus_Type(Integer32):
    """Custom type nwIpHostCtlAdminStatus based on Integer32"""
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


_NwIpHostCtlAdminStatus_Type.__name__ = "Integer32"
_NwIpHostCtlAdminStatus_Object = MibTableColumn
nwIpHostCtlAdminStatus = _NwIpHostCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 2),
    _NwIpHostCtlAdminStatus_Type()
)
nwIpHostCtlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostCtlAdminStatus.setStatus("mandatory")


class _NwIpHostCtlOperStatus_Type(Integer32):
    """Custom type nwIpHostCtlOperStatus based on Integer32"""
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


_NwIpHostCtlOperStatus_Type.__name__ = "Integer32"
_NwIpHostCtlOperStatus_Object = MibTableColumn
nwIpHostCtlOperStatus = _NwIpHostCtlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 3),
    _NwIpHostCtlOperStatus_Type()
)
nwIpHostCtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlOperStatus.setStatus("mandatory")
_NwIpHostCtlOperationalTime_Type = TimeTicks
_NwIpHostCtlOperationalTime_Object = MibTableColumn
nwIpHostCtlOperationalTime = _NwIpHostCtlOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 4),
    _NwIpHostCtlOperationalTime_Type()
)
nwIpHostCtlOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlOperationalTime.setStatus("mandatory")


class _NwIpHostCtlProtocol_Type(Integer32):
    """Custom type nwIpHostCtlProtocol based on Integer32"""
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


_NwIpHostCtlProtocol_Type.__name__ = "Integer32"
_NwIpHostCtlProtocol_Object = MibTableColumn
nwIpHostCtlProtocol = _NwIpHostCtlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 5),
    _NwIpHostCtlProtocol_Type()
)
nwIpHostCtlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostCtlProtocol.setStatus("mandatory")


class _NwIpHostCtlSnooping_Type(Integer32):
    """Custom type nwIpHostCtlSnooping based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_NwIpHostCtlSnooping_Type.__name__ = "Integer32"
_NwIpHostCtlSnooping_Object = MibTableColumn
nwIpHostCtlSnooping = _NwIpHostCtlSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 6),
    _NwIpHostCtlSnooping_Type()
)
nwIpHostCtlSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostCtlSnooping.setStatus("mandatory")


class _NwIpHostCtlProxy_Type(Integer32):
    """Custom type nwIpHostCtlProxy based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_NwIpHostCtlProxy_Type.__name__ = "Integer32"
_NwIpHostCtlProxy_Object = MibTableColumn
nwIpHostCtlProxy = _NwIpHostCtlProxy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 7),
    _NwIpHostCtlProxy_Type()
)
nwIpHostCtlProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostCtlProxy.setStatus("mandatory")


class _NwIpHostCtlCacheMax_Type(Integer32):
    """Custom type nwIpHostCtlCacheMax based on Integer32"""
    defaultValue = 1024


_NwIpHostCtlCacheMax_Object = MibTableColumn
nwIpHostCtlCacheMax = _NwIpHostCtlCacheMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 8),
    _NwIpHostCtlCacheMax_Type()
)
nwIpHostCtlCacheMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostCtlCacheMax.setStatus("mandatory")
_NwIpHostCtlCacheSize_Type = Integer32
_NwIpHostCtlCacheSize_Object = MibTableColumn
nwIpHostCtlCacheSize = _NwIpHostCtlCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 9),
    _NwIpHostCtlCacheSize_Type()
)
nwIpHostCtlCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlCacheSize.setStatus("mandatory")
_NwIpHostCtlNumStatics_Type = Counter32
_NwIpHostCtlNumStatics_Object = MibTableColumn
nwIpHostCtlNumStatics = _NwIpHostCtlNumStatics_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 10),
    _NwIpHostCtlNumStatics_Type()
)
nwIpHostCtlNumStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlNumStatics.setStatus("mandatory")
_NwIpHostCtlNumDynamics_Type = Counter32
_NwIpHostCtlNumDynamics_Object = MibTableColumn
nwIpHostCtlNumDynamics = _NwIpHostCtlNumDynamics_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 11),
    _NwIpHostCtlNumDynamics_Type()
)
nwIpHostCtlNumDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlNumDynamics.setStatus("mandatory")
_NwIpHostCtlCacheHits_Type = Counter32
_NwIpHostCtlCacheHits_Object = MibTableColumn
nwIpHostCtlCacheHits = _NwIpHostCtlCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 12),
    _NwIpHostCtlCacheHits_Type()
)
nwIpHostCtlCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlCacheHits.setStatus("mandatory")
_NwIpHostCtlCacheMisses_Type = Counter32
_NwIpHostCtlCacheMisses_Object = MibTableColumn
nwIpHostCtlCacheMisses = _NwIpHostCtlCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 2, 1, 1, 13),
    _NwIpHostCtlCacheMisses_Type()
)
nwIpHostCtlCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostCtlCacheMisses.setStatus("mandatory")
_NwIpHostsToMedia_ObjectIdentity = ObjectIdentity
nwIpHostsToMedia = _NwIpHostsToMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3)
)
_NwIpHostMapTable_Object = MibTable
nwIpHostMapTable = _NwIpHostMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    nwIpHostMapTable.setStatus("mandatory")
_NwIpHostMapEntry_Object = MibTableRow
nwIpHostMapEntry = _NwIpHostMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1)
)
nwIpHostMapEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpHostMapIfIndex"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpHostMapIpAddr"),
)
if mibBuilder.loadTexts:
    nwIpHostMapEntry.setStatus("mandatory")
_NwIpHostMapIfIndex_Type = Integer32
_NwIpHostMapIfIndex_Object = MibTableColumn
nwIpHostMapIfIndex = _NwIpHostMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1, 1),
    _NwIpHostMapIfIndex_Type()
)
nwIpHostMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostMapIfIndex.setStatus("mandatory")
_NwIpHostMapIpAddr_Type = IpAddress
_NwIpHostMapIpAddr_Object = MibTableColumn
nwIpHostMapIpAddr = _NwIpHostMapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1, 2),
    _NwIpHostMapIpAddr_Type()
)
nwIpHostMapIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostMapIpAddr.setStatus("mandatory")
_NwIpHostMapPhysAddr_Type = PhysAddress
_NwIpHostMapPhysAddr_Object = MibTableColumn
nwIpHostMapPhysAddr = _NwIpHostMapPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1, 3),
    _NwIpHostMapPhysAddr_Type()
)
nwIpHostMapPhysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostMapPhysAddr.setStatus("mandatory")


class _NwIpHostMapType_Type(Integer32):
    """Custom type nwIpHostMapType based on Integer32"""
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


_NwIpHostMapType_Type.__name__ = "Integer32"
_NwIpHostMapType_Object = MibTableColumn
nwIpHostMapType = _NwIpHostMapType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1, 4),
    _NwIpHostMapType_Type()
)
nwIpHostMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostMapType.setStatus("mandatory")
_NwIpHostMapCircuitID_Type = Integer32
_NwIpHostMapCircuitID_Object = MibTableColumn
nwIpHostMapCircuitID = _NwIpHostMapCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1, 5),
    _NwIpHostMapCircuitID_Type()
)
nwIpHostMapCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostMapCircuitID.setStatus("mandatory")


class _NwIpHostMapFraming_Type(Integer32):
    """Custom type nwIpHostMapFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
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
          ("localtalk", 7),
          ("nativewan", 8),
          ("other", 1),
          ("slip", 5),
          ("snap", 3))
    )


_NwIpHostMapFraming_Type.__name__ = "Integer32"
_NwIpHostMapFraming_Object = MibTableColumn
nwIpHostMapFraming = _NwIpHostMapFraming_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1, 6),
    _NwIpHostMapFraming_Type()
)
nwIpHostMapFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpHostMapFraming.setStatus("mandatory")
_NwIpHostMapPortNumber_Type = Integer32
_NwIpHostMapPortNumber_Object = MibTableColumn
nwIpHostMapPortNumber = _NwIpHostMapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 6, 3, 1, 1, 7),
    _NwIpHostMapPortNumber_Type()
)
nwIpHostMapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpHostMapPortNumber.setStatus("mandatory")
_NwIpAccessControl_ObjectIdentity = ObjectIdentity
nwIpAccessControl = _NwIpAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7)
)
_NwIpAclValidEntries_Type = Gauge32
_NwIpAclValidEntries_Object = MibScalar
nwIpAclValidEntries = _NwIpAclValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 1),
    _NwIpAclValidEntries_Type()
)
nwIpAclValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpAclValidEntries.setStatus("mandatory")
_NwIpAclTable_Object = MibTable
nwIpAclTable = _NwIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    nwIpAclTable.setStatus("mandatory")
_NwIpAclEntry_Object = MibTableRow
nwIpAclEntry = _NwIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1)
)
nwIpAclEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpAclIdentifier"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpAclSequence"),
)
if mibBuilder.loadTexts:
    nwIpAclEntry.setStatus("mandatory")
_NwIpAclIdentifier_Type = Integer32
_NwIpAclIdentifier_Object = MibTableColumn
nwIpAclIdentifier = _NwIpAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 1),
    _NwIpAclIdentifier_Type()
)
nwIpAclIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpAclIdentifier.setStatus("mandatory")
_NwIpAclSequence_Type = Integer32
_NwIpAclSequence_Object = MibTableColumn
nwIpAclSequence = _NwIpAclSequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 2),
    _NwIpAclSequence_Type()
)
nwIpAclSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpAclSequence.setStatus("mandatory")


class _NwIpAclPermission_Type(Integer32):
    """Custom type nwIpAclPermission based on Integer32"""
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


_NwIpAclPermission_Type.__name__ = "Integer32"
_NwIpAclPermission_Object = MibTableColumn
nwIpAclPermission = _NwIpAclPermission_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 3),
    _NwIpAclPermission_Type()
)
nwIpAclPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAclPermission.setStatus("mandatory")
_NwIpAclMatches_Type = Counter32
_NwIpAclMatches_Object = MibTableColumn
nwIpAclMatches = _NwIpAclMatches_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 4),
    _NwIpAclMatches_Type()
)
nwIpAclMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpAclMatches.setStatus("mandatory")
_NwIpAclDestAddress_Type = IpAddress
_NwIpAclDestAddress_Object = MibTableColumn
nwIpAclDestAddress = _NwIpAclDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 5),
    _NwIpAclDestAddress_Type()
)
nwIpAclDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAclDestAddress.setStatus("mandatory")
_NwIpAclDestMask_Type = IpAddress
_NwIpAclDestMask_Object = MibTableColumn
nwIpAclDestMask = _NwIpAclDestMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 6),
    _NwIpAclDestMask_Type()
)
nwIpAclDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAclDestMask.setStatus("mandatory")
_NwIpAclSrcAddress_Type = IpAddress
_NwIpAclSrcAddress_Object = MibTableColumn
nwIpAclSrcAddress = _NwIpAclSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 7),
    _NwIpAclSrcAddress_Type()
)
nwIpAclSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAclSrcAddress.setStatus("mandatory")
_NwIpAclSrcMask_Type = IpAddress
_NwIpAclSrcMask_Object = MibTableColumn
nwIpAclSrcMask = _NwIpAclSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 8),
    _NwIpAclSrcMask_Type()
)
nwIpAclSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAclSrcMask.setStatus("mandatory")


class _NwIpAclProtocol_Type(Integer32):
    """Custom type nwIpAclProtocol based on Integer32"""
    defaultValue = 2

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
        *(("all", 2),
          ("icmp", 3),
          ("other", 1),
          ("tcp", 5),
          ("udp", 4))
    )


_NwIpAclProtocol_Type.__name__ = "Integer32"
_NwIpAclProtocol_Object = MibTableColumn
nwIpAclProtocol = _NwIpAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 9),
    _NwIpAclProtocol_Type()
)
nwIpAclProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAclProtocol.setStatus("mandatory")
_NwIpAclPortNumber_Type = Integer32
_NwIpAclPortNumber_Object = MibTableColumn
nwIpAclPortNumber = _NwIpAclPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 7, 2, 1, 10),
    _NwIpAclPortNumber_Type()
)
nwIpAclPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpAclPortNumber.setStatus("mandatory")
_NwIpFilters_ObjectIdentity = ObjectIdentity
nwIpFilters = _NwIpFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 8)
)
_NwIpRedirector_ObjectIdentity = ObjectIdentity
nwIpRedirector = _NwIpRedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9)
)
_NwIpRedirectorSystem_ObjectIdentity = ObjectIdentity
nwIpRedirectorSystem = _NwIpRedirectorSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 1)
)
_NwIpRedirectTable_Object = MibTable
nwIpRedirectTable = _NwIpRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpRedirectTable.setStatus("mandatory")
_NwIpRedirectEntry_Object = MibTableRow
nwIpRedirectEntry = _NwIpRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 1, 1, 1)
)
nwIpRedirectEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpRedirectPort"),
)
if mibBuilder.loadTexts:
    nwIpRedirectEntry.setStatus("mandatory")
_NwIpRedirectPort_Type = Integer32
_NwIpRedirectPort_Object = MibTableColumn
nwIpRedirectPort = _NwIpRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 1, 1, 1, 1),
    _NwIpRedirectPort_Type()
)
nwIpRedirectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRedirectPort.setStatus("mandatory")
_NwIpRedirectAddress_Type = IpAddress
_NwIpRedirectAddress_Object = MibTableColumn
nwIpRedirectAddress = _NwIpRedirectAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 1, 1, 1, 2),
    _NwIpRedirectAddress_Type()
)
nwIpRedirectAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRedirectAddress.setStatus("mandatory")


class _NwIpRedirectType_Type(Integer32):
    """Custom type nwIpRedirectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("forward", 1))
    )


_NwIpRedirectType_Type.__name__ = "Integer32"
_NwIpRedirectType_Object = MibTableColumn
nwIpRedirectType = _NwIpRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 1, 1, 1, 3),
    _NwIpRedirectType_Type()
)
nwIpRedirectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpRedirectType.setStatus("mandatory")
_NwIpRedirectCount_Type = Counter32
_NwIpRedirectCount_Object = MibTableColumn
nwIpRedirectCount = _NwIpRedirectCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 1, 1, 1, 4),
    _NwIpRedirectCount_Type()
)
nwIpRedirectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpRedirectCount.setStatus("mandatory")
_NwIpRedirectorInterface_ObjectIdentity = ObjectIdentity
nwIpRedirectorInterface = _NwIpRedirectorInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 9, 2)
)
_NwIpEvent_ObjectIdentity = ObjectIdentity
nwIpEvent = _NwIpEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10)
)
_NwIpEventLogConfig_ObjectIdentity = ObjectIdentity
nwIpEventLogConfig = _NwIpEventLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 1)
)


class _NwIpEventAdminStatus_Type(Integer32):
    """Custom type nwIpEventAdminStatus based on Integer32"""
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


_NwIpEventAdminStatus_Type.__name__ = "Integer32"
_NwIpEventAdminStatus_Object = MibScalar
nwIpEventAdminStatus = _NwIpEventAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 1, 1),
    _NwIpEventAdminStatus_Type()
)
nwIpEventAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpEventAdminStatus.setStatus("mandatory")


class _NwIpEventMaxEntries_Type(Integer32):
    """Custom type nwIpEventMaxEntries based on Integer32"""
    defaultValue = 100


_NwIpEventMaxEntries_Object = MibScalar
nwIpEventMaxEntries = _NwIpEventMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 1, 2),
    _NwIpEventMaxEntries_Type()
)
nwIpEventMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpEventMaxEntries.setStatus("mandatory")


class _NwIpEventTraceAll_Type(Integer32):
    """Custom type nwIpEventTraceAll based on Integer32"""
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


_NwIpEventTraceAll_Type.__name__ = "Integer32"
_NwIpEventTraceAll_Object = MibScalar
nwIpEventTraceAll = _NwIpEventTraceAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 1, 3),
    _NwIpEventTraceAll_Type()
)
nwIpEventTraceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpEventTraceAll.setStatus("mandatory")
_NwIpEventLogFilterTable_ObjectIdentity = ObjectIdentity
nwIpEventLogFilterTable = _NwIpEventLogFilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2)
)
_NwIpEventFilterTable_Object = MibTable
nwIpEventFilterTable = _NwIpEventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpEventFilterTable.setStatus("mandatory")
_NwIpEventFilterEntry_Object = MibTableRow
nwIpEventFilterEntry = _NwIpEventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1, 1)
)
nwIpEventFilterEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpEventFltrProtocol"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpEventFltrIfNum"),
)
if mibBuilder.loadTexts:
    nwIpEventFilterEntry.setStatus("mandatory")
_NwIpEventFltrProtocol_Type = Integer32
_NwIpEventFltrProtocol_Object = MibTableColumn
nwIpEventFltrProtocol = _NwIpEventFltrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1, 1, 1),
    _NwIpEventFltrProtocol_Type()
)
nwIpEventFltrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventFltrProtocol.setStatus("mandatory")
_NwIpEventFltrIfNum_Type = Integer32
_NwIpEventFltrIfNum_Object = MibTableColumn
nwIpEventFltrIfNum = _NwIpEventFltrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1, 1, 2),
    _NwIpEventFltrIfNum_Type()
)
nwIpEventFltrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventFltrIfNum.setStatus("mandatory")


class _NwIpEventFltrControl_Type(Integer32):
    """Custom type nwIpEventFltrControl based on Integer32"""
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


_NwIpEventFltrControl_Type.__name__ = "Integer32"
_NwIpEventFltrControl_Object = MibTableColumn
nwIpEventFltrControl = _NwIpEventFltrControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1, 1, 3),
    _NwIpEventFltrControl_Type()
)
nwIpEventFltrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpEventFltrControl.setStatus("mandatory")


class _NwIpEventFltrType_Type(Integer32):
    """Custom type nwIpEventFltrType based on Integer32"""
    defaultValue = 64

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


_NwIpEventFltrType_Type.__name__ = "Integer32"
_NwIpEventFltrType_Object = MibTableColumn
nwIpEventFltrType = _NwIpEventFltrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1, 1, 4),
    _NwIpEventFltrType_Type()
)
nwIpEventFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpEventFltrType.setStatus("mandatory")


class _NwIpEventFltrSeverity_Type(Integer32):
    """Custom type nwIpEventFltrSeverity based on Integer32"""
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


_NwIpEventFltrSeverity_Type.__name__ = "Integer32"
_NwIpEventFltrSeverity_Object = MibTableColumn
nwIpEventFltrSeverity = _NwIpEventFltrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1, 1, 5),
    _NwIpEventFltrSeverity_Type()
)
nwIpEventFltrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpEventFltrSeverity.setStatus("mandatory")


class _NwIpEventFltrAction_Type(Integer32):
    """Custom type nwIpEventFltrAction based on Integer32"""
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


_NwIpEventFltrAction_Type.__name__ = "Integer32"
_NwIpEventFltrAction_Object = MibTableColumn
nwIpEventFltrAction = _NwIpEventFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 2, 1, 1, 6),
    _NwIpEventFltrAction_Type()
)
nwIpEventFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpEventFltrAction.setStatus("mandatory")
_NwIpEventLogTable_ObjectIdentity = ObjectIdentity
nwIpEventLogTable = _NwIpEventLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3)
)
_NwIpEventTable_Object = MibTable
nwIpEventTable = _NwIpEventTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    nwIpEventTable.setStatus("mandatory")
_NwIpEventEntry_Object = MibTableRow
nwIpEventEntry = _NwIpEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1)
)
nwIpEventEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpEventNumber"),
)
if mibBuilder.loadTexts:
    nwIpEventEntry.setStatus("mandatory")
_NwIpEventNumber_Type = Integer32
_NwIpEventNumber_Object = MibTableColumn
nwIpEventNumber = _NwIpEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1, 1),
    _NwIpEventNumber_Type()
)
nwIpEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventNumber.setStatus("mandatory")
_NwIpEventTime_Type = TimeTicks
_NwIpEventTime_Object = MibTableColumn
nwIpEventTime = _NwIpEventTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1, 2),
    _NwIpEventTime_Type()
)
nwIpEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventTime.setStatus("mandatory")


class _NwIpEventType_Type(Integer32):
    """Custom type nwIpEventType based on Integer32"""
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


_NwIpEventType_Type.__name__ = "Integer32"
_NwIpEventType_Object = MibTableColumn
nwIpEventType = _NwIpEventType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1, 3),
    _NwIpEventType_Type()
)
nwIpEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventType.setStatus("mandatory")


class _NwIpEventSeverity_Type(Integer32):
    """Custom type nwIpEventSeverity based on Integer32"""
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


_NwIpEventSeverity_Type.__name__ = "Integer32"
_NwIpEventSeverity_Object = MibTableColumn
nwIpEventSeverity = _NwIpEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1, 4),
    _NwIpEventSeverity_Type()
)
nwIpEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventSeverity.setStatus("mandatory")
_NwIpEventProtocol_Type = Integer32
_NwIpEventProtocol_Object = MibTableColumn
nwIpEventProtocol = _NwIpEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1, 5),
    _NwIpEventProtocol_Type()
)
nwIpEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventProtocol.setStatus("mandatory")
_NwIpEventIfNum_Type = Integer32
_NwIpEventIfNum_Object = MibTableColumn
nwIpEventIfNum = _NwIpEventIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1, 6),
    _NwIpEventIfNum_Type()
)
nwIpEventIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventIfNum.setStatus("mandatory")
_NwIpEventTextString_Type = OctetString
_NwIpEventTextString_Object = MibTableColumn
nwIpEventTextString = _NwIpEventTextString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 10, 3, 1, 1, 7),
    _NwIpEventTextString_Type()
)
nwIpEventTextString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpEventTextString.setStatus("mandatory")
_NwIpWorkGroup_ObjectIdentity = ObjectIdentity
nwIpWorkGroup = _NwIpWorkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11)
)
_NwIpWgDefTable_Object = MibTable
nwIpWgDefTable = _NwIpWgDefTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    nwIpWgDefTable.setStatus("mandatory")
_NwIpWgDefEntry_Object = MibTableRow
nwIpWgDefEntry = _NwIpWgDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1)
)
nwIpWgDefEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgDefIdentifier"),
)
if mibBuilder.loadTexts:
    nwIpWgDefEntry.setStatus("mandatory")
_NwIpWgDefIdentifier_Type = Integer32
_NwIpWgDefIdentifier_Object = MibTableColumn
nwIpWgDefIdentifier = _NwIpWgDefIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 1),
    _NwIpWgDefIdentifier_Type()
)
nwIpWgDefIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgDefIdentifier.setStatus("mandatory")
_NwIpWgDefHostAddress_Type = IpAddress
_NwIpWgDefHostAddress_Object = MibTableColumn
nwIpWgDefHostAddress = _NwIpWgDefHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 2),
    _NwIpWgDefHostAddress_Type()
)
nwIpWgDefHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgDefHostAddress.setStatus("mandatory")
_NwIpWgDefSubnetMask_Type = IpAddress
_NwIpWgDefSubnetMask_Object = MibTableColumn
nwIpWgDefSubnetMask = _NwIpWgDefSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 3),
    _NwIpWgDefSubnetMask_Type()
)
nwIpWgDefSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgDefSubnetMask.setStatus("mandatory")


class _NwIpWgDefSecurity_Type(Integer32):
    """Custom type nwIpWgDefSecurity based on Integer32"""
    defaultValue = 2

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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("none", 1))
    )


_NwIpWgDefSecurity_Type.__name__ = "Integer32"
_NwIpWgDefSecurity_Object = MibTableColumn
nwIpWgDefSecurity = _NwIpWgDefSecurity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 4),
    _NwIpWgDefSecurity_Type()
)
nwIpWgDefSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgDefSecurity.setStatus("mandatory")


class _NwIpWgDefFastPath_Type(Integer32):
    """Custom type nwIpWgDefFastPath based on Integer32"""
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


_NwIpWgDefFastPath_Type.__name__ = "Integer32"
_NwIpWgDefFastPath_Object = MibTableColumn
nwIpWgDefFastPath = _NwIpWgDefFastPath_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 5),
    _NwIpWgDefFastPath_Type()
)
nwIpWgDefFastPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgDefFastPath.setStatus("mandatory")


class _NwIpWgDefRowStatus_Type(Integer32):
    """Custom type nwIpWgDefRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_NwIpWgDefRowStatus_Type.__name__ = "Integer32"
_NwIpWgDefRowStatus_Object = MibTableColumn
nwIpWgDefRowStatus = _NwIpWgDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 6),
    _NwIpWgDefRowStatus_Type()
)
nwIpWgDefRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgDefRowStatus.setStatus("mandatory")


class _NwIpWgDefOperStatus_Type(Integer32):
    """Custom type nwIpWgDefOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("internalError", 4),
          ("ok", 1),
          ("subnetConflict", 3))
    )


_NwIpWgDefOperStatus_Type.__name__ = "Integer32"
_NwIpWgDefOperStatus_Object = MibTableColumn
nwIpWgDefOperStatus = _NwIpWgDefOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 7),
    _NwIpWgDefOperStatus_Type()
)
nwIpWgDefOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgDefOperStatus.setStatus("mandatory")
_NwIpWgDefNumActiveIntf_Type = Integer32
_NwIpWgDefNumActiveIntf_Object = MibTableColumn
nwIpWgDefNumActiveIntf = _NwIpWgDefNumActiveIntf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 8),
    _NwIpWgDefNumActiveIntf_Type()
)
nwIpWgDefNumActiveIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgDefNumActiveIntf.setStatus("mandatory")
_NwIpWgDefNumTotalIntf_Type = Integer32
_NwIpWgDefNumTotalIntf_Object = MibTableColumn
nwIpWgDefNumTotalIntf = _NwIpWgDefNumTotalIntf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 1, 1, 9),
    _NwIpWgDefNumTotalIntf_Type()
)
nwIpWgDefNumTotalIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgDefNumTotalIntf.setStatus("mandatory")
_NwIpWgIfTable_Object = MibTable
nwIpWgIfTable = _NwIpWgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    nwIpWgIfTable.setStatus("mandatory")
_NwIpWgIfEntry_Object = MibTableRow
nwIpWgIfEntry = _NwIpWgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2, 1)
)
nwIpWgIfEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgIfDefIdent"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgIfIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpWgIfEntry.setStatus("mandatory")
_NwIpWgIfDefIdent_Type = Integer32
_NwIpWgIfDefIdent_Object = MibTableColumn
nwIpWgIfDefIdent = _NwIpWgIfDefIdent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2, 1, 1),
    _NwIpWgIfDefIdent_Type()
)
nwIpWgIfDefIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgIfDefIdent.setStatus("mandatory")
_NwIpWgIfIfIndex_Type = Integer32
_NwIpWgIfIfIndex_Object = MibTableColumn
nwIpWgIfIfIndex = _NwIpWgIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2, 1, 2),
    _NwIpWgIfIfIndex_Type()
)
nwIpWgIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgIfIfIndex.setStatus("mandatory")
_NwIpWgIfNumActiveHosts_Type = Integer32
_NwIpWgIfNumActiveHosts_Object = MibTableColumn
nwIpWgIfNumActiveHosts = _NwIpWgIfNumActiveHosts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2, 1, 3),
    _NwIpWgIfNumActiveHosts_Type()
)
nwIpWgIfNumActiveHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgIfNumActiveHosts.setStatus("mandatory")
_NwIpWgIfNumKnownHosts_Type = Counter32
_NwIpWgIfNumKnownHosts_Object = MibTableColumn
nwIpWgIfNumKnownHosts = _NwIpWgIfNumKnownHosts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2, 1, 4),
    _NwIpWgIfNumKnownHosts_Type()
)
nwIpWgIfNumKnownHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgIfNumKnownHosts.setStatus("mandatory")


class _NwIpWgIfRowStatus_Type(Integer32):
    """Custom type nwIpWgIfRowStatus based on Integer32"""
    defaultValue = 2

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_NwIpWgIfRowStatus_Type.__name__ = "Integer32"
_NwIpWgIfRowStatus_Object = MibTableColumn
nwIpWgIfRowStatus = _NwIpWgIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2, 1, 5),
    _NwIpWgIfRowStatus_Type()
)
nwIpWgIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgIfRowStatus.setStatus("mandatory")


class _NwIpWgIfOperStatus_Type(Integer32):
    """Custom type nwIpWgIfOperStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("addressConflict", 4),
          ("disabled", 2),
          ("internalError", 8),
          ("linkDown", 6),
          ("ok", 1),
          ("resetRequired", 5),
          ("routingDown", 7),
          ("workgroupInvalid", 3))
    )


_NwIpWgIfOperStatus_Type.__name__ = "Integer32"
_NwIpWgIfOperStatus_Object = MibTableColumn
nwIpWgIfOperStatus = _NwIpWgIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 2, 1, 6),
    _NwIpWgIfOperStatus_Type()
)
nwIpWgIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgIfOperStatus.setStatus("mandatory")
_NwIpWgRngTable_Object = MibTable
nwIpWgRngTable = _NwIpWgRngTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    nwIpWgRngTable.setStatus("mandatory")
_NwIpWgRngEntry_Object = MibTableRow
nwIpWgRngEntry = _NwIpWgRngEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3, 1)
)
nwIpWgRngEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgRngBegHostAddr"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgRngEndHostAddr"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgRngIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpWgRngEntry.setStatus("mandatory")
_NwIpWgRngBegHostAddr_Type = IpAddress
_NwIpWgRngBegHostAddr_Object = MibTableColumn
nwIpWgRngBegHostAddr = _NwIpWgRngBegHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3, 1, 1),
    _NwIpWgRngBegHostAddr_Type()
)
nwIpWgRngBegHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgRngBegHostAddr.setStatus("mandatory")
_NwIpWgRngEndHostAddr_Type = IpAddress
_NwIpWgRngEndHostAddr_Object = MibTableColumn
nwIpWgRngEndHostAddr = _NwIpWgRngEndHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3, 1, 2),
    _NwIpWgRngEndHostAddr_Type()
)
nwIpWgRngEndHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgRngEndHostAddr.setStatus("mandatory")
_NwIpWgRngIfIndex_Type = Integer32
_NwIpWgRngIfIndex_Object = MibTableColumn
nwIpWgRngIfIndex = _NwIpWgRngIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3, 1, 3),
    _NwIpWgRngIfIndex_Type()
)
nwIpWgRngIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgRngIfIndex.setStatus("mandatory")


class _NwIpWgRngPhysAddr_Type(OctetString):
    """Custom type nwIpWgRngPhysAddr based on OctetString"""
    defaultHexValue = "000000000000"


_NwIpWgRngPhysAddr_Object = MibTableColumn
nwIpWgRngPhysAddr = _NwIpWgRngPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3, 1, 4),
    _NwIpWgRngPhysAddr_Type()
)
nwIpWgRngPhysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgRngPhysAddr.setStatus("mandatory")


class _NwIpWgRngRowStatus_Type(Integer32):
    """Custom type nwIpWgRngRowStatus based on Integer32"""
    defaultValue = 2

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_NwIpWgRngRowStatus_Type.__name__ = "Integer32"
_NwIpWgRngRowStatus_Object = MibTableColumn
nwIpWgRngRowStatus = _NwIpWgRngRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3, 1, 5),
    _NwIpWgRngRowStatus_Type()
)
nwIpWgRngRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpWgRngRowStatus.setStatus("mandatory")


class _NwIpWgRngOperStatus_Type(Integer32):
    """Custom type nwIpWgRngOperStatus based on Integer32"""
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
          ("interfaceInvalid", 4),
          ("internalError", 6),
          ("ok", 1),
          ("physAddrRequired", 5),
          ("workgroupInvalid", 3))
    )


_NwIpWgRngOperStatus_Type.__name__ = "Integer32"
_NwIpWgRngOperStatus_Object = MibTableColumn
nwIpWgRngOperStatus = _NwIpWgRngOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 3, 1, 6),
    _NwIpWgRngOperStatus_Type()
)
nwIpWgRngOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgRngOperStatus.setStatus("mandatory")
_NwIpWgHostTable_Object = MibTable
nwIpWgHostTable = _NwIpWgHostTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    nwIpWgHostTable.setStatus("mandatory")
_NwIpWgHostEntry_Object = MibTableRow
nwIpWgHostEntry = _NwIpWgHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 4, 1)
)
nwIpWgHostEntry.setIndexNames(
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgHostHostAddr"),
    (0, "CTRON-IP-ROUTER-MIB", "nwIpWgHostIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpWgHostEntry.setStatus("mandatory")
_NwIpWgHostHostAddr_Type = IpAddress
_NwIpWgHostHostAddr_Object = MibTableColumn
nwIpWgHostHostAddr = _NwIpWgHostHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 4, 1, 1),
    _NwIpWgHostHostAddr_Type()
)
nwIpWgHostHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgHostHostAddr.setStatus("mandatory")
_NwIpWgHostIfIndex_Type = Integer32
_NwIpWgHostIfIndex_Object = MibTableColumn
nwIpWgHostIfIndex = _NwIpWgHostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 4, 1, 2),
    _NwIpWgHostIfIndex_Type()
)
nwIpWgHostIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgHostIfIndex.setStatus("mandatory")
_NwIpWgHostDefIdent_Type = Integer32
_NwIpWgHostDefIdent_Object = MibTableColumn
nwIpWgHostDefIdent = _NwIpWgHostDefIdent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 4, 1, 3),
    _NwIpWgHostDefIdent_Type()
)
nwIpWgHostDefIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgHostDefIdent.setStatus("mandatory")
_NwIpWgHostPhysAddr_Type = OctetString
_NwIpWgHostPhysAddr_Object = MibTableColumn
nwIpWgHostPhysAddr = _NwIpWgHostPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 4, 1, 4),
    _NwIpWgHostPhysAddr_Type()
)
nwIpWgHostPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgHostPhysAddr.setStatus("mandatory")


class _NwIpWgHostStatus_Type(Integer32):
    """Custom type nwIpWgHostStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("invalid-expired", 9),
          ("invalid-interface", 7),
          ("invalid-multiple", 4),
          ("invalid-physaddr", 5),
          ("invalid-range", 6),
          ("invalid-workgroup", 8),
          ("other", 1),
          ("unknown", 2),
          ("valid", 3))
    )


_NwIpWgHostStatus_Type.__name__ = "Integer32"
_NwIpWgHostStatus_Object = MibTableColumn
nwIpWgHostStatus = _NwIpWgHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 11, 4, 1, 5),
    _NwIpWgHostStatus_Type()
)
nwIpWgHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpWgHostStatus.setStatus("mandatory")
_NwIpClientServices_ObjectIdentity = ObjectIdentity
nwIpClientServices = _NwIpClientServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-IP-ROUTER-MIB",
    **{"nwIpRouter": nwIpRouter,
       "nwIpMibs": nwIpMibs,
       "nwIpMibRevText": nwIpMibRevText,
       "nwIpComponents": nwIpComponents,
       "nwIpSystem": nwIpSystem,
       "nwIpSysConfig": nwIpSysConfig,
       "nwIpSysRouterId": nwIpSysRouterId,
       "nwIpSysAdministration": nwIpSysAdministration,
       "nwIpSysAdminStatus": nwIpSysAdminStatus,
       "nwIpSysOperStatus": nwIpSysOperStatus,
       "nwIpSysAdminReset": nwIpSysAdminReset,
       "nwIpSysOperationalTime": nwIpSysOperationalTime,
       "nwIpSysVersion": nwIpSysVersion,
       "nwIpForwarding": nwIpForwarding,
       "nwIpFwdSystem": nwIpFwdSystem,
       "nwIpFwdCounters": nwIpFwdCounters,
       "nwIpFwdCtrAdminStatus": nwIpFwdCtrAdminStatus,
       "nwIpFwdCtrReset": nwIpFwdCtrReset,
       "nwIpFwdCtrOperationalTime": nwIpFwdCtrOperationalTime,
       "nwIpFwdCtrInPkts": nwIpFwdCtrInPkts,
       "nwIpFwdCtrOutPkts": nwIpFwdCtrOutPkts,
       "nwIpFwdCtrFwdPkts": nwIpFwdCtrFwdPkts,
       "nwIpFwdCtrFilteredPkts": nwIpFwdCtrFilteredPkts,
       "nwIpFwdCtrDiscardPkts": nwIpFwdCtrDiscardPkts,
       "nwIpFwdCtrAddrErrPkts": nwIpFwdCtrAddrErrPkts,
       "nwIpFwdCtrLenErrPkts": nwIpFwdCtrLenErrPkts,
       "nwIpFwdCtrHdrErrPkts": nwIpFwdCtrHdrErrPkts,
       "nwIpFwdCtrInBytes": nwIpFwdCtrInBytes,
       "nwIpFwdCtrOutBytes": nwIpFwdCtrOutBytes,
       "nwIpFwdCtrFwdBytes": nwIpFwdCtrFwdBytes,
       "nwIpFwdCtrFilteredBytes": nwIpFwdCtrFilteredBytes,
       "nwIpFwdCtrDiscardBytes": nwIpFwdCtrDiscardBytes,
       "nwIpFwdCtrHostInPkts": nwIpFwdCtrHostInPkts,
       "nwIpFwdCtrHostOutPkts": nwIpFwdCtrHostOutPkts,
       "nwIpFwdCtrHostDiscardPkts": nwIpFwdCtrHostDiscardPkts,
       "nwIpFwdCtrHostInBytes": nwIpFwdCtrHostInBytes,
       "nwIpFwdCtrHostOutBytes": nwIpFwdCtrHostOutBytes,
       "nwIpFwdCtrHostDiscardBytes": nwIpFwdCtrHostDiscardBytes,
       "nwIpFwdInterfaces": nwIpFwdInterfaces,
       "nwIpFwdIfConfig": nwIpFwdIfConfig,
       "nwIpFwdIfTable": nwIpFwdIfTable,
       "nwIpFwdIfEntry": nwIpFwdIfEntry,
       "nwIpFwdIfIndex": nwIpFwdIfIndex,
       "nwIpFwdIfAdminStatus": nwIpFwdIfAdminStatus,
       "nwIpFwdIfOperStatus": nwIpFwdIfOperStatus,
       "nwIpFwdIfOperationalTime": nwIpFwdIfOperationalTime,
       "nwIpFwdIfControl": nwIpFwdIfControl,
       "nwIpFwdIfMtu": nwIpFwdIfMtu,
       "nwIpFwdIfForwarding": nwIpFwdIfForwarding,
       "nwIpFwdIfFrameType": nwIpFwdIfFrameType,
       "nwIpFwdIfAclIdentifier": nwIpFwdIfAclIdentifier,
       "nwIpFwdIfAclStatus": nwIpFwdIfAclStatus,
       "nwIpFwdIfCacheControl": nwIpFwdIfCacheControl,
       "nwIpFwdIfCacheEntries": nwIpFwdIfCacheEntries,
       "nwIpFwdIfCacheHits": nwIpFwdIfCacheHits,
       "nwIpFwdIfCacheMisses": nwIpFwdIfCacheMisses,
       "nwIpAddressTable": nwIpAddressTable,
       "nwIpAddrEntry": nwIpAddrEntry,
       "nwIpAddrIfIndex": nwIpAddrIfIndex,
       "nwIpAddrIfAddress": nwIpAddrIfAddress,
       "nwIpAddrIfControl": nwIpAddrIfControl,
       "nwIpAddrIfAddrType": nwIpAddrIfAddrType,
       "nwIpAddrIfMask": nwIpAddrIfMask,
       "nwIpAddrIfBcastAddr": nwIpAddrIfBcastAddr,
       "nwIpFwdIfCounters": nwIpFwdIfCounters,
       "nwIpFwdIfCtrTable": nwIpFwdIfCtrTable,
       "nwIpFwdIfCtrEntry": nwIpFwdIfCtrEntry,
       "nwIpFwdIfCtrIfIndex": nwIpFwdIfCtrIfIndex,
       "nwIpFwdIfCtrAdminStatus": nwIpFwdIfCtrAdminStatus,
       "nwIpFwdIfCtrReset": nwIpFwdIfCtrReset,
       "nwIpFwdIfCtrOperationalTime": nwIpFwdIfCtrOperationalTime,
       "nwIpFwdIfCtrInPkts": nwIpFwdIfCtrInPkts,
       "nwIpFwdIfCtrOutPkts": nwIpFwdIfCtrOutPkts,
       "nwIpFwdIfCtrFwdPkts": nwIpFwdIfCtrFwdPkts,
       "nwIpFwdIfCtrFilteredPkts": nwIpFwdIfCtrFilteredPkts,
       "nwIpFwdIfCtrDiscardPkts": nwIpFwdIfCtrDiscardPkts,
       "nwIpFwdIfCtrAddrErrPkts": nwIpFwdIfCtrAddrErrPkts,
       "nwIpFwdIfCtrLenErrPkts": nwIpFwdIfCtrLenErrPkts,
       "nwIpFwdIfCtrHdrErrPkts": nwIpFwdIfCtrHdrErrPkts,
       "nwIpFwdIfCtrInBytes": nwIpFwdIfCtrInBytes,
       "nwIpFwdIfCtrOutBytes": nwIpFwdIfCtrOutBytes,
       "nwIpFwdIfCtrFwdBytes": nwIpFwdIfCtrFwdBytes,
       "nwIpFwdIfCtrFilteredBytes": nwIpFwdIfCtrFilteredBytes,
       "nwIpFwdIfCtrDiscardBytes": nwIpFwdIfCtrDiscardBytes,
       "nwIpFwdIfCtrHostInPkts": nwIpFwdIfCtrHostInPkts,
       "nwIpFwdIfCtrHostOutPkts": nwIpFwdIfCtrHostOutPkts,
       "nwIpFwdIfCtrHostDiscardPkts": nwIpFwdIfCtrHostDiscardPkts,
       "nwIpFwdIfCtrHostInBytes": nwIpFwdIfCtrHostInBytes,
       "nwIpFwdIfCtrHostOutBytes": nwIpFwdIfCtrHostOutBytes,
       "nwIpFwdIfCtrHostDiscardBytes": nwIpFwdIfCtrHostDiscardBytes,
       "nwIpTopology": nwIpTopology,
       "nwIpDistanceVector": nwIpDistanceVector,
       "nwIpRip": nwIpRip,
       "nwIpRipSystem": nwIpRipSystem,
       "nwIpRipConfig": nwIpRipConfig,
       "nwIpRipAdminStatus": nwIpRipAdminStatus,
       "nwIpRipOperStatus": nwIpRipOperStatus,
       "nwIpRipAdminReset": nwIpRipAdminReset,
       "nwIpRipOperationalTime": nwIpRipOperationalTime,
       "nwIpRipVersion": nwIpRipVersion,
       "nwIpRipStackSize": nwIpRipStackSize,
       "nwIpRipThreadPriority": nwIpRipThreadPriority,
       "nwIpRipDatabaseThreshold": nwIpRipDatabaseThreshold,
       "nwIpRipAgeOut": nwIpRipAgeOut,
       "nwIpRipHoldDown": nwIpRipHoldDown,
       "nwIpRipCounters": nwIpRipCounters,
       "nwIpRipCtrAdminStatus": nwIpRipCtrAdminStatus,
       "nwIpRipCtrReset": nwIpRipCtrReset,
       "nwIpRipCtrOperationalTime": nwIpRipCtrOperationalTime,
       "nwIpRipCtrInPkts": nwIpRipCtrInPkts,
       "nwIpRipCtrOutPkts": nwIpRipCtrOutPkts,
       "nwIpRipCtrFilteredPkts": nwIpRipCtrFilteredPkts,
       "nwIpRipCtrDiscardPkts": nwIpRipCtrDiscardPkts,
       "nwIpRipCtrInBytes": nwIpRipCtrInBytes,
       "nwIpRipCtrOutBytes": nwIpRipCtrOutBytes,
       "nwIpRipCtrFilteredBytes": nwIpRipCtrFilteredBytes,
       "nwIpRipCtrDiscardBytes": nwIpRipCtrDiscardBytes,
       "nwIpRipInterfaces": nwIpRipInterfaces,
       "nwIpRipIfConfig": nwIpRipIfConfig,
       "nwIpRipIfTable": nwIpRipIfTable,
       "nwIpRipIfEntry": nwIpRipIfEntry,
       "nwIpRipIfIndex": nwIpRipIfIndex,
       "nwIpRipIfAdminStatus": nwIpRipIfAdminStatus,
       "nwIpRipIfOperStatus": nwIpRipIfOperStatus,
       "nwIpRipIfOperationalTime": nwIpRipIfOperationalTime,
       "nwIpRipIfVersion": nwIpRipIfVersion,
       "nwIpRipIfAdvertisement": nwIpRipIfAdvertisement,
       "nwIpRipIfFloodDelay": nwIpRipIfFloodDelay,
       "nwIpRipIfRequestDelay": nwIpRipIfRequestDelay,
       "nwIpRipIfPriority": nwIpRipIfPriority,
       "nwIpRipIfHelloTimer": nwIpRipIfHelloTimer,
       "nwIpRipIfSplitHorizon": nwIpRipIfSplitHorizon,
       "nwIpRipIfPoisonReverse": nwIpRipIfPoisonReverse,
       "nwIpRipIfSnooping": nwIpRipIfSnooping,
       "nwIpRipIfType": nwIpRipIfType,
       "nwIpRipIfXmitCost": nwIpRipIfXmitCost,
       "nwIpRipIfAclIdentifier": nwIpRipIfAclIdentifier,
       "nwIpRipIfAclStatus": nwIpRipIfAclStatus,
       "nwIpRipIfCounters": nwIpRipIfCounters,
       "nwIpRipIfCtrTable": nwIpRipIfCtrTable,
       "nwIpRipIfCtrEntry": nwIpRipIfCtrEntry,
       "nwIpRipIfCtrIfIndex": nwIpRipIfCtrIfIndex,
       "nwIpRipIfCtrAdminStatus": nwIpRipIfCtrAdminStatus,
       "nwIpRipIfCtrReset": nwIpRipIfCtrReset,
       "nwIpRipIfCtrOperationalTime": nwIpRipIfCtrOperationalTime,
       "nwIpRipIfCtrInPkts": nwIpRipIfCtrInPkts,
       "nwIpRipIfCtrOutPkts": nwIpRipIfCtrOutPkts,
       "nwIpRipIfCtrFilteredPkts": nwIpRipIfCtrFilteredPkts,
       "nwIpRipIfCtrDiscardPkts": nwIpRipIfCtrDiscardPkts,
       "nwIpRipIfCtrInBytes": nwIpRipIfCtrInBytes,
       "nwIpRipIfCtrOutBytes": nwIpRipIfCtrOutBytes,
       "nwIpRipIfCtrFilteredBytes": nwIpRipIfCtrFilteredBytes,
       "nwIpRipIfCtrDiscardBytes": nwIpRipIfCtrDiscardBytes,
       "nwIpRipDatabase": nwIpRipDatabase,
       "nwIpRipRouteTable": nwIpRipRouteTable,
       "nwIpRipRouteEntry": nwIpRipRouteEntry,
       "nwIpRipRtNetId": nwIpRipRtNetId,
       "nwIpRipRtIfIndex": nwIpRipRtIfIndex,
       "nwIpRipRtSrcNode": nwIpRipRtSrcNode,
       "nwIpRipRtMask": nwIpRipRtMask,
       "nwIpRipRtHops": nwIpRipRtHops,
       "nwIpRipRtAge": nwIpRipRtAge,
       "nwIpRipRtType": nwIpRipRtType,
       "nwIpRipRtFlags": nwIpRipRtFlags,
       "nwIpRipFilters": nwIpRipFilters,
       "nwIpLinkState": nwIpLinkState,
       "nwIpOspf": nwIpOspf,
       "nwIpOspfSystem": nwIpOspfSystem,
       "nwIpOspfConfig": nwIpOspfConfig,
       "nwIpOspfAdminStatus": nwIpOspfAdminStatus,
       "nwIpOspfOperStatus": nwIpOspfOperStatus,
       "nwIpOspfAdminReset": nwIpOspfAdminReset,
       "nwIpOspfOperationalTime": nwIpOspfOperationalTime,
       "nwIpOspfVersion": nwIpOspfVersion,
       "nwIpOspfStackSize": nwIpOspfStackSize,
       "nwIpOspfThreadPriority": nwIpOspfThreadPriority,
       "nwIpOspfCounters": nwIpOspfCounters,
       "nwIpOspfCtrAdminStatus": nwIpOspfCtrAdminStatus,
       "nwIpOspfCtrReset": nwIpOspfCtrReset,
       "nwIpOspfCtrOperationalTime": nwIpOspfCtrOperationalTime,
       "nwIpOspfCtrInPkts": nwIpOspfCtrInPkts,
       "nwIpOspfCtrOutPkts": nwIpOspfCtrOutPkts,
       "nwIpOspfCtrFilteredPkts": nwIpOspfCtrFilteredPkts,
       "nwIpOspfCtrDiscardPkts": nwIpOspfCtrDiscardPkts,
       "nwIpOspfCtrInBytes": nwIpOspfCtrInBytes,
       "nwIpOspfCtrOutBytes": nwIpOspfCtrOutBytes,
       "nwIpOspfCtrFilteredBytes": nwIpOspfCtrFilteredBytes,
       "nwIpOspfCtrDiscardBytes": nwIpOspfCtrDiscardBytes,
       "nwIpOspfInterfaces": nwIpOspfInterfaces,
       "nwIpOspfIfConfig": nwIpOspfIfConfig,
       "nwIpOspfIfTable": nwIpOspfIfTable,
       "nwIpOspfIfEntry": nwIpOspfIfEntry,
       "nwIpOspfIfIndex": nwIpOspfIfIndex,
       "nwIpOspfIfAdminStatus": nwIpOspfIfAdminStatus,
       "nwIpOspfIfOperStatus": nwIpOspfIfOperStatus,
       "nwIpOspfIfOperationalTime": nwIpOspfIfOperationalTime,
       "nwIpOspfIfVersion": nwIpOspfIfVersion,
       "nwIpOspfIfSnooping": nwIpOspfIfSnooping,
       "nwIpOspfIfType": nwIpOspfIfType,
       "nwIpOspfIfAclIdentifier": nwIpOspfIfAclIdentifier,
       "nwIpOspfIfAclStatus": nwIpOspfIfAclStatus,
       "nwIpOspfIfCounters": nwIpOspfIfCounters,
       "nwIpOspfIfCtrTable": nwIpOspfIfCtrTable,
       "nwIpOspfIfCtrEntry": nwIpOspfIfCtrEntry,
       "nwIpOspfIfCtrIfIndex": nwIpOspfIfCtrIfIndex,
       "nwIpOspfIfCtrAdminStatus": nwIpOspfIfCtrAdminStatus,
       "nwIpOspfIfCtrReset": nwIpOspfIfCtrReset,
       "nwIpOspfIfCtrOperationalTime": nwIpOspfIfCtrOperationalTime,
       "nwIpOspfIfCtrInPkts": nwIpOspfIfCtrInPkts,
       "nwIpOspfIfCtrOutPkts": nwIpOspfIfCtrOutPkts,
       "nwIpOspfIfCtrFilteredPkts": nwIpOspfIfCtrFilteredPkts,
       "nwIpOspfIfCtrDiscardPkts": nwIpOspfIfCtrDiscardPkts,
       "nwIpOspfIfCtrInBytes": nwIpOspfIfCtrInBytes,
       "nwIpOspfIfCtrOutBytes": nwIpOspfIfCtrOutBytes,
       "nwIpOspfIfCtrFilteredBytes": nwIpOspfIfCtrFilteredBytes,
       "nwIpOspfIfCtrDiscardBytes": nwIpOspfIfCtrDiscardBytes,
       "nwIpOspfDatabase": nwIpOspfDatabase,
       "nwIpOspfFilters": nwIpOspfFilters,
       "nwIpFib": nwIpFib,
       "nwIpFibSystem": nwIpFibSystem,
       "nwIpRipRoutePriority": nwIpRipRoutePriority,
       "nwIpOSPFRoutePriority": nwIpOSPFRoutePriority,
       "nwIpStaticRoutePriority": nwIpStaticRoutePriority,
       "nwIpOspfFib": nwIpOspfFib,
       "nwIpOspfFibControl": nwIpOspfFibControl,
       "nwIpOspfForward": nwIpOspfForward,
       "nwIpOspfLeakAllStaticRoutes": nwIpOspfLeakAllStaticRoutes,
       "nwIpOspfLeakAllRipRoutes": nwIpOspfLeakAllRipRoutes,
       "nwIpOspfLeakAllBgp4Routes": nwIpOspfLeakAllBgp4Routes,
       "nwIpOspfFibEntries": nwIpOspfFibEntries,
       "nwIpOspfStaticTable": nwIpOspfStaticTable,
       "nwIpOspfStaticEntry": nwIpOspfStaticEntry,
       "nwIpOspfStaticDest": nwIpOspfStaticDest,
       "nwIpOspfStaticForwardMask": nwIpOspfStaticForwardMask,
       "nwIpOspfStaticNextHop": nwIpOspfStaticNextHop,
       "nwIpOspfStaticMetric": nwIpOspfStaticMetric,
       "nwIpOspfStaticMetricType": nwIpOspfStaticMetricType,
       "nwIpOspfStaticStatus": nwIpOspfStaticStatus,
       "nwIpOspfDynamicTable": nwIpOspfDynamicTable,
       "nwIpOspfRipTable": nwIpOspfRipTable,
       "nwIpOspfBgp4Table": nwIpOspfBgp4Table,
       "nwIpEndSystems": nwIpEndSystems,
       "nwIpHostsSystem": nwIpHostsSystem,
       "nwIpHostsTimeToLive": nwIpHostsTimeToLive,
       "nwIpHostsRetryCount": nwIpHostsRetryCount,
       "nwIpHostsInterfaces": nwIpHostsInterfaces,
       "nwIpHostCtlTable": nwIpHostCtlTable,
       "nwIpHostCtlEntry": nwIpHostCtlEntry,
       "nwIpHostCtlIfIndex": nwIpHostCtlIfIndex,
       "nwIpHostCtlAdminStatus": nwIpHostCtlAdminStatus,
       "nwIpHostCtlOperStatus": nwIpHostCtlOperStatus,
       "nwIpHostCtlOperationalTime": nwIpHostCtlOperationalTime,
       "nwIpHostCtlProtocol": nwIpHostCtlProtocol,
       "nwIpHostCtlSnooping": nwIpHostCtlSnooping,
       "nwIpHostCtlProxy": nwIpHostCtlProxy,
       "nwIpHostCtlCacheMax": nwIpHostCtlCacheMax,
       "nwIpHostCtlCacheSize": nwIpHostCtlCacheSize,
       "nwIpHostCtlNumStatics": nwIpHostCtlNumStatics,
       "nwIpHostCtlNumDynamics": nwIpHostCtlNumDynamics,
       "nwIpHostCtlCacheHits": nwIpHostCtlCacheHits,
       "nwIpHostCtlCacheMisses": nwIpHostCtlCacheMisses,
       "nwIpHostsToMedia": nwIpHostsToMedia,
       "nwIpHostMapTable": nwIpHostMapTable,
       "nwIpHostMapEntry": nwIpHostMapEntry,
       "nwIpHostMapIfIndex": nwIpHostMapIfIndex,
       "nwIpHostMapIpAddr": nwIpHostMapIpAddr,
       "nwIpHostMapPhysAddr": nwIpHostMapPhysAddr,
       "nwIpHostMapType": nwIpHostMapType,
       "nwIpHostMapCircuitID": nwIpHostMapCircuitID,
       "nwIpHostMapFraming": nwIpHostMapFraming,
       "nwIpHostMapPortNumber": nwIpHostMapPortNumber,
       "nwIpAccessControl": nwIpAccessControl,
       "nwIpAclValidEntries": nwIpAclValidEntries,
       "nwIpAclTable": nwIpAclTable,
       "nwIpAclEntry": nwIpAclEntry,
       "nwIpAclIdentifier": nwIpAclIdentifier,
       "nwIpAclSequence": nwIpAclSequence,
       "nwIpAclPermission": nwIpAclPermission,
       "nwIpAclMatches": nwIpAclMatches,
       "nwIpAclDestAddress": nwIpAclDestAddress,
       "nwIpAclDestMask": nwIpAclDestMask,
       "nwIpAclSrcAddress": nwIpAclSrcAddress,
       "nwIpAclSrcMask": nwIpAclSrcMask,
       "nwIpAclProtocol": nwIpAclProtocol,
       "nwIpAclPortNumber": nwIpAclPortNumber,
       "nwIpFilters": nwIpFilters,
       "nwIpRedirector": nwIpRedirector,
       "nwIpRedirectorSystem": nwIpRedirectorSystem,
       "nwIpRedirectTable": nwIpRedirectTable,
       "nwIpRedirectEntry": nwIpRedirectEntry,
       "nwIpRedirectPort": nwIpRedirectPort,
       "nwIpRedirectAddress": nwIpRedirectAddress,
       "nwIpRedirectType": nwIpRedirectType,
       "nwIpRedirectCount": nwIpRedirectCount,
       "nwIpRedirectorInterface": nwIpRedirectorInterface,
       "nwIpEvent": nwIpEvent,
       "nwIpEventLogConfig": nwIpEventLogConfig,
       "nwIpEventAdminStatus": nwIpEventAdminStatus,
       "nwIpEventMaxEntries": nwIpEventMaxEntries,
       "nwIpEventTraceAll": nwIpEventTraceAll,
       "nwIpEventLogFilterTable": nwIpEventLogFilterTable,
       "nwIpEventFilterTable": nwIpEventFilterTable,
       "nwIpEventFilterEntry": nwIpEventFilterEntry,
       "nwIpEventFltrProtocol": nwIpEventFltrProtocol,
       "nwIpEventFltrIfNum": nwIpEventFltrIfNum,
       "nwIpEventFltrControl": nwIpEventFltrControl,
       "nwIpEventFltrType": nwIpEventFltrType,
       "nwIpEventFltrSeverity": nwIpEventFltrSeverity,
       "nwIpEventFltrAction": nwIpEventFltrAction,
       "nwIpEventLogTable": nwIpEventLogTable,
       "nwIpEventTable": nwIpEventTable,
       "nwIpEventEntry": nwIpEventEntry,
       "nwIpEventNumber": nwIpEventNumber,
       "nwIpEventTime": nwIpEventTime,
       "nwIpEventType": nwIpEventType,
       "nwIpEventSeverity": nwIpEventSeverity,
       "nwIpEventProtocol": nwIpEventProtocol,
       "nwIpEventIfNum": nwIpEventIfNum,
       "nwIpEventTextString": nwIpEventTextString,
       "nwIpWorkGroup": nwIpWorkGroup,
       "nwIpWgDefTable": nwIpWgDefTable,
       "nwIpWgDefEntry": nwIpWgDefEntry,
       "nwIpWgDefIdentifier": nwIpWgDefIdentifier,
       "nwIpWgDefHostAddress": nwIpWgDefHostAddress,
       "nwIpWgDefSubnetMask": nwIpWgDefSubnetMask,
       "nwIpWgDefSecurity": nwIpWgDefSecurity,
       "nwIpWgDefFastPath": nwIpWgDefFastPath,
       "nwIpWgDefRowStatus": nwIpWgDefRowStatus,
       "nwIpWgDefOperStatus": nwIpWgDefOperStatus,
       "nwIpWgDefNumActiveIntf": nwIpWgDefNumActiveIntf,
       "nwIpWgDefNumTotalIntf": nwIpWgDefNumTotalIntf,
       "nwIpWgIfTable": nwIpWgIfTable,
       "nwIpWgIfEntry": nwIpWgIfEntry,
       "nwIpWgIfDefIdent": nwIpWgIfDefIdent,
       "nwIpWgIfIfIndex": nwIpWgIfIfIndex,
       "nwIpWgIfNumActiveHosts": nwIpWgIfNumActiveHosts,
       "nwIpWgIfNumKnownHosts": nwIpWgIfNumKnownHosts,
       "nwIpWgIfRowStatus": nwIpWgIfRowStatus,
       "nwIpWgIfOperStatus": nwIpWgIfOperStatus,
       "nwIpWgRngTable": nwIpWgRngTable,
       "nwIpWgRngEntry": nwIpWgRngEntry,
       "nwIpWgRngBegHostAddr": nwIpWgRngBegHostAddr,
       "nwIpWgRngEndHostAddr": nwIpWgRngEndHostAddr,
       "nwIpWgRngIfIndex": nwIpWgRngIfIndex,
       "nwIpWgRngPhysAddr": nwIpWgRngPhysAddr,
       "nwIpWgRngRowStatus": nwIpWgRngRowStatus,
       "nwIpWgRngOperStatus": nwIpWgRngOperStatus,
       "nwIpWgHostTable": nwIpWgHostTable,
       "nwIpWgHostEntry": nwIpWgHostEntry,
       "nwIpWgHostHostAddr": nwIpWgHostHostAddr,
       "nwIpWgHostIfIndex": nwIpWgHostIfIndex,
       "nwIpWgHostDefIdent": nwIpWgHostDefIdent,
       "nwIpWgHostPhysAddr": nwIpWgHostPhysAddr,
       "nwIpWgHostStatus": nwIpWgHostStatus,
       "nwIpClientServices": nwIpClientServices}
)
