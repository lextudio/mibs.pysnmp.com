# SNMP MIB module (CTRON-AppleTalk-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-AppleTalk-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:33 2024
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

(nwRouter,
 nwRtrProtoSuites) = mibBuilder.importSymbols(
    "ROUTER-OIDS",
    "nwRouter",
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



class AtNetworkNumber(OctetString):
    """Custom type AtNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class AtDdpNodeAddress(OctetString):
    """Custom type AtDdpNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class AtName(OctetString):
    """Custom type AtName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NwAtRouter_ObjectIdentity = ObjectIdentity
nwAtRouter = _NwAtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4)
)
_NwAtMibs_ObjectIdentity = ObjectIdentity
nwAtMibs = _NwAtMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 1)
)
_NwAtMibRevText_Type = DisplayString
_NwAtMibRevText_Object = MibScalar
nwAtMibRevText = _NwAtMibRevText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 1, 1),
    _NwAtMibRevText_Type()
)
nwAtMibRevText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtMibRevText.setStatus("mandatory")
_NwAtComponents_ObjectIdentity = ObjectIdentity
nwAtComponents = _NwAtComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2)
)
_NwAtSystem_ObjectIdentity = ObjectIdentity
nwAtSystem = _NwAtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1)
)
_NwAtSysConfig_ObjectIdentity = ObjectIdentity
nwAtSysConfig = _NwAtSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 1)
)
_NwAtSysRouterId_Type = AtNetworkNumber
_NwAtSysRouterId_Object = MibScalar
nwAtSysRouterId = _NwAtSysRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 1, 1),
    _NwAtSysRouterId_Type()
)
nwAtSysRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtSysRouterId.setStatus("mandatory")
_NwAtSysAdministration_ObjectIdentity = ObjectIdentity
nwAtSysAdministration = _NwAtSysAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 2)
)


class _NwAtSysAdminSTATUS_Type(Integer32):
    """Custom type nwAtSysAdminSTATUS based on Integer32"""
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


_NwAtSysAdminSTATUS_Type.__name__ = "Integer32"
_NwAtSysAdminSTATUS_Object = MibScalar
nwAtSysAdminSTATUS = _NwAtSysAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 2, 1),
    _NwAtSysAdminSTATUS_Type()
)
nwAtSysAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtSysAdminSTATUS.setStatus("mandatory")


class _NwAtSysOperSTATUS_Type(Integer32):
    """Custom type nwAtSysOperSTATUS based on Integer32"""
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


_NwAtSysOperSTATUS_Type.__name__ = "Integer32"
_NwAtSysOperSTATUS_Object = MibScalar
nwAtSysOperSTATUS = _NwAtSysOperSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 2, 2),
    _NwAtSysOperSTATUS_Type()
)
nwAtSysOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtSysOperSTATUS.setStatus("mandatory")


class _NwAtSysAdminReset_Type(Integer32):
    """Custom type nwAtSysAdminReset based on Integer32"""
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


_NwAtSysAdminReset_Type.__name__ = "Integer32"
_NwAtSysAdminReset_Object = MibScalar
nwAtSysAdminReset = _NwAtSysAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 2, 3),
    _NwAtSysAdminReset_Type()
)
nwAtSysAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtSysAdminReset.setStatus("mandatory")
_NwAtSysOperationalTime_Type = TimeTicks
_NwAtSysOperationalTime_Object = MibScalar
nwAtSysOperationalTime = _NwAtSysOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 2, 4),
    _NwAtSysOperationalTime_Type()
)
nwAtSysOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtSysOperationalTime.setStatus("mandatory")
_NwAtSysVersion_Type = DisplayString
_NwAtSysVersion_Object = MibScalar
nwAtSysVersion = _NwAtSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 1, 2, 5),
    _NwAtSysVersion_Type()
)
nwAtSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtSysVersion.setStatus("mandatory")
_NwAtForwarding_ObjectIdentity = ObjectIdentity
nwAtForwarding = _NwAtForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2)
)
_NwAtFwdSystem_ObjectIdentity = ObjectIdentity
nwAtFwdSystem = _NwAtFwdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1)
)
_NwAtFwdCounters_ObjectIdentity = ObjectIdentity
nwAtFwdCounters = _NwAtFwdCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1)
)


class _NwAtFwdCtrAdminSTATUS_Type(Integer32):
    """Custom type nwAtFwdCtrAdminSTATUS based on Integer32"""
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


_NwAtFwdCtrAdminSTATUS_Type.__name__ = "Integer32"
_NwAtFwdCtrAdminSTATUS_Object = MibScalar
nwAtFwdCtrAdminSTATUS = _NwAtFwdCtrAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 1),
    _NwAtFwdCtrAdminSTATUS_Type()
)
nwAtFwdCtrAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdCtrAdminSTATUS.setStatus("mandatory")


class _NwAtFwdCtrReset_Type(Integer32):
    """Custom type nwAtFwdCtrReset based on Integer32"""
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


_NwAtFwdCtrReset_Type.__name__ = "Integer32"
_NwAtFwdCtrReset_Object = MibScalar
nwAtFwdCtrReset = _NwAtFwdCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 2),
    _NwAtFwdCtrReset_Type()
)
nwAtFwdCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdCtrReset.setStatus("mandatory")
_NwAtFwdCtrOperationalTime_Type = TimeTicks
_NwAtFwdCtrOperationalTime_Object = MibScalar
nwAtFwdCtrOperationalTime = _NwAtFwdCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 3),
    _NwAtFwdCtrOperationalTime_Type()
)
nwAtFwdCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrOperationalTime.setStatus("mandatory")
_NwAtFwdCtrInPkts_Type = Counter32
_NwAtFwdCtrInPkts_Object = MibScalar
nwAtFwdCtrInPkts = _NwAtFwdCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 4),
    _NwAtFwdCtrInPkts_Type()
)
nwAtFwdCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrInPkts.setStatus("mandatory")
_NwAtFwdCtrOutPkts_Type = Counter32
_NwAtFwdCtrOutPkts_Object = MibScalar
nwAtFwdCtrOutPkts = _NwAtFwdCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 5),
    _NwAtFwdCtrOutPkts_Type()
)
nwAtFwdCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrOutPkts.setStatus("mandatory")
_NwAtFwdCtrFwdPkts_Type = Counter32
_NwAtFwdCtrFwdPkts_Object = MibScalar
nwAtFwdCtrFwdPkts = _NwAtFwdCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 6),
    _NwAtFwdCtrFwdPkts_Type()
)
nwAtFwdCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrFwdPkts.setStatus("mandatory")
_NwAtFwdCtrFilteredPkts_Type = Counter32
_NwAtFwdCtrFilteredPkts_Object = MibScalar
nwAtFwdCtrFilteredPkts = _NwAtFwdCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 7),
    _NwAtFwdCtrFilteredPkts_Type()
)
nwAtFwdCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrFilteredPkts.setStatus("mandatory")
_NwAtFwdCtrDiscardPkts_Type = Counter32
_NwAtFwdCtrDiscardPkts_Object = MibScalar
nwAtFwdCtrDiscardPkts = _NwAtFwdCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 8),
    _NwAtFwdCtrDiscardPkts_Type()
)
nwAtFwdCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrDiscardPkts.setStatus("mandatory")
_NwAtFwdCtrAddrErrPkts_Type = Counter32
_NwAtFwdCtrAddrErrPkts_Object = MibScalar
nwAtFwdCtrAddrErrPkts = _NwAtFwdCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 9),
    _NwAtFwdCtrAddrErrPkts_Type()
)
nwAtFwdCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrAddrErrPkts.setStatus("mandatory")
_NwAtFwdCtrLenErrPkts_Type = Counter32
_NwAtFwdCtrLenErrPkts_Object = MibScalar
nwAtFwdCtrLenErrPkts = _NwAtFwdCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 10),
    _NwAtFwdCtrLenErrPkts_Type()
)
nwAtFwdCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrLenErrPkts.setStatus("mandatory")
_NwAtFwdCtrHdrErrPkts_Type = Counter32
_NwAtFwdCtrHdrErrPkts_Object = MibScalar
nwAtFwdCtrHdrErrPkts = _NwAtFwdCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 11),
    _NwAtFwdCtrHdrErrPkts_Type()
)
nwAtFwdCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrHdrErrPkts.setStatus("mandatory")
_NwAtFwdCtrInBytes_Type = Counter32
_NwAtFwdCtrInBytes_Object = MibScalar
nwAtFwdCtrInBytes = _NwAtFwdCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 12),
    _NwAtFwdCtrInBytes_Type()
)
nwAtFwdCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrInBytes.setStatus("mandatory")
_NwAtFwdCtrOutBytes_Type = Counter32
_NwAtFwdCtrOutBytes_Object = MibScalar
nwAtFwdCtrOutBytes = _NwAtFwdCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 13),
    _NwAtFwdCtrOutBytes_Type()
)
nwAtFwdCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrOutBytes.setStatus("mandatory")
_NwAtFwdCtrFwdBytes_Type = Counter32
_NwAtFwdCtrFwdBytes_Object = MibScalar
nwAtFwdCtrFwdBytes = _NwAtFwdCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 14),
    _NwAtFwdCtrFwdBytes_Type()
)
nwAtFwdCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrFwdBytes.setStatus("mandatory")
_NwAtFwdCtrFilteredBytes_Type = Counter32
_NwAtFwdCtrFilteredBytes_Object = MibScalar
nwAtFwdCtrFilteredBytes = _NwAtFwdCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 15),
    _NwAtFwdCtrFilteredBytes_Type()
)
nwAtFwdCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrFilteredBytes.setStatus("mandatory")
_NwAtFwdCtrDiscardBytes_Type = Counter32
_NwAtFwdCtrDiscardBytes_Object = MibScalar
nwAtFwdCtrDiscardBytes = _NwAtFwdCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 16),
    _NwAtFwdCtrDiscardBytes_Type()
)
nwAtFwdCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrDiscardBytes.setStatus("mandatory")
_NwAtFwdCtrHostInPkts_Type = Counter32
_NwAtFwdCtrHostInPkts_Object = MibScalar
nwAtFwdCtrHostInPkts = _NwAtFwdCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 17),
    _NwAtFwdCtrHostInPkts_Type()
)
nwAtFwdCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrHostInPkts.setStatus("mandatory")
_NwAtFwdCtrHostOutPkts_Type = Counter32
_NwAtFwdCtrHostOutPkts_Object = MibScalar
nwAtFwdCtrHostOutPkts = _NwAtFwdCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 18),
    _NwAtFwdCtrHostOutPkts_Type()
)
nwAtFwdCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrHostOutPkts.setStatus("mandatory")
_NwAtFwdCtrHostDiscardPkts_Type = Counter32
_NwAtFwdCtrHostDiscardPkts_Object = MibScalar
nwAtFwdCtrHostDiscardPkts = _NwAtFwdCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 19),
    _NwAtFwdCtrHostDiscardPkts_Type()
)
nwAtFwdCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrHostDiscardPkts.setStatus("mandatory")
_NwAtFwdCtrHostInBytes_Type = Counter32
_NwAtFwdCtrHostInBytes_Object = MibScalar
nwAtFwdCtrHostInBytes = _NwAtFwdCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 20),
    _NwAtFwdCtrHostInBytes_Type()
)
nwAtFwdCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrHostInBytes.setStatus("mandatory")
_NwAtFwdCtrHostOutBytes_Type = Counter32
_NwAtFwdCtrHostOutBytes_Object = MibScalar
nwAtFwdCtrHostOutBytes = _NwAtFwdCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 21),
    _NwAtFwdCtrHostOutBytes_Type()
)
nwAtFwdCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrHostOutBytes.setStatus("mandatory")
_NwAtFwdCtrHostDiscardBytes_Type = Counter32
_NwAtFwdCtrHostDiscardBytes_Object = MibScalar
nwAtFwdCtrHostDiscardBytes = _NwAtFwdCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 1, 1, 22),
    _NwAtFwdCtrHostDiscardBytes_Type()
)
nwAtFwdCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdCtrHostDiscardBytes.setStatus("mandatory")
_NwAtFwdInterfaces_ObjectIdentity = ObjectIdentity
nwAtFwdInterfaces = _NwAtFwdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2)
)
_NwAtFwdIfConfig_ObjectIdentity = ObjectIdentity
nwAtFwdIfConfig = _NwAtFwdIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1)
)
_NwAtFwdIfTable_Object = MibTable
nwAtFwdIfTable = _NwAtFwdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwAtFwdIfTable.setStatus("mandatory")
_NwAtFwdIfEntry_Object = MibTableRow
nwAtFwdIfEntry = _NwAtFwdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1)
)
nwAtFwdIfEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtFwdIfIndex"),
)
if mibBuilder.loadTexts:
    nwAtFwdIfEntry.setStatus("mandatory")
_NwAtFwdIfIndex_Type = Integer32
_NwAtFwdIfIndex_Object = MibTableColumn
nwAtFwdIfIndex = _NwAtFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 1),
    _NwAtFwdIfIndex_Type()
)
nwAtFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfIndex.setStatus("mandatory")


class _NwAtFwdIfAdminSTATUS_Type(Integer32):
    """Custom type nwAtFwdIfAdminSTATUS based on Integer32"""
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


_NwAtFwdIfAdminSTATUS_Type.__name__ = "Integer32"
_NwAtFwdIfAdminSTATUS_Object = MibTableColumn
nwAtFwdIfAdminSTATUS = _NwAtFwdIfAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 2),
    _NwAtFwdIfAdminSTATUS_Type()
)
nwAtFwdIfAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfAdminSTATUS.setStatus("mandatory")


class _NwAtFwdIfOperSTATUS_Type(Integer32):
    """Custom type nwAtFwdIfOperSTATUS based on Integer32"""
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


_NwAtFwdIfOperSTATUS_Type.__name__ = "Integer32"
_NwAtFwdIfOperSTATUS_Object = MibTableColumn
nwAtFwdIfOperSTATUS = _NwAtFwdIfOperSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 3),
    _NwAtFwdIfOperSTATUS_Type()
)
nwAtFwdIfOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfOperSTATUS.setStatus("mandatory")
_NwAtFwdIfOperationalTime_Type = TimeTicks
_NwAtFwdIfOperationalTime_Object = MibTableColumn
nwAtFwdIfOperationalTime = _NwAtFwdIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 4),
    _NwAtFwdIfOperationalTime_Type()
)
nwAtFwdIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfOperationalTime.setStatus("mandatory")


class _NwAtFwdIfControl_Type(Integer32):
    """Custom type nwAtFwdIfControl based on Integer32"""
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


_NwAtFwdIfControl_Type.__name__ = "Integer32"
_NwAtFwdIfControl_Object = MibTableColumn
nwAtFwdIfControl = _NwAtFwdIfControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 5),
    _NwAtFwdIfControl_Type()
)
nwAtFwdIfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfControl.setStatus("mandatory")
_NwAtFwdIfMtu_Type = Integer32
_NwAtFwdIfMtu_Object = MibTableColumn
nwAtFwdIfMtu = _NwAtFwdIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 6),
    _NwAtFwdIfMtu_Type()
)
nwAtFwdIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfMtu.setStatus("mandatory")


class _NwAtFwdIfForwarding_Type(Integer32):
    """Custom type nwAtFwdIfForwarding based on Integer32"""
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


_NwAtFwdIfForwarding_Type.__name__ = "Integer32"
_NwAtFwdIfForwarding_Object = MibTableColumn
nwAtFwdIfForwarding = _NwAtFwdIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 7),
    _NwAtFwdIfForwarding_Type()
)
nwAtFwdIfForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfForwarding.setStatus("mandatory")


class _NwAtFwdIfFrameType_Type(Integer32):
    """Custom type nwAtFwdIfFrameType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              9,
              11,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 17),
          ("encapenet", 9),
          ("encapenetsnap", 11),
          ("encapfddisnap", 16),
          ("ethernet", 2),
          ("nativewan", 8),
          ("other", 1),
          ("snap", 3))
    )


