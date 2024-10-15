# SNMP MIB module (ACC-HUB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-HUB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:18 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccEnetHub_ObjectIdentity = ObjectIdentity
accEnetHub = _AccEnetHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39)
)
_AccEnetHubStatTable_Object = MibTable
accEnetHubStatTable = _AccEnetHubStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1)
)
if mibBuilder.loadTexts:
    accEnetHubStatTable.setStatus("mandatory")
_AccEnetHubStatEntry_Object = MibTableRow
accEnetHubStatEntry = _AccEnetHubStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1)
)
accEnetHubStatEntry.setIndexNames(
    (0, "ACC-HUB", "accEnetPortIndex"),
    (0, "ACC-HUB", "accEnetHubIndex"),
)
if mibBuilder.loadTexts:
    accEnetHubStatEntry.setStatus("mandatory")
_AccEnetPortIndex_Type = Integer32
_AccEnetPortIndex_Object = MibTableColumn
accEnetPortIndex = _AccEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 1),
    _AccEnetPortIndex_Type()
)
accEnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetPortIndex.setStatus("mandatory")
_AccEnetHubIndex_Type = Integer32
_AccEnetHubIndex_Object = MibTableColumn
accEnetHubIndex = _AccEnetHubIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 2),
    _AccEnetHubIndex_Type()
)
accEnetHubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubIndex.setStatus("mandatory")


class _AccEnetHubAdStatus_Type(Integer32):
    """Custom type accEnetHubAdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AccEnetHubAdStatus_Type.__name__ = "Integer32"
_AccEnetHubAdStatus_Object = MibTableColumn
accEnetHubAdStatus = _AccEnetHubAdStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 3),
    _AccEnetHubAdStatus_Type()
)
accEnetHubAdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEnetHubAdStatus.setStatus("mandatory")


class _AccEnetHubOpStatus_Type(Integer32):
    """Custom type accEnetHubOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disabled", 3),
          ("partitioned", 2))
    )


_AccEnetHubOpStatus_Type.__name__ = "Integer32"
_AccEnetHubOpStatus_Object = MibTableColumn
accEnetHubOpStatus = _AccEnetHubOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 4),
    _AccEnetHubOpStatus_Type()
)
accEnetHubOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubOpStatus.setStatus("mandatory")


class _AccEnetHubBitError_Type(Integer32):
    """Custom type accEnetHubBitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccEnetHubBitError_Type.__name__ = "Integer32"
_AccEnetHubBitError_Object = MibTableColumn
accEnetHubBitError = _AccEnetHubBitError_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 5),
    _AccEnetHubBitError_Type()
)
accEnetHubBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubBitError.setStatus("mandatory")


class _AccEnetHubLinkTest_Type(Integer32):
    """Custom type accEnetHubLinkTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("pass", 1))
    )


_AccEnetHubLinkTest_Type.__name__ = "Integer32"
_AccEnetHubLinkTest_Object = MibTableColumn
accEnetHubLinkTest = _AccEnetHubLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 6),
    _AccEnetHubLinkTest_Type()
)
accEnetHubLinkTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubLinkTest.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-HUB",
    **{"accEnetHub": accEnetHub,
       "accEnetHubStatTable": accEnetHubStatTable,
       "accEnetHubStatEntry": accEnetHubStatEntry,
       "accEnetPortIndex": accEnetPortIndex,
       "accEnetHubIndex": accEnetHubIndex,
       "accEnetHubAdStatus": accEnetHubAdStatus,
       "accEnetHubOpStatus": accEnetHubOpStatus,
       "accEnetHubBitError": accEnetHubBitError,
       "accEnetHubLinkTest": accEnetHubLinkTest}
)
