# SNMP MIB module (CTRON-IPX-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-IPX-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:59 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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



class IpxAddress(OctetString):
    """Custom type IpxAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NwIpxRouter_ObjectIdentity = ObjectIdentity
nwIpxRouter = _NwIpxRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2)
)
_NwIpxMibs_ObjectIdentity = ObjectIdentity
nwIpxMibs = _NwIpxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 1)
)
_NwIpxMibRevText_Type = DisplayString
_NwIpxMibRevText_Object = MibScalar
nwIpxMibRevText = _NwIpxMibRevText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 1, 1),
    _NwIpxMibRevText_Type()
)
nwIpxMibRevText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxMibRevText.setStatus("mandatory")
_NwIpxComponents_ObjectIdentity = ObjectIdentity
nwIpxComponents = _NwIpxComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2)
)
_NwIpxSystem_ObjectIdentity = ObjectIdentity
nwIpxSystem = _NwIpxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1)
)
_NwIpxSysConfig_ObjectIdentity = ObjectIdentity
nwIpxSysConfig = _NwIpxSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 1)
)
_NwIpxSysRouterId_Type = IpxAddress
_NwIpxSysRouterId_Object = MibScalar
nwIpxSysRouterId = _NwIpxSysRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 1, 1),
    _NwIpxSysRouterId_Type()
)
nwIpxSysRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSysRouterId.setStatus("mandatory")
_NwIpxSysAdministration_ObjectIdentity = ObjectIdentity
nwIpxSysAdministration = _NwIpxSysAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 2)
)


class _NwIpxSysAdminStatus_Type(Integer32):
    """Custom type nwIpxSysAdminStatus based on Integer32"""
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


_NwIpxSysAdminStatus_Type.__name__ = "Integer32"
_NwIpxSysAdminStatus_Object = MibScalar
nwIpxSysAdminStatus = _NwIpxSysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 2, 1),
    _NwIpxSysAdminStatus_Type()
)
nwIpxSysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSysAdminStatus.setStatus("mandatory")


class _NwIpxSysOperStatus_Type(Integer32):
    """Custom type nwIpxSysOperStatus based on Integer32"""
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


_NwIpxSysOperStatus_Type.__name__ = "Integer32"
_NwIpxSysOperStatus_Object = MibScalar
nwIpxSysOperStatus = _NwIpxSysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 2, 2),
    _NwIpxSysOperStatus_Type()
)
nwIpxSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSysOperStatus.setStatus("mandatory")


class _NwIpxSysAdminReset_Type(Integer32):
    """Custom type nwIpxSysAdminReset based on Integer32"""
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


_NwIpxSysAdminReset_Type.__name__ = "Integer32"
_NwIpxSysAdminReset_Object = MibScalar
nwIpxSysAdminReset = _NwIpxSysAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 2, 3),
    _NwIpxSysAdminReset_Type()
)
nwIpxSysAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSysAdminReset.setStatus("mandatory")
_NwIpxSysOperationalTimel_Type = TimeTicks
_NwIpxSysOperationalTimel_Object = MibScalar
nwIpxSysOperationalTimel = _NwIpxSysOperationalTimel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 2, 4),
    _NwIpxSysOperationalTimel_Type()
)
nwIpxSysOperationalTimel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSysOperationalTimel.setStatus("mandatory")
_NwIpxSysVersion_Type = DisplayString
_NwIpxSysVersion_Object = MibScalar
nwIpxSysVersion = _NwIpxSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 1, 2, 5),
    _NwIpxSysVersion_Type()
)
nwIpxSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSysVersion.setStatus("mandatory")
_NwIpxForwarding_ObjectIdentity = ObjectIdentity
nwIpxForwarding = _NwIpxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2)
)
_NwIpxFwdSystem_ObjectIdentity = ObjectIdentity
nwIpxFwdSystem = _NwIpxFwdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1)
)
_NwIpxFwdCounters_ObjectIdentity = ObjectIdentity
nwIpxFwdCounters = _NwIpxFwdCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1)
)


class _NwIpxFwdCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxFwdCtrAdminStatus based on Integer32"""
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


_NwIpxFwdCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxFwdCtrAdminStatus_Object = MibScalar
nwIpxFwdCtrAdminStatus = _NwIpxFwdCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 1),
    _NwIpxFwdCtrAdminStatus_Type()
)
nwIpxFwdCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdCtrAdminStatus.setStatus("mandatory")


class _NwIpxFwdCtrReset_Type(Integer32):
    """Custom type nwIpxFwdCtrReset based on Integer32"""
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


_NwIpxFwdCtrReset_Type.__name__ = "Integer32"
_NwIpxFwdCtrReset_Object = MibScalar
nwIpxFwdCtrReset = _NwIpxFwdCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 2),
    _NwIpxFwdCtrReset_Type()
)
nwIpxFwdCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdCtrReset.setStatus("mandatory")
_NwIpxFwdCtrOperationalTime_Type = TimeTicks
_NwIpxFwdCtrOperationalTime_Object = MibScalar
nwIpxFwdCtrOperationalTime = _NwIpxFwdCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 3),
    _NwIpxFwdCtrOperationalTime_Type()
)
nwIpxFwdCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrOperationalTime.setStatus("mandatory")
_NwIpxFwdCtrInPkts_Type = Counter32
_NwIpxFwdCtrInPkts_Object = MibScalar
nwIpxFwdCtrInPkts = _NwIpxFwdCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 4),
    _NwIpxFwdCtrInPkts_Type()
)
nwIpxFwdCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrInPkts.setStatus("mandatory")
_NwIpxFwdCtrOutPkts_Type = Counter32
_NwIpxFwdCtrOutPkts_Object = MibScalar
nwIpxFwdCtrOutPkts = _NwIpxFwdCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 5),
    _NwIpxFwdCtrOutPkts_Type()
)
nwIpxFwdCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrOutPkts.setStatus("mandatory")
_NwIpxFwdCtrFwdPkts_Type = Counter32
_NwIpxFwdCtrFwdPkts_Object = MibScalar
nwIpxFwdCtrFwdPkts = _NwIpxFwdCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 6),
    _NwIpxFwdCtrFwdPkts_Type()
)
nwIpxFwdCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrFwdPkts.setStatus("mandatory")
_NwIpxFwdCtrFilteredPkts_Type = Counter32
_NwIpxFwdCtrFilteredPkts_Object = MibScalar
nwIpxFwdCtrFilteredPkts = _NwIpxFwdCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 7),
    _NwIpxFwdCtrFilteredPkts_Type()
)
nwIpxFwdCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrFilteredPkts.setStatus("mandatory")
_NwIpxFwdCtrDiscardPkts_Type = Counter32
_NwIpxFwdCtrDiscardPkts_Object = MibScalar
nwIpxFwdCtrDiscardPkts = _NwIpxFwdCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 8),
    _NwIpxFwdCtrDiscardPkts_Type()
)
nwIpxFwdCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrDiscardPkts.setStatus("mandatory")
_NwIpxFwdCtrAddrErrPkts_Type = Counter32
_NwIpxFwdCtrAddrErrPkts_Object = MibScalar
nwIpxFwdCtrAddrErrPkts = _NwIpxFwdCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 9),
    _NwIpxFwdCtrAddrErrPkts_Type()
)
nwIpxFwdCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrAddrErrPkts.setStatus("mandatory")
_NwIpxFwdCtrLenErrPkts_Type = Counter32
_NwIpxFwdCtrLenErrPkts_Object = MibScalar
nwIpxFwdCtrLenErrPkts = _NwIpxFwdCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 10),
    _NwIpxFwdCtrLenErrPkts_Type()
)
nwIpxFwdCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrLenErrPkts.setStatus("mandatory")
_NwIpxFwdCtrHdrErrPkts_Type = Counter32
_NwIpxFwdCtrHdrErrPkts_Object = MibScalar
nwIpxFwdCtrHdrErrPkts = _NwIpxFwdCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 11),
    _NwIpxFwdCtrHdrErrPkts_Type()
)
nwIpxFwdCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrHdrErrPkts.setStatus("mandatory")
_NwIpxFwdCtrInBytes_Type = Counter32
_NwIpxFwdCtrInBytes_Object = MibScalar
nwIpxFwdCtrInBytes = _NwIpxFwdCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 12),
    _NwIpxFwdCtrInBytes_Type()
)
nwIpxFwdCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrInBytes.setStatus("mandatory")
_NwIpxFwdCtrOutBytes_Type = Counter32
_NwIpxFwdCtrOutBytes_Object = MibScalar
nwIpxFwdCtrOutBytes = _NwIpxFwdCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 13),
    _NwIpxFwdCtrOutBytes_Type()
)
nwIpxFwdCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrOutBytes.setStatus("mandatory")
_NwIpxFwdCtrFwdBytes_Type = Counter32
_NwIpxFwdCtrFwdBytes_Object = MibScalar
nwIpxFwdCtrFwdBytes = _NwIpxFwdCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 14),
    _NwIpxFwdCtrFwdBytes_Type()
)
nwIpxFwdCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrFwdBytes.setStatus("mandatory")
_NwIpxFwdCtrFilteredBytes_Type = Counter32
_NwIpxFwdCtrFilteredBytes_Object = MibScalar
nwIpxFwdCtrFilteredBytes = _NwIpxFwdCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 15),
    _NwIpxFwdCtrFilteredBytes_Type()
)
nwIpxFwdCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrFilteredBytes.setStatus("mandatory")
_NwIpxFwdCtrDiscardBytes_Type = Counter32
_NwIpxFwdCtrDiscardBytes_Object = MibScalar
nwIpxFwdCtrDiscardBytes = _NwIpxFwdCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 16),
    _NwIpxFwdCtrDiscardBytes_Type()
)
nwIpxFwdCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrDiscardBytes.setStatus("mandatory")
_NwIpxFwdCtrHostInPkts_Type = Counter32
_NwIpxFwdCtrHostInPkts_Object = MibScalar
nwIpxFwdCtrHostInPkts = _NwIpxFwdCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 17),
    _NwIpxFwdCtrHostInPkts_Type()
)
nwIpxFwdCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrHostInPkts.setStatus("mandatory")
_NwIpxFwdCtrHostOutPkts_Type = Counter32
_NwIpxFwdCtrHostOutPkts_Object = MibScalar
nwIpxFwdCtrHostOutPkts = _NwIpxFwdCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 18),
    _NwIpxFwdCtrHostOutPkts_Type()
)
nwIpxFwdCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrHostOutPkts.setStatus("mandatory")
_NwIpxFwdCtrHostDiscardPkts_Type = Counter32
_NwIpxFwdCtrHostDiscardPkts_Object = MibScalar
nwIpxFwdCtrHostDiscardPkts = _NwIpxFwdCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 19),
    _NwIpxFwdCtrHostDiscardPkts_Type()
)
nwIpxFwdCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrHostDiscardPkts.setStatus("mandatory")
_NwIpxFwdCtrHostInBytes_Type = Counter32
_NwIpxFwdCtrHostInBytes_Object = MibScalar
nwIpxFwdCtrHostInBytes = _NwIpxFwdCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 20),
    _NwIpxFwdCtrHostInBytes_Type()
)
nwIpxFwdCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrHostInBytes.setStatus("mandatory")
_NwIpxFwdCtrHostOutBytes_Type = Counter32
_NwIpxFwdCtrHostOutBytes_Object = MibScalar
nwIpxFwdCtrHostOutBytes = _NwIpxFwdCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 21),
    _NwIpxFwdCtrHostOutBytes_Type()
)
nwIpxFwdCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrHostOutBytes.setStatus("mandatory")
_NwIpxFwdCtrHostDiscardBytes_Type = Counter32
_NwIpxFwdCtrHostDiscardBytes_Object = MibScalar
nwIpxFwdCtrHostDiscardBytes = _NwIpxFwdCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 1, 1, 22),
    _NwIpxFwdCtrHostDiscardBytes_Type()
)
nwIpxFwdCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdCtrHostDiscardBytes.setStatus("mandatory")
_NwIpxFwdInterfaces_ObjectIdentity = ObjectIdentity
nwIpxFwdInterfaces = _NwIpxFwdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2)
)
_NwIpxFwdIfConfig_ObjectIdentity = ObjectIdentity
nwIpxFwdIfConfig = _NwIpxFwdIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1)
)
_NwIpxFwdIfTable_Object = MibTable
nwIpxFwdIfTable = _NwIpxFwdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpxFwdIfTable.setStatus("mandatory")
_NwIpxFwdIfEntry_Object = MibTableRow
nwIpxFwdIfEntry = _NwIpxFwdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1)
)
nwIpxFwdIfEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxFwdIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxFwdIfEntry.setStatus("mandatory")
_NwIpxFwdIfIndex_Type = Integer32
_NwIpxFwdIfIndex_Object = MibTableColumn
nwIpxFwdIfIndex = _NwIpxFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1),
    _NwIpxFwdIfIndex_Type()
)
nwIpxFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfIndex.setStatus("mandatory")


class _NwIpxFwdIfAdminStatus_Type(Integer32):
    """Custom type nwIpxFwdIfAdminStatus based on Integer32"""
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


_NwIpxFwdIfAdminStatus_Type.__name__ = "Integer32"
_NwIpxFwdIfAdminStatus_Object = MibTableColumn
nwIpxFwdIfAdminStatus = _NwIpxFwdIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 2),
    _NwIpxFwdIfAdminStatus_Type()
)
nwIpxFwdIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfAdminStatus.setStatus("mandatory")


class _NwIpxFwdIfOperStatus_Type(Integer32):
    """Custom type nwIpxFwdIfOperStatus based on Integer32"""
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


_NwIpxFwdIfOperStatus_Type.__name__ = "Integer32"
_NwIpxFwdIfOperStatus_Object = MibTableColumn
nwIpxFwdIfOperStatus = _NwIpxFwdIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 3),
    _NwIpxFwdIfOperStatus_Type()
)
nwIpxFwdIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfOperStatus.setStatus("mandatory")
_NwIpxFwdIfOperationalTime_Type = TimeTicks
_NwIpxFwdIfOperationalTime_Object = MibTableColumn
nwIpxFwdIfOperationalTime = _NwIpxFwdIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 4),
    _NwIpxFwdIfOperationalTime_Type()
)
nwIpxFwdIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfOperationalTime.setStatus("mandatory")


class _NwIpxFwdIfControl_Type(Integer32):
    """Custom type nwIpxFwdIfControl based on Integer32"""
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
        *(("add", 2),
          ("delete", 3),
          ("other", 1))
    )


_NwIpxFwdIfControl_Type.__name__ = "Integer32"
_NwIpxFwdIfControl_Object = MibTableColumn
nwIpxFwdIfControl = _NwIpxFwdIfControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 5),
    _NwIpxFwdIfControl_Type()
)
nwIpxFwdIfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfControl.setStatus("mandatory")


class _NwIpxFwdIfMtu_Type(Integer32):
    """Custom type nwIpxFwdIfMtu based on Integer32"""
    defaultValue = 1500


_NwIpxFwdIfMtu_Object = MibTableColumn
nwIpxFwdIfMtu = _NwIpxFwdIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 6),
    _NwIpxFwdIfMtu_Type()
)
nwIpxFwdIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfMtu.setStatus("mandatory")


class _NwIpxFwdIfForwarding_Type(Integer32):
    """Custom type nwIpxFwdIfForwarding based on Integer32"""
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


_NwIpxFwdIfForwarding_Type.__name__ = "Integer32"
_NwIpxFwdIfForwarding_Object = MibTableColumn
nwIpxFwdIfForwarding = _NwIpxFwdIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 7),
    _NwIpxFwdIfForwarding_Type()
)
nwIpxFwdIfForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfForwarding.setStatus("mandatory")


class _NwIpxFwdIfFrameType_Type(Integer32):
    """Custom type nwIpxFwdIfFrameType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 17),
          ("encapenet", 9),
          ("encapenet8022", 10),
          ("encapenetnovell", 12),
          ("encapenetsnap", 11),
          ("encapfddi8022", 15),
          ("encapfddisnap", 16),
          ("encaptr8022", 13),
          ("encaptrsnap", 14),
          ("ethernet", 2),
          ("i8022", 4),
          ("nativewan", 8),
          ("novell", 6),
          ("other", 1),
          ("snap", 3))
    )


_NwIpxFwdIfFrameType_Type.__name__ = "Integer32"
_NwIpxFwdIfFrameType_Object = MibTableColumn
nwIpxFwdIfFrameType = _NwIpxFwdIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 8),
    _NwIpxFwdIfFrameType_Type()
)
nwIpxFwdIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfFrameType.setStatus("mandatory")


class _NwIpxFwdIfAclIdentifier_Type(Integer32):
    """Custom type nwIpxFwdIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwIpxFwdIfAclIdentifier_Object = MibTableColumn
nwIpxFwdIfAclIdentifier = _NwIpxFwdIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 9),
    _NwIpxFwdIfAclIdentifier_Type()
)
nwIpxFwdIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfAclIdentifier.setStatus("mandatory")


class _NwIpxFwdIfAclStatus_Type(Integer32):
    """Custom type nwIpxFwdIfAclStatus based on Integer32"""
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


_NwIpxFwdIfAclStatus_Type.__name__ = "Integer32"
_NwIpxFwdIfAclStatus_Object = MibTableColumn
nwIpxFwdIfAclStatus = _NwIpxFwdIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 10),
    _NwIpxFwdIfAclStatus_Type()
)
nwIpxFwdIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfAclStatus.setStatus("mandatory")


class _NwIpxFwdIfCacheControl_Type(Integer32):
    """Custom type nwIpxFwdIfCacheControl based on Integer32"""
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


_NwIpxFwdIfCacheControl_Type.__name__ = "Integer32"
_NwIpxFwdIfCacheControl_Object = MibTableColumn
nwIpxFwdIfCacheControl = _NwIpxFwdIfCacheControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 11),
    _NwIpxFwdIfCacheControl_Type()
)
nwIpxFwdIfCacheControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfCacheControl.setStatus("mandatory")
_NwIpxFwdIfCacheEntries_Type = Counter32
_NwIpxFwdIfCacheEntries_Object = MibTableColumn
nwIpxFwdIfCacheEntries = _NwIpxFwdIfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 12),
    _NwIpxFwdIfCacheEntries_Type()
)
nwIpxFwdIfCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCacheEntries.setStatus("mandatory")
_NwIpxFwdIfCacheHits_Type = Counter32
_NwIpxFwdIfCacheHits_Object = MibTableColumn
nwIpxFwdIfCacheHits = _NwIpxFwdIfCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 13),
    _NwIpxFwdIfCacheHits_Type()
)
nwIpxFwdIfCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCacheHits.setStatus("mandatory")
_NwIpxFwdIfCacheMisses_Type = Counter32
_NwIpxFwdIfCacheMisses_Object = MibTableColumn
nwIpxFwdIfCacheMisses = _NwIpxFwdIfCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 14),
    _NwIpxFwdIfCacheMisses_Type()
)
nwIpxFwdIfCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCacheMisses.setStatus("mandatory")
_NwIpxAddressTable_Object = MibTable
nwIpxAddressTable = _NwIpxAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nwIpxAddressTable.setStatus("mandatory")
_NwIpxAddrEntry_Object = MibTableRow
nwIpxAddrEntry = _NwIpxAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 2, 1)
)
nwIpxAddrEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxAddrIfIndex"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxAddrIfAddress"),
)
if mibBuilder.loadTexts:
    nwIpxAddrEntry.setStatus("mandatory")
_NwIpxAddrIfIndex_Type = Integer32
_NwIpxAddrIfIndex_Object = MibTableColumn
nwIpxAddrIfIndex = _NwIpxAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 2, 1, 1),
    _NwIpxAddrIfIndex_Type()
)
nwIpxAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxAddrIfIndex.setStatus("mandatory")
_NwIpxAddrIfAddress_Type = IpxAddress
_NwIpxAddrIfAddress_Object = MibTableColumn
nwIpxAddrIfAddress = _NwIpxAddrIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 2, 1, 2),
    _NwIpxAddrIfAddress_Type()
)
nwIpxAddrIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxAddrIfAddress.setStatus("mandatory")


class _NwIpxAddrIfControl_Type(Integer32):
    """Custom type nwIpxAddrIfControl based on Integer32"""
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


_NwIpxAddrIfControl_Type.__name__ = "Integer32"
_NwIpxAddrIfControl_Object = MibTableColumn
nwIpxAddrIfControl = _NwIpxAddrIfControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 2, 1, 3),
    _NwIpxAddrIfControl_Type()
)
nwIpxAddrIfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAddrIfControl.setStatus("mandatory")


class _NwIpxAddrIfAddrType_Type(Integer32):
    """Custom type nwIpxAddrIfAddrType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_NwIpxAddrIfAddrType_Type.__name__ = "Integer32"
_NwIpxAddrIfAddrType_Object = MibTableColumn
nwIpxAddrIfAddrType = _NwIpxAddrIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 2, 1, 4),
    _NwIpxAddrIfAddrType_Type()
)
nwIpxAddrIfAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAddrIfAddrType.setStatus("mandatory")
_NwIpxFwdIfCounters_ObjectIdentity = ObjectIdentity
nwIpxFwdIfCounters = _NwIpxFwdIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2)
)
_NwIpxFwdIfCtrTable_Object = MibTable
nwIpxFwdIfCtrTable = _NwIpxFwdIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrTable.setStatus("mandatory")
_NwIpxFwdIfCtrEntry_Object = MibTableRow
nwIpxFwdIfCtrEntry = _NwIpxFwdIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1)
)
nwIpxFwdIfCtrEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxFwdIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrEntry.setStatus("mandatory")
_NwIpxFwdIfCtrIfIndex_Type = Integer32
_NwIpxFwdIfCtrIfIndex_Object = MibTableColumn
nwIpxFwdIfCtrIfIndex = _NwIpxFwdIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1),
    _NwIpxFwdIfCtrIfIndex_Type()
)
nwIpxFwdIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrIfIndex.setStatus("mandatory")


class _NwIpxFwdIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxFwdIfCtrAdminStatus based on Integer32"""
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


_NwIpxFwdIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxFwdIfCtrAdminStatus_Object = MibTableColumn
nwIpxFwdIfCtrAdminStatus = _NwIpxFwdIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 2),
    _NwIpxFwdIfCtrAdminStatus_Type()
)
nwIpxFwdIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrAdminStatus.setStatus("mandatory")


class _NwIpxFwdIfCtrReset_Type(Integer32):
    """Custom type nwIpxFwdIfCtrReset based on Integer32"""
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