_NwAtFwdIfFrameType_Type.__name__ = "Integer32"
_NwAtFwdIfFrameType_Object = MibTableColumn
nwAtFwdIfFrameType = _NwAtFwdIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 8),
    _NwAtFwdIfFrameType_Type()
)
nwAtFwdIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfFrameType.setStatus("mandatory")
_NwAtFwdIfAclIdentifier_Type = Integer32
_NwAtFwdIfAclIdentifier_Object = MibTableColumn
nwAtFwdIfAclIdentifier = _NwAtFwdIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 9),
    _NwAtFwdIfAclIdentifier_Type()
)
nwAtFwdIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfAclIdentifier.setStatus("mandatory")


class _NwAtFwdIfAclSTATUS_Type(Integer32):
    """Custom type nwAtFwdIfAclSTATUS based on Integer32"""
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


_NwAtFwdIfAclSTATUS_Type.__name__ = "Integer32"
_NwAtFwdIfAclSTATUS_Object = MibTableColumn
nwAtFwdIfAclSTATUS = _NwAtFwdIfAclSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 10),
    _NwAtFwdIfAclSTATUS_Type()
)
nwAtFwdIfAclSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfAclSTATUS.setStatus("mandatory")


class _NwAtFwdIfCacheControl_Type(Integer32):
    """Custom type nwAtFwdIfCacheControl based on Integer32"""
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


_NwAtFwdIfCacheControl_Type.__name__ = "Integer32"
_NwAtFwdIfCacheControl_Object = MibTableColumn
nwAtFwdIfCacheControl = _NwAtFwdIfCacheControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 11),
    _NwAtFwdIfCacheControl_Type()
)
nwAtFwdIfCacheControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfCacheControl.setStatus("mandatory")
_NwAtFwdIfCacheEntries_Type = Counter32
_NwAtFwdIfCacheEntries_Object = MibTableColumn
nwAtFwdIfCacheEntries = _NwAtFwdIfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 12),
    _NwAtFwdIfCacheEntries_Type()
)
nwAtFwdIfCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCacheEntries.setStatus("mandatory")
_NwAtFwdIfCacheHits_Type = Counter32
_NwAtFwdIfCacheHits_Object = MibTableColumn
nwAtFwdIfCacheHits = _NwAtFwdIfCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 13),
    _NwAtFwdIfCacheHits_Type()
)
nwAtFwdIfCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCacheHits.setStatus("mandatory")
_NwAtFwdIfCacheMisses_Type = Counter32
_NwAtFwdIfCacheMisses_Object = MibTableColumn
nwAtFwdIfCacheMisses = _NwAtFwdIfCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 1, 1, 14),
    _NwAtFwdIfCacheMisses_Type()
)
nwAtFwdIfCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCacheMisses.setStatus("mandatory")
_NwAtportTable_Object = MibTable
nwAtportTable = _NwAtportTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nwAtportTable.setStatus("mandatory")
_NwAtportEntry_Object = MibTableRow
nwAtportEntry = _NwAtportEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1)
)
nwAtportEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtportIndex"),
)
if mibBuilder.loadTexts:
    nwAtportEntry.setStatus("mandatory")
_NwAtportIndex_Type = Integer32
_NwAtportIndex_Object = MibTableColumn
nwAtportIndex = _NwAtportIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 1),
    _NwAtportIndex_Type()
)
nwAtportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportIndex.setStatus("mandatory")
_NwAtportDescr_Type = DisplayString
_NwAtportDescr_Object = MibTableColumn
nwAtportDescr = _NwAtportDescr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 2),
    _NwAtportDescr_Type()
)
nwAtportDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportDescr.setStatus("mandatory")


class _NwAtportType_Type(Integer32):
    """Custom type nwAtportType based on Integer32"""
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
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("arap", 19),
          ("arctalk", 11),
          ("arns", 23),
          ("aurp", 13),
          ("decnetIV", 18),
          ("ethertalk1", 3),
          ("ethertalk2", 4),
          ("fdditalk", 10),
          ("frameRelay", 14),
          ("hdlc", 24),
          ("ip", 16),
          ("iptalk", 6),
          ("ipx", 22),
          ("isdnInThePacketMode", 20),
          ("localtalk", 2),
          ("nonAppleTalk3Com", 21),
          ("osi", 17),
          ("other", 1),
          ("serialNonstandard", 8),
          ("serialPPP", 7),
          ("smdstalk", 12),
          ("tokentalk", 5),
          ("virtual", 9),
          ("x25", 15))
    )


_NwAtportType_Type.__name__ = "Integer32"
_NwAtportType_Object = MibTableColumn
nwAtportType = _NwAtportType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 3),
    _NwAtportType_Type()
)
nwAtportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportType.setStatus("mandatory")
_NwAtportNetStart_Type = AtNetworkNumber
_NwAtportNetStart_Object = MibTableColumn
nwAtportNetStart = _NwAtportNetStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 4),
    _NwAtportNetStart_Type()
)
nwAtportNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportNetStart.setStatus("mandatory")
_NwAtportNetEnd_Type = AtNetworkNumber
_NwAtportNetEnd_Object = MibTableColumn
nwAtportNetEnd = _NwAtportNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 5),
    _NwAtportNetEnd_Type()
)
nwAtportNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportNetEnd.setStatus("mandatory")
_NwAtportNetAddress_Type = AtDdpNodeAddress
_NwAtportNetAddress_Object = MibTableColumn
nwAtportNetAddress = _NwAtportNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 6),
    _NwAtportNetAddress_Type()
)
nwAtportNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportNetAddress.setStatus("mandatory")


class _NwAtportSTATUS_Type(Integer32):
    """Custom type nwAtportSTATUS based on Integer32"""
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
        *(("endNode", 5),
          ("invalid", 4),
          ("off", 3),
          ("offDueToConflict", 6),
          ("other", 7),
          ("routing", 1),
          ("unconfigured", 2))
    )


_NwAtportSTATUS_Type.__name__ = "Integer32"
_NwAtportSTATUS_Object = MibTableColumn
nwAtportSTATUS = _NwAtportSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 7),
    _NwAtportSTATUS_Type()
)
nwAtportSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportSTATUS.setStatus("mandatory")


class _NwAtportNetConfig_Type(Integer32):
    """Custom type nwAtportNetConfig based on Integer32"""
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
        *(("conflictAverseSeed", 5),
          ("conflictOrientedSeed", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("softSeed", 6),
          ("unconfigured", 4))
    )


_NwAtportNetConfig_Type.__name__ = "Integer32"
_NwAtportNetConfig_Object = MibTableColumn
nwAtportNetConfig = _NwAtportNetConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 8),
    _NwAtportNetConfig_Type()
)
nwAtportNetConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportNetConfig.setStatus("mandatory")


class _NwAtportZoneConfig_Type(Integer32):
    """Custom type nwAtportZoneConfig based on Integer32"""
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
        *(("conflictAverseSeed", 5),
          ("conflictOrientedSeed", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("softSeed", 6),
          ("unconfigured", 4))
    )


_NwAtportZoneConfig_Type.__name__ = "Integer32"
_NwAtportZoneConfig_Object = MibTableColumn
nwAtportZoneConfig = _NwAtportZoneConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 9),
    _NwAtportZoneConfig_Type()
)
nwAtportZoneConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportZoneConfig.setStatus("mandatory")
_NwAtportZoneDefault_Type = AtName
_NwAtportZoneDefault_Object = MibTableColumn
nwAtportZoneDefault = _NwAtportZoneDefault_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 10),
    _NwAtportZoneDefault_Type()
)
nwAtportZoneDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportZoneDefault.setStatus("mandatory")
_NwAtportIfIndex_Type = Integer32
_NwAtportIfIndex_Object = MibTableColumn
nwAtportIfIndex = _NwAtportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 11),
    _NwAtportIfIndex_Type()
)
nwAtportIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportIfIndex.setStatus("mandatory")
_NwAtportNetFrom_Type = AtDdpNodeAddress
_NwAtportNetFrom_Object = MibTableColumn
nwAtportNetFrom = _NwAtportNetFrom_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 12),
    _NwAtportNetFrom_Type()
)
nwAtportNetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportNetFrom.setStatus("mandatory")
_NwAtportZoneFrom_Type = AtDdpNodeAddress
_NwAtportZoneFrom_Object = MibTableColumn
nwAtportZoneFrom = _NwAtportZoneFrom_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 13),
    _NwAtportZoneFrom_Type()
)
nwAtportZoneFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportZoneFrom.setStatus("mandatory")
_NwAtportInPkts_Type = Counter32
_NwAtportInPkts_Object = MibTableColumn
nwAtportInPkts = _NwAtportInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 14),
    _NwAtportInPkts_Type()
)
nwAtportInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportInPkts.setStatus("mandatory")
_NwAtportOutPkts_Type = Counter32
_NwAtportOutPkts_Object = MibTableColumn
nwAtportOutPkts = _NwAtportOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 15),
    _NwAtportOutPkts_Type()
)
nwAtportOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportOutPkts.setStatus("mandatory")


