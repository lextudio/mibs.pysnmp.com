# SNMP MIB module (BEGEMOT-MIB2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEGEMOT-MIB2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:45 2024
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

(begemotIp,) = mibBuilder.importSymbols(
    "BEGEMOT-IP-MIB",
    "begemotIp")

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

begemotMib2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BegemotIfMaxspeed_Type = Counter64
_BegemotIfMaxspeed_Object = MibScalar
begemotIfMaxspeed = _BegemotIfMaxspeed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 1),
    _BegemotIfMaxspeed_Type()
)
begemotIfMaxspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotIfMaxspeed.setStatus("current")
if mibBuilder.loadTexts:
    begemotIfMaxspeed.setUnits("bps")
_BegemotIfPoll_Type = TimeTicks
_BegemotIfPoll_Object = MibScalar
begemotIfPoll = _BegemotIfPoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 2),
    _BegemotIfPoll_Type()
)
begemotIfPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotIfPoll.setStatus("current")
_BegemotIfForcePoll_Type = TimeTicks
_BegemotIfForcePoll_Object = MibScalar
begemotIfForcePoll = _BegemotIfForcePoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 3),
    _BegemotIfForcePoll_Type()
)
begemotIfForcePoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotIfForcePoll.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-MIB2-MIB",
    **{"begemotMib2": begemotMib2,
       "begemotIfMaxspeed": begemotIfMaxspeed,
       "begemotIfPoll": begemotIfPoll,
       "begemotIfForcePoll": begemotIfForcePoll}
)