_NwIpxFwdIfCtrReset_Type.__name__ = "Integer32"
_NwIpxFwdIfCtrReset_Object = MibTableColumn
nwIpxFwdIfCtrReset = _NwIpxFwdIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 3),
    _NwIpxFwdIfCtrReset_Type()
)
nwIpxFwdIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrReset.setStatus("mandatory")
_NwIpxFwdIfCtrOperationalTime_Type = TimeTicks
_NwIpxFwdIfCtrOperationalTime_Object = MibTableColumn
nwIpxFwdIfCtrOperationalTime = _NwIpxFwdIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 4),
    _NwIpxFwdIfCtrOperationalTime_Type()
)
nwIpxFwdIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrOperationalTime.setStatus("mandatory")
_NwIpxFwdIfCtrInPkts_Type = Counter32
_NwIpxFwdIfCtrInPkts_Object = MibTableColumn
nwIpxFwdIfCtrInPkts = _NwIpxFwdIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 5),
    _NwIpxFwdIfCtrInPkts_Type()
)
nwIpxFwdIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrInPkts.setStatus("mandatory")
_NwIpxFwdIfCtrOutPkts_Type = Counter32
_NwIpxFwdIfCtrOutPkts_Object = MibTableColumn
nwIpxFwdIfCtrOutPkts = _NwIpxFwdIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 6),
    _NwIpxFwdIfCtrOutPkts_Type()
)
nwIpxFwdIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrOutPkts.setStatus("mandatory")
_NwIpxFwdIfCtrFwdPkts_Type = Counter32
_NwIpxFwdIfCtrFwdPkts_Object = MibTableColumn
nwIpxFwdIfCtrFwdPkts = _NwIpxFwdIfCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 7),
    _NwIpxFwdIfCtrFwdPkts_Type()
)
nwIpxFwdIfCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrFwdPkts.setStatus("mandatory")
_NwIpxFwdIfCtrFilteredPkts_Type = Counter32
_NwIpxFwdIfCtrFilteredPkts_Object = MibTableColumn
nwIpxFwdIfCtrFilteredPkts = _NwIpxFwdIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 8),
    _NwIpxFwdIfCtrFilteredPkts_Type()
)
nwIpxFwdIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrFilteredPkts.setStatus("mandatory")
_NwIpxFwdIfCtrDiscardPkts_Type = Counter32
_NwIpxFwdIfCtrDiscardPkts_Object = MibTableColumn
nwIpxFwdIfCtrDiscardPkts = _NwIpxFwdIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 9),
    _NwIpxFwdIfCtrDiscardPkts_Type()
)
nwIpxFwdIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrDiscardPkts.setStatus("mandatory")
_NwIpxFwdIfCtrAddrErrPkts_Type = Counter32
_NwIpxFwdIfCtrAddrErrPkts_Object = MibTableColumn
nwIpxFwdIfCtrAddrErrPkts = _NwIpxFwdIfCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 10),
    _NwIpxFwdIfCtrAddrErrPkts_Type()
)
nwIpxFwdIfCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrAddrErrPkts.setStatus("mandatory")
_NwIpxFwdIfCtrLenErrPkts_Type = Counter32
_NwIpxFwdIfCtrLenErrPkts_Object = MibTableColumn
nwIpxFwdIfCtrLenErrPkts = _NwIpxFwdIfCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 11),
    _NwIpxFwdIfCtrLenErrPkts_Type()
)
nwIpxFwdIfCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrLenErrPkts.setStatus("mandatory")
_NwIpxFwdIfCtrHdrErrPkts_Type = Counter32
_NwIpxFwdIfCtrHdrErrPkts_Object = MibTableColumn
nwIpxFwdIfCtrHdrErrPkts = _NwIpxFwdIfCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 12),
    _NwIpxFwdIfCtrHdrErrPkts_Type()
)
nwIpxFwdIfCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrHdrErrPkts.setStatus("mandatory")
_NwIpxFwdIfCtrInBytes_Type = Counter32
_NwIpxFwdIfCtrInBytes_Object = MibTableColumn
nwIpxFwdIfCtrInBytes = _NwIpxFwdIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 13),
    _NwIpxFwdIfCtrInBytes_Type()
)
nwIpxFwdIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrInBytes.setStatus("mandatory")
_NwIpxFwdIfCtrOutBytes_Type = Counter32
_NwIpxFwdIfCtrOutBytes_Object = MibTableColumn
nwIpxFwdIfCtrOutBytes = _NwIpxFwdIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 14),
    _NwIpxFwdIfCtrOutBytes_Type()
)
nwIpxFwdIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrOutBytes.setStatus("mandatory")
_NwIpxFwdIfCtrFwdBytes_Type = Counter32
_NwIpxFwdIfCtrFwdBytes_Object = MibTableColumn
nwIpxFwdIfCtrFwdBytes = _NwIpxFwdIfCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 15),
    _NwIpxFwdIfCtrFwdBytes_Type()
)
nwIpxFwdIfCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrFwdBytes.setStatus("mandatory")
_NwIpxFwdIfCtrFilteredBytes_Type = Counter32
_NwIpxFwdIfCtrFilteredBytes_Object = MibTableColumn
nwIpxFwdIfCtrFilteredBytes = _NwIpxFwdIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 16),
    _NwIpxFwdIfCtrFilteredBytes_Type()
)
nwIpxFwdIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrFilteredBytes.setStatus("mandatory")
_NwIpxFwdIfCtrDiscardBytes_Type = Counter32
_NwIpxFwdIfCtrDiscardBytes_Object = MibTableColumn
nwIpxFwdIfCtrDiscardBytes = _NwIpxFwdIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 17),
    _NwIpxFwdIfCtrDiscardBytes_Type()
)
nwIpxFwdIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrDiscardBytes.setStatus("mandatory")
_NwIpxFwdIfCtrHostInPkts_Type = Counter32
_NwIpxFwdIfCtrHostInPkts_Object = MibTableColumn
nwIpxFwdIfCtrHostInPkts = _NwIpxFwdIfCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 18),
    _NwIpxFwdIfCtrHostInPkts_Type()
)
nwIpxFwdIfCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrHostInPkts.setStatus("mandatory")
_NwIpxFwdIfCtrHostOutPkts_Type = Counter32
_NwIpxFwdIfCtrHostOutPkts_Object = MibTableColumn
nwIpxFwdIfCtrHostOutPkts = _NwIpxFwdIfCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 19),
    _NwIpxFwdIfCtrHostOutPkts_Type()
)
nwIpxFwdIfCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrHostOutPkts.setStatus("mandatory")
_NwIpxFwdIfCtrHostDiscardPkts_Type = Counter32
_NwIpxFwdIfCtrHostDiscardPkts_Object = MibTableColumn
nwIpxFwdIfCtrHostDiscardPkts = _NwIpxFwdIfCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 20),
    _NwIpxFwdIfCtrHostDiscardPkts_Type()
)
nwIpxFwdIfCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrHostDiscardPkts.setStatus("mandatory")
_NwIpxFwdIfCtrHostInBytes_Type = Counter32
_NwIpxFwdIfCtrHostInBytes_Object = MibTableColumn
nwIpxFwdIfCtrHostInBytes = _NwIpxFwdIfCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 21),
    _NwIpxFwdIfCtrHostInBytes_Type()
)
nwIpxFwdIfCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrHostInBytes.setStatus("mandatory")
_NwIpxFwdIfCtrHostOutBytes_Type = Counter32
_NwIpxFwdIfCtrHostOutBytes_Object = MibTableColumn
nwIpxFwdIfCtrHostOutBytes = _NwIpxFwdIfCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 22),
    _NwIpxFwdIfCtrHostOutBytes_Type()
)
nwIpxFwdIfCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrHostOutBytes.setStatus("mandatory")
_NwIpxFwdIfCtrHostDiscardBytes_Type = Counter32
_NwIpxFwdIfCtrHostDiscardBytes_Object = MibTableColumn
nwIpxFwdIfCtrHostDiscardBytes = _NwIpxFwdIfCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 23),
    _NwIpxFwdIfCtrHostDiscardBytes_Type()
)
nwIpxFwdIfCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFwdIfCtrHostDiscardBytes.setStatus("mandatory")
_NwIpxTopology_ObjectIdentity = ObjectIdentity
nwIpxTopology = _NwIpxTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4)
)
_NwIpxDistanceVector_ObjectIdentity = ObjectIdentity
nwIpxDistanceVector = _NwIpxDistanceVector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1)
)
_NwIpxRip_ObjectIdentity = ObjectIdentity
nwIpxRip = _NwIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1)
)
_NwIpxRipSystem_ObjectIdentity = ObjectIdentity
nwIpxRipSystem = _NwIpxRipSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1)
)
_NwIpxRipConfig_ObjectIdentity = ObjectIdentity
nwIpxRipConfig = _NwIpxRipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1)
)


class _NwIpxRipAdminStatus_Type(Integer32):
    """Custom type nwIpxRipAdminStatus based on Integer32"""
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


_NwIpxRipAdminStatus_Type.__name__ = "Integer32"
_NwIpxRipAdminStatus_Object = MibScalar
nwIpxRipAdminStatus = _NwIpxRipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 1),
    _NwIpxRipAdminStatus_Type()
)
nwIpxRipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipAdminStatus.setStatus("mandatory")


class _NwIpxRipOperStatus_Type(Integer32):
    """Custom type nwIpxRipOperStatus based on Integer32"""
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


_NwIpxRipOperStatus_Type.__name__ = "Integer32"
_NwIpxRipOperStatus_Object = MibScalar
nwIpxRipOperStatus = _NwIpxRipOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 2),
    _NwIpxRipOperStatus_Type()
)
nwIpxRipOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipOperStatus.setStatus("mandatory")


class _NwIpxRipAdminReset_Type(Integer32):
    """Custom type nwIpxRipAdminReset based on Integer32"""
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


_NwIpxRipAdminReset_Type.__name__ = "Integer32"
_NwIpxRipAdminReset_Object = MibScalar
nwIpxRipAdminReset = _NwIpxRipAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 3),
    _NwIpxRipAdminReset_Type()
)
nwIpxRipAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipAdminReset.setStatus("mandatory")
_NwIpxRipOperationalTime_Type = TimeTicks
_NwIpxRipOperationalTime_Object = MibScalar
nwIpxRipOperationalTime = _NwIpxRipOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 4),
    _NwIpxRipOperationalTime_Type()
)
nwIpxRipOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipOperationalTime.setStatus("mandatory")
_NwIpxRipVersion_Type = DisplayString
_NwIpxRipVersion_Object = MibScalar
nwIpxRipVersion = _NwIpxRipVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 5),
    _NwIpxRipVersion_Type()
)
nwIpxRipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipVersion.setStatus("mandatory")


class _NwIpxRipStackSize_Type(Integer32):
    """Custom type nwIpxRipStackSize based on Integer32"""
    defaultValue = 4096


_NwIpxRipStackSize_Object = MibScalar
nwIpxRipStackSize = _NwIpxRipStackSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 6),
    _NwIpxRipStackSize_Type()
)
nwIpxRipStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipStackSize.setStatus("mandatory")


class _NwIpxRipThreadPriority_Type(Integer32):
    """Custom type nwIpxRipThreadPriority based on Integer32"""
    defaultValue = 127


_NwIpxRipThreadPriority_Object = MibScalar
nwIpxRipThreadPriority = _NwIpxRipThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 7),
    _NwIpxRipThreadPriority_Type()
)
nwIpxRipThreadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipThreadPriority.setStatus("mandatory")


class _NwIpxRipDatabaseThreshold_Type(Integer32):
    """Custom type nwIpxRipDatabaseThreshold based on Integer32"""
    defaultValue = 2000


_NwIpxRipDatabaseThreshold_Object = MibScalar
nwIpxRipDatabaseThreshold = _NwIpxRipDatabaseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 8),
    _NwIpxRipDatabaseThreshold_Type()
)
nwIpxRipDatabaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipDatabaseThreshold.setStatus("mandatory")


class _NwIpxRipAgeOut_Type(Integer32):
    """Custom type nwIpxRipAgeOut based on Integer32"""
    defaultValue = 180


_NwIpxRipAgeOut_Object = MibScalar
nwIpxRipAgeOut = _NwIpxRipAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 9),
    _NwIpxRipAgeOut_Type()
)
nwIpxRipAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipAgeOut.setStatus("mandatory")


class _NwIpxRipHoldDown_Type(Integer32):
    """Custom type nwIpxRipHoldDown based on Integer32"""
    defaultValue = 120


_NwIpxRipHoldDown_Object = MibScalar
nwIpxRipHoldDown = _NwIpxRipHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 1, 10),
    _NwIpxRipHoldDown_Type()
)
nwIpxRipHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipHoldDown.setStatus("mandatory")
_NwIpxRipCounters_ObjectIdentity = ObjectIdentity
nwIpxRipCounters = _NwIpxRipCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2)
)


class _NwIpxRipCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxRipCtrAdminStatus based on Integer32"""
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


_NwIpxRipCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxRipCtrAdminStatus_Object = MibScalar
nwIpxRipCtrAdminStatus = _NwIpxRipCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 1),
    _NwIpxRipCtrAdminStatus_Type()
)
nwIpxRipCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipCtrAdminStatus.setStatus("mandatory")


class _NwIpxRipCtrReset_Type(Integer32):
    """Custom type nwIpxRipCtrReset based on Integer32"""
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


_NwIpxRipCtrReset_Type.__name__ = "Integer32"
_NwIpxRipCtrReset_Object = MibScalar
nwIpxRipCtrReset = _NwIpxRipCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 2),
    _NwIpxRipCtrReset_Type()
)
nwIpxRipCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipCtrReset.setStatus("mandatory")
_NwIpxRipCtrOperationalTime_Type = TimeTicks
_NwIpxRipCtrOperationalTime_Object = MibScalar
nwIpxRipCtrOperationalTime = _NwIpxRipCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 3),
    _NwIpxRipCtrOperationalTime_Type()
)
nwIpxRipCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrOperationalTime.setStatus("mandatory")
_NwIpxRipCtrInPkts_Type = Counter32
_NwIpxRipCtrInPkts_Object = MibScalar
nwIpxRipCtrInPkts = _NwIpxRipCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 4),
    _NwIpxRipCtrInPkts_Type()
)
nwIpxRipCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrInPkts.setStatus("mandatory")
_NwIpxRipCtrOutPkts_Type = Counter32
_NwIpxRipCtrOutPkts_Object = MibScalar
nwIpxRipCtrOutPkts = _NwIpxRipCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 5),
    _NwIpxRipCtrOutPkts_Type()
)
nwIpxRipCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrOutPkts.setStatus("mandatory")
_NwIpxRipCtrFilteredPkts_Type = Counter32
_NwIpxRipCtrFilteredPkts_Object = MibScalar
nwIpxRipCtrFilteredPkts = _NwIpxRipCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 6),
    _NwIpxRipCtrFilteredPkts_Type()
)
nwIpxRipCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrFilteredPkts.setStatus("mandatory")
_NwIpxRipCtrDiscardPkts_Type = Counter32
_NwIpxRipCtrDiscardPkts_Object = MibScalar
nwIpxRipCtrDiscardPkts = _NwIpxRipCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 7),
    _NwIpxRipCtrDiscardPkts_Type()
)
nwIpxRipCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrDiscardPkts.setStatus("mandatory")
_NwIpxRipCtrInBytes_Type = Counter32
_NwIpxRipCtrInBytes_Object = MibScalar
nwIpxRipCtrInBytes = _NwIpxRipCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 8),
    _NwIpxRipCtrInBytes_Type()
)
nwIpxRipCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrInBytes.setStatus("mandatory")
_NwIpxRipCtrOutBytes_Type = Counter32
_NwIpxRipCtrOutBytes_Object = MibScalar
nwIpxRipCtrOutBytes = _NwIpxRipCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 9),
    _NwIpxRipCtrOutBytes_Type()
)
nwIpxRipCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrOutBytes.setStatus("mandatory")
_NwIpxRipCtrFilteredBytes_Type = Counter32
_NwIpxRipCtrFilteredBytes_Object = MibScalar
nwIpxRipCtrFilteredBytes = _NwIpxRipCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 10),
    _NwIpxRipCtrFilteredBytes_Type()
)
nwIpxRipCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrFilteredBytes.setStatus("mandatory")
_NwIpxRipCtrDiscardBytes_Type = Counter32
_NwIpxRipCtrDiscardBytes_Object = MibScalar
nwIpxRipCtrDiscardBytes = _NwIpxRipCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 11),
    _NwIpxRipCtrDiscardBytes_Type()
)
nwIpxRipCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipCtrDiscardBytes.setStatus("mandatory")
_NwIpxRipInterfaces_ObjectIdentity = ObjectIdentity
nwIpxRipInterfaces = _NwIpxRipInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2)
)
_NwIpxRipIfConfig_ObjectIdentity = ObjectIdentity
nwIpxRipIfConfig = _NwIpxRipIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1)
)
_NwIpxRipIfTable_Object = MibTable
nwIpxRipIfTable = _NwIpxRipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpxRipIfTable.setStatus("mandatory")
_NwIpxRipIfEntry_Object = MibTableRow
nwIpxRipIfEntry = _NwIpxRipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1)
)
nwIpxRipIfEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxRipIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxRipIfEntry.setStatus("mandatory")
_NwIpxRipIfIndex_Type = Integer32
_NwIpxRipIfIndex_Object = MibTableColumn
nwIpxRipIfIndex = _NwIpxRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 1),
    _NwIpxRipIfIndex_Type()
)
nwIpxRipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfIndex.setStatus("mandatory")


class _NwIpxRipIfAdminStatus_Type(Integer32):
    """Custom type nwIpxRipIfAdminStatus based on Integer32"""
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


_NwIpxRipIfAdminStatus_Type.__name__ = "Integer32"
_NwIpxRipIfAdminStatus_Object = MibTableColumn
nwIpxRipIfAdminStatus = _NwIpxRipIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 2),
    _NwIpxRipIfAdminStatus_Type()
)
nwIpxRipIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfAdminStatus.setStatus("mandatory")


class _NwIpxRipIfOperStatus_Type(Integer32):
    """Custom type nwIpxRipIfOperStatus based on Integer32"""
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


_NwIpxRipIfOperStatus_Type.__name__ = "Integer32"
_NwIpxRipIfOperStatus_Object = MibTableColumn
nwIpxRipIfOperStatus = _NwIpxRipIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 3),
    _NwIpxRipIfOperStatus_Type()
)
nwIpxRipIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfOperStatus.setStatus("mandatory")
_NwIpxRipIfOperationalTime_Type = TimeTicks
_NwIpxRipIfOperationalTime_Object = MibTableColumn
nwIpxRipIfOperationalTime = _NwIpxRipIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 4),
    _NwIpxRipIfOperationalTime_Type()
)
nwIpxRipIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfOperationalTime.setStatus("mandatory")


class _NwIpxRipIfVersion_Type(Integer32):
    """Custom type nwIpxRipIfVersion based on Integer32"""
    defaultValue = 1


_NwIpxRipIfVersion_Object = MibTableColumn
nwIpxRipIfVersion = _NwIpxRipIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 5),
    _NwIpxRipIfVersion_Type()
)
nwIpxRipIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfVersion.setStatus("mandatory")


class _NwIpxRipIfAdvertisement_Type(Integer32):
    """Custom type nwIpxRipIfAdvertisement based on Integer32"""
    defaultValue = 60


_NwIpxRipIfAdvertisement_Object = MibTableColumn
nwIpxRipIfAdvertisement = _NwIpxRipIfAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 6),
    _NwIpxRipIfAdvertisement_Type()
)
nwIpxRipIfAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfAdvertisement.setStatus("mandatory")


class _NwIpxRipIfFloodDelay_Type(Integer32):
    """Custom type nwIpxRipIfFloodDelay based on Integer32"""
    defaultValue = 2


_NwIpxRipIfFloodDelay_Object = MibTableColumn
nwIpxRipIfFloodDelay = _NwIpxRipIfFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 7),
    _NwIpxRipIfFloodDelay_Type()
)
nwIpxRipIfFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfFloodDelay.setStatus("mandatory")


class _NwIpxRipIfRequestDelay_Type(Integer32):
    """Custom type nwIpxRipIfRequestDelay based on Integer32"""
    defaultValue = 6


_NwIpxRipIfRequestDelay_Object = MibTableColumn
nwIpxRipIfRequestDelay = _NwIpxRipIfRequestDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 8),
    _NwIpxRipIfRequestDelay_Type()
)
nwIpxRipIfRequestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfRequestDelay.setStatus("mandatory")


class _NwIpxRipIfPriority_Type(Integer32):
    """Custom type nwIpxRipIfPriority based on Integer32"""
    defaultValue = 1


_NwIpxRipIfPriority_Object = MibTableColumn
nwIpxRipIfPriority = _NwIpxRipIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 9),
    _NwIpxRipIfPriority_Type()
)
nwIpxRipIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfPriority.setStatus("mandatory")


class _NwIpxRipIfHelloTimer_Type(Integer32):
    """Custom type nwIpxRipIfHelloTimer based on Integer32"""
    defaultValue = 10


_NwIpxRipIfHelloTimer_Object = MibTableColumn
nwIpxRipIfHelloTimer = _NwIpxRipIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 10),
    _NwIpxRipIfHelloTimer_Type()
)
nwIpxRipIfHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfHelloTimer.setStatus("mandatory")


class _NwIpxRipIfSplitHorizon_Type(Integer32):
    """Custom type nwIpxRipIfSplitHorizon based on Integer32"""
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


_NwIpxRipIfSplitHorizon_Type.__name__ = "Integer32"
_NwIpxRipIfSplitHorizon_Object = MibTableColumn
nwIpxRipIfSplitHorizon = _NwIpxRipIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 11),
    _NwIpxRipIfSplitHorizon_Type()
)
nwIpxRipIfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfSplitHorizon.setStatus("mandatory")


class _NwIpxRipIfPoisonReverse_Type(Integer32):
    """Custom type nwIpxRipIfPoisonReverse based on Integer32"""
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


_NwIpxRipIfPoisonReverse_Type.__name__ = "Integer32"
_NwIpxRipIfPoisonReverse_Object = MibTableColumn
nwIpxRipIfPoisonReverse = _NwIpxRipIfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 12),
    _NwIpxRipIfPoisonReverse_Type()
)
nwIpxRipIfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfPoisonReverse.setStatus("mandatory")


class _NwIpxRipIfSnooping_Type(Integer32):
    """Custom type nwIpxRipIfSnooping based on Integer32"""
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


_NwIpxRipIfSnooping_Type.__name__ = "Integer32"
_NwIpxRipIfSnooping_Object = MibTableColumn
nwIpxRipIfSnooping = _NwIpxRipIfSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 13),
    _NwIpxRipIfSnooping_Type()
)
nwIpxRipIfSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfSnooping.setStatus("mandatory")


class _NwIpxRipIfType_Type(Integer32):
    """Custom type nwIpxRipIfType based on Integer32"""
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


_NwIpxRipIfType_Type.__name__ = "Integer32"
_NwIpxRipIfType_Object = MibTableColumn
nwIpxRipIfType = _NwIpxRipIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 14),
    _NwIpxRipIfType_Type()
)
nwIpxRipIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfType.setStatus("mandatory")


class _NwIpxRipIfXmitCost_Type(Integer32):
    """Custom type nwIpxRipIfXmitCost based on Integer32"""
    defaultValue = 0


_NwIpxRipIfXmitCost_Object = MibTableColumn
nwIpxRipIfXmitCost = _NwIpxRipIfXmitCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 15),
    _NwIpxRipIfXmitCost_Type()
)
nwIpxRipIfXmitCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfXmitCost.setStatus("mandatory")


class _NwIpxRipIfAclIdentifier_Type(Integer32):
    """Custom type nwIpxRipIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwIpxRipIfAclIdentifier_Object = MibTableColumn