class _NwAtportHome_Type(Integer32):
    """Custom type nwAtportHome based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("home", 1),
          ("notHome", 2))
    )


_NwAtportHome_Type.__name__ = "Integer32"
_NwAtportHome_Object = MibTableColumn
nwAtportHome = _NwAtportHome_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 16),
    _NwAtportHome_Type()
)
nwAtportHome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportHome.setStatus("mandatory")
_NwAtportCurrentZone_Type = AtName
_NwAtportCurrentZone_Object = MibTableColumn
nwAtportCurrentZone = _NwAtportCurrentZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 17),
    _NwAtportCurrentZone_Type()
)
nwAtportCurrentZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportCurrentZone.setStatus("mandatory")
_NwAtportConflictPhysAddr_Type = OctetString
_NwAtportConflictPhysAddr_Object = MibTableColumn
nwAtportConflictPhysAddr = _NwAtportConflictPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 1, 2, 1, 18),
    _NwAtportConflictPhysAddr_Type()
)
nwAtportConflictPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportConflictPhysAddr.setStatus("mandatory")
_NwAtFwdIfCounters_ObjectIdentity = ObjectIdentity
nwAtFwdIfCounters = _NwAtFwdIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2)
)
_NwAtFwdIfCtrTable_Object = MibTable
nwAtFwdIfCtrTable = _NwAtFwdIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwAtFwdIfCtrTable.setStatus("mandatory")
_NwAtFwdIfCtrEntry_Object = MibTableRow
nwAtFwdIfCtrEntry = _NwAtFwdIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1)
)
nwAtFwdIfCtrEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtFwdIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwAtFwdIfCtrEntry.setStatus("mandatory")
_NwAtFwdIfCtrIfIndex_Type = Integer32
_NwAtFwdIfCtrIfIndex_Object = MibTableColumn
nwAtFwdIfCtrIfIndex = _NwAtFwdIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 1),
    _NwAtFwdIfCtrIfIndex_Type()
)
nwAtFwdIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrIfIndex.setStatus("mandatory")


class _NwAtFwdIfCtrAdminSTATUS_Type(Integer32):
    """Custom type nwAtFwdIfCtrAdminSTATUS based on Integer32"""
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


_NwAtFwdIfCtrAdminSTATUS_Type.__name__ = "Integer32"
_NwAtFwdIfCtrAdminSTATUS_Object = MibTableColumn
nwAtFwdIfCtrAdminSTATUS = _NwAtFwdIfCtrAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 2),
    _NwAtFwdIfCtrAdminSTATUS_Type()
)
nwAtFwdIfCtrAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrAdminSTATUS.setStatus("mandatory")


class _NwAtFwdIfCtrReset_Type(Integer32):
    """Custom type nwAtFwdIfCtrReset based on Integer32"""
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


_NwAtFwdIfCtrReset_Type.__name__ = "Integer32"
_NwAtFwdIfCtrReset_Object = MibTableColumn
nwAtFwdIfCtrReset = _NwAtFwdIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 3),
    _NwAtFwdIfCtrReset_Type()
)
nwAtFwdIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrReset.setStatus("mandatory")
_NwAtFwdIfCtrOperationalTime_Type = TimeTicks
_NwAtFwdIfCtrOperationalTime_Object = MibTableColumn
nwAtFwdIfCtrOperationalTime = _NwAtFwdIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 4),
    _NwAtFwdIfCtrOperationalTime_Type()
)
nwAtFwdIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrOperationalTime.setStatus("mandatory")
_NwAtFwdIfCtrInPkts_Type = Counter32
_NwAtFwdIfCtrInPkts_Object = MibTableColumn
nwAtFwdIfCtrInPkts = _NwAtFwdIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 5),
    _NwAtFwdIfCtrInPkts_Type()
)
nwAtFwdIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrInPkts.setStatus("mandatory")
_NwAtFwdIfCtrOutPkts_Type = Counter32
_NwAtFwdIfCtrOutPkts_Object = MibTableColumn
nwAtFwdIfCtrOutPkts = _NwAtFwdIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 6),
    _NwAtFwdIfCtrOutPkts_Type()
)
nwAtFwdIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrOutPkts.setStatus("mandatory")
_NwAtFwdIfCtrFwdPkts_Type = Counter32
_NwAtFwdIfCtrFwdPkts_Object = MibTableColumn
nwAtFwdIfCtrFwdPkts = _NwAtFwdIfCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 7),
    _NwAtFwdIfCtrFwdPkts_Type()
)
nwAtFwdIfCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrFwdPkts.setStatus("mandatory")
_NwAtFwdIfCtrFilteredPkts_Type = Counter32
_NwAtFwdIfCtrFilteredPkts_Object = MibTableColumn
nwAtFwdIfCtrFilteredPkts = _NwAtFwdIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 8),
    _NwAtFwdIfCtrFilteredPkts_Type()
)
nwAtFwdIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrFilteredPkts.setStatus("mandatory")
_NwAtFwdIfCtrDiscardPkts_Type = Counter32
_NwAtFwdIfCtrDiscardPkts_Object = MibTableColumn
nwAtFwdIfCtrDiscardPkts = _NwAtFwdIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 9),
    _NwAtFwdIfCtrDiscardPkts_Type()
)
nwAtFwdIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrDiscardPkts.setStatus("mandatory")
_NwAtFwdIfCtrAddrErrPkts_Type = Counter32
_NwAtFwdIfCtrAddrErrPkts_Object = MibTableColumn
nwAtFwdIfCtrAddrErrPkts = _NwAtFwdIfCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 10),
    _NwAtFwdIfCtrAddrErrPkts_Type()
)
nwAtFwdIfCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrAddrErrPkts.setStatus("mandatory")
_NwAtFwdIfCtrLenErrPkts_Type = Counter32
_NwAtFwdIfCtrLenErrPkts_Object = MibTableColumn
nwAtFwdIfCtrLenErrPkts = _NwAtFwdIfCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 11),
    _NwAtFwdIfCtrLenErrPkts_Type()
)
nwAtFwdIfCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrLenErrPkts.setStatus("mandatory")
_NwAtFwdIfCtrHdrErrPkts_Type = Counter32
_NwAtFwdIfCtrHdrErrPkts_Object = MibTableColumn
nwAtFwdIfCtrHdrErrPkts = _NwAtFwdIfCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 12),
    _NwAtFwdIfCtrHdrErrPkts_Type()
)
nwAtFwdIfCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrHdrErrPkts.setStatus("mandatory")
_NwAtFwdIfCtrInBytes_Type = Counter32
_NwAtFwdIfCtrInBytes_Object = MibTableColumn
nwAtFwdIfCtrInBytes = _NwAtFwdIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 13),
    _NwAtFwdIfCtrInBytes_Type()
)
nwAtFwdIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrInBytes.setStatus("mandatory")
_NwAtFwdIfCtrOutBytes_Type = Counter32
_NwAtFwdIfCtrOutBytes_Object = MibTableColumn
nwAtFwdIfCtrOutBytes = _NwAtFwdIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 14),
    _NwAtFwdIfCtrOutBytes_Type()
)
nwAtFwdIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrOutBytes.setStatus("mandatory")
_NwAtFwdIfCtrFwdBytes_Type = Counter32
_NwAtFwdIfCtrFwdBytes_Object = MibTableColumn
nwAtFwdIfCtrFwdBytes = _NwAtFwdIfCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 15),
    _NwAtFwdIfCtrFwdBytes_Type()
)
nwAtFwdIfCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrFwdBytes.setStatus("mandatory")
_NwAtFwdIfCtrFilteredBytes_Type = Counter32
_NwAtFwdIfCtrFilteredBytes_Object = MibTableColumn
nwAtFwdIfCtrFilteredBytes = _NwAtFwdIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 16),
    _NwAtFwdIfCtrFilteredBytes_Type()
)
nwAtFwdIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrFilteredBytes.setStatus("mandatory")
_NwAtFwdIfCtrDiscardBytes_Type = Counter32
_NwAtFwdIfCtrDiscardBytes_Object = MibTableColumn
nwAtFwdIfCtrDiscardBytes = _NwAtFwdIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 17),
    _NwAtFwdIfCtrDiscardBytes_Type()
)
nwAtFwdIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrDiscardBytes.setStatus("mandatory")
_NwAtFwdIfCtrHostInPkts_Type = Counter32
_NwAtFwdIfCtrHostInPkts_Object = MibTableColumn
nwAtFwdIfCtrHostInPkts = _NwAtFwdIfCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 18),
    _NwAtFwdIfCtrHostInPkts_Type()
)
nwAtFwdIfCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrHostInPkts.setStatus("mandatory")
_NwAtFwdIfCtrHostOutPkts_Type = Counter32
_NwAtFwdIfCtrHostOutPkts_Object = MibTableColumn
nwAtFwdIfCtrHostOutPkts = _NwAtFwdIfCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 19),
    _NwAtFwdIfCtrHostOutPkts_Type()
)
nwAtFwdIfCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrHostOutPkts.setStatus("mandatory")
_NwAtFwdIfCtrHostDiscardPkts_Type = Counter32
_NwAtFwdIfCtrHostDiscardPkts_Object = MibTableColumn
nwAtFwdIfCtrHostDiscardPkts = _NwAtFwdIfCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 20),
    _NwAtFwdIfCtrHostDiscardPkts_Type()
)
nwAtFwdIfCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrHostDiscardPkts.setStatus("mandatory")
_NwAtFwdIfCtrHostInBytes_Type = Counter32
_NwAtFwdIfCtrHostInBytes_Object = MibTableColumn
nwAtFwdIfCtrHostInBytes = _NwAtFwdIfCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 21),
    _NwAtFwdIfCtrHostInBytes_Type()
)
nwAtFwdIfCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrHostInBytes.setStatus("mandatory")
_NwAtFwdIfCtrHostOutBytes_Type = Counter32
_NwAtFwdIfCtrHostOutBytes_Object = MibTableColumn
nwAtFwdIfCtrHostOutBytes = _NwAtFwdIfCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 22),
    _NwAtFwdIfCtrHostOutBytes_Type()
)
nwAtFwdIfCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrHostOutBytes.setStatus("mandatory")
_NwAtFwdIfCtrHostDiscardBytes_Type = Counter32
_NwAtFwdIfCtrHostDiscardBytes_Object = MibTableColumn
nwAtFwdIfCtrHostDiscardBytes = _NwAtFwdIfCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 2, 2, 2, 1, 1, 23),
    _NwAtFwdIfCtrHostDiscardBytes_Type()
)
nwAtFwdIfCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFwdIfCtrHostDiscardBytes.setStatus("mandatory")
_NwAtTopology_ObjectIdentity = ObjectIdentity
nwAtTopology = _NwAtTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4)
)
_NwAtDistanceVector_ObjectIdentity = ObjectIdentity
nwAtDistanceVector = _NwAtDistanceVector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1)
)
_NwAtProto_ObjectIdentity = ObjectIdentity
nwAtProto = _NwAtProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1)
)
_NwAtProtoSystem_ObjectIdentity = ObjectIdentity
nwAtProtoSystem = _NwAtProtoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1)
)
_NwAtProtoConfig_ObjectIdentity = ObjectIdentity
nwAtProtoConfig = _NwAtProtoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1)
)


class _NwAtProtoAdminSTATUS_Type(Integer32):
    """Custom type nwAtProtoAdminSTATUS based on Integer32"""
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


_NwAtProtoAdminSTATUS_Type.__name__ = "Integer32"
_NwAtProtoAdminSTATUS_Object = MibScalar
nwAtProtoAdminSTATUS = _NwAtProtoAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 1),
    _NwAtProtoAdminSTATUS_Type()
)
nwAtProtoAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoAdminSTATUS.setStatus("mandatory")


class _NwAtProtoOperSTATUS_Type(Integer32):
    """Custom type nwAtProtoOperSTATUS based on Integer32"""
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


_NwAtProtoOperSTATUS_Type.__name__ = "Integer32"
_NwAtProtoOperSTATUS_Object = MibScalar
nwAtProtoOperSTATUS = _NwAtProtoOperSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 2),
    _NwAtProtoOperSTATUS_Type()
)
nwAtProtoOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoOperSTATUS.setStatus("mandatory")


class _NwAtProtoAdminReset_Type(Integer32):
    """Custom type nwAtProtoAdminReset based on Integer32"""
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


_NwAtProtoAdminReset_Type.__name__ = "Integer32"
_NwAtProtoAdminReset_Object = MibScalar
nwAtProtoAdminReset = _NwAtProtoAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 3),
    _NwAtProtoAdminReset_Type()
)
nwAtProtoAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoAdminReset.setStatus("mandatory")
_NwAtProtoOperationalTime_Type = TimeTicks
_NwAtProtoOperationalTime_Object = MibScalar
nwAtProtoOperationalTime = _NwAtProtoOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 4),
    _NwAtProtoOperationalTime_Type()
)
nwAtProtoOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoOperationalTime.setStatus("mandatory")
_NwAtProtoVersion_Type = DisplayString
_NwAtProtoVersion_Object = MibScalar
nwAtProtoVersion = _NwAtProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 5),
    _NwAtProtoVersion_Type()
)
nwAtProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoVersion.setStatus("mandatory")
_NwAtProtoStackSize_Type = Integer32
_NwAtProtoStackSize_Object = MibScalar
nwAtProtoStackSize = _NwAtProtoStackSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 6),
    _NwAtProtoStackSize_Type()
)
nwAtProtoStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoStackSize.setStatus("mandatory")
_NwAtProtoThreadPriority_Type = Integer32
_NwAtProtoThreadPriority_Object = MibScalar
nwAtProtoThreadPriority = _NwAtProtoThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 7),
    _NwAtProtoThreadPriority_Type()
)
nwAtProtoThreadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoThreadPriority.setStatus("mandatory")
_NwAtProtoDatabaseThreshold_Type = Integer32
_NwAtProtoDatabaseThreshold_Object = MibScalar
nwAtProtoDatabaseThreshold = _NwAtProtoDatabaseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 8),
    _NwAtProtoDatabaseThreshold_Type()
)
nwAtProtoDatabaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoDatabaseThreshold.setStatus("mandatory")
_NwAtProtoAgeOut_Type = Integer32
_NwAtProtoAgeOut_Object = MibScalar
nwAtProtoAgeOut = _NwAtProtoAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 9),
    _NwAtProtoAgeOut_Type()
)
nwAtProtoAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoAgeOut.setStatus("mandatory")
_NwAtProtoHoldDown_Type = Integer32
_NwAtProtoHoldDown_Object = MibScalar
nwAtProtoHoldDown = _NwAtProtoHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 1, 10),
    _NwAtProtoHoldDown_Type()
)
nwAtProtoHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoHoldDown.setStatus("mandatory")
_NwAtProtoCounters_ObjectIdentity = ObjectIdentity
nwAtProtoCounters = _NwAtProtoCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2)
)


class _NwAtProtoCtrAdminSTATUS_Type(Integer32):
    """Custom type nwAtProtoCtrAdminSTATUS based on Integer32"""
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


_NwAtProtoCtrAdminSTATUS_Type.__name__ = "Integer32"
_NwAtProtoCtrAdminSTATUS_Object = MibScalar
nwAtProtoCtrAdminSTATUS = _NwAtProtoCtrAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 1),
    _NwAtProtoCtrAdminSTATUS_Type()
)
nwAtProtoCtrAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoCtrAdminSTATUS.setStatus("mandatory")


class _NwAtProtoCtrReset_Type(Integer32):
    """Custom type nwAtProtoCtrReset based on Integer32"""
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


_NwAtProtoCtrReset_Type.__name__ = "Integer32"
_NwAtProtoCtrReset_Object = MibScalar
nwAtProtoCtrReset = _NwAtProtoCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 2),
    _NwAtProtoCtrReset_Type()
)
nwAtProtoCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoCtrReset.setStatus("mandatory")
_NwAtProtoCtrOperationalTime_Type = TimeTicks
_NwAtProtoCtrOperationalTime_Object = MibScalar
nwAtProtoCtrOperationalTime = _NwAtProtoCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 3),
    _NwAtProtoCtrOperationalTime_Type()
)
nwAtProtoCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrOperationalTime.setStatus("mandatory")
_NwAtProtoCtrInPkts_Type = Counter32
_NwAtProtoCtrInPkts_Object = MibScalar
nwAtProtoCtrInPkts = _NwAtProtoCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 4),
    _NwAtProtoCtrInPkts_Type()
)
nwAtProtoCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrInPkts.setStatus("mandatory")
_NwAtProtoCtrOutPkts_Type = Counter32
_NwAtProtoCtrOutPkts_Object = MibScalar
nwAtProtoCtrOutPkts = _NwAtProtoCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 5),
    _NwAtProtoCtrOutPkts_Type()
)
nwAtProtoCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrOutPkts.setStatus("mandatory")
_NwAtProtoCtrFilteredPkts_Type = Counter32
_NwAtProtoCtrFilteredPkts_Object = MibScalar
nwAtProtoCtrFilteredPkts = _NwAtProtoCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 6),
    _NwAtProtoCtrFilteredPkts_Type()
)
nwAtProtoCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrFilteredPkts.setStatus("mandatory")
_NwAtProtoCtrDiscardPkts_Type = Counter32
_NwAtProtoCtrDiscardPkts_Object = MibScalar
nwAtProtoCtrDiscardPkts = _NwAtProtoCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 7),
    _NwAtProtoCtrDiscardPkts_Type()
)
nwAtProtoCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrDiscardPkts.setStatus("mandatory")
_NwAtProtoCtrInBytes_Type = Counter32
_NwAtProtoCtrInBytes_Object = MibScalar
nwAtProtoCtrInBytes = _NwAtProtoCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 8),
    _NwAtProtoCtrInBytes_Type()
)
nwAtProtoCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrInBytes.setStatus("mandatory")
_NwAtProtoCtrOutBytes_Type = Counter32
_NwAtProtoCtrOutBytes_Object = MibScalar
nwAtProtoCtrOutBytes = _NwAtProtoCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 9),
    _NwAtProtoCtrOutBytes_Type()
)
nwAtProtoCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrOutBytes.setStatus("mandatory")
_NwAtProtoCtrFilteredBytes_Type = Counter32
_NwAtProtoCtrFilteredBytes_Object = MibScalar
nwAtProtoCtrFilteredBytes = _NwAtProtoCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 10),
    _NwAtProtoCtrFilteredBytes_Type()
)
nwAtProtoCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrFilteredBytes.setStatus("mandatory")
_NwAtProtoCtrDiscardBytes_Type = Counter32
_NwAtProtoCtrDiscardBytes_Object = MibScalar
nwAtProtoCtrDiscardBytes = _NwAtProtoCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 1, 2, 11),
    _NwAtProtoCtrDiscardBytes_Type()
)
nwAtProtoCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoCtrDiscardBytes.setStatus("mandatory")
_NwAtProtoInterface_ObjectIdentity = ObjectIdentity
nwAtProtoInterface = _NwAtProtoInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2)
)
_NwAtProtoIfConfig_ObjectIdentity = ObjectIdentity
nwAtProtoIfConfig = _NwAtProtoIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1)
)
_NwAtProtoIfTable_Object = MibTable
nwAtProtoIfTable = _NwAtProtoIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwAtProtoIfTable.setStatus("mandatory")
_NwAtProtoIfEntry_Object = MibTableRow
nwAtProtoIfEntry = _NwAtProtoIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1)
)
nwAtProtoIfEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtProtoIfIndex"),
)
if mibBuilder.loadTexts:
    nwAtProtoIfEntry.setStatus("mandatory")
_NwAtProtoIfIndex_Type = Integer32
_NwAtProtoIfIndex_Object = MibTableColumn
nwAtProtoIfIndex = _NwAtProtoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 1),
    _NwAtProtoIfIndex_Type()
)
nwAtProtoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfIndex.setStatus("mandatory")


class _NwAtProtoIfAdminSTATUS_Type(Integer32):
    """Custom type nwAtProtoIfAdminSTATUS based on Integer32"""
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


_NwAtProtoIfAdminSTATUS_Type.__name__ = "Integer32"
_NwAtProtoIfAdminSTATUS_Object = MibTableColumn
nwAtProtoIfAdminSTATUS = _NwAtProtoIfAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 2),
    _NwAtProtoIfAdminSTATUS_Type()
)
nwAtProtoIfAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfAdminSTATUS.setStatus("mandatory")


class _NwAtProtoIfOperSTATUS_Type(Integer32):
    """Custom type nwAtProtoIfOperSTATUS based on Integer32"""
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


_NwAtProtoIfOperSTATUS_Type.__name__ = "Integer32"
_NwAtProtoIfOperSTATUS_Object = MibTableColumn
nwAtProtoIfOperSTATUS = _NwAtProtoIfOperSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 3),
    _NwAtProtoIfOperSTATUS_Type()
)
nwAtProtoIfOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfOperSTATUS.setStatus("mandatory")
_NwAtProtoIfOperationalTime_Type = TimeTicks
_NwAtProtoIfOperationalTime_Object = MibTableColumn
nwAtProtoIfOperationalTime = _NwAtProtoIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 4),
    _NwAtProtoIfOperationalTime_Type()
)
nwAtProtoIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfOperationalTime.setStatus("mandatory")
_NwAtProtoIfVersion_Type = Integer32
_NwAtProtoIfVersion_Object = MibTableColumn
nwAtProtoIfVersion = _NwAtProtoIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 5),
    _NwAtProtoIfVersion_Type()
)
nwAtProtoIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfVersion.setStatus("mandatory")


class _NwAtProtoIfAdvertisement_Type(Integer32):
    """Custom type nwAtProtoIfAdvertisement based on Integer32"""
    defaultValue = 60


_NwAtProtoIfAdvertisement_Object = MibTableColumn
nwAtProtoIfAdvertisement = _NwAtProtoIfAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 6),
    _NwAtProtoIfAdvertisement_Type()
)
nwAtProtoIfAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfAdvertisement.setStatus("mandatory")
_NwAtProtoIfFloodDelay_Type = Integer32
_NwAtProtoIfFloodDelay_Object = MibTableColumn
nwAtProtoIfFloodDelay = _NwAtProtoIfFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 7),
    _NwAtProtoIfFloodDelay_Type()
)
nwAtProtoIfFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfFloodDelay.setStatus("mandatory")
_NwAtProtoIfRequestDelay_Type = Integer32
_NwAtProtoIfRequestDelay_Object = MibTableColumn
nwAtProtoIfRequestDelay = _NwAtProtoIfRequestDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 8),
    _NwAtProtoIfRequestDelay_Type()
)
nwAtProtoIfRequestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfRequestDelay.setStatus("mandatory")
_NwAtProtoIfPriority_Type = Integer32
_NwAtProtoIfPriority_Object = MibTableColumn
nwAtProtoIfPriority = _NwAtProtoIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 9),
    _NwAtProtoIfPriority_Type()
)
nwAtProtoIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfPriority.setStatus("mandatory")
_NwAtProtoIfHelloTimer_Type = Integer32
_NwAtProtoIfHelloTimer_Object = MibTableColumn
nwAtProtoIfHelloTimer = _NwAtProtoIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 10),
    _NwAtProtoIfHelloTimer_Type()
)
nwAtProtoIfHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfHelloTimer.setStatus("mandatory")


class _NwAtProtoIfSplitHorizon_Type(Integer32):
    """Custom type nwAtProtoIfSplitHorizon based on Integer32"""
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


_NwAtProtoIfSplitHorizon_Type.__name__ = "Integer32"
_NwAtProtoIfSplitHorizon_Object = MibTableColumn
nwAtProtoIfSplitHorizon = _NwAtProtoIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 11),
    _NwAtProtoIfSplitHorizon_Type()
)
nwAtProtoIfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfSplitHorizon.setStatus("mandatory")


class _NwAtProtoIfPoisonReverse_Type(Integer32):
    """Custom type nwAtProtoIfPoisonReverse based on Integer32"""
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


_NwAtProtoIfPoisonReverse_Type.__name__ = "Integer32"
_NwAtProtoIfPoisonReverse_Object = MibTableColumn
nwAtProtoIfPoisonReverse = _NwAtProtoIfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 12),
    _NwAtProtoIfPoisonReverse_Type()
)
nwAtProtoIfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfPoisonReverse.setStatus("mandatory")


class _NwAtProtoIfSnooping_Type(Integer32):
    """Custom type nwAtProtoIfSnooping based on Integer32"""
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


_NwAtProtoIfSnooping_Type.__name__ = "Integer32"
_NwAtProtoIfSnooping_Object = MibTableColumn
nwAtProtoIfSnooping = _NwAtProtoIfSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 13),
    _NwAtProtoIfSnooping_Type()
)
nwAtProtoIfSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfSnooping.setStatus("mandatory")


class _NwAtProtoIfType_Type(Integer32):
    """Custom type nwAtProtoIfType based on Integer32"""
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


_NwAtProtoIfType_Type.__name__ = "Integer32"
_NwAtProtoIfType_Object = MibTableColumn
nwAtProtoIfType = _NwAtProtoIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 14),
    _NwAtProtoIfType_Type()
)
nwAtProtoIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfType.setStatus("mandatory")
_NwAtProtoIfXmitCost_Type = Integer32
_NwAtProtoIfXmitCost_Object = MibTableColumn
nwAtProtoIfXmitCost = _NwAtProtoIfXmitCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 15),
    _NwAtProtoIfXmitCost_Type()
)
nwAtProtoIfXmitCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfXmitCost.setStatus("mandatory")
_NwAtProtoIfAclIdentifier_Type = Integer32
_NwAtProtoIfAclIdentifier_Object = MibTableColumn
nwAtProtoIfAclIdentifier = _NwAtProtoIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 16),
    _NwAtProtoIfAclIdentifier_Type()
)
nwAtProtoIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfAclIdentifier.setStatus("mandatory")


class _NwAtProtoIfAclSTATUS_Type(Integer32):
    """Custom type nwAtProtoIfAclSTATUS based on Integer32"""
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


_NwAtProtoIfAclSTATUS_Type.__name__ = "Integer32"
_NwAtProtoIfAclSTATUS_Object = MibTableColumn
nwAtProtoIfAclSTATUS = _NwAtProtoIfAclSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 1, 1, 1, 17),
    _NwAtProtoIfAclSTATUS_Type()
)
nwAtProtoIfAclSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfAclSTATUS.setStatus("mandatory")
_NwAtProtoIfCounters_ObjectIdentity = ObjectIdentity
nwAtProtoIfCounters = _NwAtProtoIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2)
)
_NwAtProtoIfCtrTable_Object = MibTable
nwAtProtoIfCtrTable = _NwAtProtoIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwAtProtoIfCtrTable.setStatus("mandatory")
_NwAtProtoIfCtrEntry_Object = MibTableRow
nwAtProtoIfCtrEntry = _NwAtProtoIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1)
)
nwAtProtoIfCtrEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtProtoIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwAtProtoIfCtrEntry.setStatus("mandatory")
_NwAtProtoIfCtrIfIndex_Type = Integer32
_NwAtProtoIfCtrIfIndex_Object = MibTableColumn
nwAtProtoIfCtrIfIndex = _NwAtProtoIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 1),
    _NwAtProtoIfCtrIfIndex_Type()
)
nwAtProtoIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrIfIndex.setStatus("mandatory")


class _NwAtProtoIfCtrAdminSTATUS_Type(Integer32):
    """Custom type nwAtProtoIfCtrAdminSTATUS based on Integer32"""
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


_NwAtProtoIfCtrAdminSTATUS_Type.__name__ = "Integer32"
_NwAtProtoIfCtrAdminSTATUS_Object = MibTableColumn
nwAtProtoIfCtrAdminSTATUS = _NwAtProtoIfCtrAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 2),
    _NwAtProtoIfCtrAdminSTATUS_Type()
)
nwAtProtoIfCtrAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrAdminSTATUS.setStatus("mandatory")


class _NwAtProtoIfCtrReset_Type(Integer32):
    """Custom type nwAtProtoIfCtrReset based on Integer32"""
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


_NwAtProtoIfCtrReset_Type.__name__ = "Integer32"
_NwAtProtoIfCtrReset_Object = MibTableColumn
nwAtProtoIfCtrReset = _NwAtProtoIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 3),
    _NwAtProtoIfCtrReset_Type()
)
nwAtProtoIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrReset.setStatus("mandatory")
_NwAtProtoIfCtrOperationalTime_Type = TimeTicks
_NwAtProtoIfCtrOperationalTime_Object = MibTableColumn
nwAtProtoIfCtrOperationalTime = _NwAtProtoIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 4),
    _NwAtProtoIfCtrOperationalTime_Type()
)
nwAtProtoIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrOperationalTime.setStatus("mandatory")
_NwAtProtoIfCtrInPkts_Type = Counter32
_NwAtProtoIfCtrInPkts_Object = MibTableColumn
nwAtProtoIfCtrInPkts = _NwAtProtoIfCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 5),
    _NwAtProtoIfCtrInPkts_Type()
)
nwAtProtoIfCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrInPkts.setStatus("mandatory")
_NwAtProtoIfCtrOutPkts_Type = Counter32
_NwAtProtoIfCtrOutPkts_Object = MibTableColumn
nwAtProtoIfCtrOutPkts = _NwAtProtoIfCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 6),
    _NwAtProtoIfCtrOutPkts_Type()
)
nwAtProtoIfCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrOutPkts.setStatus("mandatory")
_NwAtProtoIfCtrFilteredPkts_Type = Counter32
_NwAtProtoIfCtrFilteredPkts_Object = MibTableColumn
nwAtProtoIfCtrFilteredPkts = _NwAtProtoIfCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 7),
    _NwAtProtoIfCtrFilteredPkts_Type()
)
nwAtProtoIfCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrFilteredPkts.setStatus("mandatory")
_NwAtProtoIfCtrDiscardPkts_Type = Counter32
_NwAtProtoIfCtrDiscardPkts_Object = MibTableColumn
nwAtProtoIfCtrDiscardPkts = _NwAtProtoIfCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 8),
    _NwAtProtoIfCtrDiscardPkts_Type()
)
nwAtProtoIfCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrDiscardPkts.setStatus("mandatory")
_NwAtProtoIfCtrInBytes_Type = Counter32
_NwAtProtoIfCtrInBytes_Object = MibTableColumn
nwAtProtoIfCtrInBytes = _NwAtProtoIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 9),
    _NwAtProtoIfCtrInBytes_Type()
)
nwAtProtoIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrInBytes.setStatus("mandatory")
_NwAtProtoIfCtrOutBytes_Type = Counter32
_NwAtProtoIfCtrOutBytes_Object = MibTableColumn
nwAtProtoIfCtrOutBytes = _NwAtProtoIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 10),
    _NwAtProtoIfCtrOutBytes_Type()
)
nwAtProtoIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrOutBytes.setStatus("mandatory")
_NwAtProtoIfCtrFilteredBytes_Type = Counter32
_NwAtProtoIfCtrFilteredBytes_Object = MibTableColumn
nwAtProtoIfCtrFilteredBytes = _NwAtProtoIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 11),
    _NwAtProtoIfCtrFilteredBytes_Type()
)
nwAtProtoIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrFilteredBytes.setStatus("mandatory")
_NwAtProtoIfCtrDiscardBytes_Type = Counter32
_NwAtProtoIfCtrDiscardBytes_Object = MibTableColumn
nwAtProtoIfCtrDiscardBytes = _NwAtProtoIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 1, 1, 2, 2, 1, 1, 12),
    _NwAtProtoIfCtrDiscardBytes_Type()
)
nwAtProtoIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtProtoIfCtrDiscardBytes.setStatus("mandatory")
_NwAtLinkState_ObjectIdentity = ObjectIdentity
nwAtLinkState = _NwAtLinkState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 4, 2)
)
_NwAtFib_ObjectIdentity = ObjectIdentity
nwAtFib = _NwAtFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5)
)
_NwAtFibTable_Object = MibTable
nwAtFibTable = _NwAtFibTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    nwAtFibTable.setStatus("mandatory")
_NwAtFibEntry_Object = MibTableRow
nwAtFibEntry = _NwAtFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1, 1)
)
nwAtFibEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtFibStartNet"),
)
if mibBuilder.loadTexts:
    nwAtFibEntry.setStatus("mandatory")
_NwAtFibStartNet_Type = AtNetworkNumber
_NwAtFibStartNet_Object = MibTableColumn
nwAtFibStartNet = _NwAtFibStartNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1, 1, 1),
    _NwAtFibStartNet_Type()
)
nwAtFibStartNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFibStartNet.setStatus("mandatory")
_NwAtFibEndNet_Type = AtNetworkNumber
_NwAtFibEndNet_Object = MibTableColumn
nwAtFibEndNet = _NwAtFibEndNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1, 1, 2),
    _NwAtFibEndNet_Type()
)
nwAtFibEndNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFibEndNet.setStatus("mandatory")
_NwAtFibNextHop_Type = AtDdpNodeAddress
_NwAtFibNextHop_Object = MibTableColumn
nwAtFibNextHop = _NwAtFibNextHop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1, 1, 3),
    _NwAtFibNextHop_Type()
)
nwAtFibNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFibNextHop.setStatus("mandatory")
_NwAtFibNextHopIf_Type = Integer32
_NwAtFibNextHopIf_Object = MibTableColumn
nwAtFibNextHopIf = _NwAtFibNextHopIf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1, 1, 4),
    _NwAtFibNextHopIf_Type()
)
nwAtFibNextHopIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFibNextHopIf.setStatus("mandatory")
_NwAtFibHops_Type = Integer32
_NwAtFibHops_Object = MibTableColumn
nwAtFibHops = _NwAtFibHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1, 1, 5),
    _NwAtFibHops_Type()
)
nwAtFibHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFibHops.setStatus("mandatory")


class _NwAtFibRouteType_Type(Integer32):
    """Custom type nwAtFibRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 2),
          ("other", 1))
    )


