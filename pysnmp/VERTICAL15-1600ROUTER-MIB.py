# SNMP MIB module (VERTICAL15-1600ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL15-1600ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:26 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_V1600Router_ObjectIdentity = ObjectIdentity
v1600Router = _V1600Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 15)
)
_V1600InstalledSlot_Type = Integer32
_V1600InstalledSlot_Object = MibScalar
v1600InstalledSlot = _V1600InstalledSlot_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 1),
    _V1600InstalledSlot_Type()
)
v1600InstalledSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600InstalledSlot.setStatus("mandatory")
_V1600Ser0ChannelWidth_Type = Integer32
_V1600Ser0ChannelWidth_Object = MibScalar
v1600Ser0ChannelWidth = _V1600Ser0ChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 2),
    _V1600Ser0ChannelWidth_Type()
)
v1600Ser0ChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600Ser0ChannelWidth.setStatus("mandatory")
_V1600Ser0T1InterfaceSlot_Type = Integer32
_V1600Ser0T1InterfaceSlot_Object = MibScalar
v1600Ser0T1InterfaceSlot = _V1600Ser0T1InterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 3),
    _V1600Ser0T1InterfaceSlot_Type()
)
v1600Ser0T1InterfaceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600Ser0T1InterfaceSlot.setStatus("mandatory")


class _V1600Ser0T1InterfacePort_Type(Integer32):
    """Custom type v1600Ser0T1InterfacePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_V1600Ser0T1InterfacePort_Type.__name__ = "Integer32"
_V1600Ser0T1InterfacePort_Object = MibScalar
v1600Ser0T1InterfacePort = _V1600Ser0T1InterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 4),
    _V1600Ser0T1InterfacePort_Type()
)
v1600Ser0T1InterfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600Ser0T1InterfacePort.setStatus("mandatory")


class _V1600Ser0T1InterfaceStartChan_Type(Integer32):
    """Custom type v1600Ser0T1InterfaceStartChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_V1600Ser0T1InterfaceStartChan_Type.__name__ = "Integer32"
_V1600Ser0T1InterfaceStartChan_Object = MibScalar
v1600Ser0T1InterfaceStartChan = _V1600Ser0T1InterfaceStartChan_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 5),
    _V1600Ser0T1InterfaceStartChan_Type()
)
v1600Ser0T1InterfaceStartChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600Ser0T1InterfaceStartChan.setStatus("mandatory")


class _V1600FlashCardReady_Type(Integer32):
    """Custom type v1600FlashCardReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 1),
          ("ready", 0))
    )


_V1600FlashCardReady_Type.__name__ = "Integer32"
_V1600FlashCardReady_Object = MibScalar
v1600FlashCardReady = _V1600FlashCardReady_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 6),
    _V1600FlashCardReady_Type()
)
v1600FlashCardReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600FlashCardReady.setStatus("mandatory")


class _V1600CardReadyLED_Type(Integer32):
    """Custom type v1600CardReadyLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_V1600CardReadyLED_Type.__name__ = "Integer32"
_V1600CardReadyLED_Object = MibScalar
v1600CardReadyLED = _V1600CardReadyLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 7),
    _V1600CardReadyLED_Type()
)
v1600CardReadyLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600CardReadyLED.setStatus("mandatory")


class _V1600CardErrorLED_Type(Integer32):
    """Custom type v1600CardErrorLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_V1600CardErrorLED_Type.__name__ = "Integer32"
_V1600CardErrorLED_Object = MibScalar
v1600CardErrorLED = _V1600CardErrorLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 8),
    _V1600CardErrorLED_Type()
)
v1600CardErrorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600CardErrorLED.setStatus("mandatory")


class _V1600RouterOKLED_Type(Integer32):
    """Custom type v1600RouterOKLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_V1600RouterOKLED_Type.__name__ = "Integer32"
_V1600RouterOKLED_Object = MibScalar
v1600RouterOKLED = _V1600RouterOKLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 9),
    _V1600RouterOKLED_Type()
)
v1600RouterOKLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600RouterOKLED.setStatus("mandatory")


class _V1600ExtSerial1ConnOK_Type(Integer32):
    """Custom type v1600ExtSerial1ConnOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_V1600ExtSerial1ConnOK_Type.__name__ = "Integer32"
_V1600ExtSerial1ConnOK_Object = MibScalar
v1600ExtSerial1ConnOK = _V1600ExtSerial1ConnOK_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 10),
    _V1600ExtSerial1ConnOK_Type()
)
v1600ExtSerial1ConnOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600ExtSerial1ConnOK.setStatus("mandatory")


class _V1600ExtSerial1DCD_Type(Integer32):
    """Custom type v1600ExtSerial1DCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_V1600ExtSerial1DCD_Type.__name__ = "Integer32"