nwIpxRipIfAclIdentifier = _NwIpxRipIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 16),
    _NwIpxRipIfAclIdentifier_Type()
)
nwIpxRipIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfAclIdentifier.setStatus("mandatory")


class _NwIpxRipIfAclStatus_Type(Integer32):
    """Custom type nwIpxRipIfAclStatus based on Integer32"""
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


_NwIpxRipIfAclStatus_Type.__name__ = "Integer32"
_NwIpxRipIfAclStatus_Object = MibTableColumn
nwIpxRipIfAclStatus = _NwIpxRipIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 1, 1, 1, 17),
    _NwIpxRipIfAclStatus_Type()
)
nwIpxRipIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfAclStatus.setStatus("mandatory")
_NwIpxRipIfCounters_ObjectIdentity = ObjectIdentity
nwIpxRipIfCounters = _NwIpxRipIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2)
)
_NwIpxRipIfCtrTable_Object = MibTable
nwIpxRipIfCtrTable = _NwIpxRipIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpxRipIfCtrTable.setStatus("mandatory")
_NwIpxRipIfCtrEntry_Object = MibTableRow
nwIpxRipIfCtrEntry = _NwIpxRipIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1)
)
nwIpxRipIfCtrEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxRipIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxRipIfCtrEntry.setStatus("mandatory")
_NwIpxRipIfCtrIfIndex_Type = Integer32
_NwIpxRipIfCtrIfIndex_Object = MibTableColumn
nwIpxRipIfCtrIfIndex = _NwIpxRipIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 1),
    _NwIpxRipIfCtrIfIndex_Type()
)
nwIpxRipIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrIfIndex.setStatus("mandatory")


class _NwIpxRipIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxRipIfCtrAdminStatus based on Integer32"""
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


_NwIpxRipIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxRipIfCtrAdminStatus_Object = MibTableColumn
nwIpxRipIfCtrAdminStatus = _NwIpxRipIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 2),
    _NwIpxRipIfCtrAdminStatus_Type()
)
nwIpxRipIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrAdminStatus.setStatus("mandatory")


class _NwIpxRipIfCtrReset_Type(Integer32):
    """Custom type nwIpxRipIfCtrReset based on Integer32"""
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


_NwIpxRipIfCtrReset_Type.__name__ = "Integer32"
_NwIpxRipIfCtrReset_Object = MibTableColumn
nwIpxRipIfCtrReset = _NwIpxRipIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 3),
    _NwIpxRipIfCtrReset_Type()
)
nwIpxRipIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrReset.setStatus("mandatory")
_NwIpxRipIfCtrOperationalTime_Type = TimeTicks
_NwIpxRipIfCtrOperationalTime_Object = MibTableColumn
nwIpxRipIfCtrOperationalTime = _NwIpxRipIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 4),
    _NwIpxRipIfCtrOperationalTime_Type()
)
nwIpxRipIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrOperationalTime.setStatus("mandatory")
_NwIpxRipIfCtrInPkts_Type = Counter32
_NwIpxRipIfCtrInPkts_Object = MibTableColumn
nwIpxRipIfCtrInPkts = _NwIpxRipIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 5),
    _NwIpxRipIfCtrInPkts_Type()
)
nwIpxRipIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrInPkts.setStatus("mandatory")
_NwIpxRipIfCtrOutPkts_Type = Counter32
_NwIpxRipIfCtrOutPkts_Object = MibTableColumn
nwIpxRipIfCtrOutPkts = _NwIpxRipIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 6),
    _NwIpxRipIfCtrOutPkts_Type()
)
nwIpxRipIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrOutPkts.setStatus("mandatory")
_NwIpxRipIfCtrFilteredPkts_Type = Counter32
_NwIpxRipIfCtrFilteredPkts_Object = MibTableColumn
nwIpxRipIfCtrFilteredPkts = _NwIpxRipIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 7),
    _NwIpxRipIfCtrFilteredPkts_Type()
)
nwIpxRipIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrFilteredPkts.setStatus("mandatory")
_NwIpxRipIfCtrDiscardPkts_Type = Counter32
_NwIpxRipIfCtrDiscardPkts_Object = MibTableColumn
nwIpxRipIfCtrDiscardPkts = _NwIpxRipIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 8),
    _NwIpxRipIfCtrDiscardPkts_Type()
)
nwIpxRipIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrDiscardPkts.setStatus("mandatory")
_NwIpxRipIfCtrInBytes_Type = Counter32
_NwIpxRipIfCtrInBytes_Object = MibTableColumn
nwIpxRipIfCtrInBytes = _NwIpxRipIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 9),
    _NwIpxRipIfCtrInBytes_Type()
)
nwIpxRipIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrInBytes.setStatus("mandatory")
_NwIpxRipIfCtrOutBytes_Type = Counter32
_NwIpxRipIfCtrOutBytes_Object = MibTableColumn
nwIpxRipIfCtrOutBytes = _NwIpxRipIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 10),
    _NwIpxRipIfCtrOutBytes_Type()
)
nwIpxRipIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrOutBytes.setStatus("mandatory")
_NwIpxRipIfCtrFilteredBytes_Type = Counter32
_NwIpxRipIfCtrFilteredBytes_Object = MibTableColumn
nwIpxRipIfCtrFilteredBytes = _NwIpxRipIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 11),
    _NwIpxRipIfCtrFilteredBytes_Type()
)
nwIpxRipIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrFilteredBytes.setStatus("mandatory")
_NwIpxRipIfCtrDiscardBytes_Type = Counter32
_NwIpxRipIfCtrDiscardBytes_Object = MibTableColumn
nwIpxRipIfCtrDiscardBytes = _NwIpxRipIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 2, 2, 1, 1, 12),
    _NwIpxRipIfCtrDiscardBytes_Type()
)
nwIpxRipIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipIfCtrDiscardBytes.setStatus("mandatory")
_NwIpxRipDatabase_ObjectIdentity = ObjectIdentity
nwIpxRipDatabase = _NwIpxRipDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3)
)
_NwIpxRipRouteTable_Object = MibTable
nwIpxRipRouteTable = _NwIpxRipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nwIpxRipRouteTable.setStatus("mandatory")
_NwIpxRipRouteEntry_Object = MibTableRow
nwIpxRipRouteEntry = _NwIpxRipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1)
)
nwIpxRipRouteEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxRipRtNetId"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxRipRtIfIndex"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxRipRtSrcNode"),
)
if mibBuilder.loadTexts:
    nwIpxRipRouteEntry.setStatus("mandatory")
_NwIpxRipRtNetId_Type = IpxAddress
_NwIpxRipRtNetId_Object = MibTableColumn
nwIpxRipRtNetId = _NwIpxRipRtNetId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 1),
    _NwIpxRipRtNetId_Type()
)
nwIpxRipRtNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtNetId.setStatus("mandatory")
_NwIpxRipRtIfIndex_Type = Integer32
_NwIpxRipRtIfIndex_Object = MibTableColumn
nwIpxRipRtIfIndex = _NwIpxRipRtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 2),
    _NwIpxRipRtIfIndex_Type()
)
nwIpxRipRtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtIfIndex.setStatus("mandatory")
_NwIpxRipRtSrcNode_Type = IpxAddress
_NwIpxRipRtSrcNode_Object = MibTableColumn
nwIpxRipRtSrcNode = _NwIpxRipRtSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 3),
    _NwIpxRipRtSrcNode_Type()
)
nwIpxRipRtSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtSrcNode.setStatus("mandatory")
_NwIpxRipRtHops_Type = Integer32
_NwIpxRipRtHops_Object = MibTableColumn
nwIpxRipRtHops = _NwIpxRipRtHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 4),
    _NwIpxRipRtHops_Type()
)
nwIpxRipRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtHops.setStatus("mandatory")
_NwIpxRipRtTicks_Type = Integer32
_NwIpxRipRtTicks_Object = MibTableColumn
nwIpxRipRtTicks = _NwIpxRipRtTicks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 5),
    _NwIpxRipRtTicks_Type()
)
nwIpxRipRtTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtTicks.setStatus("mandatory")
_NwIpxRipRtAge_Type = Integer32
_NwIpxRipRtAge_Object = MibTableColumn
nwIpxRipRtAge = _NwIpxRipRtAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 6),
    _NwIpxRipRtAge_Type()
)
nwIpxRipRtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtAge.setStatus("mandatory")


class _NwIpxRipRtType_Type(Integer32):
    """Custom type nwIpxRipRtType based on Integer32"""
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


_NwIpxRipRtType_Type.__name__ = "Integer32"
_NwIpxRipRtType_Object = MibTableColumn
nwIpxRipRtType = _NwIpxRipRtType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 7),
    _NwIpxRipRtType_Type()
)
nwIpxRipRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtType.setStatus("mandatory")
_NwIpxRipRtFlags_Type = Integer32
_NwIpxRipRtFlags_Object = MibTableColumn
nwIpxRipRtFlags = _NwIpxRipRtFlags_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 3, 1, 1, 8),
    _NwIpxRipRtFlags_Type()
)
nwIpxRipRtFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxRipRtFlags.setStatus("mandatory")
_NwIpxRipFilters_ObjectIdentity = ObjectIdentity
nwIpxRipFilters = _NwIpxRipFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 4)
)
_NwIpxSap_ObjectIdentity = ObjectIdentity
nwIpxSap = _NwIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2)
)
_NwIpxSapSystem_ObjectIdentity = ObjectIdentity
nwIpxSapSystem = _NwIpxSapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1)
)
_NwIpxSapConfig_ObjectIdentity = ObjectIdentity
nwIpxSapConfig = _NwIpxSapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1)
)


class _NwIpxSapAdminStatus_Type(Integer32):
    """Custom type nwIpxSapAdminStatus based on Integer32"""
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


_NwIpxSapAdminStatus_Type.__name__ = "Integer32"
_NwIpxSapAdminStatus_Object = MibScalar
nwIpxSapAdminStatus = _NwIpxSapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 1),
    _NwIpxSapAdminStatus_Type()
)
nwIpxSapAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapAdminStatus.setStatus("mandatory")


class _NwIpxSapOperStatus_Type(Integer32):
    """Custom type nwIpxSapOperStatus based on Integer32"""
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


_NwIpxSapOperStatus_Type.__name__ = "Integer32"
_NwIpxSapOperStatus_Object = MibScalar
nwIpxSapOperStatus = _NwIpxSapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 2),
    _NwIpxSapOperStatus_Type()
)
nwIpxSapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapOperStatus.setStatus("mandatory")


class _NwIpxSapAdminReset_Type(Integer32):
    """Custom type nwIpxSapAdminReset based on Integer32"""
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


_NwIpxSapAdminReset_Type.__name__ = "Integer32"
_NwIpxSapAdminReset_Object = MibScalar
nwIpxSapAdminReset = _NwIpxSapAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 3),
    _NwIpxSapAdminReset_Type()
)
nwIpxSapAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapAdminReset.setStatus("mandatory")
_NwIpxSapOperationalTime_Type = TimeTicks
_NwIpxSapOperationalTime_Object = MibScalar
nwIpxSapOperationalTime = _NwIpxSapOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 4),
    _NwIpxSapOperationalTime_Type()
)
nwIpxSapOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapOperationalTime.setStatus("mandatory")
_NwIpxSapVersion_Type = DisplayString
_NwIpxSapVersion_Object = MibScalar
nwIpxSapVersion = _NwIpxSapVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 5),
    _NwIpxSapVersion_Type()
)
nwIpxSapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapVersion.setStatus("mandatory")


class _NwIpxSapStackSize_Type(Integer32):
    """Custom type nwIpxSapStackSize based on Integer32"""
    defaultValue = 4096


_NwIpxSapStackSize_Object = MibScalar
nwIpxSapStackSize = _NwIpxSapStackSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 6),
    _NwIpxSapStackSize_Type()
)
nwIpxSapStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapStackSize.setStatus("mandatory")


class _NwIpxSapThreadPriority_Type(Integer32):
    """Custom type nwIpxSapThreadPriority based on Integer32"""
    defaultValue = 127


_NwIpxSapThreadPriority_Object = MibScalar
nwIpxSapThreadPriority = _NwIpxSapThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 7),
    _NwIpxSapThreadPriority_Type()
)
nwIpxSapThreadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapThreadPriority.setStatus("mandatory")


class _NwIpxSapDatabaseThreshold_Type(Integer32):
    """Custom type nwIpxSapDatabaseThreshold based on Integer32"""
    defaultValue = 2000


_NwIpxSapDatabaseThreshold_Object = MibScalar
nwIpxSapDatabaseThreshold = _NwIpxSapDatabaseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 8),
    _NwIpxSapDatabaseThreshold_Type()
)
nwIpxSapDatabaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapDatabaseThreshold.setStatus("mandatory")


class _NwIpxSapAgeOut_Type(Integer32):
    """Custom type nwIpxSapAgeOut based on Integer32"""
    defaultValue = 180


_NwIpxSapAgeOut_Object = MibScalar
nwIpxSapAgeOut = _NwIpxSapAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 9),
    _NwIpxSapAgeOut_Type()
)
nwIpxSapAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapAgeOut.setStatus("mandatory")


class _NwIpxSapHoldDown_Type(Integer32):
    """Custom type nwIpxSapHoldDown based on Integer32"""
    defaultValue = 120


_NwIpxSapHoldDown_Object = MibScalar
nwIpxSapHoldDown = _NwIpxSapHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 1, 10),
    _NwIpxSapHoldDown_Type()
)
nwIpxSapHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapHoldDown.setStatus("mandatory")
_NwIpxSapCounters_ObjectIdentity = ObjectIdentity
nwIpxSapCounters = _NwIpxSapCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2)
)


class _NwIpxSapCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxSapCtrAdminStatus based on Integer32"""
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


_NwIpxSapCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxSapCtrAdminStatus_Object = MibScalar
nwIpxSapCtrAdminStatus = _NwIpxSapCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 1),
    _NwIpxSapCtrAdminStatus_Type()
)
nwIpxSapCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapCtrAdminStatus.setStatus("mandatory")


class _NwIpxSapCtrReset_Type(Integer32):
    """Custom type nwIpxSapCtrReset based on Integer32"""
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


_NwIpxSapCtrReset_Type.__name__ = "Integer32"
_NwIpxSapCtrReset_Object = MibScalar
nwIpxSapCtrReset = _NwIpxSapCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 2),
    _NwIpxSapCtrReset_Type()
)
nwIpxSapCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapCtrReset.setStatus("mandatory")
_NwIpxSapCtrOperationalTime_Type = TimeTicks
_NwIpxSapCtrOperationalTime_Object = MibScalar
nwIpxSapCtrOperationalTime = _NwIpxSapCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 3),
    _NwIpxSapCtrOperationalTime_Type()
)
nwIpxSapCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrOperationalTime.setStatus("mandatory")
_NwIpxSapCtrInPkts_Type = Counter32
_NwIpxSapCtrInPkts_Object = MibScalar
nwIpxSapCtrInPkts = _NwIpxSapCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 4),
    _NwIpxSapCtrInPkts_Type()
)
nwIpxSapCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrInPkts.setStatus("mandatory")
_NwIpxSapCtrOutPkts_Type = Counter32
_NwIpxSapCtrOutPkts_Object = MibScalar
nwIpxSapCtrOutPkts = _NwIpxSapCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 5),
    _NwIpxSapCtrOutPkts_Type()
)
nwIpxSapCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrOutPkts.setStatus("mandatory")
_NwIpxSapCtrFilteredPkts_Type = Counter32
_NwIpxSapCtrFilteredPkts_Object = MibScalar
nwIpxSapCtrFilteredPkts = _NwIpxSapCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 6),
    _NwIpxSapCtrFilteredPkts_Type()
)
nwIpxSapCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrFilteredPkts.setStatus("mandatory")
_NwIpxSapCtrDiscardPkts_Type = Counter32
_NwIpxSapCtrDiscardPkts_Object = MibScalar
nwIpxSapCtrDiscardPkts = _NwIpxSapCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 7),
    _NwIpxSapCtrDiscardPkts_Type()
)
nwIpxSapCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrDiscardPkts.setStatus("mandatory")
_NwIpxSapCtrInBytes_Type = Counter32
_NwIpxSapCtrInBytes_Object = MibScalar
nwIpxSapCtrInBytes = _NwIpxSapCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 8),
    _NwIpxSapCtrInBytes_Type()
)
nwIpxSapCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrInBytes.setStatus("mandatory")
_NwIpxSapCtrOutBytes_Type = Counter32
_NwIpxSapCtrOutBytes_Object = MibScalar
nwIpxSapCtrOutBytes = _NwIpxSapCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 9),
    _NwIpxSapCtrOutBytes_Type()
)
nwIpxSapCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrOutBytes.setStatus("mandatory")
_NwIpxSapCtrFilteredBytes_Type = Counter32
_NwIpxSapCtrFilteredBytes_Object = MibScalar
nwIpxSapCtrFilteredBytes = _NwIpxSapCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 10),
    _NwIpxSapCtrFilteredBytes_Type()
)
nwIpxSapCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrFilteredBytes.setStatus("mandatory")
_NwIpxSapCtrDiscardBytes_Type = Counter32
_NwIpxSapCtrDiscardBytes_Object = MibScalar
nwIpxSapCtrDiscardBytes = _NwIpxSapCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 1, 2, 11),
    _NwIpxSapCtrDiscardBytes_Type()
)
nwIpxSapCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapCtrDiscardBytes.setStatus("mandatory")
_NwIpxSapInterfaces_ObjectIdentity = ObjectIdentity
nwIpxSapInterfaces = _NwIpxSapInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2)
)
_NwIpxSapIfConfig_ObjectIdentity = ObjectIdentity
nwIpxSapIfConfig = _NwIpxSapIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1)
)
_NwIpxSapIfTable_Object = MibTable
nwIpxSapIfTable = _NwIpxSapIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpxSapIfTable.setStatus("mandatory")
_NwIpxSapIfEntry_Object = MibTableRow
nwIpxSapIfEntry = _NwIpxSapIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1)
)
nwIpxSapIfEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxSapIfEntry.setStatus("mandatory")
_NwIpxSapIfIndex_Type = Integer32
_NwIpxSapIfIndex_Object = MibTableColumn
nwIpxSapIfIndex = _NwIpxSapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 1),
    _NwIpxSapIfIndex_Type()
)
nwIpxSapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfIndex.setStatus("mandatory")


class _NwIpxSapIfAdminStatus_Type(Integer32):
    """Custom type nwIpxSapIfAdminStatus based on Integer32"""
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


_NwIpxSapIfAdminStatus_Type.__name__ = "Integer32"
_NwIpxSapIfAdminStatus_Object = MibTableColumn
nwIpxSapIfAdminStatus = _NwIpxSapIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 2),
    _NwIpxSapIfAdminStatus_Type()
)
nwIpxSapIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfAdminStatus.setStatus("mandatory")


class _NwIpxSapIfOperStatus_Type(Integer32):
    """Custom type nwIpxSapIfOperStatus based on Integer32"""
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


_NwIpxSapIfOperStatus_Type.__name__ = "Integer32"
_NwIpxSapIfOperStatus_Object = MibTableColumn
nwIpxSapIfOperStatus = _NwIpxSapIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 3),
    _NwIpxSapIfOperStatus_Type()
)
nwIpxSapIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfOperStatus.setStatus("mandatory")
_NwIpxSapIfOperationalTime_Type = TimeTicks
_NwIpxSapIfOperationalTime_Object = MibTableColumn
nwIpxSapIfOperationalTime = _NwIpxSapIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 4),
    _NwIpxSapIfOperationalTime_Type()
)
nwIpxSapIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfOperationalTime.setStatus("mandatory")


class _NwIpxSapIfVersion_Type(Integer32):
    """Custom type nwIpxSapIfVersion based on Integer32"""
    defaultValue = 1


_NwIpxSapIfVersion_Object = MibTableColumn
nwIpxSapIfVersion = _NwIpxSapIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 5),
    _NwIpxSapIfVersion_Type()
)
nwIpxSapIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfVersion.setStatus("mandatory")


class _NwIpxSapIfAdvertisement_Type(Integer32):
    """Custom type nwIpxSapIfAdvertisement based on Integer32"""
    defaultValue = 60


_NwIpxSapIfAdvertisement_Object = MibTableColumn
nwIpxSapIfAdvertisement = _NwIpxSapIfAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 6),
    _NwIpxSapIfAdvertisement_Type()
)
nwIpxSapIfAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfAdvertisement.setStatus("mandatory")


class _NwIpxSapIfFloodDelay_Type(Integer32):
    """Custom type nwIpxSapIfFloodDelay based on Integer32"""
    defaultValue = 2


_NwIpxSapIfFloodDelay_Object = MibTableColumn
nwIpxSapIfFloodDelay = _NwIpxSapIfFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 7),
    _NwIpxSapIfFloodDelay_Type()
)
nwIpxSapIfFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfFloodDelay.setStatus("mandatory")


class _NwIpxSapIfRequestDelay_Type(Integer32):
    """Custom type nwIpxSapIfRequestDelay based on Integer32"""
    defaultValue = 0


_NwIpxSapIfRequestDelay_Object = MibTableColumn
nwIpxSapIfRequestDelay = _NwIpxSapIfRequestDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 8),
    _NwIpxSapIfRequestDelay_Type()
)
nwIpxSapIfRequestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfRequestDelay.setStatus("mandatory")


class _NwIpxSapIfPriority_Type(Integer32):
    """Custom type nwIpxSapIfPriority based on Integer32"""
    defaultValue = 1


_NwIpxSapIfPriority_Object = MibTableColumn
nwIpxSapIfPriority = _NwIpxSapIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 9),
    _NwIpxSapIfPriority_Type()
)
nwIpxSapIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfPriority.setStatus("mandatory")


class _NwIpxSapIfHelloTimer_Type(Integer32):
    """Custom type nwIpxSapIfHelloTimer based on Integer32"""
    defaultValue = 10


