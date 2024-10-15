# SNMP MIB module (BSUSUBASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUSUBASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:47 2024
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

(aniBsuSuGroup,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "aniBsuSuGroup")

(aniBsuSuMacAddr,) = mibBuilder.importSymbols(
    "BSUSUINV-MIB",
    "aniBsuSuMacAddr")

(aniBsuWirelessPort,) = mibBuilder.importSymbols(
    "BSUWIRELESSIF-MIB",
    "aniBsuWirelessPort")

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

aniBsuSuBase = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuSuBaseTable_Object = MibTable
aniBsuSuBaseTable = _AniBsuSuBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    aniBsuSuBaseTable.setStatus("current")
_AniBsuSuBaseEntry_Object = MibTableRow
aniBsuSuBaseEntry = _AniBsuSuBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1)
)
aniBsuSuBaseEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUSUINV-MIB", "aniBsuSuMacAddr"),
)
if mibBuilder.loadTexts:
    aniBsuSuBaseEntry.setStatus("current")


class _AniBsuSuNetworkAccess_Type(Integer32):
    """Custom type aniBsuSuNetworkAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AniBsuSuNetworkAccess_Type.__name__ = "Integer32"
_AniBsuSuNetworkAccess_Object = MibTableColumn
aniBsuSuNetworkAccess = _AniBsuSuNetworkAccess_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 2),
    _AniBsuSuNetworkAccess_Type()
)
aniBsuSuNetworkAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuNetworkAccess.setStatus("current")


class _AniBsuSuMaxHostSupport_Type(Integer32):
    """Custom type aniBsuSuMaxHostSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AniBsuSuMaxHostSupport_Type.__name__ = "Integer32"
_AniBsuSuMaxHostSupport_Object = MibTableColumn
aniBsuSuMaxHostSupport = _AniBsuSuMaxHostSupport_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 3),
    _AniBsuSuMaxHostSupport_Type()
)
aniBsuSuMaxHostSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuMaxHostSupport.setStatus("current")
_AniBsuSuTargetFreq_Type = DisplayString
_AniBsuSuTargetFreq_Object = MibTableColumn
aniBsuSuTargetFreq = _AniBsuSuTargetFreq_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 4),
    _AniBsuSuTargetFreq_Type()
)
aniBsuSuTargetFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuTargetFreq.setStatus("current")
_AniBsuSuFrequencyTable_Type = DisplayString
_AniBsuSuFrequencyTable_Object = MibTableColumn
aniBsuSuFrequencyTable = _AniBsuSuFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 5),
    _AniBsuSuFrequencyTable_Type()
)
aniBsuSuFrequencyTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuFrequencyTable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUSUBASE-MIB",
    **{"aniBsuSuBase": aniBsuSuBase,
       "aniBsuSuBaseTable": aniBsuSuBaseTable,
       "aniBsuSuBaseEntry": aniBsuSuBaseEntry,
       "aniBsuSuNetworkAccess": aniBsuSuNetworkAccess,
       "aniBsuSuMaxHostSupport": aniBsuSuMaxHostSupport,
       "aniBsuSuTargetFreq": aniBsuSuTargetFreq,
       "aniBsuSuFrequencyTable": aniBsuSuFrequencyTable}
)
