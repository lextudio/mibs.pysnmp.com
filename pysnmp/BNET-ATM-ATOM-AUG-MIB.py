# SNMP MIB module (BNET-ATM-ATOM-AUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BNET-ATM-ATOM-AUG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:30 2024
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(atmSoftPVccLeafReference,) = mibBuilder.importSymbols(
    "ATM-SOFT-PVC-MIB",
    "atmSoftPVccLeafReference")

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(s5AtmTop,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5AtmTop")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BnetAtmAug_ObjectIdentity = ObjectIdentity
bnetAtmAug = _BnetAtmAug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3)
)
_BnetAtmDeviceAtmAddr_Type = AtmAddr
_BnetAtmDeviceAtmAddr_Object = MibScalar
bnetAtmDeviceAtmAddr = _BnetAtmDeviceAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 1),
    _BnetAtmDeviceAtmAddr_Type()
)
bnetAtmDeviceAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmDeviceAtmAddr.setStatus("mandatory")


class _BnetAtmLearnAddrs_Type(Integer32):
    """Custom type bnetAtmLearnAddrs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forgetAddrs", 3),
          ("learnAddrs", 2),
          ("other", 1))
    )


_BnetAtmLearnAddrs_Type.__name__ = "Integer32"
_BnetAtmLearnAddrs_Object = MibScalar
bnetAtmLearnAddrs = _BnetAtmLearnAddrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 2),
    _BnetAtmLearnAddrs_Type()
)
bnetAtmLearnAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnetAtmLearnAddrs.setStatus("mandatory")
_AtmfAddressClientTable_Object = MibTable
atmfAddressClientTable = _AtmfAddressClientTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 3)
)
if mibBuilder.loadTexts:
    atmfAddressClientTable.setStatus("mandatory")
_AtmfAddressClientEntry_Object = MibTableRow
atmfAddressClientEntry = _AtmfAddressClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 3, 1)
)
atmfAddressClientEntry.setIndexNames(
    (0, "BNET-ATM-ATOM-AUG-MIB", "atmfAddressPort"),
    (0, "BNET-ATM-ATOM-AUG-MIB", "atmfAddressAtmAddress"),
)
if mibBuilder.loadTexts:
    atmfAddressClientEntry.setStatus("mandatory")
_AtmfAddressPort_Type = Integer32
_AtmfAddressPort_Object = MibTableColumn
atmfAddressPort = _AtmfAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 3, 1, 1),
    _AtmfAddressPort_Type()
)
atmfAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressPort.setStatus("mandatory")
_AtmfAddressAtmAddress_Type = AtmAddr
_AtmfAddressAtmAddress_Object = MibTableColumn
atmfAddressAtmAddress = _AtmfAddressAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 3, 1, 2),
    _AtmfAddressAtmAddress_Type()
)
atmfAddressAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressAtmAddress.setStatus("mandatory")


class _AtmfAddressClientType_Type(Integer32):
    """Custom type atmfAddressClientType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bus", 8),
          ("cnCircuitSaver", 3),
          ("cnTurbo", 2),
          ("external", 6),
          ("laneCircuitSaver", 5),
          ("laneTurbo", 4),
          ("lecs", 10),
          ("les", 7),
          ("les-bus", 9),
          ("other", 1),
          ("spvc", 11))
    )


_AtmfAddressClientType_Type.__name__ = "Integer32"
_AtmfAddressClientType_Object = MibTableColumn
atmfAddressClientType = _AtmfAddressClientType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 3, 1, 3),
    _AtmfAddressClientType_Type()
)
atmfAddressClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressClientType.setStatus("mandatory")
_AtmfAddressClientCallCount_Type = Integer32
_AtmfAddressClientCallCount_Object = MibTableColumn
atmfAddressClientCallCount = _AtmfAddressClientCallCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 3, 1, 4),
    _AtmfAddressClientCallCount_Type()
)
atmfAddressClientCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressClientCallCount.setStatus("mandatory")
_BnetAtmSoftPVccExtnTable_Object = MibTable
bnetAtmSoftPVccExtnTable = _BnetAtmSoftPVccExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 4)
)
if mibBuilder.loadTexts:
    bnetAtmSoftPVccExtnTable.setStatus("mandatory")
_BnetAtmSoftPVccExtnEntry_Object = MibTableRow
bnetAtmSoftPVccExtnEntry = _BnetAtmSoftPVccExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 4, 1)
)
bnetAtmSoftPVccExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"),
)
if mibBuilder.loadTexts:
    bnetAtmSoftPVccExtnEntry.setStatus("mandatory")
_BnetAtmSoftPVccCircuitId_Type = Integer32
_BnetAtmSoftPVccCircuitId_Object = MibTableColumn
bnetAtmSoftPVccCircuitId = _BnetAtmSoftPVccCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 3, 4, 1, 1),
    _BnetAtmSoftPVccCircuitId_Type()
)
bnetAtmSoftPVccCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmSoftPVccCircuitId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BNET-ATM-ATOM-AUG-MIB",
    **{"bnetAtmAug": bnetAtmAug,
       "bnetAtmDeviceAtmAddr": bnetAtmDeviceAtmAddr,
       "bnetAtmLearnAddrs": bnetAtmLearnAddrs,
       "atmfAddressClientTable": atmfAddressClientTable,
       "atmfAddressClientEntry": atmfAddressClientEntry,
       "atmfAddressPort": atmfAddressPort,
       "atmfAddressAtmAddress": atmfAddressAtmAddress,
       "atmfAddressClientType": atmfAddressClientType,
       "atmfAddressClientCallCount": atmfAddressClientCallCount,
       "bnetAtmSoftPVccExtnTable": bnetAtmSoftPVccExtnTable,
       "bnetAtmSoftPVccExtnEntry": bnetAtmSoftPVccExtnEntry,
       "bnetAtmSoftPVccCircuitId": bnetAtmSoftPVccCircuitId}
)