_NwIpxSapIfHelloTimer_Object = MibTableColumn
nwIpxSapIfHelloTimer = _NwIpxSapIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 10),
    _NwIpxSapIfHelloTimer_Type()
)
nwIpxSapIfHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfHelloTimer.setStatus("mandatory")


class _NwIpxSapIfSplitHorizon_Type(Integer32):
    """Custom type nwIpxSapIfSplitHorizon based on Integer32"""
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


_NwIpxSapIfSplitHorizon_Type.__name__ = "Integer32"
_NwIpxSapIfSplitHorizon_Object = MibTableColumn
nwIpxSapIfSplitHorizon = _NwIpxSapIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 11),
    _NwIpxSapIfSplitHorizon_Type()
)
nwIpxSapIfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfSplitHorizon.setStatus("mandatory")


class _NwIpxSapIfPoisonReverse_Type(Integer32):
    """Custom type nwIpxSapIfPoisonReverse based on Integer32"""
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


_NwIpxSapIfPoisonReverse_Type.__name__ = "Integer32"
_NwIpxSapIfPoisonReverse_Object = MibTableColumn
nwIpxSapIfPoisonReverse = _NwIpxSapIfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 12),
    _NwIpxSapIfPoisonReverse_Type()
)
nwIpxSapIfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfPoisonReverse.setStatus("mandatory")


class _NwIpxSapIfSnooping_Type(Integer32):
    """Custom type nwIpxSapIfSnooping based on Integer32"""
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


_NwIpxSapIfSnooping_Type.__name__ = "Integer32"
_NwIpxSapIfSnooping_Object = MibTableColumn
nwIpxSapIfSnooping = _NwIpxSapIfSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 13),
    _NwIpxSapIfSnooping_Type()
)
nwIpxSapIfSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfSnooping.setStatus("mandatory")


class _NwIpxSapIfType_Type(Integer32):
    """Custom type nwIpxSapIfType based on Integer32"""
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


_NwIpxSapIfType_Type.__name__ = "Integer32"
_NwIpxSapIfType_Object = MibTableColumn
nwIpxSapIfType = _NwIpxSapIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 14),
    _NwIpxSapIfType_Type()
)
nwIpxSapIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfType.setStatus("mandatory")


class _NwIpxSapIfXmitCost_Type(Integer32):
    """Custom type nwIpxSapIfXmitCost based on Integer32"""
    defaultValue = 0


_NwIpxSapIfXmitCost_Object = MibTableColumn
nwIpxSapIfXmitCost = _NwIpxSapIfXmitCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 15),
    _NwIpxSapIfXmitCost_Type()
)
nwIpxSapIfXmitCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfXmitCost.setStatus("mandatory")


class _NwIpxSapIfAclIdentifier_Type(Integer32):
    """Custom type nwIpxSapIfAclIdentifier based on Integer32"""
    defaultValue = 0


_NwIpxSapIfAclIdentifier_Object = MibTableColumn
nwIpxSapIfAclIdentifier = _NwIpxSapIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 16),
    _NwIpxSapIfAclIdentifier_Type()
)
nwIpxSapIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfAclIdentifier.setStatus("mandatory")


class _NwIpxSapIfAclStatus_Type(Integer32):
    """Custom type nwIpxSapIfAclStatus based on Integer32"""
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


_NwIpxSapIfAclStatus_Type.__name__ = "Integer32"
_NwIpxSapIfAclStatus_Object = MibTableColumn
nwIpxSapIfAclStatus = _NwIpxSapIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 1, 1, 1, 17),
    _NwIpxSapIfAclStatus_Type()
)
nwIpxSapIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfAclStatus.setStatus("mandatory")
_NwIpxSapIfCounters_ObjectIdentity = ObjectIdentity
nwIpxSapIfCounters = _NwIpxSapIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2)
)
_NwIpxSapIfCtrTable_Object = MibTable
nwIpxSapIfCtrTable = _NwIpxSapIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpxSapIfCtrTable.setStatus("mandatory")
_NwIpxSapIfCtrEntry_Object = MibTableRow
nwIpxSapIfCtrEntry = _NwIpxSapIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1)
)
nwIpxSapIfCtrEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxSapIfCtrEntry.setStatus("mandatory")
_NwIpxSapIfCtrIfIndex_Type = Integer32
_NwIpxSapIfCtrIfIndex_Object = MibTableColumn
nwIpxSapIfCtrIfIndex = _NwIpxSapIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 1),
    _NwIpxSapIfCtrIfIndex_Type()
)
nwIpxSapIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrIfIndex.setStatus("mandatory")


class _NwIpxSapIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxSapIfCtrAdminStatus based on Integer32"""
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


_NwIpxSapIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxSapIfCtrAdminStatus_Object = MibTableColumn
nwIpxSapIfCtrAdminStatus = _NwIpxSapIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 2),
    _NwIpxSapIfCtrAdminStatus_Type()
)
nwIpxSapIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrAdminStatus.setStatus("mandatory")


class _NwIpxSapIfCtrReset_Type(Integer32):
    """Custom type nwIpxSapIfCtrReset based on Integer32"""
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


_NwIpxSapIfCtrReset_Type.__name__ = "Integer32"
_NwIpxSapIfCtrReset_Object = MibTableColumn
nwIpxSapIfCtrReset = _NwIpxSapIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 3),
    _NwIpxSapIfCtrReset_Type()
)
nwIpxSapIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrReset.setStatus("mandatory")
_NwIpxSapIfCtrOperationalTime_Type = TimeTicks
_NwIpxSapIfCtrOperationalTime_Object = MibTableColumn
nwIpxSapIfCtrOperationalTime = _NwIpxSapIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 4),
    _NwIpxSapIfCtrOperationalTime_Type()
)
nwIpxSapIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrOperationalTime.setStatus("mandatory")
_NwIpxSapIfCtrInPkts_Type = Counter32
_NwIpxSapIfCtrInPkts_Object = MibTableColumn
nwIpxSapIfCtrInPkts = _NwIpxSapIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 5),
    _NwIpxSapIfCtrInPkts_Type()
)
nwIpxSapIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrInPkts.setStatus("mandatory")
_NwIpxSapIfCtrOutPkts_Type = Counter32
_NwIpxSapIfCtrOutPkts_Object = MibTableColumn
nwIpxSapIfCtrOutPkts = _NwIpxSapIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 6),
    _NwIpxSapIfCtrOutPkts_Type()
)
nwIpxSapIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrOutPkts.setStatus("mandatory")
_NwIpxSapIfCtrFilteredPkts_Type = Counter32
_NwIpxSapIfCtrFilteredPkts_Object = MibTableColumn
nwIpxSapIfCtrFilteredPkts = _NwIpxSapIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 7),
    _NwIpxSapIfCtrFilteredPkts_Type()
)
nwIpxSapIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrFilteredPkts.setStatus("mandatory")
_NwIpxSapIfCtrDiscardPkts_Type = Counter32
_NwIpxSapIfCtrDiscardPkts_Object = MibTableColumn
nwIpxSapIfCtrDiscardPkts = _NwIpxSapIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 8),
    _NwIpxSapIfCtrDiscardPkts_Type()
)
nwIpxSapIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrDiscardPkts.setStatus("mandatory")
_NwIpxSapIfCtrInBytes_Type = Counter32
_NwIpxSapIfCtrInBytes_Object = MibTableColumn
nwIpxSapIfCtrInBytes = _NwIpxSapIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 9),
    _NwIpxSapIfCtrInBytes_Type()
)
nwIpxSapIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrInBytes.setStatus("mandatory")
_NwIpxSapIfCtrOutBytes_Type = Counter32
_NwIpxSapIfCtrOutBytes_Object = MibTableColumn
nwIpxSapIfCtrOutBytes = _NwIpxSapIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 10),
    _NwIpxSapIfCtrOutBytes_Type()
)
nwIpxSapIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrOutBytes.setStatus("mandatory")
_NwIpxSapIfCtrFilteredBytes_Type = Counter32
_NwIpxSapIfCtrFilteredBytes_Object = MibTableColumn
nwIpxSapIfCtrFilteredBytes = _NwIpxSapIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 11),
    _NwIpxSapIfCtrFilteredBytes_Type()
)
nwIpxSapIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrFilteredBytes.setStatus("mandatory")
_NwIpxSapIfCtrDiscardBytes_Type = Counter32
_NwIpxSapIfCtrDiscardBytes_Object = MibTableColumn
nwIpxSapIfCtrDiscardBytes = _NwIpxSapIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 2, 2, 1, 1, 12),
    _NwIpxSapIfCtrDiscardBytes_Type()
)
nwIpxSapIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapIfCtrDiscardBytes.setStatus("mandatory")
_NwIpxSapServerTable_ObjectIdentity = ObjectIdentity
nwIpxSapServerTable = _NwIpxSapServerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3)
)
_NwIpxSapServerIfTable_Object = MibTable
nwIpxSapServerIfTable = _NwIpxSapServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nwIpxSapServerIfTable.setStatus("mandatory")
_NwIpxSapServerIfEntry_Object = MibTableRow
nwIpxSapServerIfEntry = _NwIpxSapServerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1)
)
nwIpxSapServerIfEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapServerIfNetId"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapServerIfNode"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapServerIfSocket"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapServerIfServiceType"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapServerIfIfNum"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxSapServerIfSrcNode"),
)
if mibBuilder.loadTexts:
    nwIpxSapServerIfEntry.setStatus("mandatory")
_NwIpxSapServerIfNetId_Type = IpxAddress
_NwIpxSapServerIfNetId_Object = MibTableColumn
nwIpxSapServerIfNetId = _NwIpxSapServerIfNetId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 1),
    _NwIpxSapServerIfNetId_Type()
)
nwIpxSapServerIfNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfNetId.setStatus("mandatory")
_NwIpxSapServerIfNode_Type = OctetString
_NwIpxSapServerIfNode_Object = MibTableColumn
nwIpxSapServerIfNode = _NwIpxSapServerIfNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 2),
    _NwIpxSapServerIfNode_Type()
)
nwIpxSapServerIfNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfNode.setStatus("mandatory")
_NwIpxSapServerIfSocket_Type = OctetString
_NwIpxSapServerIfSocket_Object = MibTableColumn
nwIpxSapServerIfSocket = _NwIpxSapServerIfSocket_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 3),
    _NwIpxSapServerIfSocket_Type()
)
nwIpxSapServerIfSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfSocket.setStatus("mandatory")
_NwIpxSapServerIfServiceType_Type = Integer32
_NwIpxSapServerIfServiceType_Object = MibTableColumn
nwIpxSapServerIfServiceType = _NwIpxSapServerIfServiceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 4),
    _NwIpxSapServerIfServiceType_Type()
)
nwIpxSapServerIfServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfServiceType.setStatus("mandatory")
_NwIpxSapServerIfIfNum_Type = Integer32
_NwIpxSapServerIfIfNum_Object = MibTableColumn
nwIpxSapServerIfIfNum = _NwIpxSapServerIfIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 5),
    _NwIpxSapServerIfIfNum_Type()
)
nwIpxSapServerIfIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfIfNum.setStatus("mandatory")
_NwIpxSapServerIfSrcNode_Type = OctetString
_NwIpxSapServerIfSrcNode_Object = MibTableColumn
nwIpxSapServerIfSrcNode = _NwIpxSapServerIfSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 6),
    _NwIpxSapServerIfSrcNode_Type()
)
nwIpxSapServerIfSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfSrcNode.setStatus("mandatory")
_NwIpxSapServerIfName_Type = OctetString
_NwIpxSapServerIfName_Object = MibTableColumn
nwIpxSapServerIfName = _NwIpxSapServerIfName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 7),
    _NwIpxSapServerIfName_Type()
)
nwIpxSapServerIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfName.setStatus("mandatory")
_NwIpxSapServerIfHops_Type = Integer32
_NwIpxSapServerIfHops_Object = MibTableColumn
nwIpxSapServerIfHops = _NwIpxSapServerIfHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 8),
    _NwIpxSapServerIfHops_Type()
)
nwIpxSapServerIfHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfHops.setStatus("mandatory")
_NwIpxSapServerIfAge_Type = Integer32
_NwIpxSapServerIfAge_Object = MibTableColumn
nwIpxSapServerIfAge = _NwIpxSapServerIfAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 9),
    _NwIpxSapServerIfAge_Type()
)
nwIpxSapServerIfAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfAge.setStatus("mandatory")


class _NwIpxSapServerIfType_Type(Integer32):
    """Custom type nwIpxSapServerIfType based on Integer32"""
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


_NwIpxSapServerIfType_Type.__name__ = "Integer32"
_NwIpxSapServerIfType_Object = MibTableColumn
nwIpxSapServerIfType = _NwIpxSapServerIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 10),
    _NwIpxSapServerIfType_Type()
)
nwIpxSapServerIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfType.setStatus("mandatory")
_NwIpxSapServerIfFlags_Type = Integer32
_NwIpxSapServerIfFlags_Object = MibTableColumn
nwIpxSapServerIfFlags = _NwIpxSapServerIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 3, 1, 1, 11),
    _NwIpxSapServerIfFlags_Type()
)
nwIpxSapServerIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxSapServerIfFlags.setStatus("mandatory")
_NwIpxSapFilters_ObjectIdentity = ObjectIdentity
nwIpxSapFilters = _NwIpxSapFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 1, 2, 4)
)
_NwIpxLinkState_ObjectIdentity = ObjectIdentity
nwIpxLinkState = _NwIpxLinkState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 2)
)
_NwIpxNlsp_ObjectIdentity = ObjectIdentity
nwIpxNlsp = _NwIpxNlsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 4, 2, 1)
)
_NwIpxFib_ObjectIdentity = ObjectIdentity
nwIpxFib = _NwIpxFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5)
)
_NwIpxFibTable_Object = MibTable
nwIpxFibTable = _NwIpxFibTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    nwIpxFibTable.setStatus("mandatory")
_NwIpxFibEntry_Object = MibTableRow
nwIpxFibEntry = _NwIpxFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1)
)
nwIpxFibEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxFibNetId"),
)
if mibBuilder.loadTexts:
    nwIpxFibEntry.setStatus("mandatory")
_NwIpxFibNetId_Type = IpxAddress
_NwIpxFibNetId_Object = MibTableColumn
nwIpxFibNetId = _NwIpxFibNetId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1, 1),
    _NwIpxFibNetId_Type()
)
nwIpxFibNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxFibNetId.setStatus("mandatory")


class _NwIpxFibHops_Type(Integer32):
    """Custom type nwIpxFibHops based on Integer32"""
    defaultValue = 0


_NwIpxFibHops_Object = MibTableColumn
nwIpxFibHops = _NwIpxFibHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1, 2),
    _NwIpxFibHops_Type()
)
nwIpxFibHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFibHops.setStatus("mandatory")


class _NwIpxFibTimeTicks_Type(TimeTicks):
    """Custom type nwIpxFibTimeTicks based on TimeTicks"""
    defaultValue = 0


_NwIpxFibTimeTicks_Object = MibTableColumn
nwIpxFibTimeTicks = _NwIpxFibTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1, 3),
    _NwIpxFibTimeTicks_Type()
)
nwIpxFibTimeTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFibTimeTicks.setStatus("mandatory")
_NwIpxFibNextHopIf_Type = Integer32
_NwIpxFibNextHopIf_Object = MibTableColumn
nwIpxFibNextHopIf = _NwIpxFibNextHopIf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1, 4),
    _NwIpxFibNextHopIf_Type()
)
nwIpxFibNextHopIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFibNextHopIf.setStatus("mandatory")
_NwIpxFibNextHopNet_Type = OctetString
_NwIpxFibNextHopNet_Object = MibTableColumn
nwIpxFibNextHopNet = _NwIpxFibNextHopNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1, 5),
    _NwIpxFibNextHopNet_Type()
)
nwIpxFibNextHopNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFibNextHopNet.setStatus("mandatory")
_NwIpxFibNextHopNode_Type = MacAddress
_NwIpxFibNextHopNode_Object = MibTableColumn
nwIpxFibNextHopNode = _NwIpxFibNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1, 6),
    _NwIpxFibNextHopNode_Type()
)
nwIpxFibNextHopNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFibNextHopNode.setStatus("mandatory")


class _NwIpxFibRouteType_Type(Integer32):
    """Custom type nwIpxFibRouteType based on Integer32"""
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


_NwIpxFibRouteType_Type.__name__ = "Integer32"
_NwIpxFibRouteType_Object = MibTableColumn
nwIpxFibRouteType = _NwIpxFibRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 5, 1, 1, 7),
    _NwIpxFibRouteType_Type()
)
nwIpxFibRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxFibRouteType.setStatus("mandatory")
_NwIpxEndSystems_ObjectIdentity = ObjectIdentity
nwIpxEndSystems = _NwIpxEndSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6)
)
_NwIpxHostsSystem_ObjectIdentity = ObjectIdentity
nwIpxHostsSystem = _NwIpxHostsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 1)
)
_NwIpxHostsInterfaces_ObjectIdentity = ObjectIdentity
nwIpxHostsInterfaces = _NwIpxHostsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 2)
)
_NwIpxHostsToMedia_ObjectIdentity = ObjectIdentity
nwIpxHostsToMedia = _NwIpxHostsToMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3)
)
_NwIpxHostMapTable_Object = MibTable
nwIpxHostMapTable = _NwIpxHostMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    nwIpxHostMapTable.setStatus("mandatory")
_NwIpxHostMapEntry_Object = MibTableRow
nwIpxHostMapEntry = _NwIpxHostMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1)
)
nwIpxHostMapEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxHostMapIfIndex"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxHostMapIpxAddr"),
)
if mibBuilder.loadTexts:
    nwIpxHostMapEntry.setStatus("mandatory")
_NwIpxHostMapIfIndex_Type = Integer32
_NwIpxHostMapIfIndex_Object = MibTableColumn
nwIpxHostMapIfIndex = _NwIpxHostMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1, 1),
    _NwIpxHostMapIfIndex_Type()
)
nwIpxHostMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxHostMapIfIndex.setStatus("mandatory")
_NwIpxHostMapIpxAddr_Type = IpxAddress
_NwIpxHostMapIpxAddr_Object = MibTableColumn
nwIpxHostMapIpxAddr = _NwIpxHostMapIpxAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1, 2),
    _NwIpxHostMapIpxAddr_Type()
)
nwIpxHostMapIpxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxHostMapIpxAddr.setStatus("mandatory")
_NwIpxHostMapPhysAddr_Type = PhysAddress
_NwIpxHostMapPhysAddr_Object = MibTableColumn
nwIpxHostMapPhysAddr = _NwIpxHostMapPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1, 3),
    _NwIpxHostMapPhysAddr_Type()
)
nwIpxHostMapPhysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxHostMapPhysAddr.setStatus("mandatory")


class _NwIpxHostMapType_Type(Integer32):
    """Custom type nwIpxHostMapType based on Integer32"""
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


_NwIpxHostMapType_Type.__name__ = "Integer32"
_NwIpxHostMapType_Object = MibTableColumn
nwIpxHostMapType = _NwIpxHostMapType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1, 4),
    _NwIpxHostMapType_Type()
)
nwIpxHostMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxHostMapType.setStatus("mandatory")
_NwIpxHostMapCircuitID_Type = Integer32
_NwIpxHostMapCircuitID_Object = MibTableColumn
nwIpxHostMapCircuitID = _NwIpxHostMapCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1, 5),
    _NwIpxHostMapCircuitID_Type()
)
nwIpxHostMapCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxHostMapCircuitID.setStatus("mandatory")


class _NwIpxHostMapFraming_Type(Integer32):
    """Custom type nwIpxHostMapFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 17),
          ("encapenet", 9),
          ("encapenet8022", 10),
          ("encapenetnovell", 12),
          ("encapenetsnap", 11),
          ("encapfddi8022", 15),
          ("encapfddisnap", 16),
          ("encaptr8022", 13),
          ("encaptrsnap", 14),
          ("ethernet", 2),
          ("i8022", 4),
          ("nativewan", 8),
          ("novell", 6),
          ("other", 1),
          ("snap", 3))
    )


_NwIpxHostMapFraming_Type.__name__ = "Integer32"
_NwIpxHostMapFraming_Object = MibTableColumn
nwIpxHostMapFraming = _NwIpxHostMapFraming_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1, 6),
    _NwIpxHostMapFraming_Type()
)
nwIpxHostMapFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxHostMapFraming.setStatus("mandatory")
_NwIpxHostMapPortNumber_Type = Integer32
_NwIpxHostMapPortNumber_Object = MibTableColumn
nwIpxHostMapPortNumber = _NwIpxHostMapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 6, 3, 1, 1, 7),
    _NwIpxHostMapPortNumber_Type()
)
nwIpxHostMapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxHostMapPortNumber.setStatus("mandatory")
_NwIpxAccessControl_ObjectIdentity = ObjectIdentity
nwIpxAccessControl = _NwIpxAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7)
)
_NwIpxAclValidEntries_Type = Gauge32
_NwIpxAclValidEntries_Object = MibScalar
nwIpxAclValidEntries = _NwIpxAclValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 1),
    _NwIpxAclValidEntries_Type()
)
nwIpxAclValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxAclValidEntries.setStatus("mandatory")
_NwIpxAclTable_Object = MibTable
nwIpxAclTable = _NwIpxAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    nwIpxAclTable.setStatus("mandatory")
_NwIpxAclEntry_Object = MibTableRow
nwIpxAclEntry = _NwIpxAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1)
)
nwIpxAclEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxAclIdentifier"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxAclSequence"),
)
if mibBuilder.loadTexts:
    nwIpxAclEntry.setStatus("mandatory")
_NwIpxAclIdentifier_Type = Integer32
_NwIpxAclIdentifier_Object = MibTableColumn
nwIpxAclIdentifier = _NwIpxAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 1),
    _NwIpxAclIdentifier_Type()
)
nwIpxAclIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxAclIdentifier.setStatus("mandatory")
_NwIpxAclSequence_Type = Integer32
_NwIpxAclSequence_Object = MibTableColumn
nwIpxAclSequence = _NwIpxAclSequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 2),
    _NwIpxAclSequence_Type()
)
nwIpxAclSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxAclSequence.setStatus("mandatory")


class _NwIpxAclPermission_Type(Integer32):
    """Custom type nwIpxAclPermission based on Integer32"""
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


