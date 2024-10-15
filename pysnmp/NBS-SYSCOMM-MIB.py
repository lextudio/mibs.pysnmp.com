# SNMP MIB module (NBS-SYSCOMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-SYSCOMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:03 2024
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

(InetAddress,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsSyscommMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 214)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsSyscommInetGrp_ObjectIdentity = ObjectIdentity
nbsSyscommInetGrp = _NbsSyscommInetGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 214, 3)
)
if mibBuilder.loadTexts:
    nbsSyscommInetGrp.setStatus("current")
_NbsSyscommInetSlaacAddr_Type = InetAddress
_NbsSyscommInetSlaacAddr_Object = MibScalar
nbsSyscommInetSlaacAddr = _NbsSyscommInetSlaacAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 3),
    _NbsSyscommInetSlaacAddr_Type()
)
nbsSyscommInetSlaacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyscommInetSlaacAddr.setStatus("current")
_NbsSyscommInetSlaacAddrPrefix_Type = InetAddressPrefixLength
_NbsSyscommInetSlaacAddrPrefix_Object = MibScalar
nbsSyscommInetSlaacAddrPrefix = _NbsSyscommInetSlaacAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 5),
    _NbsSyscommInetSlaacAddrPrefix_Type()
)
nbsSyscommInetSlaacAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyscommInetSlaacAddrPrefix.setStatus("current")
_NbsSyscommInetAddrAdmin_Type = InetAddress
_NbsSyscommInetAddrAdmin_Object = MibScalar
nbsSyscommInetAddrAdmin = _NbsSyscommInetAddrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 10),
    _NbsSyscommInetAddrAdmin_Type()
)
nbsSyscommInetAddrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyscommInetAddrAdmin.setStatus("current")
_NbsSyscommInetAddrOper_Type = InetAddress
_NbsSyscommInetAddrOper_Object = MibScalar
nbsSyscommInetAddrOper = _NbsSyscommInetAddrOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 11),
    _NbsSyscommInetAddrOper_Type()
)
nbsSyscommInetAddrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyscommInetAddrOper.setStatus("current")


class _NbsSyscommInetAddrPrefixAdmin_Type(InetAddressPrefixLength):
    """Custom type nbsSyscommInetAddrPrefixAdmin based on InetAddressPrefixLength"""
    defaultValue = 64


_NbsSyscommInetAddrPrefixAdmin_Object = MibScalar
nbsSyscommInetAddrPrefixAdmin = _NbsSyscommInetAddrPrefixAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 22),
    _NbsSyscommInetAddrPrefixAdmin_Type()
)
nbsSyscommInetAddrPrefixAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyscommInetAddrPrefixAdmin.setStatus("current")
_NbsSyscommInetAddrPrefixOper_Type = InetAddressPrefixLength
_NbsSyscommInetAddrPrefixOper_Object = MibScalar
nbsSyscommInetAddrPrefixOper = _NbsSyscommInetAddrPrefixOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 23),
    _NbsSyscommInetAddrPrefixOper_Type()
)
nbsSyscommInetAddrPrefixOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyscommInetAddrPrefixOper.setStatus("current")
_NbsSyscommGateAddrAdmin_Type = InetAddress
_NbsSyscommGateAddrAdmin_Object = MibScalar
nbsSyscommGateAddrAdmin = _NbsSyscommGateAddrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 30),
    _NbsSyscommGateAddrAdmin_Type()
)
nbsSyscommGateAddrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyscommGateAddrAdmin.setStatus("current")
_NbsSyscommGateAddrOper_Type = InetAddress
_NbsSyscommGateAddrOper_Object = MibScalar
nbsSyscommGateAddrOper = _NbsSyscommGateAddrOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 3, 31),
    _NbsSyscommGateAddrOper_Type()
)
nbsSyscommGateAddrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyscommGateAddrOper.setStatus("current")
_NbsSyscommEventGrp_ObjectIdentity = ObjectIdentity
nbsSyscommEventGrp = _NbsSyscommEventGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 214, 100)
)
if mibBuilder.loadTexts:
    nbsSyscommEventGrp.setStatus("current")
_NbsSyscommEvents_ObjectIdentity = ObjectIdentity
nbsSyscommEvents = _NbsSyscommEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 214, 100, 0)
)
if mibBuilder.loadTexts:
    nbsSyscommEvents.setStatus("current")
_NbsSyscommInetAddrPrior_Type = InetAddress
_NbsSyscommInetAddrPrior_Object = MibScalar
nbsSyscommInetAddrPrior = _NbsSyscommInetAddrPrior_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 100, 311),
    _NbsSyscommInetAddrPrior_Type()
)
nbsSyscommInetAddrPrior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyscommInetAddrPrior.setStatus("current")
_NbsSyscommGateAddrPrior_Type = InetAddress
_NbsSyscommGateAddrPrior_Object = MibScalar
nbsSyscommGateAddrPrior = _NbsSyscommGateAddrPrior_Object(
    (1, 3, 6, 1, 4, 1, 629, 214, 100, 331),
    _NbsSyscommGateAddrPrior_Type()
)
nbsSyscommGateAddrPrior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyscommGateAddrPrior.setStatus("current")

# Managed Objects groups


# Notification objects

nbsSyscommInetCfgChanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 214, 100, 0, 30)
)
nbsSyscommInetCfgChanging.setObjects(
      *(("NBS-SYSCOMM-MIB", "nbsSyscommInetAddrAdmin"),
        ("NBS-SYSCOMM-MIB", "nbsSyscommGateAddrAdmin"))
)
if mibBuilder.loadTexts:
    nbsSyscommInetCfgChanging.setStatus(
        "current"
    )

nbsSyscommInetCfgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 214, 100, 0, 31)
)
nbsSyscommInetCfgChanged.setObjects(
      *(("NBS-SYSCOMM-MIB", "nbsSyscommInetAddrPrior"),
        ("NBS-SYSCOMM-MIB", "nbsSyscommGateAddrPrior"))
)
if mibBuilder.loadTexts:
    nbsSyscommInetCfgChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-SYSCOMM-MIB",
    **{"nbsSyscommMib": nbsSyscommMib,
       "nbsSyscommInetGrp": nbsSyscommInetGrp,
       "nbsSyscommInetSlaacAddr": nbsSyscommInetSlaacAddr,
       "nbsSyscommInetSlaacAddrPrefix": nbsSyscommInetSlaacAddrPrefix,
       "nbsSyscommInetAddrAdmin": nbsSyscommInetAddrAdmin,
       "nbsSyscommInetAddrOper": nbsSyscommInetAddrOper,
       "nbsSyscommInetAddrPrefixAdmin": nbsSyscommInetAddrPrefixAdmin,
       "nbsSyscommInetAddrPrefixOper": nbsSyscommInetAddrPrefixOper,
       "nbsSyscommGateAddrAdmin": nbsSyscommGateAddrAdmin,
       "nbsSyscommGateAddrOper": nbsSyscommGateAddrOper,
       "nbsSyscommEventGrp": nbsSyscommEventGrp,
       "nbsSyscommEvents": nbsSyscommEvents,
       "nbsSyscommInetCfgChanging": nbsSyscommInetCfgChanging,
       "nbsSyscommInetCfgChanged": nbsSyscommInetCfgChanged,
       "nbsSyscommInetAddrPrior": nbsSyscommInetAddrPrior,
       "nbsSyscommGateAddrPrior": nbsSyscommGateAddrPrior}
)
