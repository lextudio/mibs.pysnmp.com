# SNMP MIB module (XYLAN-MGMTSTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-MGMTSTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:08 2024
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

(xylanTrapArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanTrapArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MgmtControl_ObjectIdentity = ObjectIdentity
mgmtControl = _MgmtControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1)
)
trapEntry.setIndexNames(
    (0, "XYLAN-MGMTSTN-MIB", "stationIndex"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")


class _StationIndex_Type(Integer32):
    """Custom type stationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_StationIndex_Type.__name__ = "Integer32"
_StationIndex_Object = MibTableColumn
stationIndex = _StationIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 1),
    _StationIndex_Type()
)
stationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationIndex.setStatus("mandatory")
_StationIP_Type = IpAddress
_StationIP_Object = MibTableColumn
stationIP = _StationIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 2),
    _StationIP_Type()
)
stationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationIP.setStatus("mandatory")


class _StationPort_Type(Integer32):
    """Custom type stationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StationPort_Type.__name__ = "Integer32"
_StationPort_Object = MibTableColumn
stationPort = _StationPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 3),
    _StationPort_Type()
)
stationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationPort.setStatus("mandatory")


class _StationCommunity_Type(DisplayString):
    """Custom type stationCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_StationCommunity_Type.__name__ = "DisplayString"
_StationCommunity_Object = MibTableColumn
stationCommunity = _StationCommunity_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 4),
    _StationCommunity_Type()
)
stationCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationCommunity.setStatus("mandatory")


class _StationTrapFlags_Type(OctetString):
    """Custom type stationTrapFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_StationTrapFlags_Type.__name__ = "OctetString"
_StationTrapFlags_Object = MibTableColumn
stationTrapFlags = _StationTrapFlags_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 5),
    _StationTrapFlags_Type()
)
stationTrapFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationTrapFlags.setStatus("mandatory")
_StationEnable_Type = Integer32
_StationEnable_Object = MibTableColumn
stationEnable = _StationEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 6),
    _StationEnable_Type()
)
stationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationEnable.setStatus("mandatory")
_StationSAPrivs_Type = Integer32
_StationSAPrivs_Object = MibTableColumn
stationSAPrivs = _StationSAPrivs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 7),
    _StationSAPrivs_Type()
)
stationSAPrivs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationSAPrivs.setStatus("mandatory")
_TrapBindings_ObjectIdentity = ObjectIdentity
trapBindings = _TrapBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 2)
)
_SystemEventTrapNumber_Type = Integer32
_SystemEventTrapNumber_Object = MibScalar
systemEventTrapNumber = _SystemEventTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 2, 1),
    _SystemEventTrapNumber_Type()
)
systemEventTrapNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemEventTrapNumber.setStatus("mandatory")


class _SystemEventTrapString_Type(DisplayString):
    """Custom type systemEventTrapString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SystemEventTrapString_Type.__name__ = "DisplayString"
_SystemEventTrapString_Object = MibScalar
systemEventTrapString = _SystemEventTrapString_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 5, 2, 2),
    _SystemEventTrapString_Type()
)
systemEventTrapString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemEventTrapString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-MGMTSTN-MIB",
    **{"mgmtControl": mgmtControl,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "stationIndex": stationIndex,
       "stationIP": stationIP,
       "stationPort": stationPort,
       "stationCommunity": stationCommunity,
       "stationTrapFlags": stationTrapFlags,
       "stationEnable": stationEnable,
       "stationSAPrivs": stationSAPrivs,
       "trapBindings": trapBindings,
       "systemEventTrapNumber": systemEventTrapNumber,
       "systemEventTrapString": systemEventTrapString}
)
