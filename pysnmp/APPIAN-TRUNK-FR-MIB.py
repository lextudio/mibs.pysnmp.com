# SNMP MIB module (APPIAN-TRUNK-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-TRUNK-FR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:46 2024
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

(acTrunks,) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "acTrunks")

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

acFrTrunk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2)
)
acFrTrunk.setRevisions(
        ("1999-11-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcFrTrunkTable_Object = MibTable
acFrTrunkTable = _AcFrTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    acFrTrunkTable.setStatus("current")
_AcFrTrunkEntry_Object = MibTableRow
acFrTrunkEntry = _AcFrTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1)
)
acFrTrunkEntry.setIndexNames(
    (0, "APPIAN-TRUNK-FR-MIB", "acFrTrunkIndex"),
)
if mibBuilder.loadTexts:
    acFrTrunkEntry.setStatus("current")
_AcFrTrunkIndex_Type = Integer32
_AcFrTrunkIndex_Object = MibTableColumn
acFrTrunkIndex = _AcFrTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 1),
    _AcFrTrunkIndex_Type()
)
acFrTrunkIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acFrTrunkIndex.setStatus("current")


class _AcFrTrunkLmiProtocol_Type(Integer32):
    """Custom type acFrTrunkLmiProtocol based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 6),
          ("auto", 7),
          ("itu", 5))
    )


_AcFrTrunkLmiProtocol_Type.__name__ = "Integer32"
_AcFrTrunkLmiProtocol_Object = MibTableColumn
acFrTrunkLmiProtocol = _AcFrTrunkLmiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 2),
    _AcFrTrunkLmiProtocol_Type()
)
acFrTrunkLmiProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkLmiProtocol.setStatus("current")


class _AcFrTrunkLmiPollingMode_Type(Integer32):
    """Custom type acFrTrunkLmiPollingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("polled", 2),
          ("polling", 1))
    )


_AcFrTrunkLmiPollingMode_Type.__name__ = "Integer32"
_AcFrTrunkLmiPollingMode_Object = MibTableColumn
acFrTrunkLmiPollingMode = _AcFrTrunkLmiPollingMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 3),
    _AcFrTrunkLmiPollingMode_Type()
)
acFrTrunkLmiPollingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkLmiPollingMode.setStatus("current")


class _AcFrTrunkT391_Type(Integer32):
    """Custom type acFrTrunkT391 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AcFrTrunkT391_Type.__name__ = "Integer32"
_AcFrTrunkT391_Object = MibTableColumn
acFrTrunkT391 = _AcFrTrunkT391_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 4),
    _AcFrTrunkT391_Type()
)
acFrTrunkT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkT391.setStatus("current")


class _AcFrTrunkT392_Type(Integer32):
    """Custom type acFrTrunkT392 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AcFrTrunkT392_Type.__name__ = "Integer32"
_AcFrTrunkT392_Object = MibTableColumn
acFrTrunkT392 = _AcFrTrunkT392_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 5),
    _AcFrTrunkT392_Type()
)
acFrTrunkT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkT392.setStatus("current")


class _AcFrTrunkN391_Type(Integer32):
    """Custom type acFrTrunkN391 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AcFrTrunkN391_Type.__name__ = "Integer32"
_AcFrTrunkN391_Object = MibTableColumn
acFrTrunkN391 = _AcFrTrunkN391_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 6),
    _AcFrTrunkN391_Type()
)
acFrTrunkN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkN391.setStatus("current")


class _AcFrTrunkN392_Type(Integer32):
    """Custom type acFrTrunkN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcFrTrunkN392_Type.__name__ = "Integer32"
_AcFrTrunkN392_Object = MibTableColumn
acFrTrunkN392 = _AcFrTrunkN392_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 7),
    _AcFrTrunkN392_Type()
)
acFrTrunkN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkN392.setStatus("current")


class _AcFrTrunkN393_Type(Integer32):
    """Custom type acFrTrunkN393 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcFrTrunkN393_Type.__name__ = "Integer32"
_AcFrTrunkN393_Object = MibTableColumn
acFrTrunkN393 = _AcFrTrunkN393_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 8),
    _AcFrTrunkN393_Type()
)
acFrTrunkN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkN393.setStatus("current")


class _AcFrTrunkShared_Type(TruthValue):
    """Custom type acFrTrunkShared based on TruthValue"""


_AcFrTrunkShared_Object = MibTableColumn
acFrTrunkShared = _AcFrTrunkShared_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 2, 1, 1, 9),
    _AcFrTrunkShared_Type()
)
acFrTrunkShared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFrTrunkShared.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-TRUNK-FR-MIB",
    **{"acFrTrunk": acFrTrunk,
       "acFrTrunkTable": acFrTrunkTable,
       "acFrTrunkEntry": acFrTrunkEntry,
       "acFrTrunkIndex": acFrTrunkIndex,
       "acFrTrunkLmiProtocol": acFrTrunkLmiProtocol,
       "acFrTrunkLmiPollingMode": acFrTrunkLmiPollingMode,
       "acFrTrunkT391": acFrTrunkT391,
       "acFrTrunkT392": acFrTrunkT392,
       "acFrTrunkN391": acFrTrunkN391,
       "acFrTrunkN392": acFrTrunkN392,
       "acFrTrunkN393": acFrTrunkN393,
       "acFrTrunkShared": acFrTrunkShared}
)