_NwAtFibRouteType_Type.__name__ = "Integer32"
_NwAtFibRouteType_Object = MibTableColumn
nwAtFibRouteType = _NwAtFibRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 5, 1, 1, 6),
    _NwAtFibRouteType_Type()
)
nwAtFibRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtFibRouteType.setStatus("mandatory")
_NwAtEndSystems_ObjectIdentity = ObjectIdentity
nwAtEndSystems = _NwAtEndSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6)
)
_NwAtHostsSystem_ObjectIdentity = ObjectIdentity
nwAtHostsSystem = _NwAtHostsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 1)
)
_NwAtHostsTimeToLive_Type = Integer32
_NwAtHostsTimeToLive_Object = MibScalar
nwAtHostsTimeToLive = _NwAtHostsTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 1, 1),
    _NwAtHostsTimeToLive_Type()
)
nwAtHostsTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostsTimeToLive.setStatus("mandatory")
_NwAtHostsRetryCount_Type = Counter32
_NwAtHostsRetryCount_Object = MibScalar
nwAtHostsRetryCount = _NwAtHostsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 1, 2),
    _NwAtHostsRetryCount_Type()
)
nwAtHostsRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostsRetryCount.setStatus("mandatory")
_NwAtHostsInterfaces_ObjectIdentity = ObjectIdentity
nwAtHostsInterfaces = _NwAtHostsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2)
)
_NwAtHostCtlTable_Object = MibTable
nwAtHostCtlTable = _NwAtHostCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    nwAtHostCtlTable.setStatus("mandatory")
_NwAtHostCtlEntry_Object = MibTableRow
nwAtHostCtlEntry = _NwAtHostCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1)
)
nwAtHostCtlEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtHostCtlIfIndex"),
)
if mibBuilder.loadTexts:
    nwAtHostCtlEntry.setStatus("mandatory")
