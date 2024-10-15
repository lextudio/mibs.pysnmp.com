# SNMP MIB module (CONTIVITY-INFO-V1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CONTIVITY-INFO-V1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:59 2024
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

(contivity,) = mibBuilder.importSymbols(
    "NEWOAK-MIB",
    "contivity")

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

snmpAgentInfo_ces = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15)
)
snmpAgentInfo_ces.setRevisions(
        ("1900-08-07 22:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpAgentInfo_Utilities_ces_ObjectIdentity = ObjectIdentity
snmpAgentInfo_Utilities_ces = _SnmpAgentInfo_Utilities_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1)
)
_SnmpAgentInfo_Utilities_Ping_ces_ObjectIdentity = ObjectIdentity
snmpAgentInfo_Utilities_Ping_ces = _SnmpAgentInfo_Utilities_Ping_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1)
)
_SnmpAgentInfo_Utilities_RevDate_ces_Type = DisplayString
_SnmpAgentInfo_Utilities_RevDate_ces_Object = MibScalar
snmpAgentInfo_Utilities_RevDate_ces = _SnmpAgentInfo_Utilities_RevDate_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 1),
    _SnmpAgentInfo_Utilities_RevDate_ces_Type()
)
snmpAgentInfo_Utilities_RevDate_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentInfo_Utilities_RevDate_ces.setStatus("mandatory")
_SnmpAgentInfo_Utilities_Rev_ces_Type = Integer32
_SnmpAgentInfo_Utilities_Rev_ces_Object = MibScalar
snmpAgentInfo_Utilities_Rev_ces = _SnmpAgentInfo_Utilities_Rev_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 2),
    _SnmpAgentInfo_Utilities_Rev_ces_Type()
)
snmpAgentInfo_Utilities_Rev_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentInfo_Utilities_Rev_ces.setStatus("mandatory")
_SnmpAgentInfo_Utilities_ServerRev_ces_Type = DisplayString
_SnmpAgentInfo_Utilities_ServerRev_ces_Object = MibScalar
snmpAgentInfo_Utilities_ServerRev_ces = _SnmpAgentInfo_Utilities_ServerRev_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 3),
    _SnmpAgentInfo_Utilities_ServerRev_ces_Type()
)
snmpAgentInfo_Utilities_ServerRev_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentInfo_Utilities_ServerRev_ces.setStatus("mandatory")
_PingAddress_ces_Type = IpAddress
_PingAddress_ces_Object = MibScalar
pingAddress_ces = _PingAddress_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 4),
    _PingAddress_ces_Type()
)
pingAddress_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingAddress_ces.setStatus("mandatory")


class _PingRepetitions_ces_Type(Integer32):
    """Custom type pingRepetitions_ces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PingRepetitions_ces_Type.__name__ = "Integer32"
_PingRepetitions_ces_Object = MibScalar
pingRepetitions_ces = _PingRepetitions_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 5),
    _PingRepetitions_ces_Type()
)
pingRepetitions_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingRepetitions_ces.setStatus("mandatory")


class _PingPacketSize_ces_Type(Integer32):
    """Custom type pingPacketSize_ces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4076),
    )


_PingPacketSize_ces_Type.__name__ = "Integer32"
_PingPacketSize_ces_Object = MibScalar
pingPacketSize_ces = _PingPacketSize_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 6),
    _PingPacketSize_ces_Type()
)
pingPacketSize_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingPacketSize_ces.setStatus("mandatory")
_PingSrcAddress_ces_Type = IpAddress
_PingSrcAddress_ces_Object = MibScalar
pingSrcAddress_ces = _PingSrcAddress_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 7),
    _PingSrcAddress_ces_Type()
)
pingSrcAddress_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingSrcAddress_ces.setStatus("mandatory")
_PingTable_ces_Object = MibTable
pingTable_ces = _PingTable_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 8)
)
if mibBuilder.loadTexts:
    pingTable_ces.setStatus("mandatory")
_PingEntry_ces_Object = MibTableRow
pingEntry_ces = _PingEntry_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 8, 1)
)
pingEntry_ces.setIndexNames(
    (0, "CONTIVITY-INFO-V1-MIB", "pingAddress-ces"),
    (0, "CONTIVITY-INFO-V1-MIB", "pingRepetitions-ces"),
    (0, "CONTIVITY-INFO-V1-MIB", "pingPacketSize-ces"),
    (0, "CONTIVITY-INFO-V1-MIB", "pingSrcAddress-ces"),
)
if mibBuilder.loadTexts:
    pingEntry_ces.setStatus("mandatory")
_PingAverageTime_ces_Type = Integer32
_PingAverageTime_ces_Object = MibScalar
pingAverageTime_ces = _PingAverageTime_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 8, 1, 1),
    _PingAverageTime_ces_Type()
)
pingAverageTime_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingAverageTime_ces.setStatus("mandatory")
_PingPercentLoss_ces_Type = Integer32
_PingPercentLoss_ces_Object = MibScalar
pingPercentLoss_ces = _PingPercentLoss_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 1, 8, 1, 2),
    _PingPercentLoss_ces_Type()
)
pingPercentLoss_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingPercentLoss_ces.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTIVITY-INFO-V1-MIB",
    **{"snmpAgentInfo-ces": snmpAgentInfo_ces,
       "snmpAgentInfo-Utilities-ces": snmpAgentInfo_Utilities_ces,
       "snmpAgentInfo-Utilities-Ping-ces": snmpAgentInfo_Utilities_Ping_ces,
       "snmpAgentInfo-Utilities-RevDate-ces": snmpAgentInfo_Utilities_RevDate_ces,
       "snmpAgentInfo-Utilities-Rev-ces": snmpAgentInfo_Utilities_Rev_ces,
       "snmpAgentInfo-Utilities-ServerRev-ces": snmpAgentInfo_Utilities_ServerRev_ces,
       "pingAddress-ces": pingAddress_ces,
       "pingRepetitions-ces": pingRepetitions_ces,
       "pingPacketSize-ces": pingPacketSize_ces,
       "pingSrcAddress-ces": pingSrcAddress_ces,
       "pingTable-ces": pingTable_ces,
       "pingEntry-ces": pingEntry_ces,
       "pingAverageTime-ces": pingAverageTime_ces,
       "pingPercentLoss-ces": pingPercentLoss_ces}
)
