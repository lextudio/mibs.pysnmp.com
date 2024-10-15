# SNMP MIB module (CXEthIo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXEthIo-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:21 2024
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

(Alias,
 cxEthIo) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxEthIo")

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

_EthSapOprTable_Object = MibTable
ethSapOprTable = _EthSapOprTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1)
)
if mibBuilder.loadTexts:
    ethSapOprTable.setStatus("mandatory")
_EthSapOprEntry_Object = MibTableRow
ethSapOprEntry = _EthSapOprEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1)
)
ethSapOprEntry.setIndexNames(
    (0, "CXEthIo-MIB", "ethSapOprNumber"),
)
if mibBuilder.loadTexts:
    ethSapOprEntry.setStatus("mandatory")
_EthSapOprNumber_Type = Integer32
_EthSapOprNumber_Object = MibTableColumn
ethSapOprNumber = _EthSapOprNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 1),
    _EthSapOprNumber_Type()
)
ethSapOprNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSapOprNumber.setStatus("mandatory")
_EthSapOprAlias_Type = Alias
_EthSapOprAlias_Object = MibTableColumn
ethSapOprAlias = _EthSapOprAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 2),
    _EthSapOprAlias_Type()
)
ethSapOprAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSapOprAlias.setStatus("mandatory")


class _EthSapOprConnectorType_Type(Integer32):
    """Custom type ethSapOprConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aui", 2),
          ("auto", 1),
          ("baset-100", 4),
          ("tbaset", 3))
    )


_EthSapOprConnectorType_Type.__name__ = "Integer32"
_EthSapOprConnectorType_Object = MibTableColumn
ethSapOprConnectorType = _EthSapOprConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 3),
    _EthSapOprConnectorType_Type()
)
ethSapOprConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSapOprConnectorType.setStatus("mandatory")


class _EthSapOprDataGenerator_Type(Integer32):
    """Custom type ethSapOprDataGenerator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-verify", 3),
          ("retrigger", 4))
    )


_EthSapOprDataGenerator_Type.__name__ = "Integer32"
_EthSapOprDataGenerator_Object = MibTableColumn
ethSapOprDataGenerator = _EthSapOprDataGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 4),
    _EthSapOprDataGenerator_Type()
)
ethSapOprDataGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapOprDataGenerator.setStatus("mandatory")
_EthSapOprGenFrames_Type = Integer32
_EthSapOprGenFrames_Object = MibTableColumn
ethSapOprGenFrames = _EthSapOprGenFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 5),
    _EthSapOprGenFrames_Type()
)
ethSapOprGenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapOprGenFrames.setStatus("mandatory")
_EthSapOprGenFrameSize_Type = Integer32
_EthSapOprGenFrameSize_Object = MibTableColumn
ethSapOprGenFrameSize = _EthSapOprGenFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 6),
    _EthSapOprGenFrameSize_Type()
)
ethSapOprGenFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapOprGenFrameSize.setStatus("mandatory")


class _EthSapOprLoopbackType_Type(Integer32):
    """Custom type ethSapOprLoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("local", 2),
          ("none", 1),
          ("remote", 3))
    )


_EthSapOprLoopbackType_Type.__name__ = "Integer32"
_EthSapOprLoopbackType_Object = MibTableColumn
ethSapOprLoopbackType = _EthSapOprLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 7),
    _EthSapOprLoopbackType_Type()
)
ethSapOprLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSapOprLoopbackType.setStatus("mandatory")


class _EthOprControlStats_Type(Integer32):
    """Custom type ethOprControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearSapStats", 1)
    )


_EthOprControlStats_Type.__name__ = "Integer32"
_EthOprControlStats_Object = MibTableColumn
ethOprControlStats = _EthOprControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 12),
    _EthOprControlStats_Type()
)
ethOprControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ethOprControlStats.setStatus("mandatory")