_NwAtHostCtlIfIndex_Type = Integer32
_NwAtHostCtlIfIndex_Object = MibTableColumn
nwAtHostCtlIfIndex = _NwAtHostCtlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 1),
    _NwAtHostCtlIfIndex_Type()
)
nwAtHostCtlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostCtlIfIndex.setStatus("mandatory")


class _NwAtHostCtlAdminSTATUS_Type(Integer32):
    """Custom type nwAtHostCtlAdminSTATUS based on Integer32"""
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


_NwAtHostCtlAdminSTATUS_Type.__name__ = "Integer32"
_NwAtHostCtlAdminSTATUS_Object = MibTableColumn
nwAtHostCtlAdminSTATUS = _NwAtHostCtlAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 2),
    _NwAtHostCtlAdminSTATUS_Type()
)
nwAtHostCtlAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostCtlAdminSTATUS.setStatus("mandatory")


class _NwAtHostCtlOperSTATUS_Type(Integer32):
    """Custom type nwAtHostCtlOperSTATUS based on Integer32"""
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


_NwAtHostCtlOperSTATUS_Type.__name__ = "Integer32"
_NwAtHostCtlOperSTATUS_Object = MibTableColumn
nwAtHostCtlOperSTATUS = _NwAtHostCtlOperSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 3),
    _NwAtHostCtlOperSTATUS_Type()
)
nwAtHostCtlOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostCtlOperSTATUS.setStatus("mandatory")
_NwAtHostCtlOperationalTime_Type = TimeTicks
_NwAtHostCtlOperationalTime_Object = MibTableColumn
nwAtHostCtlOperationalTime = _NwAtHostCtlOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 4),
    _NwAtHostCtlOperationalTime_Type()
)
nwAtHostCtlOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostCtlOperationalTime.setStatus("mandatory")


class _NwAtHostCtlProtocol_Type(Integer32):
    """Custom type nwAtHostCtlProtocol based on Integer32"""
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


_NwAtHostCtlProtocol_Type.__name__ = "Integer32"
_NwAtHostCtlProtocol_Object = MibTableColumn
nwAtHostCtlProtocol = _NwAtHostCtlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 5),
    _NwAtHostCtlProtocol_Type()
)
nwAtHostCtlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostCtlProtocol.setStatus("mandatory")


class _NwAtHostCtlSnooping_Type(Integer32):
    """Custom type nwAtHostCtlSnooping based on Integer32"""
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


_NwAtHostCtlSnooping_Type.__name__ = "Integer32"
_NwAtHostCtlSnooping_Object = MibTableColumn
nwAtHostCtlSnooping = _NwAtHostCtlSnooping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 6),
    _NwAtHostCtlSnooping_Type()
)
nwAtHostCtlSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostCtlSnooping.setStatus("mandatory")


class _NwAtHostCtlProxy_Type(Integer32):
    """Custom type nwAtHostCtlProxy based on Integer32"""
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


_NwAtHostCtlProxy_Type.__name__ = "Integer32"
_NwAtHostCtlProxy_Object = MibTableColumn
nwAtHostCtlProxy = _NwAtHostCtlProxy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 7),
    _NwAtHostCtlProxy_Type()
)
nwAtHostCtlProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostCtlProxy.setStatus("mandatory")
_NwAtHostCtlCacheMax_Type = Integer32
_NwAtHostCtlCacheMax_Object = MibTableColumn
nwAtHostCtlCacheMax = _NwAtHostCtlCacheMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 8),
    _NwAtHostCtlCacheMax_Type()
)
nwAtHostCtlCacheMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostCtlCacheMax.setStatus("mandatory")
_NwAtHostCtlCacheSize_Type = Integer32
_NwAtHostCtlCacheSize_Object = MibTableColumn
nwAtHostCtlCacheSize = _NwAtHostCtlCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 9),
    _NwAtHostCtlCacheSize_Type()
)
nwAtHostCtlCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostCtlCacheSize.setStatus("mandatory")
_NwAtHostCtlNumStatics_Type = Counter32
_NwAtHostCtlNumStatics_Object = MibTableColumn
nwAtHostCtlNumStatics = _NwAtHostCtlNumStatics_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 10),
    _NwAtHostCtlNumStatics_Type()
)
nwAtHostCtlNumStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostCtlNumStatics.setStatus("mandatory")
_NwAtHostCtlNumDynamics_Type = Counter32
_NwAtHostCtlNumDynamics_Object = MibTableColumn
nwAtHostCtlNumDynamics = _NwAtHostCtlNumDynamics_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 11),
    _NwAtHostCtlNumDynamics_Type()
)
nwAtHostCtlNumDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostCtlNumDynamics.setStatus("mandatory")
_NwAtHostCtlCacheHits_Type = Counter32
_NwAtHostCtlCacheHits_Object = MibTableColumn
nwAtHostCtlCacheHits = _NwAtHostCtlCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 12),
    _NwAtHostCtlCacheHits_Type()
)
nwAtHostCtlCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostCtlCacheHits.setStatus("mandatory")
_NwAtHostCtlCacheMisses_Type = Counter32
_NwAtHostCtlCacheMisses_Object = MibTableColumn
nwAtHostCtlCacheMisses = _NwAtHostCtlCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 2, 1, 1, 13),
    _NwAtHostCtlCacheMisses_Type()
)
nwAtHostCtlCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostCtlCacheMisses.setStatus("mandatory")
_NwAtHostsToMedia_ObjectIdentity = ObjectIdentity
nwAtHostsToMedia = _NwAtHostsToMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3)
)
_NwAtHostMapTable_Object = MibTable
nwAtHostMapTable = _NwAtHostMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    nwAtHostMapTable.setStatus("mandatory")
_NwAtHostMapEntry_Object = MibTableRow
nwAtHostMapEntry = _NwAtHostMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1)
)
nwAtHostMapEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtHostMapIfIndex"),
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtHostMapAtAddr"),
)
if mibBuilder.loadTexts:
    nwAtHostMapEntry.setStatus("mandatory")
_NwAtHostMapIfIndex_Type = Integer32
_NwAtHostMapIfIndex_Object = MibTableColumn
nwAtHostMapIfIndex = _NwAtHostMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1, 1),
    _NwAtHostMapIfIndex_Type()
)
nwAtHostMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostMapIfIndex.setStatus("mandatory")
_NwAtHostMapAtAddr_Type = AtDdpNodeAddress
_NwAtHostMapAtAddr_Object = MibTableColumn
nwAtHostMapAtAddr = _NwAtHostMapAtAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1, 2),
    _NwAtHostMapAtAddr_Type()
)
nwAtHostMapAtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostMapAtAddr.setStatus("mandatory")
_NwAtHostMapPhysAddr_Type = PhysAddress
_NwAtHostMapPhysAddr_Object = MibTableColumn
nwAtHostMapPhysAddr = _NwAtHostMapPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1, 3),
    _NwAtHostMapPhysAddr_Type()
)
nwAtHostMapPhysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostMapPhysAddr.setStatus("mandatory")


class _NwAtHostMapType_Type(Integer32):
    """Custom type nwAtHostMapType based on Integer32"""
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


_NwAtHostMapType_Type.__name__ = "Integer32"
_NwAtHostMapType_Object = MibTableColumn
nwAtHostMapType = _NwAtHostMapType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1, 4),
    _NwAtHostMapType_Type()
)
nwAtHostMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostMapType.setStatus("mandatory")
_NwAtHostMapCircuitID_Type = Integer32
_NwAtHostMapCircuitID_Object = MibTableColumn
nwAtHostMapCircuitID = _NwAtHostMapCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1, 5),
    _NwAtHostMapCircuitID_Type()
)
nwAtHostMapCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostMapCircuitID.setStatus("mandatory")