_NwIpxAclPermission_Type.__name__ = "Integer32"
_NwIpxAclPermission_Object = MibTableColumn
nwIpxAclPermission = _NwIpxAclPermission_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 3),
    _NwIpxAclPermission_Type()
)
nwIpxAclPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAclPermission.setStatus("mandatory")
_NwIpxAclMatches_Type = Counter32
_NwIpxAclMatches_Object = MibTableColumn
nwIpxAclMatches = _NwIpxAclMatches_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 4),
    _NwIpxAclMatches_Type()
)
nwIpxAclMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxAclMatches.setStatus("mandatory")
_NwIpxAclDestNetNum_Type = OctetString
_NwIpxAclDestNetNum_Object = MibTableColumn
nwIpxAclDestNetNum = _NwIpxAclDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 5),
    _NwIpxAclDestNetNum_Type()
)
nwIpxAclDestNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAclDestNetNum.setStatus("mandatory")
_NwIpxAclDestNode_Type = OctetString
_NwIpxAclDestNode_Object = MibTableColumn
nwIpxAclDestNode = _NwIpxAclDestNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 6),
    _NwIpxAclDestNode_Type()
)
nwIpxAclDestNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAclDestNode.setStatus("mandatory")
_NwIpxAclDestSocket_Type = OctetString
_NwIpxAclDestSocket_Object = MibTableColumn
nwIpxAclDestSocket = _NwIpxAclDestSocket_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 7),
    _NwIpxAclDestSocket_Type()
)
nwIpxAclDestSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAclDestSocket.setStatus("mandatory")
_NwIpxAclSrcNetNum_Type = OctetString
_NwIpxAclSrcNetNum_Object = MibTableColumn
nwIpxAclSrcNetNum = _NwIpxAclSrcNetNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 8),
    _NwIpxAclSrcNetNum_Type()
)
nwIpxAclSrcNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAclSrcNetNum.setStatus("mandatory")
_NwIpxAclSrcNode_Type = OctetString
_NwIpxAclSrcNode_Object = MibTableColumn
nwIpxAclSrcNode = _NwIpxAclSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 9),
    _NwIpxAclSrcNode_Type()
)
nwIpxAclSrcNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAclSrcNode.setStatus("mandatory")
_NwIpxAclSrcSocket_Type = OctetString
_NwIpxAclSrcSocket_Object = MibTableColumn
nwIpxAclSrcSocket = _NwIpxAclSrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 7, 2, 1, 10),
    _NwIpxAclSrcSocket_Type()
)
nwIpxAclSrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxAclSrcSocket.setStatus("mandatory")
_NwIpxFilters_ObjectIdentity = ObjectIdentity
nwIpxFilters = _NwIpxFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 8)
)
_NwIpxRedirector_ObjectIdentity = ObjectIdentity
nwIpxRedirector = _NwIpxRedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9)
)
_NwIpxNetBIOS_ObjectIdentity = ObjectIdentity
nwIpxNetBIOS = _NwIpxNetBIOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1)
)
_NwIpxNetBIOSSystem_ObjectIdentity = ObjectIdentity
nwIpxNetBIOSSystem = _NwIpxNetBIOSSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1)
)
_NwIpxNetBIOSConfig_ObjectIdentity = ObjectIdentity
nwIpxNetBIOSConfig = _NwIpxNetBIOSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 1)
)


class _NwIpxNetBIOSAdminStatus_Type(Integer32):
    """Custom type nwIpxNetBIOSAdminStatus based on Integer32"""
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


_NwIpxNetBIOSAdminStatus_Type.__name__ = "Integer32"
_NwIpxNetBIOSAdminStatus_Object = MibScalar
nwIpxNetBIOSAdminStatus = _NwIpxNetBIOSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 1, 1),
    _NwIpxNetBIOSAdminStatus_Type()
)
nwIpxNetBIOSAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSAdminStatus.setStatus("mandatory")


class _NwIpxNetBIOSOperStatus_Type(Integer32):
    """Custom type nwIpxNetBIOSOperStatus based on Integer32"""
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


_NwIpxNetBIOSOperStatus_Type.__name__ = "Integer32"
_NwIpxNetBIOSOperStatus_Object = MibScalar
nwIpxNetBIOSOperStatus = _NwIpxNetBIOSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 1, 2),
    _NwIpxNetBIOSOperStatus_Type()
)
nwIpxNetBIOSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSOperStatus.setStatus("mandatory")


class _NwIpxNetBIOSAdminReset_Type(Integer32):
    """Custom type nwIpxNetBIOSAdminReset based on Integer32"""
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


_NwIpxNetBIOSAdminReset_Type.__name__ = "Integer32"
_NwIpxNetBIOSAdminReset_Object = MibScalar
nwIpxNetBIOSAdminReset = _NwIpxNetBIOSAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 1, 3),
    _NwIpxNetBIOSAdminReset_Type()
)
nwIpxNetBIOSAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSAdminReset.setStatus("mandatory")
_NwIpxNetBIOSOperationalTime_Type = TimeTicks
_NwIpxNetBIOSOperationalTime_Object = MibScalar
nwIpxNetBIOSOperationalTime = _NwIpxNetBIOSOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 1, 4),
    _NwIpxNetBIOSOperationalTime_Type()
)
nwIpxNetBIOSOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSOperationalTime.setStatus("mandatory")
_NwIpxNetBIOSVersion_Type = DisplayString
_NwIpxNetBIOSVersion_Object = MibScalar
nwIpxNetBIOSVersion = _NwIpxNetBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 1, 5),
    _NwIpxNetBIOSVersion_Type()
)
nwIpxNetBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSVersion.setStatus("mandatory")
_NwIpxNetBIOSCounters_ObjectIdentity = ObjectIdentity
nwIpxNetBIOSCounters = _NwIpxNetBIOSCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2)
)


class _NwIpxNetBIOSCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxNetBIOSCtrAdminStatus based on Integer32"""
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


_NwIpxNetBIOSCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxNetBIOSCtrAdminStatus_Object = MibScalar
nwIpxNetBIOSCtrAdminStatus = _NwIpxNetBIOSCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 1),
    _NwIpxNetBIOSCtrAdminStatus_Type()
)
nwIpxNetBIOSCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrAdminStatus.setStatus("mandatory")


class _NwIpxNetBIOSCtrReset_Type(Integer32):
    """Custom type nwIpxNetBIOSCtrReset based on Integer32"""
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


_NwIpxNetBIOSCtrReset_Type.__name__ = "Integer32"
_NwIpxNetBIOSCtrReset_Object = MibScalar
nwIpxNetBIOSCtrReset = _NwIpxNetBIOSCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 2),
    _NwIpxNetBIOSCtrReset_Type()
)
nwIpxNetBIOSCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrReset.setStatus("mandatory")
_NwIpxNetBIOSCtrOperationalTime_Type = TimeTicks
_NwIpxNetBIOSCtrOperationalTime_Object = MibScalar
nwIpxNetBIOSCtrOperationalTime = _NwIpxNetBIOSCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 3),
    _NwIpxNetBIOSCtrOperationalTime_Type()
)
nwIpxNetBIOSCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrOperationalTime.setStatus("mandatory")
_NwIpxNetBIOSCtrInPkts_Type = Counter32
_NwIpxNetBIOSCtrInPkts_Object = MibScalar
nwIpxNetBIOSCtrInPkts = _NwIpxNetBIOSCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 4),
    _NwIpxNetBIOSCtrInPkts_Type()
)
nwIpxNetBIOSCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrInPkts.setStatus("mandatory")
_NwIpxNetBIOSCtrOutPkts_Type = Counter32
_NwIpxNetBIOSCtrOutPkts_Object = MibScalar
nwIpxNetBIOSCtrOutPkts = _NwIpxNetBIOSCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 5),
    _NwIpxNetBIOSCtrOutPkts_Type()
)
nwIpxNetBIOSCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrOutPkts.setStatus("mandatory")
_NwIpxNetBIOSCtrFilteredPkts_Type = Counter32
_NwIpxNetBIOSCtrFilteredPkts_Object = MibScalar
nwIpxNetBIOSCtrFilteredPkts = _NwIpxNetBIOSCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 6),
    _NwIpxNetBIOSCtrFilteredPkts_Type()
)
nwIpxNetBIOSCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrFilteredPkts.setStatus("mandatory")
_NwIpxNetBIOSCtrDiscardPkts_Type = Counter32
_NwIpxNetBIOSCtrDiscardPkts_Object = MibScalar
nwIpxNetBIOSCtrDiscardPkts = _NwIpxNetBIOSCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 7),
    _NwIpxNetBIOSCtrDiscardPkts_Type()
)
nwIpxNetBIOSCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrDiscardPkts.setStatus("mandatory")
_NwIpxNetBIOSCtrInBytes_Type = Counter32
_NwIpxNetBIOSCtrInBytes_Object = MibScalar
nwIpxNetBIOSCtrInBytes = _NwIpxNetBIOSCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 8),
    _NwIpxNetBIOSCtrInBytes_Type()
)
nwIpxNetBIOSCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrInBytes.setStatus("mandatory")
_NwIpxNetBIOSCtrOutBytes_Type = Counter32
_NwIpxNetBIOSCtrOutBytes_Object = MibScalar
nwIpxNetBIOSCtrOutBytes = _NwIpxNetBIOSCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 9),
    _NwIpxNetBIOSCtrOutBytes_Type()
)
nwIpxNetBIOSCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrOutBytes.setStatus("mandatory")
_NwIpxNetBIOSCtrFilteredBytes_Type = Counter32
_NwIpxNetBIOSCtrFilteredBytes_Object = MibScalar
nwIpxNetBIOSCtrFilteredBytes = _NwIpxNetBIOSCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 10),
    _NwIpxNetBIOSCtrFilteredBytes_Type()
)
nwIpxNetBIOSCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrFilteredBytes.setStatus("mandatory")
_NwIpxNetBIOSCtrDiscardBytes_Type = Counter32
_NwIpxNetBIOSCtrDiscardBytes_Object = MibScalar
nwIpxNetBIOSCtrDiscardBytes = _NwIpxNetBIOSCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 1, 2, 11),
    _NwIpxNetBIOSCtrDiscardBytes_Type()
)
nwIpxNetBIOSCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSCtrDiscardBytes.setStatus("mandatory")
_NwIpxNetBIOSInterface_ObjectIdentity = ObjectIdentity
nwIpxNetBIOSInterface = _NwIpxNetBIOSInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2)
)
_NwIpxNetBIOSIfConfig_ObjectIdentity = ObjectIdentity
nwIpxNetBIOSIfConfig = _NwIpxNetBIOSIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 1)
)
_NwIpxNetBIOSIfTable_Object = MibTable
nwIpxNetBIOSIfTable = _NwIpxNetBIOSIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfTable.setStatus("mandatory")
_NwIpxNetBIOSIfEntry_Object = MibTableRow
nwIpxNetBIOSIfEntry = _NwIpxNetBIOSIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 1, 1, 1)
)
nwIpxNetBIOSIfEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxNetBIOSIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfEntry.setStatus("mandatory")
_NwIpxNetBIOSIfIndex_Type = Integer32
_NwIpxNetBIOSIfIndex_Object = MibTableColumn
nwIpxNetBIOSIfIndex = _NwIpxNetBIOSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 1, 1, 1, 1),
    _NwIpxNetBIOSIfIndex_Type()
)
nwIpxNetBIOSIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfIndex.setStatus("mandatory")


class _NwIpxNetBIOSIfAdminStatus_Type(Integer32):
    """Custom type nwIpxNetBIOSIfAdminStatus based on Integer32"""
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


_NwIpxNetBIOSIfAdminStatus_Type.__name__ = "Integer32"
_NwIpxNetBIOSIfAdminStatus_Object = MibTableColumn
nwIpxNetBIOSIfAdminStatus = _NwIpxNetBIOSIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 1, 1, 1, 2),
    _NwIpxNetBIOSIfAdminStatus_Type()
)
nwIpxNetBIOSIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfAdminStatus.setStatus("mandatory")


class _NwIpxNetBIOSIfOperStatus_Type(Integer32):
    """Custom type nwIpxNetBIOSIfOperStatus based on Integer32"""
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


_NwIpxNetBIOSIfOperStatus_Type.__name__ = "Integer32"
_NwIpxNetBIOSIfOperStatus_Object = MibTableColumn
nwIpxNetBIOSIfOperStatus = _NwIpxNetBIOSIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 1, 1, 1, 3),
    _NwIpxNetBIOSIfOperStatus_Type()
)
nwIpxNetBIOSIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfOperStatus.setStatus("mandatory")
_NwIpxNetBIOSIfOperationalTime_Type = TimeTicks
_NwIpxNetBIOSIfOperationalTime_Object = MibTableColumn
nwIpxNetBIOSIfOperationalTime = _NwIpxNetBIOSIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 1, 1, 1, 4),
    _NwIpxNetBIOSIfOperationalTime_Type()
)
nwIpxNetBIOSIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfOperationalTime.setStatus("mandatory")
_NwIpxNetBIOSIfCounters_ObjectIdentity = ObjectIdentity
nwIpxNetBIOSIfCounters = _NwIpxNetBIOSIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2)
)
_NwIpxNetBIOSIfCtrTable_Object = MibTable
nwIpxNetBIOSIfCtrTable = _NwIpxNetBIOSIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrTable.setStatus("mandatory")
_NwIpxNetBIOSIfCtrEntry_Object = MibTableRow
nwIpxNetBIOSIfCtrEntry = _NwIpxNetBIOSIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1)
)
nwIpxNetBIOSIfCtrEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxNetBIOSIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrEntry.setStatus("mandatory")
_NwIpxNetBIOSIfCtrIfIndex_Type = Integer32
_NwIpxNetBIOSIfCtrIfIndex_Object = MibTableColumn
nwIpxNetBIOSIfCtrIfIndex = _NwIpxNetBIOSIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 1),
    _NwIpxNetBIOSIfCtrIfIndex_Type()
)
nwIpxNetBIOSIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrIfIndex.setStatus("mandatory")


class _NwIpxNetBIOSIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxNetBIOSIfCtrAdminStatus based on Integer32"""
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


_NwIpxNetBIOSIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxNetBIOSIfCtrAdminStatus_Object = MibTableColumn
nwIpxNetBIOSIfCtrAdminStatus = _NwIpxNetBIOSIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 2),
    _NwIpxNetBIOSIfCtrAdminStatus_Type()
)
nwIpxNetBIOSIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrAdminStatus.setStatus("mandatory")


class _NwIpxNetBIOSIfCtrReset_Type(Integer32):
    """Custom type nwIpxNetBIOSIfCtrReset based on Integer32"""
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


_NwIpxNetBIOSIfCtrReset_Type.__name__ = "Integer32"
_NwIpxNetBIOSIfCtrReset_Object = MibTableColumn
nwIpxNetBIOSIfCtrReset = _NwIpxNetBIOSIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 3),
    _NwIpxNetBIOSIfCtrReset_Type()
)
nwIpxNetBIOSIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrReset.setStatus("mandatory")
_NwIpxNetBIOSIfCtrOperationalTime_Type = TimeTicks
_NwIpxNetBIOSIfCtrOperationalTime_Object = MibTableColumn
nwIpxNetBIOSIfCtrOperationalTime = _NwIpxNetBIOSIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 4),
    _NwIpxNetBIOSIfCtrOperationalTime_Type()
)
nwIpxNetBIOSIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrOperationalTime.setStatus("mandatory")
_NwIpxNetBIOSIfCtrInPkts_Type = Counter32
_NwIpxNetBIOSIfCtrInPkts_Object = MibTableColumn
nwIpxNetBIOSIfCtrInPkts = _NwIpxNetBIOSIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 5),
    _NwIpxNetBIOSIfCtrInPkts_Type()
)
nwIpxNetBIOSIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrInPkts.setStatus("mandatory")
_NwIpxNetBIOSIfCtrOutPkts_Type = Counter32
_NwIpxNetBIOSIfCtrOutPkts_Object = MibTableColumn
nwIpxNetBIOSIfCtrOutPkts = _NwIpxNetBIOSIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 6),
    _NwIpxNetBIOSIfCtrOutPkts_Type()
)
nwIpxNetBIOSIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrOutPkts.setStatus("mandatory")
_NwIpxNetBIOSIfCtrFilteredPkts_Type = Counter32
_NwIpxNetBIOSIfCtrFilteredPkts_Object = MibTableColumn
nwIpxNetBIOSIfCtrFilteredPkts = _NwIpxNetBIOSIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 7),
    _NwIpxNetBIOSIfCtrFilteredPkts_Type()
)
nwIpxNetBIOSIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrFilteredPkts.setStatus("mandatory")
_NwIpxNetBIOSIfCtrDiscardPkts_Type = Counter32
_NwIpxNetBIOSIfCtrDiscardPkts_Object = MibTableColumn
nwIpxNetBIOSIfCtrDiscardPkts = _NwIpxNetBIOSIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 8),
    _NwIpxNetBIOSIfCtrDiscardPkts_Type()
)
nwIpxNetBIOSIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrDiscardPkts.setStatus("mandatory")
_NwIpxNetBIOSIfCtrInBytes_Type = Counter32
_NwIpxNetBIOSIfCtrInBytes_Object = MibTableColumn
nwIpxNetBIOSIfCtrInBytes = _NwIpxNetBIOSIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 9),
    _NwIpxNetBIOSIfCtrInBytes_Type()
)
nwIpxNetBIOSIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrInBytes.setStatus("mandatory")
_NwIpxNetBIOSIfCtrOutBytes_Type = Counter32
_NwIpxNetBIOSIfCtrOutBytes_Object = MibTableColumn
nwIpxNetBIOSIfCtrOutBytes = _NwIpxNetBIOSIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 10),
    _NwIpxNetBIOSIfCtrOutBytes_Type()
)
nwIpxNetBIOSIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrOutBytes.setStatus("mandatory")
_NwIpxNetBIOSIfCtrFilteredBytes_Type = Counter32
_NwIpxNetBIOSIfCtrFilteredBytes_Object = MibTableColumn
nwIpxNetBIOSIfCtrFilteredBytes = _NwIpxNetBIOSIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 11),
    _NwIpxNetBIOSIfCtrFilteredBytes_Type()
)
nwIpxNetBIOSIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrFilteredBytes.setStatus("mandatory")
_NwIpxNetBIOSIfCtrDiscardBytes_Type = Counter32
_NwIpxNetBIOSIfCtrDiscardBytes_Object = MibTableColumn
nwIpxNetBIOSIfCtrDiscardBytes = _NwIpxNetBIOSIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 1, 2, 2, 1, 1, 12),
    _NwIpxNetBIOSIfCtrDiscardBytes_Type()
)
nwIpxNetBIOSIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxNetBIOSIfCtrDiscardBytes.setStatus("mandatory")
_NwIpxBroadcast_ObjectIdentity = ObjectIdentity
nwIpxBroadcast = _NwIpxBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2)
)
_NwIpxBroadcastSystem_ObjectIdentity = ObjectIdentity
nwIpxBroadcastSystem = _NwIpxBroadcastSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1)
)
_NwIpxBroadcastConfig_ObjectIdentity = ObjectIdentity
nwIpxBroadcastConfig = _NwIpxBroadcastConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 1)
)


class _NwIpxBcastAdminStatus_Type(Integer32):
    """Custom type nwIpxBcastAdminStatus based on Integer32"""
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


_NwIpxBcastAdminStatus_Type.__name__ = "Integer32"
_NwIpxBcastAdminStatus_Object = MibScalar
nwIpxBcastAdminStatus = _NwIpxBcastAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 1, 1),
    _NwIpxBcastAdminStatus_Type()
)
nwIpxBcastAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastAdminStatus.setStatus("mandatory")


class _NwIpxBcastOperStatus_Type(Integer32):
    """Custom type nwIpxBcastOperStatus based on Integer32"""
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


_NwIpxBcastOperStatus_Type.__name__ = "Integer32"
_NwIpxBcastOperStatus_Object = MibScalar
nwIpxBcastOperStatus = _NwIpxBcastOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 1, 2),
    _NwIpxBcastOperStatus_Type()
)
nwIpxBcastOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastOperStatus.setStatus("mandatory")


class _NwIpxBcastAdminReset_Type(Integer32):
    """Custom type nwIpxBcastAdminReset based on Integer32"""
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


_NwIpxBcastAdminReset_Type.__name__ = "Integer32"
_NwIpxBcastAdminReset_Object = MibScalar
nwIpxBcastAdminReset = _NwIpxBcastAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 1, 3),
    _NwIpxBcastAdminReset_Type()
)
nwIpxBcastAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastAdminReset.setStatus("mandatory")
_NwIpxBcastOperationalTime_Type = TimeTicks
_NwIpxBcastOperationalTime_Object = MibScalar
nwIpxBcastOperationalTime = _NwIpxBcastOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 1, 4),
    _NwIpxBcastOperationalTime_Type()
)
nwIpxBcastOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastOperationalTime.setStatus("mandatory")
_NwIpxBcastVersion_Type = DisplayString
_NwIpxBcastVersion_Object = MibScalar
nwIpxBcastVersion = _NwIpxBcastVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 1, 5),
    _NwIpxBcastVersion_Type()
)
nwIpxBcastVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastVersion.setStatus("mandatory")
_NwIpxBroadcastCounters_ObjectIdentity = ObjectIdentity
nwIpxBroadcastCounters = _NwIpxBroadcastCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2)
)


