# SNMP MIB module (CAPWAP-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAPWAP-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:31 2024
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

(InterfaceIndex,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifGeneralInformationGroup")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

capwapBaseMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 60)
)
capwapBaseMIB.setRevisions(
        ("2010-07-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CapwapBaseObjects_ObjectIdentity = ObjectIdentity
capwapBaseObjects = _CapwapBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 1)
)
_CapwapBaseParameters_ObjectIdentity = ObjectIdentity
capwapBaseParameters = _CapwapBaseParameters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 1, 3)
)


class _CapwapBaseAcMaxRetransmit_Type(Unsigned32):
    """Custom type capwapBaseAcMaxRetransmit based on Unsigned32"""
    defaultValue = 5


_CapwapBaseAcMaxRetransmit_Object = MibScalar
capwapBaseAcMaxRetransmit = _CapwapBaseAcMaxRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 1),
    _CapwapBaseAcMaxRetransmit_Type()
)
capwapBaseAcMaxRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcMaxRetransmit.setStatus("current")


class _CapwapBaseAcChangeStatePendingTimer_Type(Unsigned32):
    """Custom type capwapBaseAcChangeStatePendingTimer based on Unsigned32"""
    defaultValue = 150


_CapwapBaseAcChangeStatePendingTimer_Object = MibScalar
capwapBaseAcChangeStatePendingTimer = _CapwapBaseAcChangeStatePendingTimer_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 2),
    _CapwapBaseAcChangeStatePendingTimer_Type()
)
capwapBaseAcChangeStatePendingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcChangeStatePendingTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcChangeStatePendingTimer.setUnits("second")


class _CapwapBaseAcDataCheckTimer_Type(Unsigned32):
    """Custom type capwapBaseAcDataCheckTimer based on Unsigned32"""
    defaultValue = 30


_CapwapBaseAcDataCheckTimer_Object = MibScalar
capwapBaseAcDataCheckTimer = _CapwapBaseAcDataCheckTimer_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 3),
    _CapwapBaseAcDataCheckTimer_Type()
)
capwapBaseAcDataCheckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcDataCheckTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcDataCheckTimer.setUnits("second")


class _CapwapBaseAcEchoInterval_Type(Unsigned32):
    """Custom type capwapBaseAcEchoInterval based on Unsigned32"""
    defaultValue = 10


_CapwapBaseAcEchoInterval_Object = MibScalar
capwapBaseAcEchoInterval = _CapwapBaseAcEchoInterval_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 5),
    _CapwapBaseAcEchoInterval_Type()
)
capwapBaseAcEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcEchoInterval.setUnits("second")


class _CapwapBaseAcRetransmitInterval_Type(Unsigned32):
    """Custom type capwapBaseAcRetransmitInterval based on Unsigned32"""
    defaultValue = 3


_CapwapBaseAcRetransmitInterval_Object = MibScalar
capwapBaseAcRetransmitInterval = _CapwapBaseAcRetransmitInterval_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 6),
    _CapwapBaseAcRetransmitInterval_Type()
)
capwapBaseAcRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcRetransmitInterval.setUnits("second")


class _CapwapBaseAcWaitJoinTimer_Type(Unsigned32):
    """Custom type capwapBaseAcWaitJoinTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4294967295),
    )


_CapwapBaseAcWaitJoinTimer_Type.__name__ = "Unsigned32"
_CapwapBaseAcWaitJoinTimer_Object = MibScalar
capwapBaseAcWaitJoinTimer = _CapwapBaseAcWaitJoinTimer_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 9),
    _CapwapBaseAcWaitJoinTimer_Type()
)
capwapBaseAcWaitJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcWaitJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcWaitJoinTimer.setUnits("second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAPWAP-BASE-MIB",
    **{"capwapBaseMIB": capwapBaseMIB,
       "capwapBaseObjects": capwapBaseObjects,
       "capwapBaseParameters": capwapBaseParameters,
       "capwapBaseAcMaxRetransmit": capwapBaseAcMaxRetransmit,
       "capwapBaseAcChangeStatePendingTimer": capwapBaseAcChangeStatePendingTimer,
       "capwapBaseAcDataCheckTimer": capwapBaseAcDataCheckTimer,
       "capwapBaseAcEchoInterval": capwapBaseAcEchoInterval,
       "capwapBaseAcRetransmitInterval": capwapBaseAcRetransmitInterval,
       "capwapBaseAcWaitJoinTimer": capwapBaseAcWaitJoinTimer}
)
