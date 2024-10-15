# SNMP MIB module (PDN-ATM-BRIDGE-IWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ATM-BRIDGE-IWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:15 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pdnAtmBridgeIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43)
)
pdnAtmBridgeIwfMIB.setRevisions(
        ("2003-04-24 00:00",
         "2003-03-24 00:00",
         "2003-03-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnAtmBridgeIwfNotifications_ObjectIdentity = ObjectIdentity
pdnAtmBridgeIwfNotifications = _PdnAtmBridgeIwfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 0)
)
_PdnAtmBridgeIwfObjects_ObjectIdentity = ObjectIdentity
pdnAtmBridgeIwfObjects = _PdnAtmBridgeIwfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1)
)
_PdnAtmBridgeIwfTable_Object = MibTable
pdnAtmBridgeIwfTable = _PdnAtmBridgeIwfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfTable.setStatus("current")
_PdnAtmBridgeIwfEntry_Object = MibTableRow
pdnAtmBridgeIwfEntry = _PdnAtmBridgeIwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1)
)
pdnAtmBridgeIwfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfVclVpi"),
    (0, "PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfVclVci"),
)
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfEntry.setStatus("current")


class _PdnAtmBridgeIwfVclVpi_Type(Unsigned32):
    """Custom type pdnAtmBridgeIwfVclVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PdnAtmBridgeIwfVclVpi_Type.__name__ = "Unsigned32"
_PdnAtmBridgeIwfVclVpi_Object = MibTableColumn
pdnAtmBridgeIwfVclVpi = _PdnAtmBridgeIwfVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 1),
    _PdnAtmBridgeIwfVclVpi_Type()
)
pdnAtmBridgeIwfVclVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfVclVpi.setStatus("current")


class _PdnAtmBridgeIwfVclVci_Type(Unsigned32):
    """Custom type pdnAtmBridgeIwfVclVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PdnAtmBridgeIwfVclVci_Type.__name__ = "Unsigned32"
_PdnAtmBridgeIwfVclVci_Object = MibTableColumn
pdnAtmBridgeIwfVclVci = _PdnAtmBridgeIwfVclVci_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 2),
    _PdnAtmBridgeIwfVclVci_Type()
)
pdnAtmBridgeIwfVclVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfVclVci.setStatus("current")
_PdnAtmBridgeIwfRowStatus_Type = RowStatus
_PdnAtmBridgeIwfRowStatus_Object = MibTableColumn
pdnAtmBridgeIwfRowStatus = _PdnAtmBridgeIwfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 3),
    _PdnAtmBridgeIwfRowStatus_Type()
)
pdnAtmBridgeIwfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfRowStatus.setStatus("current")


class _PdnAtmBridgeIwfDot1dBasePort_Type(Unsigned32):
    """Custom type pdnAtmBridgeIwfDot1dBasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnAtmBridgeIwfDot1dBasePort_Type.__name__ = "Unsigned32"
_PdnAtmBridgeIwfDot1dBasePort_Object = MibTableColumn
pdnAtmBridgeIwfDot1dBasePort = _PdnAtmBridgeIwfDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 4),
    _PdnAtmBridgeIwfDot1dBasePort_Type()
)
pdnAtmBridgeIwfDot1dBasePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfDot1dBasePort.setStatus("current")
_PdnAtmBridgeIwfConformance_ObjectIdentity = ObjectIdentity
pdnAtmBridgeIwfConformance = _PdnAtmBridgeIwfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2)
)
_PdnAtmBridgeIwfCompliances_ObjectIdentity = ObjectIdentity
pdnAtmBridgeIwfCompliances = _PdnAtmBridgeIwfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 1)
)
_PdnAtmBridgeIwfGroups_ObjectIdentity = ObjectIdentity
pdnAtmBridgeIwfGroups = _PdnAtmBridgeIwfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 2)
)

# Managed Objects groups

pdnAtmBridgeIwfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 2, 1)
)
pdnAtmBridgeIwfGroup.setObjects(
      *(("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfRowStatus"),
        ("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfDot1dBasePort"))
)
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnAtmBridgeIwfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAtmBridgeIwfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ATM-BRIDGE-IWF-MIB",
    **{"pdnAtmBridgeIwfMIB": pdnAtmBridgeIwfMIB,
       "pdnAtmBridgeIwfNotifications": pdnAtmBridgeIwfNotifications,
       "pdnAtmBridgeIwfObjects": pdnAtmBridgeIwfObjects,
       "pdnAtmBridgeIwfTable": pdnAtmBridgeIwfTable,
       "pdnAtmBridgeIwfEntry": pdnAtmBridgeIwfEntry,
       "pdnAtmBridgeIwfVclVpi": pdnAtmBridgeIwfVclVpi,
       "pdnAtmBridgeIwfVclVci": pdnAtmBridgeIwfVclVci,
       "pdnAtmBridgeIwfRowStatus": pdnAtmBridgeIwfRowStatus,
       "pdnAtmBridgeIwfDot1dBasePort": pdnAtmBridgeIwfDot1dBasePort,
       "pdnAtmBridgeIwfConformance": pdnAtmBridgeIwfConformance,
       "pdnAtmBridgeIwfCompliances": pdnAtmBridgeIwfCompliances,
       "pdnAtmBridgeIwfMIBCompliance": pdnAtmBridgeIwfMIBCompliance,
       "pdnAtmBridgeIwfGroups": pdnAtmBridgeIwfGroups,
       "pdnAtmBridgeIwfGroup": pdnAtmBridgeIwfGroup}
)