class _NwIpxBcastCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxBcastCtrAdminStatus based on Integer32"""
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


_NwIpxBcastCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxBcastCtrAdminStatus_Object = MibScalar
nwIpxBcastCtrAdminStatus = _NwIpxBcastCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 1),
    _NwIpxBcastCtrAdminStatus_Type()
)
nwIpxBcastCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastCtrAdminStatus.setStatus("mandatory")


class _NwIpxBcastCtrReset_Type(Integer32):
    """Custom type nwIpxBcastCtrReset based on Integer32"""
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


_NwIpxBcastCtrReset_Type.__name__ = "Integer32"
_NwIpxBcastCtrReset_Object = MibScalar
nwIpxBcastCtrReset = _NwIpxBcastCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 2),
    _NwIpxBcastCtrReset_Type()
)
nwIpxBcastCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastCtrReset.setStatus("mandatory")
_NwIpxBcastCtrOperationalTime_Type = TimeTicks
_NwIpxBcastCtrOperationalTime_Object = MibScalar
nwIpxBcastCtrOperationalTime = _NwIpxBcastCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 3),
    _NwIpxBcastCtrOperationalTime_Type()
)
nwIpxBcastCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrOperationalTime.setStatus("mandatory")
_NwIpxBcastCtrInPkts_Type = Counter32
_NwIpxBcastCtrInPkts_Object = MibScalar
nwIpxBcastCtrInPkts = _NwIpxBcastCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 4),
    _NwIpxBcastCtrInPkts_Type()
)
nwIpxBcastCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrInPkts.setStatus("mandatory")
_NwIpxBcastCtrOutPkts_Type = Counter32
_NwIpxBcastCtrOutPkts_Object = MibScalar
nwIpxBcastCtrOutPkts = _NwIpxBcastCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 5),
    _NwIpxBcastCtrOutPkts_Type()
)
nwIpxBcastCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrOutPkts.setStatus("mandatory")
_NwIpxBcastCtrFilteredPkts_Type = Counter32
_NwIpxBcastCtrFilteredPkts_Object = MibScalar
nwIpxBcastCtrFilteredPkts = _NwIpxBcastCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 6),
    _NwIpxBcastCtrFilteredPkts_Type()
)
nwIpxBcastCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrFilteredPkts.setStatus("mandatory")
_NwIpxBcastCtrDiscardPkts_Type = Counter32
_NwIpxBcastCtrDiscardPkts_Object = MibScalar
nwIpxBcastCtrDiscardPkts = _NwIpxBcastCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 7),
    _NwIpxBcastCtrDiscardPkts_Type()
)
nwIpxBcastCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrDiscardPkts.setStatus("mandatory")
_NwIpxBcastCtrInBytes_Type = Counter32
_NwIpxBcastCtrInBytes_Object = MibScalar
nwIpxBcastCtrInBytes = _NwIpxBcastCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 8),
    _NwIpxBcastCtrInBytes_Type()
)
nwIpxBcastCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrInBytes.setStatus("mandatory")
_NwIpxBcastCtrOutBytes_Type = Counter32
_NwIpxBcastCtrOutBytes_Object = MibScalar
nwIpxBcastCtrOutBytes = _NwIpxBcastCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 9),
    _NwIpxBcastCtrOutBytes_Type()
)
nwIpxBcastCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrOutBytes.setStatus("mandatory")
_NwIpxBcastCtrFilteredBytes_Type = Counter32
_NwIpxBcastCtrFilteredBytes_Object = MibScalar
nwIpxBcastCtrFilteredBytes = _NwIpxBcastCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 10),
    _NwIpxBcastCtrFilteredBytes_Type()
)
nwIpxBcastCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrFilteredBytes.setStatus("mandatory")
_NwIpxBcastCtrDiscardBytes_Type = Counter32
_NwIpxBcastCtrDiscardBytes_Object = MibScalar
nwIpxBcastCtrDiscardBytes = _NwIpxBcastCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 1, 2, 11),
    _NwIpxBcastCtrDiscardBytes_Type()
)
nwIpxBcastCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastCtrDiscardBytes.setStatus("mandatory")
_NwIpxBroadcastInterface_ObjectIdentity = ObjectIdentity
nwIpxBroadcastInterface = _NwIpxBroadcastInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2)
)
_NwIpxBroadcastIfConfig_ObjectIdentity = ObjectIdentity
nwIpxBroadcastIfConfig = _NwIpxBroadcastIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 1)
)
_NwIpxBcastIfTable_Object = MibTable
nwIpxBcastIfTable = _NwIpxBcastIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpxBcastIfTable.setStatus("mandatory")
_NwIpxBcastIfEntry_Object = MibTableRow
nwIpxBcastIfEntry = _NwIpxBcastIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 1, 1, 1)
)
nwIpxBcastIfEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxBcastIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxBcastIfEntry.setStatus("mandatory")
_NwIpxBcastIfIndex_Type = Integer32
_NwIpxBcastIfIndex_Object = MibTableColumn
nwIpxBcastIfIndex = _NwIpxBcastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 1, 1, 1, 1),
    _NwIpxBcastIfIndex_Type()
)
nwIpxBcastIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastIfIndex.setStatus("mandatory")


class _NwIpxBcastIfAdminStatus_Type(Integer32):
    """Custom type nwIpxBcastIfAdminStatus based on Integer32"""
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


_NwIpxBcastIfAdminStatus_Type.__name__ = "Integer32"
_NwIpxBcastIfAdminStatus_Object = MibTableColumn
nwIpxBcastIfAdminStatus = _NwIpxBcastIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 1, 1, 1, 2),
    _NwIpxBcastIfAdminStatus_Type()
)
nwIpxBcastIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastIfAdminStatus.setStatus("mandatory")


class _NwIpxBcastIfOperStatus_Type(Integer32):
    """Custom type nwIpxBcastIfOperStatus based on Integer32"""
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


_NwIpxBcastIfOperStatus_Type.__name__ = "Integer32"
_NwIpxBcastIfOperStatus_Object = MibTableColumn
nwIpxBcastIfOperStatus = _NwIpxBcastIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 1, 1, 1, 3),
    _NwIpxBcastIfOperStatus_Type()
)
nwIpxBcastIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfOperStatus.setStatus("mandatory")
_NwIpxBcastIfOperationalTime_Type = TimeTicks
_NwIpxBcastIfOperationalTime_Object = MibTableColumn
nwIpxBcastIfOperationalTime = _NwIpxBcastIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 1, 1, 1, 4),
    _NwIpxBcastIfOperationalTime_Type()
)
nwIpxBcastIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfOperationalTime.setStatus("mandatory")
_NwIpxBroadcastIfCounters_ObjectIdentity = ObjectIdentity
nwIpxBroadcastIfCounters = _NwIpxBroadcastIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2)
)
_NwIpxBcastIfCtrTable_Object = MibTable
nwIpxBcastIfCtrTable = _NwIpxBcastIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrTable.setStatus("mandatory")
_NwIpxBcastIfCtrEntry_Object = MibTableRow
nwIpxBcastIfCtrEntry = _NwIpxBcastIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1)
)
nwIpxBcastIfCtrEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxBcastIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrEntry.setStatus("mandatory")
_NwIpxBcastIfCtrIfIndex_Type = Integer32
_NwIpxBcastIfCtrIfIndex_Object = MibTableColumn
nwIpxBcastIfCtrIfIndex = _NwIpxBcastIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 1),
    _NwIpxBcastIfCtrIfIndex_Type()
)
nwIpxBcastIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrIfIndex.setStatus("mandatory")


class _NwIpxBcastIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxBcastIfCtrAdminStatus based on Integer32"""
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


_NwIpxBcastIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxBcastIfCtrAdminStatus_Object = MibTableColumn
nwIpxBcastIfCtrAdminStatus = _NwIpxBcastIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 2),
    _NwIpxBcastIfCtrAdminStatus_Type()
)
nwIpxBcastIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrAdminStatus.setStatus("mandatory")


class _NwIpxBcastIfCtrReset_Type(Integer32):
    """Custom type nwIpxBcastIfCtrReset based on Integer32"""
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


_NwIpxBcastIfCtrReset_Type.__name__ = "Integer32"
_NwIpxBcastIfCtrReset_Object = MibTableColumn
nwIpxBcastIfCtrReset = _NwIpxBcastIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 3),
    _NwIpxBcastIfCtrReset_Type()
)
nwIpxBcastIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrReset.setStatus("mandatory")
_NwIpxBcastIfCtrOperationalTime_Type = TimeTicks
_NwIpxBcastIfCtrOperationalTime_Object = MibTableColumn
nwIpxBcastIfCtrOperationalTime = _NwIpxBcastIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 4),
    _NwIpxBcastIfCtrOperationalTime_Type()
)
nwIpxBcastIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrOperationalTime.setStatus("mandatory")
_NwIpxBcastIfCtrInPkts_Type = Counter32
_NwIpxBcastIfCtrInPkts_Object = MibTableColumn
nwIpxBcastIfCtrInPkts = _NwIpxBcastIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 5),
    _NwIpxBcastIfCtrInPkts_Type()
)
nwIpxBcastIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrInPkts.setStatus("mandatory")
_NwIpxBcastIfCtrOutPkts_Type = Counter32
_NwIpxBcastIfCtrOutPkts_Object = MibTableColumn
nwIpxBcastIfCtrOutPkts = _NwIpxBcastIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 6),
    _NwIpxBcastIfCtrOutPkts_Type()
)
nwIpxBcastIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrOutPkts.setStatus("mandatory")
_NwIpxBcastIfCtrFilteredPkts_Type = Counter32
_NwIpxBcastIfCtrFilteredPkts_Object = MibTableColumn
nwIpxBcastIfCtrFilteredPkts = _NwIpxBcastIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 7),
    _NwIpxBcastIfCtrFilteredPkts_Type()
)
nwIpxBcastIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrFilteredPkts.setStatus("mandatory")
_NwIpxBcastIfCtrDiscardPkts_Type = Counter32
_NwIpxBcastIfCtrDiscardPkts_Object = MibTableColumn
nwIpxBcastIfCtrDiscardPkts = _NwIpxBcastIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 8),
    _NwIpxBcastIfCtrDiscardPkts_Type()
)
nwIpxBcastIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrDiscardPkts.setStatus("mandatory")
_NwIpxBcastIfCtrInBytes_Type = Counter32
_NwIpxBcastIfCtrInBytes_Object = MibTableColumn
nwIpxBcastIfCtrInBytes = _NwIpxBcastIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 9),
    _NwIpxBcastIfCtrInBytes_Type()
)
nwIpxBcastIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrInBytes.setStatus("mandatory")
_NwIpxBcastIfCtrOutBytes_Type = Counter32
_NwIpxBcastIfCtrOutBytes_Object = MibTableColumn
nwIpxBcastIfCtrOutBytes = _NwIpxBcastIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 10),
    _NwIpxBcastIfCtrOutBytes_Type()
)
nwIpxBcastIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrOutBytes.setStatus("mandatory")
_NwIpxBcastIfCtrFilteredBytes_Type = Counter32
_NwIpxBcastIfCtrFilteredBytes_Object = MibTableColumn
nwIpxBcastIfCtrFilteredBytes = _NwIpxBcastIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 11),
    _NwIpxBcastIfCtrFilteredBytes_Type()
)
nwIpxBcastIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrFilteredBytes.setStatus("mandatory")
_NwIpxBcastIfCtrDiscardBytes_Type = Counter32
_NwIpxBcastIfCtrDiscardBytes_Object = MibTableColumn
nwIpxBcastIfCtrDiscardBytes = _NwIpxBcastIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 2, 2, 2, 1, 1, 12),
    _NwIpxBcastIfCtrDiscardBytes_Type()
)
nwIpxBcastIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxBcastIfCtrDiscardBytes.setStatus("mandatory")
_NwIpxEcho_ObjectIdentity = ObjectIdentity
nwIpxEcho = _NwIpxEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3)
)
_NwIpxEchoSystem_ObjectIdentity = ObjectIdentity
nwIpxEchoSystem = _NwIpxEchoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1)
)
_NwIpxEchoConfig_ObjectIdentity = ObjectIdentity
nwIpxEchoConfig = _NwIpxEchoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 1)
)


class _NwIpxEchoAdminStatus_Type(Integer32):
    """Custom type nwIpxEchoAdminStatus based on Integer32"""
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


_NwIpxEchoAdminStatus_Type.__name__ = "Integer32"
_NwIpxEchoAdminStatus_Object = MibScalar
nwIpxEchoAdminStatus = _NwIpxEchoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 1, 1),
    _NwIpxEchoAdminStatus_Type()
)
nwIpxEchoAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoAdminStatus.setStatus("mandatory")


class _NwIpxEchoOperStatus_Type(Integer32):
    """Custom type nwIpxEchoOperStatus based on Integer32"""
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


_NwIpxEchoOperStatus_Type.__name__ = "Integer32"
_NwIpxEchoOperStatus_Object = MibScalar
nwIpxEchoOperStatus = _NwIpxEchoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 1, 2),
    _NwIpxEchoOperStatus_Type()
)
nwIpxEchoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoOperStatus.setStatus("mandatory")


class _NwIpxEchoAdminReset_Type(Integer32):
    """Custom type nwIpxEchoAdminReset based on Integer32"""
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


_NwIpxEchoAdminReset_Type.__name__ = "Integer32"
_NwIpxEchoAdminReset_Object = MibScalar
nwIpxEchoAdminReset = _NwIpxEchoAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 1, 3),
    _NwIpxEchoAdminReset_Type()
)
nwIpxEchoAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoAdminReset.setStatus("mandatory")
_NwIpxEchoOperationalTime_Type = TimeTicks
_NwIpxEchoOperationalTime_Object = MibScalar
nwIpxEchoOperationalTime = _NwIpxEchoOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 1, 4),
    _NwIpxEchoOperationalTime_Type()
)
nwIpxEchoOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoOperationalTime.setStatus("mandatory")
_NwIpxEchoVersion_Type = DisplayString
_NwIpxEchoVersion_Object = MibScalar
nwIpxEchoVersion = _NwIpxEchoVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 1, 5),
    _NwIpxEchoVersion_Type()
)
nwIpxEchoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoVersion.setStatus("mandatory")
_NwIpxEchoCounters_ObjectIdentity = ObjectIdentity
nwIpxEchoCounters = _NwIpxEchoCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2)
)