class _NwAtHostMapFraming_Type(Integer32):
    """Custom type nwAtHostMapFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              9,
              11,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 17),
          ("encapenet", 9),
          ("encapenetsnap", 11),
          ("encapfddisnap", 16),
          ("ethernet", 2),
          ("nativewan", 8),
          ("other", 1),
          ("snap", 3))
    )


_NwAtHostMapFraming_Type.__name__ = "Integer32"
_NwAtHostMapFraming_Object = MibTableColumn
nwAtHostMapFraming = _NwAtHostMapFraming_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1, 6),
    _NwAtHostMapFraming_Type()
)
nwAtHostMapFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtHostMapFraming.setStatus("mandatory")
_NwAtHostMapPortNumber_Type = Integer32
_NwAtHostMapPortNumber_Object = MibTableColumn
nwAtHostMapPortNumber = _NwAtHostMapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 6, 3, 1, 1, 7),
    _NwAtHostMapPortNumber_Type()
)
nwAtHostMapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtHostMapPortNumber.setStatus("mandatory")
_NwAtAccessControl_ObjectIdentity = ObjectIdentity
nwAtAccessControl = _NwAtAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7)
)
_NwAtAclValidEntries_Type = Gauge32
_NwAtAclValidEntries_Object = MibScalar
nwAtAclValidEntries = _NwAtAclValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 1),
    _NwAtAclValidEntries_Type()
)
nwAtAclValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtAclValidEntries.setStatus("mandatory")
_NwAtAclTable_Object = MibTable
nwAtAclTable = _NwAtAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2)
)
if mibBuilder.loadTexts:
    nwAtAclTable.setStatus("mandatory")
_NwAtAclEntry_Object = MibTableRow
nwAtAclEntry = _NwAtAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2, 1)
)
nwAtAclEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtAclIdentifier"),
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtAclSequence"),
)
if mibBuilder.loadTexts:
    nwAtAclEntry.setStatus("mandatory")
_NwAtAclIdentifier_Type = Integer32
_NwAtAclIdentifier_Object = MibTableColumn
nwAtAclIdentifier = _NwAtAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2, 1, 1),
    _NwAtAclIdentifier_Type()
)
nwAtAclIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtAclIdentifier.setStatus("mandatory")
_NwAtAclSequence_Type = Integer32
_NwAtAclSequence_Object = MibTableColumn
nwAtAclSequence = _NwAtAclSequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2, 1, 2),
    _NwAtAclSequence_Type()
)
nwAtAclSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtAclSequence.setStatus("mandatory")


class _NwAtAclPermission_Type(Integer32):
    """Custom type nwAtAclPermission based on Integer32"""
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


_NwAtAclPermission_Type.__name__ = "Integer32"
_NwAtAclPermission_Object = MibTableColumn
nwAtAclPermission = _NwAtAclPermission_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2, 1, 3),
    _NwAtAclPermission_Type()
)
nwAtAclPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtAclPermission.setStatus("mandatory")
_NwAtAclMatches_Type = Counter32
_NwAtAclMatches_Object = MibTableColumn
nwAtAclMatches = _NwAtAclMatches_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2, 1, 4),
    _NwAtAclMatches_Type()
)
nwAtAclMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtAclMatches.setStatus("mandatory")
_NwAtAclDestZone_Type = AtName
_NwAtAclDestZone_Object = MibTableColumn
nwAtAclDestZone = _NwAtAclDestZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2, 1, 5),
    _NwAtAclDestZone_Type()
)
nwAtAclDestZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtAclDestZone.setStatus("mandatory")
_NwAtAclSrcZone_Type = AtName
_NwAtAclSrcZone_Object = MibTableColumn
nwAtAclSrcZone = _NwAtAclSrcZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 7, 2, 1, 6),
    _NwAtAclSrcZone_Type()
)
nwAtAclSrcZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtAclSrcZone.setStatus("mandatory")
_NwAtFilters_ObjectIdentity = ObjectIdentity
nwAtFilters = _NwAtFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 8)
)
_NwAtRedirector_ObjectIdentity = ObjectIdentity
nwAtRedirector = _NwAtRedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 9)
)
_NwAtEvent_ObjectIdentity = ObjectIdentity
nwAtEvent = _NwAtEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10)
)
_NwAtEventLogConfig_ObjectIdentity = ObjectIdentity
nwAtEventLogConfig = _NwAtEventLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 1)
)


class _NwAtEventAdminSTATUS_Type(Integer32):
    """Custom type nwAtEventAdminSTATUS based on Integer32"""
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


_NwAtEventAdminSTATUS_Type.__name__ = "Integer32"
_NwAtEventAdminSTATUS_Object = MibScalar
nwAtEventAdminSTATUS = _NwAtEventAdminSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 1, 1),
    _NwAtEventAdminSTATUS_Type()
)
nwAtEventAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtEventAdminSTATUS.setStatus("mandatory")
_NwAtEventMaxEntries_Type = Integer32
_NwAtEventMaxEntries_Object = MibScalar
nwAtEventMaxEntries = _NwAtEventMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 1, 2),
    _NwAtEventMaxEntries_Type()
)
nwAtEventMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtEventMaxEntries.setStatus("mandatory")


class _NwAtEventTraceAll_Type(Integer32):
    """Custom type nwAtEventTraceAll based on Integer32"""
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


_NwAtEventTraceAll_Type.__name__ = "Integer32"
_NwAtEventTraceAll_Object = MibScalar
nwAtEventTraceAll = _NwAtEventTraceAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 1, 3),
    _NwAtEventTraceAll_Type()
)
nwAtEventTraceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtEventTraceAll.setStatus("mandatory")
_NwAtEventLogFilterTable_ObjectIdentity = ObjectIdentity
nwAtEventLogFilterTable = _NwAtEventLogFilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2)
)
_NwAtEventFilterTable_Object = MibTable
nwAtEventFilterTable = _NwAtEventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    nwAtEventFilterTable.setStatus("mandatory")
_NwAtEventFilterEntry_Object = MibTableRow
nwAtEventFilterEntry = _NwAtEventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1, 1)
)
nwAtEventFilterEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtEventFltrProtocol"),
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtEventFltrIfNum"),
)
if mibBuilder.loadTexts:
    nwAtEventFilterEntry.setStatus("mandatory")
_NwAtEventFltrProtocol_Type = Integer32
_NwAtEventFltrProtocol_Object = MibTableColumn
nwAtEventFltrProtocol = _NwAtEventFltrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1, 1, 1),
    _NwAtEventFltrProtocol_Type()
)
nwAtEventFltrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventFltrProtocol.setStatus("mandatory")
_NwAtEventFltrIfNum_Type = Integer32
_NwAtEventFltrIfNum_Object = MibTableColumn
nwAtEventFltrIfNum = _NwAtEventFltrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1, 1, 2),
    _NwAtEventFltrIfNum_Type()
)
nwAtEventFltrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventFltrIfNum.setStatus("mandatory")


class _NwAtEventFltrControl_Type(Integer32):
    """Custom type nwAtEventFltrControl based on Integer32"""
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


_NwAtEventFltrControl_Type.__name__ = "Integer32"
_NwAtEventFltrControl_Object = MibTableColumn
nwAtEventFltrControl = _NwAtEventFltrControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1, 1, 3),
    _NwAtEventFltrControl_Type()
)
nwAtEventFltrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtEventFltrControl.setStatus("mandatory")


class _NwAtEventFltrType_Type(Integer32):
    """Custom type nwAtEventFltrType based on Integer32"""
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


_NwAtEventFltrType_Type.__name__ = "Integer32"
_NwAtEventFltrType_Object = MibTableColumn
nwAtEventFltrType = _NwAtEventFltrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1, 1, 4),
    _NwAtEventFltrType_Type()
)
nwAtEventFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtEventFltrType.setStatus("mandatory")


class _NwAtEventFltrSeverity_Type(Integer32):
    """Custom type nwAtEventFltrSeverity based on Integer32"""
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


_NwAtEventFltrSeverity_Type.__name__ = "Integer32"
_NwAtEventFltrSeverity_Object = MibTableColumn
nwAtEventFltrSeverity = _NwAtEventFltrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1, 1, 5),
    _NwAtEventFltrSeverity_Type()
)
nwAtEventFltrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtEventFltrSeverity.setStatus("mandatory")


class _NwAtEventFltrAction_Type(Integer32):
    """Custom type nwAtEventFltrAction based on Integer32"""
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


_NwAtEventFltrAction_Type.__name__ = "Integer32"
_NwAtEventFltrAction_Object = MibTableColumn
nwAtEventFltrAction = _NwAtEventFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 2, 1, 1, 6),
    _NwAtEventFltrAction_Type()
)
nwAtEventFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtEventFltrAction.setStatus("mandatory")
_NwAtEventLogTable_ObjectIdentity = ObjectIdentity
nwAtEventLogTable = _NwAtEventLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3)
)
_NwAtEventTable_Object = MibTable
nwAtEventTable = _NwAtEventTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    nwAtEventTable.setStatus("mandatory")
_NwAtEventEntry_Object = MibTableRow
nwAtEventEntry = _NwAtEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1)
)
nwAtEventEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtEventNumber"),
)
if mibBuilder.loadTexts:
    nwAtEventEntry.setStatus("mandatory")
_NwAtEventNumber_Type = Integer32
_NwAtEventNumber_Object = MibTableColumn
nwAtEventNumber = _NwAtEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1, 1),
    _NwAtEventNumber_Type()
)
nwAtEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventNumber.setStatus("mandatory")
_NwAtEventTime_Type = TimeTicks
_NwAtEventTime_Object = MibTableColumn
nwAtEventTime = _NwAtEventTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1, 2),
    _NwAtEventTime_Type()
)
nwAtEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventTime.setStatus("mandatory")


class _NwAtEventType_Type(Integer32):
    """Custom type nwAtEventType based on Integer32"""
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


_NwAtEventType_Type.__name__ = "Integer32"
_NwAtEventType_Object = MibTableColumn
nwAtEventType = _NwAtEventType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1, 3),
    _NwAtEventType_Type()
)
nwAtEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventType.setStatus("mandatory")


class _NwAtEventSeverity_Type(Integer32):
    """Custom type nwAtEventSeverity based on Integer32"""
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


_NwAtEventSeverity_Type.__name__ = "Integer32"
_NwAtEventSeverity_Object = MibTableColumn
nwAtEventSeverity = _NwAtEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1, 4),
    _NwAtEventSeverity_Type()
)
nwAtEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventSeverity.setStatus("mandatory")
_NwAtEventProtocol_Type = Integer32
_NwAtEventProtocol_Object = MibTableColumn
nwAtEventProtocol = _NwAtEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1, 5),
    _NwAtEventProtocol_Type()
)
nwAtEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventProtocol.setStatus("mandatory")
_NwAtEventIfNum_Type = Integer32
_NwAtEventIfNum_Object = MibTableColumn
nwAtEventIfNum = _NwAtEventIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1, 6),
    _NwAtEventIfNum_Type()
)
nwAtEventIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventIfNum.setStatus("mandatory")
_NwAtEventTextString_Type = OctetString
_NwAtEventTextString_Object = MibTableColumn
nwAtEventTextString = _NwAtEventTextString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 10, 3, 1, 1, 7),
    _NwAtEventTextString_Type()
)
nwAtEventTextString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtEventTextString.setStatus("mandatory")
_NwAtWorkGroup_ObjectIdentity = ObjectIdentity
nwAtWorkGroup = _NwAtWorkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 11)
)
_NwAtNetDiag_ObjectIdentity = ObjectIdentity
nwAtNetDiag = _NwAtNetDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12)
)
_NwAtNetDiagPing_ObjectIdentity = ObjectIdentity
nwAtNetDiagPing = _NwAtNetDiagPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 1)
)
_NwAtNetDiagTelnet_ObjectIdentity = ObjectIdentity
nwAtNetDiagTelnet = _NwAtNetDiagTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 2)
)
_NwAtNetDiagOutbound_ObjectIdentity = ObjectIdentity
nwAtNetDiagOutbound = _NwAtNetDiagOutbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3)
)
_NwAtNetDiagOutboundNetAddress_Type = AtDdpNodeAddress
_NwAtNetDiagOutboundNetAddress_Object = MibScalar
nwAtNetDiagOutboundNetAddress = _NwAtNetDiagOutboundNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 1),
    _NwAtNetDiagOutboundNetAddress_Type()
)
nwAtNetDiagOutboundNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundNetAddress.setStatus("mandatory")
_NwAtNetDiagOutboundPort_Type = Integer32
_NwAtNetDiagOutboundPort_Object = MibScalar
nwAtNetDiagOutboundPort = _NwAtNetDiagOutboundPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 2),
    _NwAtNetDiagOutboundPort_Type()
)
nwAtNetDiagOutboundPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundPort.setStatus("mandatory")
_NwAtNetDiagOutboundTimeout_Type = Integer32
_NwAtNetDiagOutboundTimeout_Object = MibScalar
nwAtNetDiagOutboundTimeout = _NwAtNetDiagOutboundTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 3),
    _NwAtNetDiagOutboundTimeout_Type()
)
nwAtNetDiagOutboundTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundTimeout.setStatus("mandatory")
_NwAtNetDiagOutboundRetries_Type = Integer32
_NwAtNetDiagOutboundRetries_Object = MibScalar
nwAtNetDiagOutboundRetries = _NwAtNetDiagOutboundRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 4),
    _NwAtNetDiagOutboundRetries_Type()
)
nwAtNetDiagOutboundRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundRetries.setStatus("mandatory")


class _NwAtNetDiagOutboundATEchoType_Type(Integer32):
    """Custom type nwAtNetDiagOutboundATEchoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("other", 3),
          ("sendEchoRequest", 2))
    )


_NwAtNetDiagOutboundATEchoType_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundATEchoType_Object = MibScalar
nwAtNetDiagOutboundATEchoType = _NwAtNetDiagOutboundATEchoType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 5),
    _NwAtNetDiagOutboundATEchoType_Type()
)
nwAtNetDiagOutboundATEchoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundATEchoType.setStatus("mandatory")


class _NwAtNetDiagOutboundATEchoStatus_Type(Integer32):
    """Custom type nwAtNetDiagOutboundATEchoStatus based on Integer32"""
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
        *(("inProgress", 2),
          ("inactive", 1),
          ("success", 4),
          ("timeout", 3))
    )


_NwAtNetDiagOutboundATEchoStatus_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundATEchoStatus_Object = MibScalar
nwAtNetDiagOutboundATEchoStatus = _NwAtNetDiagOutboundATEchoStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 6),
    _NwAtNetDiagOutboundATEchoStatus_Type()
)
nwAtNetDiagOutboundATEchoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundATEchoStatus.setStatus("mandatory")
_NwAtNetDiagOutboundNBPEntityObject_Type = AtName
_NwAtNetDiagOutboundNBPEntityObject_Object = MibScalar
nwAtNetDiagOutboundNBPEntityObject = _NwAtNetDiagOutboundNBPEntityObject_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 7),
    _NwAtNetDiagOutboundNBPEntityObject_Type()
)
nwAtNetDiagOutboundNBPEntityObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundNBPEntityObject.setStatus("mandatory")
_NwAtNetDiagOutboundNBPEntityType_Type = AtName
_NwAtNetDiagOutboundNBPEntityType_Object = MibScalar
nwAtNetDiagOutboundNBPEntityType = _NwAtNetDiagOutboundNBPEntityType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 8),
    _NwAtNetDiagOutboundNBPEntityType_Type()
)
nwAtNetDiagOutboundNBPEntityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundNBPEntityType.setStatus("mandatory")
_NwAtNetDiagOutboundNBPEntityZone_Type = AtName
_NwAtNetDiagOutboundNBPEntityZone_Object = MibScalar
nwAtNetDiagOutboundNBPEntityZone = _NwAtNetDiagOutboundNBPEntityZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 9),
    _NwAtNetDiagOutboundNBPEntityZone_Type()
)
nwAtNetDiagOutboundNBPEntityZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundNBPEntityZone.setStatus("mandatory")


class _NwAtNetDiagOutboundNBPType_Type(Integer32):
    """Custom type nwAtNetDiagOutboundNBPType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bcastRequestBcast", 6),
          ("bcastRequestDirect", 7),
          ("forwardRequestBcast", 8),
          ("forwardRequestDirect", 9),
          ("localRequest", 2),
          ("lookupBcast", 4),
          ("lookupDirect", 5),
          ("lookupMcast", 3),
          ("noAction", 1),
          ("other", 10))
    )


_NwAtNetDiagOutboundNBPType_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundNBPType_Object = MibScalar
nwAtNetDiagOutboundNBPType = _NwAtNetDiagOutboundNBPType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 10),
    _NwAtNetDiagOutboundNBPType_Type()
)
nwAtNetDiagOutboundNBPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundNBPType.setStatus("mandatory")


class _NwAtNetDiagOutboundNBPStatus_Type(Integer32):
    """Custom type nwAtNetDiagOutboundNBPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 3),
          ("inProgress", 2),
          ("inactive", 1))
    )


_NwAtNetDiagOutboundNBPStatus_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundNBPStatus_Object = MibScalar
nwAtNetDiagOutboundNBPStatus = _NwAtNetDiagOutboundNBPStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 11),
    _NwAtNetDiagOutboundNBPStatus_Type()
)
nwAtNetDiagOutboundNBPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundNBPStatus.setStatus("mandatory")


class _NwAtNetDiagOutboundRTMPType_Type(Integer32):
    """Custom type nwAtNetDiagOutboundRTMPType based on Integer32"""
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
        *(("bcastRDRequestFullTable", 7),
          ("bcastRDRequestSplitHorizon", 5),
          ("bcastRequest", 3),
          ("noAction", 1),
          ("other", 8),
          ("sendRDRequestFullTable", 6),
          ("sendRDRequestSplitHorizon", 4),
          ("sendRequest", 2))
    )


_NwAtNetDiagOutboundRTMPType_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundRTMPType_Object = MibScalar
nwAtNetDiagOutboundRTMPType = _NwAtNetDiagOutboundRTMPType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 12),
    _NwAtNetDiagOutboundRTMPType_Type()
)
nwAtNetDiagOutboundRTMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundRTMPType.setStatus("mandatory")


