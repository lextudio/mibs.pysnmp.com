# SNMP MIB module (IFEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IFEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:55 2024
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

(ifExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "ifExt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ifExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApIfTable_Object = MibTable
apIfTable = _ApIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2)
)
if mibBuilder.loadTexts:
    apIfTable.setStatus("current")
_ApIfEntry_Object = MibTableRow
apIfEntry = _ApIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2, 1)
)
apIfEntry.setIndexNames(
    (0, "IFEXT-MIB", "apIfIndex"),
)
if mibBuilder.loadTexts:
    apIfEntry.setStatus("current")
_ApIfIndex_Type = Integer32
_ApIfIndex_Object = MibTableColumn
apIfIndex = _ApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2, 1, 1),
    _ApIfIndex_Type()
)
apIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfIndex.setStatus("current")


class _ApIfType_Type(Integer32):
    """Custom type apIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              18,
              22,
              23,
              30,
              32,
              54,
              81,
              82,
              108,
              117,
              1005,
              1006)
        )
    )
    namedValues = NamedValues(
        *(("console", 22),
          ("ct", 54),
          ("ds0", 81),
          ("ds0b", 82),
          ("ds1", 18),
          ("ds3", 30),
          ("fe", 6),
          ("fr", 32),
          ("ge", 117),
          ("madlan", 1005),
          ("ppp", 23),
          ("pppmm", 108),
          ("sar", 1006))
    )


_ApIfType_Type.__name__ = "Integer32"
_ApIfType_Object = MibTableColumn
apIfType = _ApIfType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2, 1, 2),
    _ApIfType_Type()
)
apIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfType.setStatus("current")


class _ApIfCategory_Type(Integer32):
    """Custom type apIfCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-physical", 2),
          ("physical", 1))
    )


_ApIfCategory_Type.__name__ = "Integer32"
_ApIfCategory_Object = MibTableColumn
apIfCategory = _ApIfCategory_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2, 1, 3),
    _ApIfCategory_Type()
)
apIfCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfCategory.setStatus("current")
_ApIfSlot_Type = Integer32
_ApIfSlot_Object = MibTableColumn
apIfSlot = _ApIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2, 1, 4),
    _ApIfSlot_Type()
)
apIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfSlot.setStatus("current")
_ApIfPort_Type = Integer32
_ApIfPort_Object = MibTableColumn
apIfPort = _ApIfPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2, 1, 5),
    _ApIfPort_Type()
)
apIfPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfPort.setStatus("current")
_ApIfStatus_Type = RowStatus
_ApIfStatus_Object = MibTableColumn
apIfStatus = _ApIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 2, 1, 6),
    _ApIfStatus_Type()
)
apIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfStatus.setStatus("current")
_ApIfCctTable_Object = MibTable
apIfCctTable = _ApIfCctTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 3)
)
if mibBuilder.loadTexts:
    apIfCctTable.setStatus("current")
_ApIfCctEntry_Object = MibTableRow
apIfCctEntry = _ApIfCctEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 3, 1)
)
apIfCctEntry.setIndexNames(
    (0, "IFEXT-MIB", "apIfCctIfIndex"),
)
if mibBuilder.loadTexts:
    apIfCctEntry.setStatus("current")
_ApIfCctIfIndex_Type = Integer32
_ApIfCctIfIndex_Object = MibTableColumn
apIfCctIfIndex = _ApIfCctIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 3, 1, 1),
    _ApIfCctIfIndex_Type()
)
apIfCctIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfCctIfIndex.setStatus("current")
_ApIfCctStatus_Type = RowStatus
_ApIfCctStatus_Object = MibTableColumn
apIfCctStatus = _ApIfCctStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 3, 1, 2),
    _ApIfCctStatus_Type()
)
apIfCctStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfCctStatus.setStatus("current")


class _ApIfRedundantSCM_Type(Integer32):
    """Custom type apIfRedundantSCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 2),
          ("present", 1))
    )


_ApIfRedundantSCM_Type.__name__ = "Integer32"
_ApIfRedundantSCM_Object = MibScalar
apIfRedundantSCM = _ApIfRedundantSCM_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24, 4),
    _ApIfRedundantSCM_Type()
)
apIfRedundantSCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIfRedundantSCM.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IFEXT-MIB",
    **{"ifExtMib": ifExtMib,
       "apIfTable": apIfTable,
       "apIfEntry": apIfEntry,
       "apIfIndex": apIfIndex,
       "apIfType": apIfType,
       "apIfCategory": apIfCategory,
       "apIfSlot": apIfSlot,
       "apIfPort": apIfPort,
       "apIfStatus": apIfStatus,
       "apIfCctTable": apIfCctTable,
       "apIfCctEntry": apIfCctEntry,
       "apIfCctIfIndex": apIfCctIfIndex,
       "apIfCctStatus": apIfCctStatus,
       "apIfRedundantSCM": apIfRedundantSCM}
)