_V1600ExtSerial1DCD_Object = MibScalar
v1600ExtSerial1DCD = _V1600ExtSerial1DCD_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 11),
    _V1600ExtSerial1DCD_Type()
)
v1600ExtSerial1DCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600ExtSerial1DCD.setStatus("mandatory")
_V1600SwitchSlotNum_Type = Integer32
_V1600SwitchSlotNum_Object = MibScalar
v1600SwitchSlotNum = _V1600SwitchSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 12),
    _V1600SwitchSlotNum_Type()
)
v1600SwitchSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600SwitchSlotNum.setStatus("mandatory")
_V1600EthSwitchedPorts_Type = Integer32
_V1600EthSwitchedPorts_Object = MibScalar
v1600EthSwitchedPorts = _V1600EthSwitchedPorts_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 13),
    _V1600EthSwitchedPorts_Type()
)
v1600EthSwitchedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600EthSwitchedPorts.setStatus("mandatory")
_V1600SwitchStat_Type = DisplayString
_V1600SwitchStat_Object = MibScalar
v1600SwitchStat = _V1600SwitchStat_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 14),
    _V1600SwitchStat_Type()
)
v1600SwitchStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600SwitchStat.setStatus("mandatory")


class _V1600IntSerial0ConnOK_Type(Integer32):
    """Custom type v1600IntSerial0ConnOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_V1600IntSerial0ConnOK_Type.__name__ = "Integer32"
_V1600IntSerial0ConnOK_Object = MibScalar
v1600IntSerial0ConnOK = _V1600IntSerial0ConnOK_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 15),
    _V1600IntSerial0ConnOK_Type()
)
v1600IntSerial0ConnOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600IntSerial0ConnOK.setStatus("mandatory")


class _V1600IntSerial0DCD_Type(Integer32):
    """Custom type v1600IntSerial0DCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_V1600IntSerial0DCD_Type.__name__ = "Integer32"
_V1600IntSerial0DCD_Object = MibScalar
v1600IntSerial0DCD = _V1600IntSerial0DCD_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 16),
    _V1600IntSerial0DCD_Type()
)
v1600IntSerial0DCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600IntSerial0DCD.setStatus("mandatory")


class _V1600RouterEthLinkOK_Type(Integer32):
    """Custom type v1600RouterEthLinkOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_V1600RouterEthLinkOK_Type.__name__ = "Integer32"
_V1600RouterEthLinkOK_Object = MibScalar
v1600RouterEthLinkOK = _V1600RouterEthLinkOK_Object(
    (1, 3, 6, 1, 4, 1, 2338, 15, 17),
    _V1600RouterEthLinkOK_Type()
)
v1600RouterEthLinkOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1600RouterEthLinkOK.setStatus("mandatory")

# Managed Objects groups


# Notification objects

v1600CardNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 68)
)
v1600CardNotReady.setObjects(
    ("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot")
)
if mibBuilder.loadTexts:
    v1600CardNotReady.setStatus(
        ""
    )

v1600FlashCardNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 69)
)
v1600FlashCardNotReady.setObjects(
    ("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot")
)
if mibBuilder.loadTexts:
    v1600FlashCardNotReady.setStatus(
        ""
    )

v1600FlashCardReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 76)
)
v1600FlashCardReadyTrap.setObjects(
    ("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot")
)
if mibBuilder.loadTexts:
    v1600FlashCardReadyTrap.setStatus(
        ""
    )

v1600RouterReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 77)
)
v1600RouterReady.setObjects(
    ("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot")
)
if mibBuilder.loadTexts:
    v1600RouterReady.setStatus(
        ""
    )

v1600RouterNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 78)
)
v1600RouterNotReady.setObjects(
    ("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot")
)
if mibBuilder.loadTexts:
    v1600RouterNotReady.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL15-1600ROUTER-MIB",
    **{"vertical": vertical,
       "v1600CardNotReady": v1600CardNotReady,
       "v1600FlashCardNotReady": v1600FlashCardNotReady,
       "v1600FlashCardReadyTrap": v1600FlashCardReadyTrap,
       "v1600RouterReady": v1600RouterReady,
       "v1600RouterNotReady": v1600RouterNotReady,
       "v1600Router": v1600Router,
       "v1600InstalledSlot": v1600InstalledSlot,
       "v1600Ser0ChannelWidth": v1600Ser0ChannelWidth,
       "v1600Ser0T1InterfaceSlot": v1600Ser0T1InterfaceSlot,
       "v1600Ser0T1InterfacePort": v1600Ser0T1InterfacePort,
       "v1600Ser0T1InterfaceStartChan": v1600Ser0T1InterfaceStartChan,
       "v1600FlashCardReady": v1600FlashCardReady,
       "v1600CardReadyLED": v1600CardReadyLED,
       "v1600CardErrorLED": v1600CardErrorLED,
       "v1600RouterOKLED": v1600RouterOKLED,
       "v1600ExtSerial1ConnOK": v1600ExtSerial1ConnOK,
       "v1600ExtSerial1DCD": v1600ExtSerial1DCD,
       "v1600SwitchSlotNum": v1600SwitchSlotNum,
       "v1600EthSwitchedPorts": v1600EthSwitchedPorts,
       "v1600SwitchStat": v1600SwitchStat,
       "v1600IntSerial0ConnOK": v1600IntSerial0ConnOK,
       "v1600IntSerial0DCD": v1600IntSerial0DCD,
       "v1600RouterEthLinkOK": v1600RouterEthLinkOK}
)