class _EthStatOprLinkState_Type(Integer32):
    """Custom type ethStatOprLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EthStatOprLinkState_Type.__name__ = "Integer32"
_EthStatOprLinkState_Object = MibTableColumn
ethStatOprLinkState = _EthStatOprLinkState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 14),
    _EthStatOprLinkState_Type()
)
ethStatOprLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprLinkState.setStatus("mandatory")
_EthStatOprInFrames_Type = Counter32
_EthStatOprInFrames_Object = MibTableColumn
ethStatOprInFrames = _EthStatOprInFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 15),
    _EthStatOprInFrames_Type()
)
ethStatOprInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprInFrames.setStatus("mandatory")
_EthStatOprInOctets_Type = Counter32
_EthStatOprInOctets_Object = MibTableColumn
ethStatOprInOctets = _EthStatOprInOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 16),
    _EthStatOprInOctets_Type()
)
ethStatOprInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprInOctets.setStatus("mandatory")
_EthStatOprInErrors_Type = Counter32
_EthStatOprInErrors_Object = MibTableColumn
ethStatOprInErrors = _EthStatOprInErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 17),
    _EthStatOprInErrors_Type()
)
ethStatOprInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprInErrors.setStatus("mandatory")
_EthStatOprInDiscards_Type = Counter32
_EthStatOprInDiscards_Object = MibTableColumn
ethStatOprInDiscards = _EthStatOprInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 18),
    _EthStatOprInDiscards_Type()
)
ethStatOprInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprInDiscards.setStatus("mandatory")
_EthStatOprInBusyDiscards_Type = Counter32
_EthStatOprInBusyDiscards_Object = MibTableColumn
ethStatOprInBusyDiscards = _EthStatOprInBusyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 19),
    _EthStatOprInBusyDiscards_Type()
)
ethStatOprInBusyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprInBusyDiscards.setStatus("mandatory")
_EthStatOprOutFrames_Type = Counter32
_EthStatOprOutFrames_Object = MibTableColumn
ethStatOprOutFrames = _EthStatOprOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 20),
    _EthStatOprOutFrames_Type()
)
ethStatOprOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprOutFrames.setStatus("mandatory")
_EthStatOprOutOctets_Type = Counter32
_EthStatOprOutOctets_Object = MibTableColumn
ethStatOprOutOctets = _EthStatOprOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 21),
    _EthStatOprOutOctets_Type()
)
ethStatOprOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprOutOctets.setStatus("mandatory")
_EthStatOprOutErrors_Type = Counter32
_EthStatOprOutErrors_Object = MibTableColumn
ethStatOprOutErrors = _EthStatOprOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 22),
    _EthStatOprOutErrors_Type()
)
ethStatOprOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprOutErrors.setStatus("mandatory")
_EthStatOprOutDiscards_Type = Counter32
_EthStatOprOutDiscards_Object = MibTableColumn
ethStatOprOutDiscards = _EthStatOprOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 23),
    _EthStatOprOutDiscards_Type()
)
ethStatOprOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprOutDiscards.setStatus("mandatory")
_EthStatOprOutCSLostFrames_Type = Counter32
_EthStatOprOutCSLostFrames_Object = MibTableColumn
ethStatOprOutCSLostFrames = _EthStatOprOutCSLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 24),
    _EthStatOprOutCSLostFrames_Type()
)
ethStatOprOutCSLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprOutCSLostFrames.setStatus("mandatory")
_EthStatOprRxGenErrors_Type = Counter32
_EthStatOprRxGenErrors_Object = MibTableColumn
ethStatOprRxGenErrors = _EthStatOprRxGenErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 25),
    _EthStatOprRxGenErrors_Type()
)
ethStatOprRxGenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatOprRxGenErrors.setStatus("mandatory")
_EthSapAdmTable_Object = MibTable
ethSapAdmTable = _EthSapAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2)
)
if mibBuilder.loadTexts:
    ethSapAdmTable.setStatus("mandatory")
_EthSapAdmEntry_Object = MibTableRow
ethSapAdmEntry = _EthSapAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1)
)
ethSapAdmEntry.setIndexNames(
    (0, "CXEthIo-MIB", "ethSapAdmNumber"),
)
if mibBuilder.loadTexts:
    ethSapAdmEntry.setStatus("mandatory")
_EthSapAdmNumber_Type = Integer32
_EthSapAdmNumber_Object = MibTableColumn
ethSapAdmNumber = _EthSapAdmNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 1),
    _EthSapAdmNumber_Type()
)
ethSapAdmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSapAdmNumber.setStatus("mandatory")
_EthSapAdmAlias_Type = Alias
_EthSapAdmAlias_Object = MibTableColumn
ethSapAdmAlias = _EthSapAdmAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 2),
    _EthSapAdmAlias_Type()
)
ethSapAdmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapAdmAlias.setStatus("mandatory")


class _EthSapAdmConnectorType_Type(Integer32):
    """Custom type ethSapAdmConnectorType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aui", 2),
          ("auto", 1),
          ("baset-100", 4),
          ("tbaseT", 3))
    )