class _NwAtNetDiagOutboundRTMPStatus_Type(Integer32):
    """Custom type nwAtNetDiagOutboundRTMPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 3),
          ("inProgress", 2),
          ("inactive", 1))
    )


_NwAtNetDiagOutboundRTMPStatus_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundRTMPStatus_Object = MibScalar
nwAtNetDiagOutboundRTMPStatus = _NwAtNetDiagOutboundRTMPStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 13),
    _NwAtNetDiagOutboundRTMPStatus_Type()
)
nwAtNetDiagOutboundRTMPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundRTMPStatus.setStatus("mandatory")
_NwAtNetDiagOutboundRTMPNetStart_Type = AtNetworkNumber
_NwAtNetDiagOutboundRTMPNetStart_Object = MibScalar
nwAtNetDiagOutboundRTMPNetStart = _NwAtNetDiagOutboundRTMPNetStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 14),
    _NwAtNetDiagOutboundRTMPNetStart_Type()
)
nwAtNetDiagOutboundRTMPNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundRTMPNetStart.setStatus("mandatory")
_NwAtNetDiagOutboundRTMPNetEnd_Type = AtNetworkNumber
_NwAtNetDiagOutboundRTMPNetEnd_Object = MibScalar
nwAtNetDiagOutboundRTMPNetEnd = _NwAtNetDiagOutboundRTMPNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 15),
    _NwAtNetDiagOutboundRTMPNetEnd_Type()
)
nwAtNetDiagOutboundRTMPNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundRTMPNetEnd.setStatus("mandatory")


class _NwAtNetDiagOutboundZIPType_Type(Integer32):
    """Custom type nwAtNetDiagOutboundZIPType based on Integer32"""
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
        *(("bcastGetNetInfo", 8),
          ("bcastQuery", 3),
          ("noAction", 1),
          ("other", 9),
          ("sendGetLocalZones", 5),
          ("sendGetMyZone", 6),
          ("sendGetNetInfo", 7),
          ("sendGetZonesList", 4),
          ("sendQuery", 2))
    )


_NwAtNetDiagOutboundZIPType_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundZIPType_Object = MibScalar
nwAtNetDiagOutboundZIPType = _NwAtNetDiagOutboundZIPType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 16),
    _NwAtNetDiagOutboundZIPType_Type()
)
nwAtNetDiagOutboundZIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPType.setStatus("mandatory")


class _NwAtNetDiagOutboundZIPStatus_Type(Integer32):
    """Custom type nwAtNetDiagOutboundZIPStatus based on Integer32"""
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
        *(("atpInProgress", 3),
          ("done", 5),
          ("gniInProgress", 4),
          ("inactive", 1),
          ("queryInProgress", 2))
    )


_NwAtNetDiagOutboundZIPStatus_Type.__name__ = "Integer32"
_NwAtNetDiagOutboundZIPStatus_Object = MibScalar
nwAtNetDiagOutboundZIPStatus = _NwAtNetDiagOutboundZIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 17),
    _NwAtNetDiagOutboundZIPStatus_Type()
)
nwAtNetDiagOutboundZIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPStatus.setStatus("mandatory")
_NwAtNetDiagOutboundZIPQueryNet_Type = AtNetworkNumber
_NwAtNetDiagOutboundZIPQueryNet_Object = MibScalar
nwAtNetDiagOutboundZIPQueryNet = _NwAtNetDiagOutboundZIPQueryNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 18),
    _NwAtNetDiagOutboundZIPQueryNet_Type()
)
nwAtNetDiagOutboundZIPQueryNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPQueryNet.setStatus("mandatory")
_NwAtNetDiagOutboundZIPQueryZone_Type = AtName
_NwAtNetDiagOutboundZIPQueryZone_Object = MibScalar
nwAtNetDiagOutboundZIPQueryZone = _NwAtNetDiagOutboundZIPQueryZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 19),
    _NwAtNetDiagOutboundZIPQueryZone_Type()
)
nwAtNetDiagOutboundZIPQueryZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPQueryZone.setStatus("mandatory")
_NwAtNetDiagOutboundZIPGetNetInfoZone_Type = AtName
_NwAtNetDiagOutboundZIPGetNetInfoZone_Object = MibScalar
nwAtNetDiagOutboundZIPGetNetInfoZone = _NwAtNetDiagOutboundZIPGetNetInfoZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 20),
    _NwAtNetDiagOutboundZIPGetNetInfoZone_Type()
)
nwAtNetDiagOutboundZIPGetNetInfoZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPGetNetInfoZone.setStatus("mandatory")
_NwAtNetDiagOutboundZIPGetNetInfoNetStart_Type = AtNetworkNumber
_NwAtNetDiagOutboundZIPGetNetInfoNetStart_Object = MibScalar
nwAtNetDiagOutboundZIPGetNetInfoNetStart = _NwAtNetDiagOutboundZIPGetNetInfoNetStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 21),
    _NwAtNetDiagOutboundZIPGetNetInfoNetStart_Type()
)
nwAtNetDiagOutboundZIPGetNetInfoNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPGetNetInfoNetStart.setStatus("mandatory")
_NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Type = AtNetworkNumber
_NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Object = MibScalar
nwAtNetDiagOutboundZIPGetNetInfoNetEnd = _NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 22),
    _NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Type()
)
nwAtNetDiagOutboundZIPGetNetInfoNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPGetNetInfoNetEnd.setStatus("mandatory")
_NwAtNetDiagOutboundZIPGetNetInfoMulticast_Type = OctetString
_NwAtNetDiagOutboundZIPGetNetInfoMulticast_Object = MibScalar
nwAtNetDiagOutboundZIPGetNetInfoMulticast = _NwAtNetDiagOutboundZIPGetNetInfoMulticast_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 23),
    _NwAtNetDiagOutboundZIPGetNetInfoMulticast_Type()
)
nwAtNetDiagOutboundZIPGetNetInfoMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPGetNetInfoMulticast.setStatus("mandatory")
_NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Type = AtName
_NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Object = MibScalar
nwAtNetDiagOutboundZIPGetNetInfoDefaultZone = _NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 4, 2, 12, 3, 24),
    _NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Type()
)
nwAtNetDiagOutboundZIPGetNetInfoDefaultZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtNetDiagOutboundZIPGetNetInfoDefaultZone.setStatus("mandatory")
_NwRtrExperimental_ObjectIdentity = ObjectIdentity
nwRtrExperimental = _NwRtrExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 4)
)
_NwAtportZoneTable_Object = MibTable
nwAtportZoneTable = _NwAtportZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    nwAtportZoneTable.setStatus("mandatory")
_NwAtportZoneEntry_Object = MibTableRow
nwAtportZoneEntry = _NwAtportZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 4, 1, 1)
)
nwAtportZoneEntry.setIndexNames(
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtportZonePort"),
    (0, "CTRON-AppleTalk-ROUTER-MIB", "nwAtportZoneName"),
)
if mibBuilder.loadTexts:
    nwAtportZoneEntry.setStatus("mandatory")
_NwAtportZonePort_Type = Integer32
_NwAtportZonePort_Object = MibTableColumn
nwAtportZonePort = _NwAtportZonePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 4, 1, 1, 1),
    _NwAtportZonePort_Type()
)
nwAtportZonePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportZonePort.setStatus("mandatory")
_NwAtportZoneName_Type = AtName
_NwAtportZoneName_Object = MibTableColumn
nwAtportZoneName = _NwAtportZoneName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 4, 1, 1, 2),
    _NwAtportZoneName_Type()
)
nwAtportZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAtportZoneName.setStatus("mandatory")


class _NwAtportZoneStatus_Type(Integer32):
    """Custom type nwAtportZoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NwAtportZoneStatus_Type.__name__ = "Integer32"
