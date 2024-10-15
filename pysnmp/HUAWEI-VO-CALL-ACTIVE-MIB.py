# SNMP MIB module (HUAWEI-VO-CALL-ACTIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-CALL-ACTIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:28 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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

hwVoiceCallActiveMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6)
)
hwVoiceCallActiveMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoCallActiveObjects_ObjectIdentity = ObjectIdentity
hwVoCallActiveObjects = _HwVoCallActiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1)
)
_HwVoCallActiveTable_Object = MibTable
hwVoCallActiveTable = _HwVoCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwVoCallActiveTable.setStatus("current")
_HwVoCallActiveEntry_Object = MibTableRow
hwVoCallActiveEntry = _HwVoCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1)
)
hwVoCallActiveEntry.setIndexNames(
    (0, "HUAWEI-VO-CALL-ACTIVE-MIB", "hwVoCallActiveChannel"),
)
if mibBuilder.loadTexts:
    hwVoCallActiveEntry.setStatus("current")
_HwVoCallActiveChannel_Type = Integer32
_HwVoCallActiveChannel_Object = MibTableColumn
hwVoCallActiveChannel = _HwVoCallActiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 1),
    _HwVoCallActiveChannel_Type()
)
hwVoCallActiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveChannel.setStatus("current")


class _HwVoCallActiveCallerNumber_Type(OctetString):
    """Custom type hwVoCallActiveCallerNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoCallActiveCallerNumber_Type.__name__ = "OctetString"
_HwVoCallActiveCallerNumber_Object = MibTableColumn
hwVoCallActiveCallerNumber = _HwVoCallActiveCallerNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 2),
    _HwVoCallActiveCallerNumber_Type()
)
hwVoCallActiveCallerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveCallerNumber.setStatus("current")


class _HwVoCallActiveCalledNumber_Type(OctetString):
    """Custom type hwVoCallActiveCalledNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoCallActiveCalledNumber_Type.__name__ = "OctetString"
_HwVoCallActiveCalledNumber_Object = MibTableColumn
hwVoCallActiveCalledNumber = _HwVoCallActiveCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 3),
    _HwVoCallActiveCalledNumber_Type()
)
hwVoCallActiveCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveCalledNumber.setStatus("current")


class _HwVoCallActiveEncodeType_Type(Integer32):
    """Custom type hwVoCallActiveEncodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711u", 2),
          ("g723", 3),
          ("g729", 4),
          ("g729a", 5),
          ("unknown", 0))
    )


_HwVoCallActiveEncodeType_Type.__name__ = "Integer32"
_HwVoCallActiveEncodeType_Object = MibTableColumn
hwVoCallActiveEncodeType = _HwVoCallActiveEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 4),
    _HwVoCallActiveEncodeType_Type()
)
hwVoCallActiveEncodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveEncodeType.setStatus("current")
_HwVoCallActiveLocalAddress_Type = IpAddress
_HwVoCallActiveLocalAddress_Object = MibTableColumn
hwVoCallActiveLocalAddress = _HwVoCallActiveLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 5),
    _HwVoCallActiveLocalAddress_Type()
)
hwVoCallActiveLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveLocalAddress.setStatus("current")
_HwVoCallActivePeerAddress_Type = IpAddress
_HwVoCallActivePeerAddress_Object = MibTableColumn
hwVoCallActivePeerAddress = _HwVoCallActivePeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 6),
    _HwVoCallActivePeerAddress_Type()
)
hwVoCallActivePeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActivePeerAddress.setStatus("current")


class _HwVoCallActiveCallOrigin_Type(Integer32):
    """Custom type hwVoCallActiveCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 2),
          ("caller", 1))
    )


_HwVoCallActiveCallOrigin_Type.__name__ = "Integer32"
_HwVoCallActiveCallOrigin_Object = MibTableColumn
hwVoCallActiveCallOrigin = _HwVoCallActiveCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 7),
    _HwVoCallActiveCallOrigin_Type()
)
hwVoCallActiveCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveCallOrigin.setStatus("current")


class _HwVoCallActiveIPSigType_Type(Integer32):
    """Custom type hwVoCallActiveIPSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h323", 1)
    )


_HwVoCallActiveIPSigType_Type.__name__ = "Integer32"
_HwVoCallActiveIPSigType_Object = MibTableColumn
hwVoCallActiveIPSigType = _HwVoCallActiveIPSigType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 8),
    _HwVoCallActiveIPSigType_Type()
)
hwVoCallActiveIPSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveIPSigType.setStatus("current")


class _HwVoCallActivePSTNSigType_Type(Integer32):
    """Custom type hwVoCallActivePSTNSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dem", 6),
          ("dss1", 5),
          ("em", 3),
          ("fxo", 2),
          ("fxs", 1),
          ("r2", 4),
          ("unknown", 0))
    )


_HwVoCallActivePSTNSigType_Type.__name__ = "Integer32"
_HwVoCallActivePSTNSigType_Object = MibTableColumn
hwVoCallActivePSTNSigType = _HwVoCallActivePSTNSigType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 9),
    _HwVoCallActivePSTNSigType_Type()
)
hwVoCallActivePSTNSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActivePSTNSigType.setStatus("current")


class _HwVoCallActiveStatus_Type(Integer32):
    """Custom type hwVoCallActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 3),
          ("calling", 2),
          ("idle", 1),
          ("release", 5),
          ("talking", 4))
    )


_HwVoCallActiveStatus_Type.__name__ = "Integer32"
_HwVoCallActiveStatus_Object = MibTableColumn
hwVoCallActiveStatus = _HwVoCallActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6, 1, 1, 1, 10),
    _HwVoCallActiveStatus_Type()
)
hwVoCallActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallActiveStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-CALL-ACTIVE-MIB",
    **{"hwVoiceCallActiveMIB": hwVoiceCallActiveMIB,
       "hwVoCallActiveObjects": hwVoCallActiveObjects,
       "hwVoCallActiveTable": hwVoCallActiveTable,
       "hwVoCallActiveEntry": hwVoCallActiveEntry,
       "hwVoCallActiveChannel": hwVoCallActiveChannel,
       "hwVoCallActiveCallerNumber": hwVoCallActiveCallerNumber,
       "hwVoCallActiveCalledNumber": hwVoCallActiveCalledNumber,
       "hwVoCallActiveEncodeType": hwVoCallActiveEncodeType,
       "hwVoCallActiveLocalAddress": hwVoCallActiveLocalAddress,
       "hwVoCallActivePeerAddress": hwVoCallActivePeerAddress,
       "hwVoCallActiveCallOrigin": hwVoCallActiveCallOrigin,
       "hwVoCallActiveIPSigType": hwVoCallActiveIPSigType,
       "hwVoCallActivePSTNSigType": hwVoCallActivePSTNSigType,
       "hwVoCallActiveStatus": hwVoCallActiveStatus}
)
