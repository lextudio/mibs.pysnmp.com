# SNMP MIB module (AISLCALIAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISLCALIAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:19 2024
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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSLCAlias = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLCAliasTable_Object = MibTable
aiSLCAliasTable = _AiSLCAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1)
)
if mibBuilder.loadTexts:
    aiSLCAliasTable.setStatus("current")
_AiSLCAliasEntry_Object = MibTableRow
aiSLCAliasEntry = _AiSLCAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1)
)
aiSLCAliasEntry.setIndexNames(
    (1, "AISLCALIAS-MIB", "aislcaliAliasName"),
)
if mibBuilder.loadTexts:
    aiSLCAliasEntry.setStatus("current")
_AislcaliAliasName_Type = DisplayString
_AislcaliAliasName_Object = MibTableColumn
aislcaliAliasName = _AislcaliAliasName_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 1),
    _AislcaliAliasName_Type()
)
aislcaliAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcaliAliasName.setStatus("current")


class _AislcaliRowStatus_Type(RowStatus):
    """Custom type aislcaliRowStatus based on RowStatus"""


_AislcaliRowStatus_Object = MibTableColumn
aislcaliRowStatus = _AislcaliRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 2),
    _AislcaliRowStatus_Type()
)
aislcaliRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliRowStatus.setStatus("current")


class _AislcaliDescription_Type(DisplayString):
    """Custom type aislcaliDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcaliDescription_Type.__name__ = "DisplayString"
_AislcaliDescription_Object = MibTableColumn
aislcaliDescription = _AislcaliDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 3),
    _AislcaliDescription_Type()
)
aislcaliDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliDescription.setStatus("current")
_AislcaliDestination_Type = DisplayString
_AislcaliDestination_Object = MibTableColumn
aislcaliDestination = _AislcaliDestination_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 4),
    _AislcaliDestination_Type()
)
aislcaliDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliDestination.setStatus("current")
_AislcaliShowInDestMenu_Type = TruthValue
_AislcaliShowInDestMenu_Object = MibTableColumn
aislcaliShowInDestMenu = _AislcaliShowInDestMenu_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 5),
    _AislcaliShowInDestMenu_Type()
)
aislcaliShowInDestMenu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliShowInDestMenu.setStatus("current")
_AislcaliCallingAddr_Type = DisplayString
_AislcaliCallingAddr_Object = MibTableColumn
aislcaliCallingAddr = _AislcaliCallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 6),
    _AislcaliCallingAddr_Type()
)
aislcaliCallingAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliCallingAddr.setStatus("current")
_AislcaliCalledAddr_Type = DisplayString
_AislcaliCalledAddr_Object = MibTableColumn
aislcaliCalledAddr = _AislcaliCalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 7),
    _AislcaliCalledAddr_Type()
)
aislcaliCalledAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliCalledAddr.setStatus("current")
_AislcaliCallData_Type = DisplayString
_AislcaliCallData_Object = MibTableColumn
aislcaliCallData = _AislcaliCallData_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 8),
    _AislcaliCallData_Type()
)
aislcaliCallData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliCallData.setStatus("current")
_AislcaliCallingProto_Type = DisplayString
_AislcaliCallingProto_Object = MibTableColumn
aislcaliCallingProto = _AislcaliCallingProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 9),
    _AislcaliCallingProto_Type()
)
aislcaliCallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliCallingProto.setStatus("current")
_AislcaliCalledProto_Type = DisplayString
_AislcaliCalledProto_Object = MibTableColumn
aislcaliCalledProto = _AislcaliCalledProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 10),
    _AislcaliCalledProto_Type()
)
aislcaliCalledProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliCalledProto.setStatus("current")
_AislcaliAppString_Type = DisplayString
_AislcaliAppString_Object = MibTableColumn
aislcaliAppString = _AislcaliAppString_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 11),
    _AislcaliAppString_Type()
)
aislcaliAppString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliAppString.setStatus("current")
_AislcaliAltRoute_Type = DisplayString
_AislcaliAltRoute_Object = MibTableColumn
aislcaliAltRoute = _AislcaliAltRoute_Object(
    (1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 12),
    _AislcaliAltRoute_Type()
)
aislcaliAltRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aislcaliAltRoute.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISLCALIAS-MIB",
    **{"aii": aii,
       "aiSLCAlias": aiSLCAlias,
       "aiSLCAliasTable": aiSLCAliasTable,
       "aiSLCAliasEntry": aiSLCAliasEntry,
       "aislcaliAliasName": aislcaliAliasName,
       "aislcaliRowStatus": aislcaliRowStatus,
       "aislcaliDescription": aislcaliDescription,
       "aislcaliDestination": aislcaliDestination,
       "aislcaliShowInDestMenu": aislcaliShowInDestMenu,
       "aislcaliCallingAddr": aislcaliCallingAddr,
       "aislcaliCalledAddr": aislcaliCalledAddr,
       "aislcaliCallData": aislcaliCallData,
       "aislcaliCallingProto": aislcaliCallingProto,
       "aislcaliCalledProto": aislcaliCalledProto,
       "aislcaliAppString": aislcaliAppString,
       "aislcaliAltRoute": aislcaliAltRoute}
)