class _NwIpxEchoCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxEchoCtrAdminStatus based on Integer32"""
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


_NwIpxEchoCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxEchoCtrAdminStatus_Object = MibScalar
nwIpxEchoCtrAdminStatus = _NwIpxEchoCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 1),
    _NwIpxEchoCtrAdminStatus_Type()
)
nwIpxEchoCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoCtrAdminStatus.setStatus("mandatory")


class _NwIpxEchoCtrReset_Type(Integer32):
    """Custom type nwIpxEchoCtrReset based on Integer32"""
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


_NwIpxEchoCtrReset_Type.__name__ = "Integer32"
_NwIpxEchoCtrReset_Object = MibScalar
nwIpxEchoCtrReset = _NwIpxEchoCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 2),
    _NwIpxEchoCtrReset_Type()
)
nwIpxEchoCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoCtrReset.setStatus("mandatory")
_NwIpxEchoCtrOperationalTime_Type = TimeTicks
_NwIpxEchoCtrOperationalTime_Object = MibScalar
nwIpxEchoCtrOperationalTime = _NwIpxEchoCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 3),
    _NwIpxEchoCtrOperationalTime_Type()
)
nwIpxEchoCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrOperationalTime.setStatus("mandatory")
_NwIpxEchoCtrInPkts_Type = Counter32
_NwIpxEchoCtrInPkts_Object = MibScalar
nwIpxEchoCtrInPkts = _NwIpxEchoCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 4),
    _NwIpxEchoCtrInPkts_Type()
)
nwIpxEchoCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrInPkts.setStatus("mandatory")
_NwIpxEchoCtrOutPkts_Type = Counter32
_NwIpxEchoCtrOutPkts_Object = MibScalar
nwIpxEchoCtrOutPkts = _NwIpxEchoCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 5),
    _NwIpxEchoCtrOutPkts_Type()
)
nwIpxEchoCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrOutPkts.setStatus("mandatory")
_NwIpxEchoCtrFilteredPkts_Type = Counter32
_NwIpxEchoCtrFilteredPkts_Object = MibScalar
nwIpxEchoCtrFilteredPkts = _NwIpxEchoCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 6),
    _NwIpxEchoCtrFilteredPkts_Type()
)
nwIpxEchoCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrFilteredPkts.setStatus("mandatory")
_NwIpxEchoCtrDiscardPkts_Type = Counter32
_NwIpxEchoCtrDiscardPkts_Object = MibScalar
nwIpxEchoCtrDiscardPkts = _NwIpxEchoCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 7),
    _NwIpxEchoCtrDiscardPkts_Type()
)
nwIpxEchoCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrDiscardPkts.setStatus("mandatory")
_NwIpxEchoCtrInBytes_Type = Counter32
_NwIpxEchoCtrInBytes_Object = MibScalar
nwIpxEchoCtrInBytes = _NwIpxEchoCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 8),
    _NwIpxEchoCtrInBytes_Type()
)
nwIpxEchoCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrInBytes.setStatus("mandatory")
_NwIpxEchoCtrOutBytes_Type = Counter32
_NwIpxEchoCtrOutBytes_Object = MibScalar
nwIpxEchoCtrOutBytes = _NwIpxEchoCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 9),
    _NwIpxEchoCtrOutBytes_Type()
)
nwIpxEchoCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrOutBytes.setStatus("mandatory")
_NwIpxEchoCtrFilteredBytes_Type = Counter32
_NwIpxEchoCtrFilteredBytes_Object = MibScalar
nwIpxEchoCtrFilteredBytes = _NwIpxEchoCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 10),
    _NwIpxEchoCtrFilteredBytes_Type()
)
nwIpxEchoCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoCtrFilteredBytes.setStatus("mandatory")
_NwIpxEchoSCtrDiscardBytes_Type = Counter32
_NwIpxEchoSCtrDiscardBytes_Object = MibScalar
nwIpxEchoSCtrDiscardBytes = _NwIpxEchoSCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 1, 2, 11),
    _NwIpxEchoSCtrDiscardBytes_Type()
)
nwIpxEchoSCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoSCtrDiscardBytes.setStatus("mandatory")
_NwIpxEchoInterface_ObjectIdentity = ObjectIdentity
nwIpxEchoInterface = _NwIpxEchoInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2)
)
_NwIpxEchoIfConfig_ObjectIdentity = ObjectIdentity
nwIpxEchoIfConfig = _NwIpxEchoIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 1)
)
_NwIpxEchoIfTable_Object = MibTable
nwIpxEchoIfTable = _NwIpxEchoIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpxEchoIfTable.setStatus("mandatory")
_NwIpxEchoIfEntry_Object = MibTableRow
nwIpxEchoIfEntry = _NwIpxEchoIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 1, 1, 1)
)
nwIpxEchoIfEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxEchoIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxEchoIfEntry.setStatus("mandatory")
_NwIpxEchoIfIndex_Type = Integer32
_NwIpxEchoIfIndex_Object = MibTableColumn
nwIpxEchoIfIndex = _NwIpxEchoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 1, 1, 1, 1),
    _NwIpxEchoIfIndex_Type()
)
nwIpxEchoIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoIfIndex.setStatus("mandatory")


class _NwIpxEchoIfAdminStatus_Type(Integer32):
    """Custom type nwIpxEchoIfAdminStatus based on Integer32"""
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


_NwIpxEchoIfAdminStatus_Type.__name__ = "Integer32"
_NwIpxEchoIfAdminStatus_Object = MibTableColumn
nwIpxEchoIfAdminStatus = _NwIpxEchoIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 1, 1, 1, 2),
    _NwIpxEchoIfAdminStatus_Type()
)
nwIpxEchoIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoIfAdminStatus.setStatus("mandatory")


class _NwIpxEchoIfOperStatus_Type(Integer32):
    """Custom type nwIpxEchoIfOperStatus based on Integer32"""
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


_NwIpxEchoIfOperStatus_Type.__name__ = "Integer32"
_NwIpxEchoIfOperStatus_Object = MibTableColumn
nwIpxEchoIfOperStatus = _NwIpxEchoIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 1, 1, 1, 3),
    _NwIpxEchoIfOperStatus_Type()
)
nwIpxEchoIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfOperStatus.setStatus("mandatory")
_NwIpxEchoIfOperationalTime_Type = TimeTicks
_NwIpxEchoIfOperationalTime_Object = MibTableColumn
nwIpxEchoIfOperationalTime = _NwIpxEchoIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 1, 1, 1, 4),
    _NwIpxEchoIfOperationalTime_Type()
)
nwIpxEchoIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfOperationalTime.setStatus("mandatory")
_NwIpxEchoIfCounters_ObjectIdentity = ObjectIdentity
nwIpxEchoIfCounters = _NwIpxEchoIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2)
)
_NwIpxEchoIfCtrTable_Object = MibTable
nwIpxEchoIfCtrTable = _NwIpxEchoIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrTable.setStatus("mandatory")
_NwIpxEchoIfCtrEntry_Object = MibTableRow
nwIpxEchoIfCtrEntry = _NwIpxEchoIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1)
)
nwIpxEchoIfCtrEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxEchoIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrEntry.setStatus("mandatory")
_NwIpxEchoIfCtrIfIndex_Type = Integer32
_NwIpxEchoIfCtrIfIndex_Object = MibTableColumn
nwIpxEchoIfCtrIfIndex = _NwIpxEchoIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 1),
    _NwIpxEchoIfCtrIfIndex_Type()
)
nwIpxEchoIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrIfIndex.setStatus("mandatory")


class _NwIpxEchoIfCtrAdminStatus_Type(Integer32):
    """Custom type nwIpxEchoIfCtrAdminStatus based on Integer32"""
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


_NwIpxEchoIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwIpxEchoIfCtrAdminStatus_Object = MibTableColumn
nwIpxEchoIfCtrAdminStatus = _NwIpxEchoIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 2),
    _NwIpxEchoIfCtrAdminStatus_Type()
)
nwIpxEchoIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrAdminStatus.setStatus("mandatory")


class _NwIpxEchoIfCtrReset_Type(Integer32):
    """Custom type nwIpxEchoIfCtrReset based on Integer32"""
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


_NwIpxEchoIfCtrReset_Type.__name__ = "Integer32"
_NwIpxEchoIfCtrReset_Object = MibTableColumn
nwIpxEchoIfCtrReset = _NwIpxEchoIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 3),
    _NwIpxEchoIfCtrReset_Type()
)
nwIpxEchoIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrReset.setStatus("mandatory")
_NwIpxEchoIfCtrOperationalTime_Type = TimeTicks
_NwIpxEchoIfCtrOperationalTime_Object = MibTableColumn
nwIpxEchoIfCtrOperationalTime = _NwIpxEchoIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 4),
    _NwIpxEchoIfCtrOperationalTime_Type()
)
nwIpxEchoIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrOperationalTime.setStatus("mandatory")
_NwIpxEchoIfCtrInPkts_Type = Counter32
_NwIpxEchoIfCtrInPkts_Object = MibTableColumn
nwIpxEchoIfCtrInPkts = _NwIpxEchoIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 5),
    _NwIpxEchoIfCtrInPkts_Type()
)
nwIpxEchoIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrInPkts.setStatus("mandatory")
_NwIpxEchoIfCtrOutPkts_Type = Counter32
_NwIpxEchoIfCtrOutPkts_Object = MibTableColumn
nwIpxEchoIfCtrOutPkts = _NwIpxEchoIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 6),
    _NwIpxEchoIfCtrOutPkts_Type()
)
nwIpxEchoIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrOutPkts.setStatus("mandatory")
_NwIpxEchoIfCtrFilteredPkts_Type = Counter32
_NwIpxEchoIfCtrFilteredPkts_Object = MibTableColumn
nwIpxEchoIfCtrFilteredPkts = _NwIpxEchoIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 7),
    _NwIpxEchoIfCtrFilteredPkts_Type()
)
nwIpxEchoIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrFilteredPkts.setStatus("mandatory")
_NwIpxEchoIfCtrDiscardPkts_Type = Counter32
_NwIpxEchoIfCtrDiscardPkts_Object = MibTableColumn
nwIpxEchoIfCtrDiscardPkts = _NwIpxEchoIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 8),
    _NwIpxEchoIfCtrDiscardPkts_Type()
)
nwIpxEchoIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrDiscardPkts.setStatus("mandatory")
_NwIpxEchoIfCtrInBytes_Type = Counter32
_NwIpxEchoIfCtrInBytes_Object = MibTableColumn
nwIpxEchoIfCtrInBytes = _NwIpxEchoIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 9),
    _NwIpxEchoIfCtrInBytes_Type()
)
nwIpxEchoIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrInBytes.setStatus("mandatory")
_NwIpxEchoIfCtrOutBytes_Type = Counter32
_NwIpxEchoIfCtrOutBytes_Object = MibTableColumn
nwIpxEchoIfCtrOutBytes = _NwIpxEchoIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 10),
    _NwIpxEchoIfCtrOutBytes_Type()
)
nwIpxEchoIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrOutBytes.setStatus("mandatory")
_NwIpxEchoIfCtrFilteredBytes_Type = Counter32
_NwIpxEchoIfCtrFilteredBytes_Object = MibTableColumn
nwIpxEchoIfCtrFilteredBytes = _NwIpxEchoIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 11),
    _NwIpxEchoIfCtrFilteredBytes_Type()
)
nwIpxEchoIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrFilteredBytes.setStatus("mandatory")
_NwIpxEchoIfCtrDiscardBytes_Type = Counter32
_NwIpxEchoIfCtrDiscardBytes_Object = MibTableColumn
nwIpxEchoIfCtrDiscardBytes = _NwIpxEchoIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 9, 3, 2, 2, 1, 1, 12),
    _NwIpxEchoIfCtrDiscardBytes_Type()
)
nwIpxEchoIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEchoIfCtrDiscardBytes.setStatus("mandatory")
_NwIpxEvent_ObjectIdentity = ObjectIdentity
nwIpxEvent = _NwIpxEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10)
)
_NwIpxEventLogConfig_ObjectIdentity = ObjectIdentity
nwIpxEventLogConfig = _NwIpxEventLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 1)
)


class _NwIpxEventAdminStatus_Type(Integer32):
    """Custom type nwIpxEventAdminStatus based on Integer32"""
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


_NwIpxEventAdminStatus_Type.__name__ = "Integer32"
_NwIpxEventAdminStatus_Object = MibScalar
nwIpxEventAdminStatus = _NwIpxEventAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 1, 1),
    _NwIpxEventAdminStatus_Type()
)
nwIpxEventAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEventAdminStatus.setStatus("mandatory")


class _NwIpxEventMaxEntries_Type(Integer32):
    """Custom type nwIpxEventMaxEntries based on Integer32"""
    defaultValue = 100


_NwIpxEventMaxEntries_Object = MibScalar
nwIpxEventMaxEntries = _NwIpxEventMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 1, 2),
    _NwIpxEventMaxEntries_Type()
)
nwIpxEventMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEventMaxEntries.setStatus("mandatory")


class _NwIpxEventTraceAll_Type(Integer32):
    """Custom type nwIpxEventTraceAll based on Integer32"""
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


_NwIpxEventTraceAll_Type.__name__ = "Integer32"
_NwIpxEventTraceAll_Object = MibScalar
nwIpxEventTraceAll = _NwIpxEventTraceAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 1, 3),
    _NwIpxEventTraceAll_Type()
)
nwIpxEventTraceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEventTraceAll.setStatus("mandatory")
_NwIpxEventLogFilterTable_ObjectIdentity = ObjectIdentity
nwIpxEventLogFilterTable = _NwIpxEventLogFilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2)
)
_NwIpxEventFilterTable_Object = MibTable
nwIpxEventFilterTable = _NwIpxEventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpxEventFilterTable.setStatus("mandatory")
_NwIpxEventFilterEntry_Object = MibTableRow
nwIpxEventFilterEntry = _NwIpxEventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1, 1)
)
nwIpxEventFilterEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxEventFltrProtocol"),
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxEventFltrIfNum"),
)
if mibBuilder.loadTexts:
    nwIpxEventFilterEntry.setStatus("mandatory")
_NwIpxEventFltrProtocol_Type = Integer32
_NwIpxEventFltrProtocol_Object = MibTableColumn
nwIpxEventFltrProtocol = _NwIpxEventFltrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1, 1, 1),
    _NwIpxEventFltrProtocol_Type()
)
nwIpxEventFltrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventFltrProtocol.setStatus("mandatory")
_NwIpxEventFltrIfNum_Type = Integer32
_NwIpxEventFltrIfNum_Object = MibTableColumn
nwIpxEventFltrIfNum = _NwIpxEventFltrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1, 1, 2),
    _NwIpxEventFltrIfNum_Type()
)
nwIpxEventFltrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventFltrIfNum.setStatus("mandatory")


class _NwIpxEventFltrControl_Type(Integer32):
    """Custom type nwIpxEventFltrControl based on Integer32"""
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


_NwIpxEventFltrControl_Type.__name__ = "Integer32"
_NwIpxEventFltrControl_Object = MibTableColumn
nwIpxEventFltrControl = _NwIpxEventFltrControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1, 1, 3),
    _NwIpxEventFltrControl_Type()
)
nwIpxEventFltrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEventFltrControl.setStatus("mandatory")


class _NwIpxEventFltrType_Type(Integer32):
    """Custom type nwIpxEventFltrType based on Integer32"""
    defaultValue = 1

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


_NwIpxEventFltrType_Type.__name__ = "Integer32"
_NwIpxEventFltrType_Object = MibTableColumn
nwIpxEventFltrType = _NwIpxEventFltrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1, 1, 4),
    _NwIpxEventFltrType_Type()
)
nwIpxEventFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEventFltrType.setStatus("mandatory")


class _NwIpxEventFltrSeverity_Type(Integer32):
    """Custom type nwIpxEventFltrSeverity based on Integer32"""
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


_NwIpxEventFltrSeverity_Type.__name__ = "Integer32"
_NwIpxEventFltrSeverity_Object = MibTableColumn
nwIpxEventFltrSeverity = _NwIpxEventFltrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1, 1, 5),
    _NwIpxEventFltrSeverity_Type()
)
nwIpxEventFltrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEventFltrSeverity.setStatus("mandatory")


class _NwIpxEventFltrAction_Type(Integer32):
    """Custom type nwIpxEventFltrAction based on Integer32"""
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


_NwIpxEventFltrAction_Type.__name__ = "Integer32"
_NwIpxEventFltrAction_Object = MibTableColumn
nwIpxEventFltrAction = _NwIpxEventFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 2, 1, 1, 6),
    _NwIpxEventFltrAction_Type()
)
nwIpxEventFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpxEventFltrAction.setStatus("mandatory")
_NwIpxEventLogTable_ObjectIdentity = ObjectIdentity
nwIpxEventLogTable = _NwIpxEventLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3)
)
_NwIpxEventTable_Object = MibTable
nwIpxEventTable = _NwIpxEventTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    nwIpxEventTable.setStatus("mandatory")
_NwIpxEventEntry_Object = MibTableRow
nwIpxEventEntry = _NwIpxEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1)
)
nwIpxEventEntry.setIndexNames(
    (0, "CTRON-IPX-ROUTER-MIB", "nwIpxEventNumber"),
)
if mibBuilder.loadTexts:
    nwIpxEventEntry.setStatus("mandatory")
_NwIpxEventNumber_Type = Integer32
_NwIpxEventNumber_Object = MibTableColumn
nwIpxEventNumber = _NwIpxEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1, 1),
    _NwIpxEventNumber_Type()
)
nwIpxEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventNumber.setStatus("mandatory")
_NwIpxEventTime_Type = TimeTicks
_NwIpxEventTime_Object = MibTableColumn
nwIpxEventTime = _NwIpxEventTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1, 2),
    _NwIpxEventTime_Type()
)
nwIpxEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventTime.setStatus("mandatory")


class _NwIpxEventType_Type(Integer32):
    """Custom type nwIpxEventType based on Integer32"""
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


_NwIpxEventType_Type.__name__ = "Integer32"
_NwIpxEventType_Object = MibTableColumn
nwIpxEventType = _NwIpxEventType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1, 3),
    _NwIpxEventType_Type()
)
nwIpxEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventType.setStatus("mandatory")


class _NwIpxEventSeverity_Type(Integer32):
    """Custom type nwIpxEventSeverity based on Integer32"""
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


_NwIpxEventSeverity_Type.__name__ = "Integer32"
_NwIpxEventSeverity_Object = MibTableColumn
nwIpxEventSeverity = _NwIpxEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1, 4),
    _NwIpxEventSeverity_Type()
)
nwIpxEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventSeverity.setStatus("mandatory")
_NwIpxEventProtocol_Type = Integer32
_NwIpxEventProtocol_Object = MibTableColumn
nwIpxEventProtocol = _NwIpxEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1, 5),
    _NwIpxEventProtocol_Type()
)
nwIpxEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventProtocol.setStatus("mandatory")
_NwIpxEventIfNum_Type = Integer32
_NwIpxEventIfNum_Object = MibTableColumn
nwIpxEventIfNum = _NwIpxEventIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1, 6),
    _NwIpxEventIfNum_Type()
)
nwIpxEventIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventIfNum.setStatus("mandatory")
_NwIpxEventTextString_Type = OctetString
_NwIpxEventTextString_Object = MibTableColumn
nwIpxEventTextString = _NwIpxEventTextString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 10, 3, 1, 1, 7),
    _NwIpxEventTextString_Type()
)
nwIpxEventTextString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpxEventTextString.setStatus("mandatory")
_NwIpxWorkGroup_ObjectIdentity = ObjectIdentity
nwIpxWorkGroup = _NwIpxWorkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 2, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-IPX-ROUTER-MIB",
    **{"IpxAddress": IpxAddress,
       "nwIpxRouter": nwIpxRouter,
       "nwIpxMibs": nwIpxMibs,
       "nwIpxMibRevText": nwIpxMibRevText,
       "nwIpxComponents": nwIpxComponents,
       "nwIpxSystem": nwIpxSystem,
       "nwIpxSysConfig": nwIpxSysConfig,
       "nwIpxSysRouterId": nwIpxSysRouterId,
       "nwIpxSysAdministration": nwIpxSysAdministration,
       "nwIpxSysAdminStatus": nwIpxSysAdminStatus,
       "nwIpxSysOperStatus": nwIpxSysOperStatus,
       "nwIpxSysAdminReset": nwIpxSysAdminReset,
       "nwIpxSysOperationalTimel": nwIpxSysOperationalTimel,
       "nwIpxSysVersion": nwIpxSysVersion,
       "nwIpxForwarding": nwIpxForwarding,
       "nwIpxFwdSystem": nwIpxFwdSystem,
       "nwIpxFwdCounters": nwIpxFwdCounters,
       "nwIpxFwdCtrAdminStatus": nwIpxFwdCtrAdminStatus,
       "nwIpxFwdCtrReset": nwIpxFwdCtrReset,
       "nwIpxFwdCtrOperationalTime": nwIpxFwdCtrOperationalTime,
       "nwIpxFwdCtrInPkts": nwIpxFwdCtrInPkts,
       "nwIpxFwdCtrOutPkts": nwIpxFwdCtrOutPkts,
       "nwIpxFwdCtrFwdPkts": nwIpxFwdCtrFwdPkts,
       "nwIpxFwdCtrFilteredPkts": nwIpxFwdCtrFilteredPkts,
       "nwIpxFwdCtrDiscardPkts": nwIpxFwdCtrDiscardPkts,
       "nwIpxFwdCtrAddrErrPkts": nwIpxFwdCtrAddrErrPkts,
       "nwIpxFwdCtrLenErrPkts": nwIpxFwdCtrLenErrPkts,
       "nwIpxFwdCtrHdrErrPkts": nwIpxFwdCtrHdrErrPkts,
       "nwIpxFwdCtrInBytes": nwIpxFwdCtrInBytes,
       "nwIpxFwdCtrOutBytes": nwIpxFwdCtrOutBytes,
       "nwIpxFwdCtrFwdBytes": nwIpxFwdCtrFwdBytes,
       "nwIpxFwdCtrFilteredBytes": nwIpxFwdCtrFilteredBytes,
       "nwIpxFwdCtrDiscardBytes": nwIpxFwdCtrDiscardBytes,
       "nwIpxFwdCtrHostInPkts": nwIpxFwdCtrHostInPkts,
       "nwIpxFwdCtrHostOutPkts": nwIpxFwdCtrHostOutPkts,
       "nwIpxFwdCtrHostDiscardPkts": nwIpxFwdCtrHostDiscardPkts,
       "nwIpxFwdCtrHostInBytes": nwIpxFwdCtrHostInBytes,
       "nwIpxFwdCtrHostOutBytes": nwIpxFwdCtrHostOutBytes,
       "nwIpxFwdCtrHostDiscardBytes": nwIpxFwdCtrHostDiscardBytes,
       "nwIpxFwdInterfaces": nwIpxFwdInterfaces,
       "nwIpxFwdIfConfig": nwIpxFwdIfConfig,
       "nwIpxFwdIfTable": nwIpxFwdIfTable,
       "nwIpxFwdIfEntry": nwIpxFwdIfEntry,
       "nwIpxFwdIfIndex": nwIpxFwdIfIndex,
       "nwIpxFwdIfAdminStatus": nwIpxFwdIfAdminStatus,
       "nwIpxFwdIfOperStatus": nwIpxFwdIfOperStatus,
       "nwIpxFwdIfOperationalTime": nwIpxFwdIfOperationalTime,
       "nwIpxFwdIfControl": nwIpxFwdIfControl,
       "nwIpxFwdIfMtu": nwIpxFwdIfMtu,
       "nwIpxFwdIfForwarding": nwIpxFwdIfForwarding,
       "nwIpxFwdIfFrameType": nwIpxFwdIfFrameType,
       "nwIpxFwdIfAclIdentifier": nwIpxFwdIfAclIdentifier,
       "nwIpxFwdIfAclStatus": nwIpxFwdIfAclStatus,
       "nwIpxFwdIfCacheControl": nwIpxFwdIfCacheControl,
       "nwIpxFwdIfCacheEntries": nwIpxFwdIfCacheEntries,
       "nwIpxFwdIfCacheHits": nwIpxFwdIfCacheHits,
       "nwIpxFwdIfCacheMisses": nwIpxFwdIfCacheMisses,
       "nwIpxAddressTable": nwIpxAddressTable,
       "nwIpxAddrEntry": nwIpxAddrEntry,
       "nwIpxAddrIfIndex": nwIpxAddrIfIndex,
       "nwIpxAddrIfAddress": nwIpxAddrIfAddress,
       "nwIpxAddrIfControl": nwIpxAddrIfControl,
       "nwIpxAddrIfAddrType": nwIpxAddrIfAddrType,
       "nwIpxFwdIfCounters": nwIpxFwdIfCounters,
       "nwIpxFwdIfCtrTable": nwIpxFwdIfCtrTable,
       "nwIpxFwdIfCtrEntry": nwIpxFwdIfCtrEntry,
       "nwIpxFwdIfCtrIfIndex": nwIpxFwdIfCtrIfIndex,
       "nwIpxFwdIfCtrAdminStatus": nwIpxFwdIfCtrAdminStatus,
       "nwIpxFwdIfCtrReset": nwIpxFwdIfCtrReset,
       "nwIpxFwdIfCtrOperationalTime": nwIpxFwdIfCtrOperationalTime,
       "nwIpxFwdIfCtrInPkts": nwIpxFwdIfCtrInPkts,
       "nwIpxFwdIfCtrOutPkts": nwIpxFwdIfCtrOutPkts,
       "nwIpxFwdIfCtrFwdPkts": nwIpxFwdIfCtrFwdPkts,
       "nwIpxFwdIfCtrFilteredPkts": nwIpxFwdIfCtrFilteredPkts,
       "nwIpxFwdIfCtrDiscardPkts": nwIpxFwdIfCtrDiscardPkts,
       "nwIpxFwdIfCtrAddrErrPkts": nwIpxFwdIfCtrAddrErrPkts,
       "nwIpxFwdIfCtrLenErrPkts": nwIpxFwdIfCtrLenErrPkts,
       "nwIpxFwdIfCtrHdrErrPkts": nwIpxFwdIfCtrHdrErrPkts,
       "nwIpxFwdIfCtrInBytes": nwIpxFwdIfCtrInBytes,
       "nwIpxFwdIfCtrOutBytes": nwIpxFwdIfCtrOutBytes,
       "nwIpxFwdIfCtrFwdBytes": nwIpxFwdIfCtrFwdBytes,
       "nwIpxFwdIfCtrFilteredBytes": nwIpxFwdIfCtrFilteredBytes,
       "nwIpxFwdIfCtrDiscardBytes": nwIpxFwdIfCtrDiscardBytes,
       "nwIpxFwdIfCtrHostInPkts": nwIpxFwdIfCtrHostInPkts,
       "nwIpxFwdIfCtrHostOutPkts": nwIpxFwdIfCtrHostOutPkts,
       "nwIpxFwdIfCtrHostDiscardPkts": nwIpxFwdIfCtrHostDiscardPkts,
       "nwIpxFwdIfCtrHostInBytes": nwIpxFwdIfCtrHostInBytes,
       "nwIpxFwdIfCtrHostOutBytes": nwIpxFwdIfCtrHostOutBytes,
       "nwIpxFwdIfCtrHostDiscardBytes": nwIpxFwdIfCtrHostDiscardBytes,
       "nwIpxTopology": nwIpxTopology,
       "nwIpxDistanceVector": nwIpxDistanceVector,
       "nwIpxRip": nwIpxRip,
       "nwIpxRipSystem": nwIpxRipSystem,
       "nwIpxRipConfig": nwIpxRipConfig,
       "nwIpxRipAdminStatus": nwIpxRipAdminStatus,
       "nwIpxRipOperStatus": nwIpxRipOperStatus,
       "nwIpxRipAdminReset": nwIpxRipAdminReset,
       "nwIpxRipOperationalTime": nwIpxRipOperationalTime,
       "nwIpxRipVersion": nwIpxRipVersion,
       "nwIpxRipStackSize": nwIpxRipStackSize,
       "nwIpxRipThreadPriority": nwIpxRipThreadPriority,
       "nwIpxRipDatabaseThreshold": nwIpxRipDatabaseThreshold,
       "nwIpxRipAgeOut": nwIpxRipAgeOut,
       "nwIpxRipHoldDown": nwIpxRipHoldDown,
       "nwIpxRipCounters": nwIpxRipCounters,
       "nwIpxRipCtrAdminStatus": nwIpxRipCtrAdminStatus,
       "nwIpxRipCtrReset": nwIpxRipCtrReset,
       "nwIpxRipCtrOperationalTime": nwIpxRipCtrOperationalTime,
       "nwIpxRipCtrInPkts": nwIpxRipCtrInPkts,
       "nwIpxRipCtrOutPkts": nwIpxRipCtrOutPkts,
       "nwIpxRipCtrFilteredPkts": nwIpxRipCtrFilteredPkts,
       "nwIpxRipCtrDiscardPkts": nwIpxRipCtrDiscardPkts,
       "nwIpxRipCtrInBytes": nwIpxRipCtrInBytes,
       "nwIpxRipCtrOutBytes": nwIpxRipCtrOutBytes,
       "nwIpxRipCtrFilteredBytes": nwIpxRipCtrFilteredBytes,
       "nwIpxRipCtrDiscardBytes": nwIpxRipCtrDiscardBytes,
       "nwIpxRipInterfaces": nwIpxRipInterfaces,
       "nwIpxRipIfConfig": nwIpxRipIfConfig,
       "nwIpxRipIfTable": nwIpxRipIfTable,
       "nwIpxRipIfEntry": nwIpxRipIfEntry,
       "nwIpxRipIfIndex": nwIpxRipIfIndex,
       "nwIpxRipIfAdminStatus": nwIpxRipIfAdminStatus,
       "nwIpxRipIfOperStatus": nwIpxRipIfOperStatus,
       "nwIpxRipIfOperationalTime": nwIpxRipIfOperationalTime,
       "nwIpxRipIfVersion": nwIpxRipIfVersion,
       "nwIpxRipIfAdvertisement": nwIpxRipIfAdvertisement,
       "nwIpxRipIfFloodDelay": nwIpxRipIfFloodDelay,
       "nwIpxRipIfRequestDelay": nwIpxRipIfRequestDelay,
       "nwIpxRipIfPriority": nwIpxRipIfPriority,
       "nwIpxRipIfHelloTimer": nwIpxRipIfHelloTimer,
       "nwIpxRipIfSplitHorizon": nwIpxRipIfSplitHorizon,
       "nwIpxRipIfPoisonReverse": nwIpxRipIfPoisonReverse,
       "nwIpxRipIfSnooping": nwIpxRipIfSnooping,
       "nwIpxRipIfType": nwIpxRipIfType,
       "nwIpxRipIfXmitCost": nwIpxRipIfXmitCost,
       "nwIpxRipIfAclIdentifier": nwIpxRipIfAclIdentifier,
       "nwIpxRipIfAclStatus": nwIpxRipIfAclStatus,
       "nwIpxRipIfCounters": nwIpxRipIfCounters,
       "nwIpxRipIfCtrTable": nwIpxRipIfCtrTable,
       "nwIpxRipIfCtrEntry": nwIpxRipIfCtrEntry,
       "nwIpxRipIfCtrIfIndex": nwIpxRipIfCtrIfIndex,
       "nwIpxRipIfCtrAdminStatus": nwIpxRipIfCtrAdminStatus,
       "nwIpxRipIfCtrReset": nwIpxRipIfCtrReset,
       "nwIpxRipIfCtrOperationalTime": nwIpxRipIfCtrOperationalTime,
       "nwIpxRipIfCtrInPkts": nwIpxRipIfCtrInPkts,
       "nwIpxRipIfCtrOutPkts": nwIpxRipIfCtrOutPkts,
       "nwIpxRipIfCtrFilteredPkts": nwIpxRipIfCtrFilteredPkts,
       "nwIpxRipIfCtrDiscardPkts": nwIpxRipIfCtrDiscardPkts,
       "nwIpxRipIfCtrInBytes": nwIpxRipIfCtrInBytes,
       "nwIpxRipIfCtrOutBytes": nwIpxRipIfCtrOutBytes,
       "nwIpxRipIfCtrFilteredBytes": nwIpxRipIfCtrFilteredBytes,
       "nwIpxRipIfCtrDiscardBytes": nwIpxRipIfCtrDiscardBytes,
       "nwIpxRipDatabase": nwIpxRipDatabase,
       "nwIpxRipRouteTable": nwIpxRipRouteTable,
       "nwIpxRipRouteEntry": nwIpxRipRouteEntry,
       "nwIpxRipRtNetId": nwIpxRipRtNetId,
       "nwIpxRipRtIfIndex": nwIpxRipRtIfIndex,
       "nwIpxRipRtSrcNode": nwIpxRipRtSrcNode,
       "nwIpxRipRtHops": nwIpxRipRtHops,
       "nwIpxRipRtTicks": nwIpxRipRtTicks,
       "nwIpxRipRtAge": nwIpxRipRtAge,
       "nwIpxRipRtType": nwIpxRipRtType,
       "nwIpxRipRtFlags": nwIpxRipRtFlags,
       "nwIpxRipFilters": nwIpxRipFilters,
       "nwIpxSap": nwIpxSap,
       "nwIpxSapSystem": nwIpxSapSystem,
       "nwIpxSapConfig": nwIpxSapConfig,
       "nwIpxSapAdminStatus": nwIpxSapAdminStatus,
       "nwIpxSapOperStatus": nwIpxSapOperStatus,
       "nwIpxSapAdminReset": nwIpxSapAdminReset,
       "nwIpxSapOperationalTime": nwIpxSapOperationalTime,
       "nwIpxSapVersion": nwIpxSapVersion,
       "nwIpxSapStackSize": nwIpxSapStackSize,
       "nwIpxSapThreadPriority": nwIpxSapThreadPriority,
       "nwIpxSapDatabaseThreshold": nwIpxSapDatabaseThreshold,
       "nwIpxSapAgeOut": nwIpxSapAgeOut,
       "nwIpxSapHoldDown": nwIpxSapHoldDown,
       "nwIpxSapCounters": nwIpxSapCounters,
       "nwIpxSapCtrAdminStatus": nwIpxSapCtrAdminStatus,
       "nwIpxSapCtrReset": nwIpxSapCtrReset,
       "nwIpxSapCtrOperationalTime": nwIpxSapCtrOperationalTime,
       "nwIpxSapCtrInPkts": nwIpxSapCtrInPkts,
       "nwIpxSapCtrOutPkts": nwIpxSapCtrOutPkts,
       "nwIpxSapCtrFilteredPkts": nwIpxSapCtrFilteredPkts,
       "nwIpxSapCtrDiscardPkts": nwIpxSapCtrDiscardPkts,
       "nwIpxSapCtrInBytes": nwIpxSapCtrInBytes,
       "nwIpxSapCtrOutBytes": nwIpxSapCtrOutBytes,
       "nwIpxSapCtrFilteredBytes": nwIpxSapCtrFilteredBytes,
       "nwIpxSapCtrDiscardBytes": nwIpxSapCtrDiscardBytes,
       "nwIpxSapInterfaces": nwIpxSapInterfaces,
       "nwIpxSapIfConfig": nwIpxSapIfConfig,
       "nwIpxSapIfTable": nwIpxSapIfTable,
       "nwIpxSapIfEntry": nwIpxSapIfEntry,
       "nwIpxSapIfIndex": nwIpxSapIfIndex,
       "nwIpxSapIfAdminStatus": nwIpxSapIfAdminStatus,
       "nwIpxSapIfOperStatus": nwIpxSapIfOperStatus,
       "nwIpxSapIfOperationalTime": nwIpxSapIfOperationalTime,
       "nwIpxSapIfVersion": nwIpxSapIfVersion,
       "nwIpxSapIfAdvertisement": nwIpxSapIfAdvertisement,
       "nwIpxSapIfFloodDelay": nwIpxSapIfFloodDelay,
       "nwIpxSapIfRequestDelay": nwIpxSapIfRequestDelay,
       "nwIpxSapIfPriority": nwIpxSapIfPriority,
       "nwIpxSapIfHelloTimer": nwIpxSapIfHelloTimer,
       "nwIpxSapIfSplitHorizon": nwIpxSapIfSplitHorizon,
       "nwIpxSapIfPoisonReverse": nwIpxSapIfPoisonReverse,
       "nwIpxSapIfSnooping": nwIpxSapIfSnooping,
       "nwIpxSapIfType": nwIpxSapIfType,
       "nwIpxSapIfXmitCost": nwIpxSapIfXmitCost,
       "nwIpxSapIfAclIdentifier": nwIpxSapIfAclIdentifier,
       "nwIpxSapIfAclStatus": nwIpxSapIfAclStatus,
       "nwIpxSapIfCounters": nwIpxSapIfCounters,
       "nwIpxSapIfCtrTable": nwIpxSapIfCtrTable,
       "nwIpxSapIfCtrEntry": nwIpxSapIfCtrEntry,
       "nwIpxSapIfCtrIfIndex": nwIpxSapIfCtrIfIndex,
       "nwIpxSapIfCtrAdminStatus": nwIpxSapIfCtrAdminStatus,
       "nwIpxSapIfCtrReset": nwIpxSapIfCtrReset,
       "nwIpxSapIfCtrOperationalTime": nwIpxSapIfCtrOperationalTime,
       "nwIpxSapIfCtrInPkts": nwIpxSapIfCtrInPkts,
       "nwIpxSapIfCtrOutPkts": nwIpxSapIfCtrOutPkts,
       "nwIpxSapIfCtrFilteredPkts": nwIpxSapIfCtrFilteredPkts,
       "nwIpxSapIfCtrDiscardPkts": nwIpxSapIfCtrDiscardPkts,
       "nwIpxSapIfCtrInBytes": nwIpxSapIfCtrInBytes,
       "nwIpxSapIfCtrOutBytes": nwIpxSapIfCtrOutBytes,
       "nwIpxSapIfCtrFilteredBytes": nwIpxSapIfCtrFilteredBytes,
       "nwIpxSapIfCtrDiscardBytes": nwIpxSapIfCtrDiscardBytes,
       "nwIpxSapServerTable": nwIpxSapServerTable,
       "nwIpxSapServerIfTable": nwIpxSapServerIfTable,
       "nwIpxSapServerIfEntry": nwIpxSapServerIfEntry,
       "nwIpxSapServerIfNetId": nwIpxSapServerIfNetId,
       "nwIpxSapServerIfNode": nwIpxSapServerIfNode,
       "nwIpxSapServerIfSocket": nwIpxSapServerIfSocket,
       "nwIpxSapServerIfServiceType": nwIpxSapServerIfServiceType,
       "nwIpxSapServerIfIfNum": nwIpxSapServerIfIfNum,
       "nwIpxSapServerIfSrcNode": nwIpxSapServerIfSrcNode,
       "nwIpxSapServerIfName": nwIpxSapServerIfName,
       "nwIpxSapServerIfHops": nwIpxSapServerIfHops,
       "nwIpxSapServerIfAge": nwIpxSapServerIfAge,
       "nwIpxSapServerIfType": nwIpxSapServerIfType,
       "nwIpxSapServerIfFlags": nwIpxSapServerIfFlags,
       "nwIpxSapFilters": nwIpxSapFilters,
       "nwIpxLinkState": nwIpxLinkState,
       "nwIpxNlsp": nwIpxNlsp,
       "nwIpxFib": nwIpxFib,
       "nwIpxFibTable": nwIpxFibTable,
       "nwIpxFibEntry": nwIpxFibEntry,
       "nwIpxFibNetId": nwIpxFibNetId,
       "nwIpxFibHops": nwIpxFibHops,
       "nwIpxFibTimeTicks": nwIpxFibTimeTicks,
       "nwIpxFibNextHopIf": nwIpxFibNextHopIf,
       "nwIpxFibNextHopNet": nwIpxFibNextHopNet,
       "nwIpxFibNextHopNode": nwIpxFibNextHopNode,
       "nwIpxFibRouteType": nwIpxFibRouteType,
       "nwIpxEndSystems": nwIpxEndSystems,
       "nwIpxHostsSystem": nwIpxHostsSystem,
       "nwIpxHostsInterfaces": nwIpxHostsInterfaces,
       "nwIpxHostsToMedia": nwIpxHostsToMedia,
       "nwIpxHostMapTable": nwIpxHostMapTable,
       "nwIpxHostMapEntry": nwIpxHostMapEntry,
       "nwIpxHostMapIfIndex": nwIpxHostMapIfIndex,
       "nwIpxHostMapIpxAddr": nwIpxHostMapIpxAddr,
       "nwIpxHostMapPhysAddr": nwIpxHostMapPhysAddr,
       "nwIpxHostMapType": nwIpxHostMapType,
       "nwIpxHostMapCircuitID": nwIpxHostMapCircuitID,
       "nwIpxHostMapFraming": nwIpxHostMapFraming,
       "nwIpxHostMapPortNumber": nwIpxHostMapPortNumber,
       "nwIpxAccessControl": nwIpxAccessControl,
       "nwIpxAclValidEntries": nwIpxAclValidEntries,
       "nwIpxAclTable": nwIpxAclTable,
       "nwIpxAclEntry": nwIpxAclEntry,
       "nwIpxAclIdentifier": nwIpxAclIdentifier,
       "nwIpxAclSequence": nwIpxAclSequence,
       "nwIpxAclPermission": nwIpxAclPermission,
       "nwIpxAclMatches": nwIpxAclMatches,
       "nwIpxAclDestNetNum": nwIpxAclDestNetNum,
       "nwIpxAclDestNode": nwIpxAclDestNode,
       "nwIpxAclDestSocket": nwIpxAclDestSocket,
       "nwIpxAclSrcNetNum": nwIpxAclSrcNetNum,
       "nwIpxAclSrcNode": nwIpxAclSrcNode,
       "nwIpxAclSrcSocket": nwIpxAclSrcSocket,
       "nwIpxFilters": nwIpxFilters,
       "nwIpxRedirector": nwIpxRedirector,
       "nwIpxNetBIOS": nwIpxNetBIOS,
       "nwIpxNetBIOSSystem": nwIpxNetBIOSSystem,
       "nwIpxNetBIOSConfig": nwIpxNetBIOSConfig,
       "nwIpxNetBIOSAdminStatus": nwIpxNetBIOSAdminStatus,
       "nwIpxNetBIOSOperStatus": nwIpxNetBIOSOperStatus,
       "nwIpxNetBIOSAdminReset": nwIpxNetBIOSAdminReset,
       "nwIpxNetBIOSOperationalTime": nwIpxNetBIOSOperationalTime,
       "nwIpxNetBIOSVersion": nwIpxNetBIOSVersion,
       "nwIpxNetBIOSCounters": nwIpxNetBIOSCounters,
       "nwIpxNetBIOSCtrAdminStatus": nwIpxNetBIOSCtrAdminStatus,
       "nwIpxNetBIOSCtrReset": nwIpxNetBIOSCtrReset,
       "nwIpxNetBIOSCtrOperationalTime": nwIpxNetBIOSCtrOperationalTime,
       "nwIpxNetBIOSCtrInPkts": nwIpxNetBIOSCtrInPkts,
       "nwIpxNetBIOSCtrOutPkts": nwIpxNetBIOSCtrOutPkts,
       "nwIpxNetBIOSCtrFilteredPkts": nwIpxNetBIOSCtrFilteredPkts,
       "nwIpxNetBIOSCtrDiscardPkts": nwIpxNetBIOSCtrDiscardPkts,
       "nwIpxNetBIOSCtrInBytes": nwIpxNetBIOSCtrInBytes,
       "nwIpxNetBIOSCtrOutBytes": nwIpxNetBIOSCtrOutBytes,
       "nwIpxNetBIOSCtrFilteredBytes": nwIpxNetBIOSCtrFilteredBytes,
       "nwIpxNetBIOSCtrDiscardBytes": nwIpxNetBIOSCtrDiscardBytes,
       "nwIpxNetBIOSInterface": nwIpxNetBIOSInterface,
       "nwIpxNetBIOSIfConfig": nwIpxNetBIOSIfConfig,
       "nwIpxNetBIOSIfTable": nwIpxNetBIOSIfTable,
       "nwIpxNetBIOSIfEntry": nwIpxNetBIOSIfEntry,
       "nwIpxNetBIOSIfIndex": nwIpxNetBIOSIfIndex,
       "nwIpxNetBIOSIfAdminStatus": nwIpxNetBIOSIfAdminStatus,
       "nwIpxNetBIOSIfOperStatus": nwIpxNetBIOSIfOperStatus,
       "nwIpxNetBIOSIfOperationalTime": nwIpxNetBIOSIfOperationalTime,
       "nwIpxNetBIOSIfCounters": nwIpxNetBIOSIfCounters,
       "nwIpxNetBIOSIfCtrTable": nwIpxNetBIOSIfCtrTable,
       "nwIpxNetBIOSIfCtrEntry": nwIpxNetBIOSIfCtrEntry,
       "nwIpxNetBIOSIfCtrIfIndex": nwIpxNetBIOSIfCtrIfIndex,
       "nwIpxNetBIOSIfCtrAdminStatus": nwIpxNetBIOSIfCtrAdminStatus,
       "nwIpxNetBIOSIfCtrReset": nwIpxNetBIOSIfCtrReset,
       "nwIpxNetBIOSIfCtrOperationalTime": nwIpxNetBIOSIfCtrOperationalTime,
       "nwIpxNetBIOSIfCtrInPkts": nwIpxNetBIOSIfCtrInPkts,
       "nwIpxNetBIOSIfCtrOutPkts": nwIpxNetBIOSIfCtrOutPkts,
       "nwIpxNetBIOSIfCtrFilteredPkts": nwIpxNetBIOSIfCtrFilteredPkts,
       "nwIpxNetBIOSIfCtrDiscardPkts": nwIpxNetBIOSIfCtrDiscardPkts,
       "nwIpxNetBIOSIfCtrInBytes": nwIpxNetBIOSIfCtrInBytes,
       "nwIpxNetBIOSIfCtrOutBytes": nwIpxNetBIOSIfCtrOutBytes,
       "nwIpxNetBIOSIfCtrFilteredBytes": nwIpxNetBIOSIfCtrFilteredBytes,
       "nwIpxNetBIOSIfCtrDiscardBytes": nwIpxNetBIOSIfCtrDiscardBytes,
       "nwIpxBroadcast": nwIpxBroadcast,
       "nwIpxBroadcastSystem": nwIpxBroadcastSystem,
       "nwIpxBroadcastConfig": nwIpxBroadcastConfig,
       "nwIpxBcastAdminStatus": nwIpxBcastAdminStatus,
       "nwIpxBcastOperStatus": nwIpxBcastOperStatus,
       "nwIpxBcastAdminReset": nwIpxBcastAdminReset,
       "nwIpxBcastOperationalTime": nwIpxBcastOperationalTime,
       "nwIpxBcastVersion": nwIpxBcastVersion,
       "nwIpxBroadcastCounters": nwIpxBroadcastCounters,
       "nwIpxBcastCtrAdminStatus": nwIpxBcastCtrAdminStatus,
       "nwIpxBcastCtrReset": nwIpxBcastCtrReset,
       "nwIpxBcastCtrOperationalTime": nwIpxBcastCtrOperationalTime,
       "nwIpxBcastCtrInPkts": nwIpxBcastCtrInPkts,
       "nwIpxBcastCtrOutPkts": nwIpxBcastCtrOutPkts,
       "nwIpxBcastCtrFilteredPkts": nwIpxBcastCtrFilteredPkts,
       "nwIpxBcastCtrDiscardPkts": nwIpxBcastCtrDiscardPkts,
       "nwIpxBcastCtrInBytes": nwIpxBcastCtrInBytes,
       "nwIpxBcastCtrOutBytes": nwIpxBcastCtrOutBytes,
       "nwIpxBcastCtrFilteredBytes": nwIpxBcastCtrFilteredBytes,
       "nwIpxBcastCtrDiscardBytes": nwIpxBcastCtrDiscardBytes,
       "nwIpxBroadcastInterface": nwIpxBroadcastInterface,
       "nwIpxBroadcastIfConfig": nwIpxBroadcastIfConfig,
       "nwIpxBcastIfTable": nwIpxBcastIfTable,
       "nwIpxBcastIfEntry": nwIpxBcastIfEntry,
       "nwIpxBcastIfIndex": nwIpxBcastIfIndex,
       "nwIpxBcastIfAdminStatus": nwIpxBcastIfAdminStatus,
       "nwIpxBcastIfOperStatus": nwIpxBcastIfOperStatus,
       "nwIpxBcastIfOperationalTime": nwIpxBcastIfOperationalTime,
       "nwIpxBroadcastIfCounters": nwIpxBroadcastIfCounters,
       "nwIpxBcastIfCtrTable": nwIpxBcastIfCtrTable,
       "nwIpxBcastIfCtrEntry": nwIpxBcastIfCtrEntry,
       "nwIpxBcastIfCtrIfIndex": nwIpxBcastIfCtrIfIndex,
       "nwIpxBcastIfCtrAdminStatus": nwIpxBcastIfCtrAdminStatus,
       "nwIpxBcastIfCtrReset": nwIpxBcastIfCtrReset,
       "nwIpxBcastIfCtrOperationalTime": nwIpxBcastIfCtrOperationalTime,
       "nwIpxBcastIfCtrInPkts": nwIpxBcastIfCtrInPkts,
       "nwIpxBcastIfCtrOutPkts": nwIpxBcastIfCtrOutPkts,
       "nwIpxBcastIfCtrFilteredPkts": nwIpxBcastIfCtrFilteredPkts,
       "nwIpxBcastIfCtrDiscardPkts": nwIpxBcastIfCtrDiscardPkts,
       "nwIpxBcastIfCtrInBytes": nwIpxBcastIfCtrInBytes,
       "nwIpxBcastIfCtrOutBytes": nwIpxBcastIfCtrOutBytes,
       "nwIpxBcastIfCtrFilteredBytes": nwIpxBcastIfCtrFilteredBytes,
       "nwIpxBcastIfCtrDiscardBytes": nwIpxBcastIfCtrDiscardBytes,
       "nwIpxEcho": nwIpxEcho,
       "nwIpxEchoSystem": nwIpxEchoSystem,
       "nwIpxEchoConfig": nwIpxEchoConfig,
       "nwIpxEchoAdminStatus": nwIpxEchoAdminStatus,
       "nwIpxEchoOperStatus": nwIpxEchoOperStatus,
       "nwIpxEchoAdminReset": nwIpxEchoAdminReset,
       "nwIpxEchoOperationalTime": nwIpxEchoOperationalTime,
       "nwIpxEchoVersion": nwIpxEchoVersion,
       "nwIpxEchoCounters": nwIpxEchoCounters,
       "nwIpxEchoCtrAdminStatus": nwIpxEchoCtrAdminStatus,
       "nwIpxEchoCtrReset": nwIpxEchoCtrReset,
       "nwIpxEchoCtrOperationalTime": nwIpxEchoCtrOperationalTime,
       "nwIpxEchoCtrInPkts": nwIpxEchoCtrInPkts,
       "nwIpxEchoCtrOutPkts": nwIpxEchoCtrOutPkts,
       "nwIpxEchoCtrFilteredPkts": nwIpxEchoCtrFilteredPkts,
       "nwIpxEchoCtrDiscardPkts": nwIpxEchoCtrDiscardPkts,
       "nwIpxEchoCtrInBytes": nwIpxEchoCtrInBytes,
       "nwIpxEchoCtrOutBytes": nwIpxEchoCtrOutBytes,
       "nwIpxEchoCtrFilteredBytes": nwIpxEchoCtrFilteredBytes,
       "nwIpxEchoSCtrDiscardBytes": nwIpxEchoSCtrDiscardBytes,
       "nwIpxEchoInterface": nwIpxEchoInterface,
       "nwIpxEchoIfConfig": nwIpxEchoIfConfig,
       "nwIpxEchoIfTable": nwIpxEchoIfTable,
       "nwIpxEchoIfEntry": nwIpxEchoIfEntry,
       "nwIpxEchoIfIndex": nwIpxEchoIfIndex,
       "nwIpxEchoIfAdminStatus": nwIpxEchoIfAdminStatus,
       "nwIpxEchoIfOperStatus": nwIpxEchoIfOperStatus,
       "nwIpxEchoIfOperationalTime": nwIpxEchoIfOperationalTime,
       "nwIpxEchoIfCounters": nwIpxEchoIfCounters,
       "nwIpxEchoIfCtrTable": nwIpxEchoIfCtrTable,
       "nwIpxEchoIfCtrEntry": nwIpxEchoIfCtrEntry,
       "nwIpxEchoIfCtrIfIndex": nwIpxEchoIfCtrIfIndex,
       "nwIpxEchoIfCtrAdminStatus": nwIpxEchoIfCtrAdminStatus,
       "nwIpxEchoIfCtrReset": nwIpxEchoIfCtrReset,
       "nwIpxEchoIfCtrOperationalTime": nwIpxEchoIfCtrOperationalTime,
       "nwIpxEchoIfCtrInPkts": nwIpxEchoIfCtrInPkts,
       "nwIpxEchoIfCtrOutPkts": nwIpxEchoIfCtrOutPkts,
       "nwIpxEchoIfCtrFilteredPkts": nwIpxEchoIfCtrFilteredPkts,
       "nwIpxEchoIfCtrDiscardPkts": nwIpxEchoIfCtrDiscardPkts,
       "nwIpxEchoIfCtrInBytes": nwIpxEchoIfCtrInBytes,
       "nwIpxEchoIfCtrOutBytes": nwIpxEchoIfCtrOutBytes,
       "nwIpxEchoIfCtrFilteredBytes": nwIpxEchoIfCtrFilteredBytes,
       "nwIpxEchoIfCtrDiscardBytes": nwIpxEchoIfCtrDiscardBytes,
       "nwIpxEvent": nwIpxEvent,
       "nwIpxEventLogConfig": nwIpxEventLogConfig,
       "nwIpxEventAdminStatus": nwIpxEventAdminStatus,
       "nwIpxEventMaxEntries": nwIpxEventMaxEntries,
       "nwIpxEventTraceAll": nwIpxEventTraceAll,
       "nwIpxEventLogFilterTable": nwIpxEventLogFilterTable,
       "nwIpxEventFilterTable": nwIpxEventFilterTable,
       "nwIpxEventFilterEntry": nwIpxEventFilterEntry,
       "nwIpxEventFltrProtocol": nwIpxEventFltrProtocol,
       "nwIpxEventFltrIfNum": nwIpxEventFltrIfNum,
       "nwIpxEventFltrControl": nwIpxEventFltrControl,
       "nwIpxEventFltrType": nwIpxEventFltrType,
       "nwIpxEventFltrSeverity": nwIpxEventFltrSeverity,
       "nwIpxEventFltrAction": nwIpxEventFltrAction,
       "nwIpxEventLogTable": nwIpxEventLogTable,
       "nwIpxEventTable": nwIpxEventTable,
       "nwIpxEventEntry": nwIpxEventEntry,
       "nwIpxEventNumber": nwIpxEventNumber,
       "nwIpxEventTime": nwIpxEventTime,
       "nwIpxEventType": nwIpxEventType,
       "nwIpxEventSeverity": nwIpxEventSeverity,
       "nwIpxEventProtocol": nwIpxEventProtocol,
       "nwIpxEventIfNum": nwIpxEventIfNum,
       "nwIpxEventTextString": nwIpxEventTextString,
       "nwIpxWorkGroup": nwIpxWorkGroup}
)
