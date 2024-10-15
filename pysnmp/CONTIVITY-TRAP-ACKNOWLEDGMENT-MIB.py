# SNMP MIB module (CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:00 2024
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

(snmpAgentInfo_Utilities_ces,) = mibBuilder.importSymbols(
    "CONTIVITY-INFO-V1-MIB",
    "snmpAgentInfo-Utilities-ces")

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

snmpAgentInfo_Utilities_TrapAck_ces = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrapAck_RevInfo_ces_ObjectIdentity = ObjectIdentity
trapAck_RevInfo_ces = _TrapAck_RevInfo_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 1)
)
_TrapAck_RevDate_ces_Type = DisplayString
_TrapAck_RevDate_ces_Object = MibScalar
trapAck_RevDate_ces = _TrapAck_RevDate_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 1, 1),
    _TrapAck_RevDate_ces_Type()
)
trapAck_RevDate_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAck_RevDate_ces.setStatus("mandatory")
_TrapAck_Rev_ces_Type = Integer32
_TrapAck_Rev_ces_Object = MibScalar
trapAck_Rev_ces = _TrapAck_Rev_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 1, 2),
    _TrapAck_Rev_ces_Type()
)
trapAck_Rev_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAck_Rev_ces.setStatus("mandatory")
_TrapAck_ServerRev_ces_Type = DisplayString
_TrapAck_ServerRev_ces_Object = MibScalar
trapAck_ServerRev_ces = _TrapAck_ServerRev_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 1, 3),
    _TrapAck_ServerRev_ces_Type()
)
trapAck_ServerRev_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAck_ServerRev_ces.setStatus("mandatory")
_TrapSeverity_ces_Type = Integer32
_TrapSeverity_ces_Object = MibScalar
trapSeverity_ces = _TrapSeverity_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 2),
    _TrapSeverity_ces_Type()
)
trapSeverity_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSeverity_ces.setStatus("mandatory")
_TrapDescription_ces_Type = Integer32
_TrapDescription_ces_Object = MibScalar
trapDescription_ces = _TrapDescription_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 3),
    _TrapDescription_ces_Type()
)
trapDescription_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDescription_ces.setStatus("mandatory")
_TrapSysUpTime_ces_Type = Integer32
_TrapSysUpTime_ces_Object = MibScalar
trapSysUpTime_ces = _TrapSysUpTime_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 4),
    _TrapSysUpTime_ces_Type()
)
trapSysUpTime_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSysUpTime_ces.setStatus("mandatory")
_TrapOID_ces_Type = ObjectIdentifier
_TrapOID_ces_Object = MibScalar
trapOID_ces = _TrapOID_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 5),
    _TrapOID_ces_Type()
)
trapOID_ces.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapOID_ces.setStatus("mandatory")
_TrapAckTable_ces_Object = MibTable
trapAckTable_ces = _TrapAckTable_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 6)
)
if mibBuilder.loadTexts:
    trapAckTable_ces.setStatus("mandatory")
_TrapAckEntry_ces_Object = MibTableRow
trapAckEntry_ces = _TrapAckEntry_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 6, 1)
)
trapAckEntry_ces.setIndexNames(
    (0, "CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB", "trapSeverity-ces"),
    (0, "CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB", "trapDescription-ces"),
    (0, "CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB", "trapSysUpTime-ces"),
    (0, "CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB", "trapOID-ces"),
)
if mibBuilder.loadTexts:
    trapAckEntry_ces.setStatus("mandatory")
_TrapAcknowledgement_ces_Type = Integer32
_TrapAcknowledgement_ces_Object = MibScalar
trapAcknowledgement_ces = _TrapAcknowledgement_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 15, 1, 2, 6, 1, 1),
    _TrapAcknowledgement_ces_Type()
)
trapAcknowledgement_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAcknowledgement_ces.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB",
    **{"snmpAgentInfo-Utilities-TrapAck-ces": snmpAgentInfo_Utilities_TrapAck_ces,
       "trapAck-RevInfo-ces": trapAck_RevInfo_ces,
       "trapAck-RevDate-ces": trapAck_RevDate_ces,
       "trapAck-Rev-ces": trapAck_Rev_ces,
       "trapAck-ServerRev-ces": trapAck_ServerRev_ces,
       "trapSeverity-ces": trapSeverity_ces,
       "trapDescription-ces": trapDescription_ces,
       "trapSysUpTime-ces": trapSysUpTime_ces,
       "trapOID-ces": trapOID_ces,
       "trapAckTable-ces": trapAckTable_ces,
       "trapAckEntry-ces": trapAckEntry_ces,
       "trapAcknowledgement-ces": trapAcknowledgement_ces}
)
