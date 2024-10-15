# SNMP MIB module (EXTREME-VC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeVC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeVCLinkTable_Object = MibTable
extremeVCLinkTable = _ExtremeVCLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1)
)
if mibBuilder.loadTexts:
    extremeVCLinkTable.setStatus("deprecated")
_ExtremeVCLinkEntry_Object = MibTableRow
extremeVCLinkEntry = _ExtremeVCLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1)
)
extremeVCLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeVCLinkEntry.setStatus("deprecated")
_ExtremeVCLinkValid_Type = TruthValue
_ExtremeVCLinkValid_Object = MibTableColumn
extremeVCLinkValid = _ExtremeVCLinkValid_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 1),
    _ExtremeVCLinkValid_Type()
)
extremeVCLinkValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkValid.setStatus("deprecated")
_ExtremeVCLinkDeviceId_Type = Integer32
_ExtremeVCLinkDeviceId_Object = MibTableColumn
extremeVCLinkDeviceId = _ExtremeVCLinkDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 2),
    _ExtremeVCLinkDeviceId_Type()
)
extremeVCLinkDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkDeviceId.setStatus("deprecated")
_ExtremeVCLinkPortIndex_Type = Integer32
_ExtremeVCLinkPortIndex_Object = MibTableColumn
extremeVCLinkPortIndex = _ExtremeVCLinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 3),
    _ExtremeVCLinkPortIndex_Type()
)
extremeVCLinkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkPortIndex.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-VC-MIB",
    **{"extremeVC": extremeVC,
       "extremeVCLinkTable": extremeVCLinkTable,
       "extremeVCLinkEntry": extremeVCLinkEntry,
       "extremeVCLinkValid": extremeVCLinkValid,
       "extremeVCLinkDeviceId": extremeVCLinkDeviceId,
       "extremeVCLinkPortIndex": extremeVCLinkPortIndex}
)