_NwAtportZoneStatus_Object = MibTableColumn
nwAtportZoneStatus = _NwAtportZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 4, 1, 1, 3),
    _NwAtportZoneStatus_Type()
)
nwAtportZoneStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAtportZoneStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-AppleTalk-ROUTER-MIB",
    **{"AtNetworkNumber": AtNetworkNumber,
       "AtDdpNodeAddress": AtDdpNodeAddress,
       "AtName": AtName,
       "nwAtRouter": nwAtRouter,
       "nwAtMibs": nwAtMibs,
       "nwAtMibRevText": nwAtMibRevText,
       "nwAtComponents": nwAtComponents,
       "nwAtSystem": nwAtSystem,
       "nwAtSysConfig": nwAtSysConfig,
       "nwAtSysRouterId": nwAtSysRouterId,
       "nwAtSysAdministration": nwAtSysAdministration,
       "nwAtSysAdminSTATUS": nwAtSysAdminSTATUS,
       "nwAtSysOperSTATUS": nwAtSysOperSTATUS,
       "nwAtSysAdminReset": nwAtSysAdminReset,
       "nwAtSysOperationalTime": nwAtSysOperationalTime,
       "nwAtSysVersion": nwAtSysVersion,
       "nwAtForwarding": nwAtForwarding,
       "nwAtFwdSystem": nwAtFwdSystem,
       "nwAtFwdCounters": nwAtFwdCounters,
       "nwAtFwdCtrAdminSTATUS": nwAtFwdCtrAdminSTATUS,
       "nwAtFwdCtrReset": nwAtFwdCtrReset,
       "nwAtFwdCtrOperationalTime": nwAtFwdCtrOperationalTime,
       "nwAtFwdCtrInPkts": nwAtFwdCtrInPkts,
       "nwAtFwdCtrOutPkts": nwAtFwdCtrOutPkts,
       "nwAtFwdCtrFwdPkts": nwAtFwdCtrFwdPkts,
       "nwAtFwdCtrFilteredPkts": nwAtFwdCtrFilteredPkts,
       "nwAtFwdCtrDiscardPkts": nwAtFwdCtrDiscardPkts,
       "nwAtFwdCtrAddrErrPkts": nwAtFwdCtrAddrErrPkts,
       "nwAtFwdCtrLenErrPkts": nwAtFwdCtrLenErrPkts,
       "nwAtFwdCtrHdrErrPkts": nwAtFwdCtrHdrErrPkts,
       "nwAtFwdCtrInBytes": nwAtFwdCtrInBytes,
       "nwAtFwdCtrOutBytes": nwAtFwdCtrOutBytes,
       "nwAtFwdCtrFwdBytes": nwAtFwdCtrFwdBytes,
       "nwAtFwdCtrFilteredBytes": nwAtFwdCtrFilteredBytes,
       "nwAtFwdCtrDiscardBytes": nwAtFwdCtrDiscardBytes,
       "nwAtFwdCtrHostInPkts": nwAtFwdCtrHostInPkts,
       "nwAtFwdCtrHostOutPkts": nwAtFwdCtrHostOutPkts,
       "nwAtFwdCtrHostDiscardPkts": nwAtFwdCtrHostDiscardPkts,
       "nwAtFwdCtrHostInBytes": nwAtFwdCtrHostInBytes,
       "nwAtFwdCtrHostOutBytes": nwAtFwdCtrHostOutBytes,
       "nwAtFwdCtrHostDiscardBytes": nwAtFwdCtrHostDiscardBytes,
       "nwAtFwdInterfaces": nwAtFwdInterfaces,
       "nwAtFwdIfConfig": nwAtFwdIfConfig,
       "nwAtFwdIfTable": nwAtFwdIfTable,
       "nwAtFwdIfEntry": nwAtFwdIfEntry,
       "nwAtFwdIfIndex": nwAtFwdIfIndex,
       "nwAtFwdIfAdminSTATUS": nwAtFwdIfAdminSTATUS,
       "nwAtFwdIfOperSTATUS": nwAtFwdIfOperSTATUS,
       "nwAtFwdIfOperationalTime": nwAtFwdIfOperationalTime,
       "nwAtFwdIfControl": nwAtFwdIfControl,
       "nwAtFwdIfMtu": nwAtFwdIfMtu,
       "nwAtFwdIfForwarding": nwAtFwdIfForwarding,
       "nwAtFwdIfFrameType": nwAtFwdIfFrameType,
       "nwAtFwdIfAclIdentifier": nwAtFwdIfAclIdentifier,
       "nwAtFwdIfAclSTATUS": nwAtFwdIfAclSTATUS,
       "nwAtFwdIfCacheControl": nwAtFwdIfCacheControl,
       "nwAtFwdIfCacheEntries": nwAtFwdIfCacheEntries,
       "nwAtFwdIfCacheHits": nwAtFwdIfCacheHits,
       "nwAtFwdIfCacheMisses": nwAtFwdIfCacheMisses,
       "nwAtportTable": nwAtportTable,
       "nwAtportEntry": nwAtportEntry,
       "nwAtportIndex": nwAtportIndex,
       "nwAtportDescr": nwAtportDescr,
       "nwAtportType": nwAtportType,
       "nwAtportNetStart": nwAtportNetStart,
       "nwAtportNetEnd": nwAtportNetEnd,
       "nwAtportNetAddress": nwAtportNetAddress,
       "nwAtportSTATUS": nwAtportSTATUS,
       "nwAtportNetConfig": nwAtportNetConfig,
       "nwAtportZoneConfig": nwAtportZoneConfig,
       "nwAtportZoneDefault": nwAtportZoneDefault,
       "nwAtportIfIndex": nwAtportIfIndex,
       "nwAtportNetFrom": nwAtportNetFrom,
       "nwAtportZoneFrom": nwAtportZoneFrom,
       "nwAtportInPkts": nwAtportInPkts,
       "nwAtportOutPkts": nwAtportOutPkts,
       "nwAtportHome": nwAtportHome,
       "nwAtportCurrentZone": nwAtportCurrentZone,
       "nwAtportConflictPhysAddr": nwAtportConflictPhysAddr,
       "nwAtFwdIfCounters": nwAtFwdIfCounters,
       "nwAtFwdIfCtrTable": nwAtFwdIfCtrTable,
       "nwAtFwdIfCtrEntry": nwAtFwdIfCtrEntry,
       "nwAtFwdIfCtrIfIndex": nwAtFwdIfCtrIfIndex,
       "nwAtFwdIfCtrAdminSTATUS": nwAtFwdIfCtrAdminSTATUS,
       "nwAtFwdIfCtrReset": nwAtFwdIfCtrReset,
       "nwAtFwdIfCtrOperationalTime": nwAtFwdIfCtrOperationalTime,
       "nwAtFwdIfCtrInPkts": nwAtFwdIfCtrInPkts,
       "nwAtFwdIfCtrOutPkts": nwAtFwdIfCtrOutPkts,
       "nwAtFwdIfCtrFwdPkts": nwAtFwdIfCtrFwdPkts,
       "nwAtFwdIfCtrFilteredPkts": nwAtFwdIfCtrFilteredPkts,
       "nwAtFwdIfCtrDiscardPkts": nwAtFwdIfCtrDiscardPkts,
       "nwAtFwdIfCtrAddrErrPkts": nwAtFwdIfCtrAddrErrPkts,
       "nwAtFwdIfCtrLenErrPkts": nwAtFwdIfCtrLenErrPkts,
       "nwAtFwdIfCtrHdrErrPkts": nwAtFwdIfCtrHdrErrPkts,
       "nwAtFwdIfCtrInBytes": nwAtFwdIfCtrInBytes,
       "nwAtFwdIfCtrOutBytes": nwAtFwdIfCtrOutBytes,
       "nwAtFwdIfCtrFwdBytes": nwAtFwdIfCtrFwdBytes,
       "nwAtFwdIfCtrFilteredBytes": nwAtFwdIfCtrFilteredBytes,
       "nwAtFwdIfCtrDiscardBytes": nwAtFwdIfCtrDiscardBytes,
       "nwAtFwdIfCtrHostInPkts": nwAtFwdIfCtrHostInPkts,
       "nwAtFwdIfCtrHostOutPkts": nwAtFwdIfCtrHostOutPkts,
       "nwAtFwdIfCtrHostDiscardPkts": nwAtFwdIfCtrHostDiscardPkts,
       "nwAtFwdIfCtrHostInBytes": nwAtFwdIfCtrHostInBytes,
       "nwAtFwdIfCtrHostOutBytes": nwAtFwdIfCtrHostOutBytes,
       "nwAtFwdIfCtrHostDiscardBytes": nwAtFwdIfCtrHostDiscardBytes,
       "nwAtTopology": nwAtTopology,
       "nwAtDistanceVector": nwAtDistanceVector,
       "nwAtProto": nwAtProto,
       "nwAtProtoSystem": nwAtProtoSystem,
       "nwAtProtoConfig": nwAtProtoConfig,
       "nwAtProtoAdminSTATUS": nwAtProtoAdminSTATUS,
       "nwAtProtoOperSTATUS": nwAtProtoOperSTATUS,
       "nwAtProtoAdminReset": nwAtProtoAdminReset,
       "nwAtProtoOperationalTime": nwAtProtoOperationalTime,
       "nwAtProtoVersion": nwAtProtoVersion,
       "nwAtProtoStackSize": nwAtProtoStackSize,
       "nwAtProtoThreadPriority": nwAtProtoThreadPriority,
       "nwAtProtoDatabaseThreshold": nwAtProtoDatabaseThreshold,
       "nwAtProtoAgeOut": nwAtProtoAgeOut,
       "nwAtProtoHoldDown": nwAtProtoHoldDown,
       "nwAtProtoCounters": nwAtProtoCounters,
       "nwAtProtoCtrAdminSTATUS": nwAtProtoCtrAdminSTATUS,
       "nwAtProtoCtrReset": nwAtProtoCtrReset,
       "nwAtProtoCtrOperationalTime": nwAtProtoCtrOperationalTime,
       "nwAtProtoCtrInPkts": nwAtProtoCtrInPkts,
       "nwAtProtoCtrOutPkts": nwAtProtoCtrOutPkts,
       "nwAtProtoCtrFilteredPkts": nwAtProtoCtrFilteredPkts,
       "nwAtProtoCtrDiscardPkts": nwAtProtoCtrDiscardPkts,
       "nwAtProtoCtrInBytes": nwAtProtoCtrInBytes,
       "nwAtProtoCtrOutBytes": nwAtProtoCtrOutBytes,
       "nwAtProtoCtrFilteredBytes": nwAtProtoCtrFilteredBytes,
       "nwAtProtoCtrDiscardBytes": nwAtProtoCtrDiscardBytes,
       "nwAtProtoInterface": nwAtProtoInterface,
       "nwAtProtoIfConfig": nwAtProtoIfConfig,
       "nwAtProtoIfTable": nwAtProtoIfTable,
       "nwAtProtoIfEntry": nwAtProtoIfEntry,
       "nwAtProtoIfIndex": nwAtProtoIfIndex,
       "nwAtProtoIfAdminSTATUS": nwAtProtoIfAdminSTATUS,
       "nwAtProtoIfOperSTATUS": nwAtProtoIfOperSTATUS,
       "nwAtProtoIfOperationalTime": nwAtProtoIfOperationalTime,
       "nwAtProtoIfVersion": nwAtProtoIfVersion,
       "nwAtProtoIfAdvertisement": nwAtProtoIfAdvertisement,
       "nwAtProtoIfFloodDelay": nwAtProtoIfFloodDelay,
       "nwAtProtoIfRequestDelay": nwAtProtoIfRequestDelay,
       "nwAtProtoIfPriority": nwAtProtoIfPriority,
       "nwAtProtoIfHelloTimer": nwAtProtoIfHelloTimer,
       "nwAtProtoIfSplitHorizon": nwAtProtoIfSplitHorizon,
       "nwAtProtoIfPoisonReverse": nwAtProtoIfPoisonReverse,
       "nwAtProtoIfSnooping": nwAtProtoIfSnooping,
       "nwAtProtoIfType": nwAtProtoIfType,
       "nwAtProtoIfXmitCost": nwAtProtoIfXmitCost,
       "nwAtProtoIfAclIdentifier": nwAtProtoIfAclIdentifier,
       "nwAtProtoIfAclSTATUS": nwAtProtoIfAclSTATUS,
       "nwAtProtoIfCounters": nwAtProtoIfCounters,
       "nwAtProtoIfCtrTable": nwAtProtoIfCtrTable,
       "nwAtProtoIfCtrEntry": nwAtProtoIfCtrEntry,
       "nwAtProtoIfCtrIfIndex": nwAtProtoIfCtrIfIndex,
       "nwAtProtoIfCtrAdminSTATUS": nwAtProtoIfCtrAdminSTATUS,
       "nwAtProtoIfCtrReset": nwAtProtoIfCtrReset,
       "nwAtProtoIfCtrOperationalTime": nwAtProtoIfCtrOperationalTime,
       "nwAtProtoIfCtrInPkts": nwAtProtoIfCtrInPkts,
       "nwAtProtoIfCtrOutPkts": nwAtProtoIfCtrOutPkts,
       "nwAtProtoIfCtrFilteredPkts": nwAtProtoIfCtrFilteredPkts,
       "nwAtProtoIfCtrDiscardPkts": nwAtProtoIfCtrDiscardPkts,
       "nwAtProtoIfCtrInBytes": nwAtProtoIfCtrInBytes,
       "nwAtProtoIfCtrOutBytes": nwAtProtoIfCtrOutBytes,
       "nwAtProtoIfCtrFilteredBytes": nwAtProtoIfCtrFilteredBytes,
       "nwAtProtoIfCtrDiscardBytes": nwAtProtoIfCtrDiscardBytes,
       "nwAtLinkState": nwAtLinkState,
       "nwAtFib": nwAtFib,
       "nwAtFibTable": nwAtFibTable,
       "nwAtFibEntry": nwAtFibEntry,
       "nwAtFibStartNet": nwAtFibStartNet,
       "nwAtFibEndNet": nwAtFibEndNet,
       "nwAtFibNextHop": nwAtFibNextHop,
       "nwAtFibNextHopIf": nwAtFibNextHopIf,
       "nwAtFibHops": nwAtFibHops,
       "nwAtFibRouteType": nwAtFibRouteType,
       "nwAtEndSystems": nwAtEndSystems,
       "nwAtHostsSystem": nwAtHostsSystem,
       "nwAtHostsTimeToLive": nwAtHostsTimeToLive,
       "nwAtHostsRetryCount": nwAtHostsRetryCount,
       "nwAtHostsInterfaces": nwAtHostsInterfaces,
       "nwAtHostCtlTable": nwAtHostCtlTable,
       "nwAtHostCtlEntry": nwAtHostCtlEntry,
       "nwAtHostCtlIfIndex": nwAtHostCtlIfIndex,
       "nwAtHostCtlAdminSTATUS": nwAtHostCtlAdminSTATUS,
       "nwAtHostCtlOperSTATUS": nwAtHostCtlOperSTATUS,
       "nwAtHostCtlOperationalTime": nwAtHostCtlOperationalTime,
       "nwAtHostCtlProtocol": nwAtHostCtlProtocol,
       "nwAtHostCtlSnooping": nwAtHostCtlSnooping,
       "nwAtHostCtlProxy": nwAtHostCtlProxy,
       "nwAtHostCtlCacheMax": nwAtHostCtlCacheMax,
       "nwAtHostCtlCacheSize": nwAtHostCtlCacheSize,
       "nwAtHostCtlNumStatics": nwAtHostCtlNumStatics,
       "nwAtHostCtlNumDynamics": nwAtHostCtlNumDynamics,
       "nwAtHostCtlCacheHits": nwAtHostCtlCacheHits,
       "nwAtHostCtlCacheMisses": nwAtHostCtlCacheMisses,
       "nwAtHostsToMedia": nwAtHostsToMedia,
       "nwAtHostMapTable": nwAtHostMapTable,
       "nwAtHostMapEntry": nwAtHostMapEntry,
       "nwAtHostMapIfIndex": nwAtHostMapIfIndex,
       "nwAtHostMapAtAddr": nwAtHostMapAtAddr,
       "nwAtHostMapPhysAddr": nwAtHostMapPhysAddr,
       "nwAtHostMapType": nwAtHostMapType,
       "nwAtHostMapCircuitID": nwAtHostMapCircuitID,
       "nwAtHostMapFraming": nwAtHostMapFraming,
       "nwAtHostMapPortNumber": nwAtHostMapPortNumber,
       "nwAtAccessControl": nwAtAccessControl,
       "nwAtAclValidEntries": nwAtAclValidEntries,
       "nwAtAclTable": nwAtAclTable,
       "nwAtAclEntry": nwAtAclEntry,
       "nwAtAclIdentifier": nwAtAclIdentifier,
       "nwAtAclSequence": nwAtAclSequence,
       "nwAtAclPermission": nwAtAclPermission,
       "nwAtAclMatches": nwAtAclMatches,
       "nwAtAclDestZone": nwAtAclDestZone,
       "nwAtAclSrcZone": nwAtAclSrcZone,
       "nwAtFilters": nwAtFilters,
       "nwAtRedirector": nwAtRedirector,
       "nwAtEvent": nwAtEvent,
       "nwAtEventLogConfig": nwAtEventLogConfig,
       "nwAtEventAdminSTATUS": nwAtEventAdminSTATUS,
       "nwAtEventMaxEntries": nwAtEventMaxEntries,
       "nwAtEventTraceAll": nwAtEventTraceAll,
       "nwAtEventLogFilterTable": nwAtEventLogFilterTable,
       "nwAtEventFilterTable": nwAtEventFilterTable,
       "nwAtEventFilterEntry": nwAtEventFilterEntry,
       "nwAtEventFltrProtocol": nwAtEventFltrProtocol,
       "nwAtEventFltrIfNum": nwAtEventFltrIfNum,
       "nwAtEventFltrControl": nwAtEventFltrControl,
       "nwAtEventFltrType": nwAtEventFltrType,
       "nwAtEventFltrSeverity": nwAtEventFltrSeverity,
       "nwAtEventFltrAction": nwAtEventFltrAction,
       "nwAtEventLogTable": nwAtEventLogTable,
       "nwAtEventTable": nwAtEventTable,
       "nwAtEventEntry": nwAtEventEntry,
       "nwAtEventNumber": nwAtEventNumber,
       "nwAtEventTime": nwAtEventTime,
       "nwAtEventType": nwAtEventType,
       "nwAtEventSeverity": nwAtEventSeverity,
       "nwAtEventProtocol": nwAtEventProtocol,
       "nwAtEventIfNum": nwAtEventIfNum,
       "nwAtEventTextString": nwAtEventTextString,
       "nwAtWorkGroup": nwAtWorkGroup,
       "nwAtNetDiag": nwAtNetDiag,
       "nwAtNetDiagPing": nwAtNetDiagPing,
       "nwAtNetDiagTelnet": nwAtNetDiagTelnet,
       "nwAtNetDiagOutbound": nwAtNetDiagOutbound,
       "nwAtNetDiagOutboundNetAddress": nwAtNetDiagOutboundNetAddress,
       "nwAtNetDiagOutboundPort": nwAtNetDiagOutboundPort,
       "nwAtNetDiagOutboundTimeout": nwAtNetDiagOutboundTimeout,
       "nwAtNetDiagOutboundRetries": nwAtNetDiagOutboundRetries,
       "nwAtNetDiagOutboundATEchoType": nwAtNetDiagOutboundATEchoType,
       "nwAtNetDiagOutboundATEchoStatus": nwAtNetDiagOutboundATEchoStatus,
       "nwAtNetDiagOutboundNBPEntityObject": nwAtNetDiagOutboundNBPEntityObject,
       "nwAtNetDiagOutboundNBPEntityType": nwAtNetDiagOutboundNBPEntityType,
       "nwAtNetDiagOutboundNBPEntityZone": nwAtNetDiagOutboundNBPEntityZone,
       "nwAtNetDiagOutboundNBPType": nwAtNetDiagOutboundNBPType,
       "nwAtNetDiagOutboundNBPStatus": nwAtNetDiagOutboundNBPStatus,
       "nwAtNetDiagOutboundRTMPType": nwAtNetDiagOutboundRTMPType,
       "nwAtNetDiagOutboundRTMPStatus": nwAtNetDiagOutboundRTMPStatus,
       "nwAtNetDiagOutboundRTMPNetStart": nwAtNetDiagOutboundRTMPNetStart,
       "nwAtNetDiagOutboundRTMPNetEnd": nwAtNetDiagOutboundRTMPNetEnd,
       "nwAtNetDiagOutboundZIPType": nwAtNetDiagOutboundZIPType,
       "nwAtNetDiagOutboundZIPStatus": nwAtNetDiagOutboundZIPStatus,
       "nwAtNetDiagOutboundZIPQueryNet": nwAtNetDiagOutboundZIPQueryNet,
       "nwAtNetDiagOutboundZIPQueryZone": nwAtNetDiagOutboundZIPQueryZone,
       "nwAtNetDiagOutboundZIPGetNetInfoZone": nwAtNetDiagOutboundZIPGetNetInfoZone,
       "nwAtNetDiagOutboundZIPGetNetInfoNetStart": nwAtNetDiagOutboundZIPGetNetInfoNetStart,
       "nwAtNetDiagOutboundZIPGetNetInfoNetEnd": nwAtNetDiagOutboundZIPGetNetInfoNetEnd,
       "nwAtNetDiagOutboundZIPGetNetInfoMulticast": nwAtNetDiagOutboundZIPGetNetInfoMulticast,
       "nwAtNetDiagOutboundZIPGetNetInfoDefaultZone": nwAtNetDiagOutboundZIPGetNetInfoDefaultZone,
       "nwRtrExperimental": nwRtrExperimental,
       "nwAtportZoneTable": nwAtportZoneTable,
       "nwAtportZoneEntry": nwAtportZoneEntry,
       "nwAtportZonePort": nwAtportZonePort,
       "nwAtportZoneName": nwAtportZoneName,
       "nwAtportZoneStatus": nwAtportZoneStatus}
)
