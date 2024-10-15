# SNMP MIB module (HIRSCHMANN-SNMP-RETURN-SET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-SNMP-RETURN-SET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:47 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(AutonomousType,
 DisplayString,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

hmMgmtSEReturnSetGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1)
)
hmMgmtSEReturnSetGroup.setRevisions(
        ("2010-09-14 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_HmMgmtSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hmMgmtSNMPExtensionGroup = _HmMgmtSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1)
)
_HmMgmtSESReturns_ObjectIdentity = ObjectIdentity
hmMgmtSESReturns = _HmMgmtSESReturns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hmMgmtSESReturns.setStatus("current")
_HmMgmtSESOkReturn_ObjectIdentity = ObjectIdentity
hmMgmtSESOkReturn = _HmMgmtSESOkReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hmMgmtSESOkReturn.setStatus("current")
_HmMgmtSESPendingReturn_ObjectIdentity = ObjectIdentity
hmMgmtSESPendingReturn = _HmMgmtSESPendingReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hmMgmtSESPendingReturn.setStatus("current")
_HmMgmtSESFailureReturn_ObjectIdentity = ObjectIdentity
hmMgmtSESFailureReturn = _HmMgmtSESFailureReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hmMgmtSESFailureReturn.setStatus("current")
_HmMgmtSESTestReturn_ObjectIdentity = ObjectIdentity
hmMgmtSESTestReturn = _HmMgmtSESTestReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 1, 100)
)
if mibBuilder.loadTexts:
    hmMgmtSESTestReturn.setStatus("current")
_HmMgmtSESpinLock_Type = TestAndIncr
_HmMgmtSESpinLock_Object = MibScalar
hmMgmtSESpinLock = _HmMgmtSESpinLock_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 2),
    _HmMgmtSESpinLock_Type()
)
hmMgmtSESpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtSESpinLock.setStatus("current")
_HmMgmtSEReturnTable_Object = MibTable
hmMgmtSEReturnTable = _HmMgmtSEReturnTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hmMgmtSEReturnTable.setStatus("current")
_HmMgmtSEReturnEntry_Object = MibTableRow
hmMgmtSEReturnEntry = _HmMgmtSEReturnEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 3, 1)
)
hmMgmtSEReturnEntry.setIndexNames(
    (0, "HIRSCHMANN-SNMP-RETURN-SET-MIB", "hmMgmtSeReturnKey"),
)
if mibBuilder.loadTexts:
    hmMgmtSEReturnEntry.setStatus("current")


class _HmMgmtSeReturnKey_Type(Integer32):
    """Custom type hmMgmtSeReturnKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmMgmtSeReturnKey_Type.__name__ = "Integer32"
_HmMgmtSeReturnKey_Object = MibTableColumn
hmMgmtSeReturnKey = _HmMgmtSeReturnKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 3, 1, 1),
    _HmMgmtSeReturnKey_Type()
)
hmMgmtSeReturnKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmMgmtSeReturnKey.setStatus("current")
_HmMgmtSeReturnCode_Type = AutonomousType
_HmMgmtSeReturnCode_Object = MibTableColumn
hmMgmtSeReturnCode = _HmMgmtSeReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 3, 1, 2),
    _HmMgmtSeReturnCode_Type()
)
hmMgmtSeReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtSeReturnCode.setStatus("current")
_HmMgmtSEParameterTable_Object = MibTable
hmMgmtSEParameterTable = _HmMgmtSEParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hmMgmtSEParameterTable.setStatus("current")
_HmMgmtSEParameterEntry_Object = MibTableRow
hmMgmtSEParameterEntry = _HmMgmtSEParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 4, 1)
)
hmMgmtSEParameterEntry.setIndexNames(
    (0, "HIRSCHMANN-SNMP-RETURN-SET-MIB", "hmMgmtSeReturnKey"),
    (0, "HIRSCHMANN-SNMP-RETURN-SET-MIB", "hmMgmtSEParameterID"),
)
if mibBuilder.loadTexts:
    hmMgmtSEParameterEntry.setStatus("current")
_HmMgmtSEParameterID_Type = Integer32
_HmMgmtSEParameterID_Object = MibTableColumn
hmMgmtSEParameterID = _HmMgmtSEParameterID_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 4, 1, 1),
    _HmMgmtSEParameterID_Type()
)
hmMgmtSEParameterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmMgmtSEParameterID.setStatus("current")
_HmMgmtSEParameterValue_Type = DisplayString
_HmMgmtSEParameterValue_Object = MibTableColumn
hmMgmtSEParameterValue = _HmMgmtSEParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 4, 1, 2),
    _HmMgmtSEParameterValue_Type()
)
hmMgmtSEParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtSEParameterValue.setStatus("current")
_HmMgmtSETestGroup_ObjectIdentity = ObjectIdentity
hmMgmtSETestGroup = _HmMgmtSETestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 100)
)
_HmMgmtSETestVar_Type = OctetString
_HmMgmtSETestVar_Object = MibScalar
hmMgmtSETestVar = _HmMgmtSETestVar_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 1, 1, 100, 1),
    _HmMgmtSETestVar_Type()
)
hmMgmtSETestVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtSETestVar.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-SNMP-RETURN-SET-MIB",
    **{"hirschmann": hirschmann,
       "hmMgmtSNMPExtensionGroup": hmMgmtSNMPExtensionGroup,
       "hmMgmtSEReturnSetGroup": hmMgmtSEReturnSetGroup,
       "hmMgmtSESReturns": hmMgmtSESReturns,
       "hmMgmtSESOkReturn": hmMgmtSESOkReturn,
       "hmMgmtSESPendingReturn": hmMgmtSESPendingReturn,
       "hmMgmtSESFailureReturn": hmMgmtSESFailureReturn,
       "hmMgmtSESTestReturn": hmMgmtSESTestReturn,
       "hmMgmtSESpinLock": hmMgmtSESpinLock,
       "hmMgmtSEReturnTable": hmMgmtSEReturnTable,
       "hmMgmtSEReturnEntry": hmMgmtSEReturnEntry,
       "hmMgmtSeReturnKey": hmMgmtSeReturnKey,
       "hmMgmtSeReturnCode": hmMgmtSeReturnCode,
       "hmMgmtSEParameterTable": hmMgmtSEParameterTable,
       "hmMgmtSEParameterEntry": hmMgmtSEParameterEntry,
       "hmMgmtSEParameterID": hmMgmtSEParameterID,
       "hmMgmtSEParameterValue": hmMgmtSEParameterValue,
       "hmMgmtSETestGroup": hmMgmtSETestGroup,
       "hmMgmtSETestVar": hmMgmtSETestVar}
)