_EthSapAdmConnectorType_Type.__name__ = "Integer32"
_EthSapAdmConnectorType_Object = MibTableColumn
ethSapAdmConnectorType = _EthSapAdmConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 3),
    _EthSapAdmConnectorType_Type()
)
ethSapAdmConnectorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapAdmConnectorType.setStatus("mandatory")


class _EthSapAdmDataGenerator_Type(Integer32):
    """Custom type ethSapAdmDataGenerator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-verify", 3))
    )


_EthSapAdmDataGenerator_Type.__name__ = "Integer32"
_EthSapAdmDataGenerator_Object = MibTableColumn
ethSapAdmDataGenerator = _EthSapAdmDataGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 4),
    _EthSapAdmDataGenerator_Type()
)
ethSapAdmDataGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapAdmDataGenerator.setStatus("mandatory")


class _EthSapAdmGenFrames_Type(Integer32):
    """Custom type ethSapAdmGenFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EthSapAdmGenFrames_Type.__name__ = "Integer32"
_EthSapAdmGenFrames_Object = MibTableColumn
ethSapAdmGenFrames = _EthSapAdmGenFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 5),
    _EthSapAdmGenFrames_Type()
)
ethSapAdmGenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapAdmGenFrames.setStatus("mandatory")


class _EthSapAdmGenFrameSize_Type(Integer32):
    """Custom type ethSapAdmGenFrameSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1514),
    )


_EthSapAdmGenFrameSize_Type.__name__ = "Integer32"
_EthSapAdmGenFrameSize_Object = MibTableColumn
ethSapAdmGenFrameSize = _EthSapAdmGenFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 6),
    _EthSapAdmGenFrameSize_Type()
)
ethSapAdmGenFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapAdmGenFrameSize.setStatus("mandatory")


class _EthSapAdmLoopbackType_Type(Integer32):
    """Custom type ethSapAdmLoopbackType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("local", 2),
          ("none", 1),
          ("remote", 3))
    )


_EthSapAdmLoopbackType_Type.__name__ = "Integer32"
_EthSapAdmLoopbackType_Object = MibTableColumn
ethSapAdmLoopbackType = _EthSapAdmLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 7),
    _EthSapAdmLoopbackType_Type()
)
ethSapAdmLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSapAdmLoopbackType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXEthIo-MIB",
    **{"ethSapOprTable": ethSapOprTable,
       "ethSapOprEntry": ethSapOprEntry,
       "ethSapOprNumber": ethSapOprNumber,
       "ethSapOprAlias": ethSapOprAlias,
       "ethSapOprConnectorType": ethSapOprConnectorType,
       "ethSapOprDataGenerator": ethSapOprDataGenerator,
       "ethSapOprGenFrames": ethSapOprGenFrames,
       "ethSapOprGenFrameSize": ethSapOprGenFrameSize,
       "ethSapOprLoopbackType": ethSapOprLoopbackType,
       "ethOprControlStats": ethOprControlStats,
       "ethStatOprLinkState": ethStatOprLinkState,
       "ethStatOprInFrames": ethStatOprInFrames,
       "ethStatOprInOctets": ethStatOprInOctets,
       "ethStatOprInErrors": ethStatOprInErrors,
       "ethStatOprInDiscards": ethStatOprInDiscards,
       "ethStatOprInBusyDiscards": ethStatOprInBusyDiscards,
       "ethStatOprOutFrames": ethStatOprOutFrames,
       "ethStatOprOutOctets": ethStatOprOutOctets,
       "ethStatOprOutErrors": ethStatOprOutErrors,
       "ethStatOprOutDiscards": ethStatOprOutDiscards,
       "ethStatOprOutCSLostFrames": ethStatOprOutCSLostFrames,
       "ethStatOprRxGenErrors": ethStatOprRxGenErrors,
       "ethSapAdmTable": ethSapAdmTable,
       "ethSapAdmEntry": ethSapAdmEntry,
       "ethSapAdmNumber": ethSapAdmNumber,
       "ethSapAdmAlias": ethSapAdmAlias,
       "ethSapAdmConnectorType": ethSapAdmConnectorType,
       "ethSapAdmDataGenerator": ethSapAdmDataGenerator,
       "ethSapAdmGenFrames": ethSapAdmGenFrames,
       "ethSapAdmGenFrameSize": ethSapAdmGenFrameSize,
       "ethSapAdmLoopbackType": ethSapAdmLoopbackType}
)
