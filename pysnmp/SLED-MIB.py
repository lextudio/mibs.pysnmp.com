# SNMP MIB module (SLED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SLED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:14 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sledMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13)
)
sledMib.setRevisions(
        ("2007-05-18 00:00",
         "2006-07-28 00:00",
         "2005-02-09 00:00",
         "2004-11-24 00:00",
         "2003-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SledNotifications_ObjectIdentity = ObjectIdentity
sledNotifications = _SledNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 0)
)
_SledMibObjects_ObjectIdentity = ObjectIdentity
sledMibObjects = _SledMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1)
)
_SledGlobal_ObjectIdentity = ObjectIdentity
sledGlobal = _SledGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 1)
)


class _SledGlobalEnable_Type(TruthValue):
    """Custom type sledGlobalEnable based on TruthValue"""


_SledGlobalEnable_Object = MibScalar
sledGlobalEnable = _SledGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 1, 1),
    _SledGlobalEnable_Type()
)
sledGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledGlobalEnable.setStatus("current")
_SledLoopback_ObjectIdentity = ObjectIdentity
sledLoopback = _SledLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 2)
)
_SledLoopbackInterface_Type = InterfaceIndex
_SledLoopbackInterface_Object = MibScalar
sledLoopbackInterface = _SledLoopbackInterface_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 2, 1),
    _SledLoopbackInterface_Type()
)
sledLoopbackInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledLoopbackInterface.setStatus("current")


class _SledLoopbackEnable_Type(TruthValue):
    """Custom type sledLoopbackEnable based on TruthValue"""


_SledLoopbackEnable_Object = MibScalar
sledLoopbackEnable = _SledLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 2, 2),
    _SledLoopbackEnable_Type()
)
sledLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledLoopbackEnable.setStatus("current")


class _SledLoopbackPktHdr_Type(OctetString):
    """Custom type sledLoopbackPktHdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(42, 42),
    )


_SledLoopbackPktHdr_Type.__name__ = "OctetString"
_SledLoopbackPktHdr_Object = MibScalar
sledLoopbackPktHdr = _SledLoopbackPktHdr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 2, 3),
    _SledLoopbackPktHdr_Type()
)
sledLoopbackPktHdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledLoopbackPktHdr.setStatus("current")
_SledPktGen_ObjectIdentity = ObjectIdentity
sledPktGen = _SledPktGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 3)
)
_SledPktGenInterface_Type = InterfaceIndex
_SledPktGenInterface_Object = MibScalar
sledPktGenInterface = _SledPktGenInterface_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 3, 1),
    _SledPktGenInterface_Type()
)
sledPktGenInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledPktGenInterface.setStatus("current")


class _SledPktGenPayload_Type(OctetString):
    """Custom type sledPktGenPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 1518),
    )


_SledPktGenPayload_Type.__name__ = "OctetString"
_SledPktGenPayload_Object = MibScalar
sledPktGenPayload = _SledPktGenPayload_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 3, 2),
    _SledPktGenPayload_Type()
)
sledPktGenPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledPktGenPayload.setStatus("current")


class _SledPktGenRate_Type(Unsigned32):
    """Custom type sledPktGenRate based on Unsigned32"""
    defaultValue = 10


_SledPktGenRate_Object = MibScalar
sledPktGenRate = _SledPktGenRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 3, 3),
    _SledPktGenRate_Type()
)
sledPktGenRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledPktGenRate.setStatus("current")


class _SledPktGenNumPkts_Type(Unsigned32):
    """Custom type sledPktGenNumPkts based on Unsigned32"""
    defaultValue = 1


_SledPktGenNumPkts_Object = MibScalar
sledPktGenNumPkts = _SledPktGenNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 3, 4),
    _SledPktGenNumPkts_Type()
)
sledPktGenNumPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledPktGenNumPkts.setStatus("current")


class _SledPktGenTrigger_Type(Integer32):
    """Custom type sledPktGenTrigger based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_SledPktGenTrigger_Type.__name__ = "Integer32"
_SledPktGenTrigger_Object = MibScalar
sledPktGenTrigger = _SledPktGenTrigger_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 3, 5),
    _SledPktGenTrigger_Type()
)
sledPktGenTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sledPktGenTrigger.setStatus("current")
_SledPktGenLastTrigger_Type = TimeStamp
_SledPktGenLastTrigger_Object = MibScalar
sledPktGenLastTrigger = _SledPktGenLastTrigger_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 1, 3, 6),
    _SledPktGenLastTrigger_Type()
)
sledPktGenLastTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sledPktGenLastTrigger.setStatus("current")
_SledMibNotificationsObjects_ObjectIdentity = ObjectIdentity
sledMibNotificationsObjects = _SledMibNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 2)
)
_SledMibConformance_ObjectIdentity = ObjectIdentity
sledMibConformance = _SledMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 3)
)
_SledMibCompliances_ObjectIdentity = ObjectIdentity
sledMibCompliances = _SledMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 3, 1)
)
_SledMibGroups_ObjectIdentity = ObjectIdentity
sledMibGroups = _SledMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 3, 2)
)

# Managed Objects groups

sledMibBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 3, 2, 1)
)
sledMibBaseGroup.setObjects(
      *(("SLED-MIB", "sledGlobalEnable"),
        ("SLED-MIB", "sledLoopbackInterface"),
        ("SLED-MIB", "sledLoopbackEnable"),
        ("SLED-MIB", "sledLoopbackPktHdr"),
        ("SLED-MIB", "sledPktGenInterface"),
        ("SLED-MIB", "sledPktGenPayload"),
        ("SLED-MIB", "sledPktGenRate"),
        ("SLED-MIB", "sledPktGenNumPkts"),
        ("SLED-MIB", "sledPktGenTrigger"),
        ("SLED-MIB", "sledPktGenLastTrigger"))
)
if mibBuilder.loadTexts:
    sledMibBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sledMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sledMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLED-MIB",
    **{"sledMib": sledMib,
       "sledNotifications": sledNotifications,
       "sledMibObjects": sledMibObjects,
       "sledGlobal": sledGlobal,
       "sledGlobalEnable": sledGlobalEnable,
       "sledLoopback": sledLoopback,
       "sledLoopbackInterface": sledLoopbackInterface,
       "sledLoopbackEnable": sledLoopbackEnable,
       "sledLoopbackPktHdr": sledLoopbackPktHdr,
       "sledPktGen": sledPktGen,
       "sledPktGenInterface": sledPktGenInterface,
       "sledPktGenPayload": sledPktGenPayload,
       "sledPktGenRate": sledPktGenRate,
       "sledPktGenNumPkts": sledPktGenNumPkts,
       "sledPktGenTrigger": sledPktGenTrigger,
       "sledPktGenLastTrigger": sledPktGenLastTrigger,
       "sledMibNotificationsObjects": sledMibNotificationsObjects,
       "sledMibConformance": sledMibConformance,
       "sledMibCompliances": sledMibCompliances,
       "sledMibCompliance": sledMibCompliance,
       "sledMibGroups": sledMibGroups,
       "sledMibBaseGroup": sledMibBaseGroup}
)
