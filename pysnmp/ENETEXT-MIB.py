# SNMP MIB module (ENETEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENETEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:33 2024
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

(enetExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "enetExt")

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

apEnetExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApEnetPhyTable_Object = MibTable
apEnetPhyTable = _ApEnetPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39, 2)
)
if mibBuilder.loadTexts:
    apEnetPhyTable.setStatus("current")
_ApEnetPhyEntry_Object = MibTableRow
apEnetPhyEntry = _ApEnetPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39, 2, 1)
)
apEnetPhyEntry.setIndexNames(
    (0, "ENETEXT-MIB", "apEnetPhyIfIndex"),
)
if mibBuilder.loadTexts:
    apEnetPhyEntry.setStatus("current")
_ApEnetPhyIfIndex_Type = Integer32
_ApEnetPhyIfIndex_Object = MibTableColumn
apEnetPhyIfIndex = _ApEnetPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39, 2, 1, 1),
    _ApEnetPhyIfIndex_Type()
)
apEnetPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnetPhyIfIndex.setStatus("current")


class _ApEnetPhyConfig_Type(Integer32):
    """Custom type apEnetPhyConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("auto-negotiate", 4),
          ("disabled", 5),
          ("giga-full-duplex-asym-pause", 8),
          ("giga-full-duplex-loopback", 11),
          ("giga-full-duplex-no-pause", 7),
          ("giga-full-duplex-sym-asym-pause", 10),
          ("giga-full-duplex-sym-pause", 9),
          ("hundred-full-duplex", 3),
          ("hundred-full-duplex-loopback", 6),
          ("hundred-half-duplex", 2),
          ("ten-full-duplex", 1),
          ("ten-half-duplex", 0))
    )


_ApEnetPhyConfig_Type.__name__ = "Integer32"
_ApEnetPhyConfig_Object = MibTableColumn
apEnetPhyConfig = _ApEnetPhyConfig_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39, 2, 1, 2),
    _ApEnetPhyConfig_Type()
)
apEnetPhyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEnetPhyConfig.setStatus("current")


class _ApEnetPhyConfigActual_Type(Integer32):
    """Custom type apEnetPhyConfigActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("giga-full-duplex-asym-pause", 5),
          ("giga-full-duplex-no-pause", 4),
          ("giga-full-duplex-sym-asym-pause", 7),
          ("giga-full-duplex-sym-pause", 6),
          ("hundred-full-duplex", 3),
          ("hundred-half-duplex", 2),
          ("ten-full-duplex", 1),
          ("ten-half-duplex", 0))
    )


_ApEnetPhyConfigActual_Type.__name__ = "Integer32"
_ApEnetPhyConfigActual_Object = MibTableColumn
apEnetPhyConfigActual = _ApEnetPhyConfigActual_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39, 2, 1, 3),
    _ApEnetPhyConfigActual_Type()
)
apEnetPhyConfigActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnetPhyConfigActual.setStatus("current")


class _ApEnetDescr_Type(DisplayString):
    """Custom type apEnetDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApEnetDescr_Type.__name__ = "DisplayString"
_ApEnetDescr_Object = MibTableColumn
apEnetDescr = _ApEnetDescr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39, 2, 1, 4),
    _ApEnetDescr_Type()
)
apEnetDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEnetDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENETEXT-MIB",
    **{"apEnetExtMib": apEnetExtMib,
       "apEnetPhyTable": apEnetPhyTable,
       "apEnetPhyEntry": apEnetPhyEntry,
       "apEnetPhyIfIndex": apEnetPhyIfIndex,
       "apEnetPhyConfig": apEnetPhyConfig,
       "apEnetPhyConfigActual": apEnetPhyConfigActual,
       "apEnetDescr": apEnetDescr}
)
