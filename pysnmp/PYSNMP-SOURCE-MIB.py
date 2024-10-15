# SNMP MIB module (PYSNMP-SOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PYSNMP-SOURCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:25 2024
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

(pysnmpModuleIDs,) = mibBuilder.importSymbols(
    "PYSNMP-MIB",
    "pysnmpModuleIDs")

(snmpTargetAddrEntry,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

pysnmpSourceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8)
)
pysnmpSourceMIB.setRevisions(
        ("2017-04-14 00:00",
         "2015-01-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PysnmpSourceMIBObjects_ObjectIdentity = ObjectIdentity
pysnmpSourceMIBObjects = _PysnmpSourceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1)
)
_SnmpSourceAddrTable_Object = MibTable
snmpSourceAddrTable = _SnmpSourceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    snmpSourceAddrTable.setStatus("current")
_SnmpSourceAddrEntry_Object = MibTableRow
snmpSourceAddrEntry = _SnmpSourceAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snmpSourceAddrEntry.setStatus("current")
_SnmpSourceAddrTAddress_Type = TAddress
_SnmpSourceAddrTAddress_Object = MibTableColumn
snmpSourceAddrTAddress = _SnmpSourceAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1, 1, 1),
    _SnmpSourceAddrTAddress_Type()
)
snmpSourceAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSourceAddrTAddress.setStatus("current")
_PysnmpSourceMIBConformance_ObjectIdentity = ObjectIdentity
pysnmpSourceMIBConformance = _PysnmpSourceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2)
)
_PysnmpSourceMIBCompliances_ObjectIdentity = ObjectIdentity
pysnmpSourceMIBCompliances = _PysnmpSourceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2, 1)
)
_PysnmpSourceMIBGroups_ObjectIdentity = ObjectIdentity
pysnmpSourceMIBGroups = _PysnmpSourceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2, 2)
)
snmpTargetAddrEntry.registerAugmentions(
    ("PYSNMP-SOURCE-MIB",
     "snmpSourceAddrEntry")
)
snmpSourceAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PYSNMP-SOURCE-MIB",
    **{"pysnmpSourceMIB": pysnmpSourceMIB,
       "pysnmpSourceMIBObjects": pysnmpSourceMIBObjects,
       "snmpSourceAddrTable": snmpSourceAddrTable,
       "snmpSourceAddrEntry": snmpSourceAddrEntry,
       "snmpSourceAddrTAddress": snmpSourceAddrTAddress,
       "pysnmpSourceMIBConformance": pysnmpSourceMIBConformance,
       "pysnmpSourceMIBCompliances": pysnmpSourceMIBCompliances,
       "pysnmpSourceMIBGroups": pysnmpSourceMIBGroups}
)
