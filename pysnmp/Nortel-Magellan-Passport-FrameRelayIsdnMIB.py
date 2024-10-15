# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayIsdnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayIsdnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:46 2024
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

(frUni,
 frUniIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-FrameRelayUniMIB",
    "frUni",
    "frUniIndex")

(Counter32,
 DisplayString,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(DigitString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "DigitString",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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

_FrUniIsdn_ObjectIdentity = ObjectIdentity
frUniIsdn = _FrUniIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100)
)
_FrUniIsdnRowStatusTable_Object = MibTable
frUniIsdnRowStatusTable = _FrUniIsdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1)
)
if mibBuilder.loadTexts:
    frUniIsdnRowStatusTable.setStatus("mandatory")
_FrUniIsdnRowStatusEntry_Object = MibTableRow
frUniIsdnRowStatusEntry = _FrUniIsdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1)
)
frUniIsdnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayIsdnMIB", "frUniIsdnIndex"),
)
if mibBuilder.loadTexts:
    frUniIsdnRowStatusEntry.setStatus("mandatory")
_FrUniIsdnRowStatus_Type = RowStatus
_FrUniIsdnRowStatus_Object = MibTableColumn
frUniIsdnRowStatus = _FrUniIsdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 1),
    _FrUniIsdnRowStatus_Type()
)
frUniIsdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniIsdnRowStatus.setStatus("mandatory")
_FrUniIsdnComponentName_Type = DisplayString
_FrUniIsdnComponentName_Object = MibTableColumn
frUniIsdnComponentName = _FrUniIsdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 2),
    _FrUniIsdnComponentName_Type()
)
frUniIsdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIsdnComponentName.setStatus("mandatory")
_FrUniIsdnStorageType_Type = StorageType
_FrUniIsdnStorageType_Object = MibTableColumn
frUniIsdnStorageType = _FrUniIsdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 4),
    _FrUniIsdnStorageType_Type()
)
frUniIsdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIsdnStorageType.setStatus("mandatory")
_FrUniIsdnIndex_Type = NonReplicated
_FrUniIsdnIndex_Object = MibTableColumn
frUniIsdnIndex = _FrUniIsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 10),
    _FrUniIsdnIndex_Type()
)
frUniIsdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniIsdnIndex.setStatus("mandatory")
_FrUniIsdnProvTable_Object = MibTable
frUniIsdnProvTable = _FrUniIsdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11)
)
if mibBuilder.loadTexts:
    frUniIsdnProvTable.setStatus("mandatory")
_FrUniIsdnProvEntry_Object = MibTableRow
frUniIsdnProvEntry = _FrUniIsdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11, 1)
)
frUniIsdnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayIsdnMIB", "frUniIsdnIndex"),
)
if mibBuilder.loadTexts:
    frUniIsdnProvEntry.setStatus("mandatory")


class _FrUniIsdnT320_Type(Unsigned32):
    """Custom type frUniIsdnT320 based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniIsdnT320_Type.__name__ = "Unsigned32"
_FrUniIsdnT320_Object = MibTableColumn
frUniIsdnT320 = _FrUniIsdnT320_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11, 1, 1),
    _FrUniIsdnT320_Type()
)
frUniIsdnT320.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniIsdnT320.setStatus("mandatory")


class _FrUniIsdnAddressSignalling_Type(Integer32):
    """Custom type frUniIsdnAddressSignalling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isdnDna", 0),
          ("normalBehavior", 1))
    )


_FrUniIsdnAddressSignalling_Type.__name__ = "Integer32"
_FrUniIsdnAddressSignalling_Object = MibTableColumn
frUniIsdnAddressSignalling = _FrUniIsdnAddressSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11, 1, 2),
    _FrUniIsdnAddressSignalling_Type()
)
frUniIsdnAddressSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniIsdnAddressSignalling.setStatus("mandatory")
_FrUniIsdnOperTable_Object = MibTable
frUniIsdnOperTable = _FrUniIsdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12)
)
if mibBuilder.loadTexts:
    frUniIsdnOperTable.setStatus("mandatory")
_FrUniIsdnOperEntry_Object = MibTableRow
frUniIsdnOperEntry = _FrUniIsdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1)
)
frUniIsdnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayIsdnMIB", "frUniIsdnIndex"),
)
if mibBuilder.loadTexts:
    frUniIsdnOperEntry.setStatus("mandatory")


class _FrUniIsdnDataSigChan_Type(Integer32):
    """Custom type frUniIsdnDataSigChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrUniIsdnDataSigChan_Type.__name__ = "Integer32"
_FrUniIsdnDataSigChan_Object = MibTableColumn
frUniIsdnDataSigChan = _FrUniIsdnDataSigChan_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 1),
    _FrUniIsdnDataSigChan_Type()
)
frUniIsdnDataSigChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIsdnDataSigChan.setStatus("mandatory")


class _FrUniIsdnBChannelState_Type(Integer32):
    """Custom type frUniIsdnBChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("disabled", 2),
          ("idle", 0))
    )


_FrUniIsdnBChannelState_Type.__name__ = "Integer32"
_FrUniIsdnBChannelState_Object = MibTableColumn
frUniIsdnBChannelState = _FrUniIsdnBChannelState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 2),
    _FrUniIsdnBChannelState_Type()
)
frUniIsdnBChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIsdnBChannelState.setStatus("mandatory")


class _FrUniIsdnLastUsedCgpn_Type(DigitString):
    """Custom type frUniIsdnLastUsedCgpn based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_FrUniIsdnLastUsedCgpn_Type.__name__ = "DigitString"
_FrUniIsdnLastUsedCgpn_Object = MibTableColumn
frUniIsdnLastUsedCgpn = _FrUniIsdnLastUsedCgpn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 3),
    _FrUniIsdnLastUsedCgpn_Type()
)
frUniIsdnLastUsedCgpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIsdnLastUsedCgpn.setStatus("mandatory")


class _FrUniIsdnBChanIntState_Type(Integer32):
    """Custom type frUniIsdnBChanIntState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 7),
          ("enabling", 4),
          ("isdnInit", 0),
          ("releasing", 8),
          ("up", 6),
          ("waitAccEnable", 1),
          ("waitAccRegAck", 5),
          ("waitFramerData", 3),
          ("waitLnsResponse", 2))
    )


_FrUniIsdnBChanIntState_Type.__name__ = "Integer32"
_FrUniIsdnBChanIntState_Object = MibTableColumn
frUniIsdnBChanIntState = _FrUniIsdnBChanIntState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 4),
    _FrUniIsdnBChanIntState_Type()
)
frUniIsdnBChanIntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIsdnBChanIntState.setStatus("mandatory")
_FrUniIsdnActiveVirtualCircuitsCount_Type = Counter32
_FrUniIsdnActiveVirtualCircuitsCount_Object = MibTableColumn
frUniIsdnActiveVirtualCircuitsCount = _FrUniIsdnActiveVirtualCircuitsCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 5),
    _FrUniIsdnActiveVirtualCircuitsCount_Type()
)
frUniIsdnActiveVirtualCircuitsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIsdnActiveVirtualCircuitsCount.setStatus("mandatory")
_FrameRelayIsdnMIB_ObjectIdentity = ObjectIdentity
frameRelayIsdnMIB = _FrameRelayIsdnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122)
)
_FrameRelayIsdnGroup_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroup = _FrameRelayIsdnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1)
)
_FrameRelayIsdnGroupBD_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroupBD = _FrameRelayIsdnGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1, 4)
)
_FrameRelayIsdnGroupBD02_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroupBD02 = _FrameRelayIsdnGroupBD02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1, 4, 3)
)
_FrameRelayIsdnGroupBD02A_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroupBD02A = _FrameRelayIsdnGroupBD02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1, 4, 3, 2)
)
_FrameRelayIsdnCapabilities_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilities = _FrameRelayIsdnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3)
)
_FrameRelayIsdnCapabilitiesBD_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilitiesBD = _FrameRelayIsdnCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3, 4)
)
_FrameRelayIsdnCapabilitiesBD02_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilitiesBD02 = _FrameRelayIsdnCapabilitiesBD02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3, 4, 3)
)
_FrameRelayIsdnCapabilitiesBD02A_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilitiesBD02A = _FrameRelayIsdnCapabilitiesBD02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3, 4, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayIsdnMIB",
    **{"frUniIsdn": frUniIsdn,
       "frUniIsdnRowStatusTable": frUniIsdnRowStatusTable,
       "frUniIsdnRowStatusEntry": frUniIsdnRowStatusEntry,
       "frUniIsdnRowStatus": frUniIsdnRowStatus,
       "frUniIsdnComponentName": frUniIsdnComponentName,
       "frUniIsdnStorageType": frUniIsdnStorageType,
       "frUniIsdnIndex": frUniIsdnIndex,
       "frUniIsdnProvTable": frUniIsdnProvTable,
       "frUniIsdnProvEntry": frUniIsdnProvEntry,
       "frUniIsdnT320": frUniIsdnT320,
       "frUniIsdnAddressSignalling": frUniIsdnAddressSignalling,
       "frUniIsdnOperTable": frUniIsdnOperTable,
       "frUniIsdnOperEntry": frUniIsdnOperEntry,
       "frUniIsdnDataSigChan": frUniIsdnDataSigChan,
       "frUniIsdnBChannelState": frUniIsdnBChannelState,
       "frUniIsdnLastUsedCgpn": frUniIsdnLastUsedCgpn,
       "frUniIsdnBChanIntState": frUniIsdnBChanIntState,
       "frUniIsdnActiveVirtualCircuitsCount": frUniIsdnActiveVirtualCircuitsCount,
       "frameRelayIsdnMIB": frameRelayIsdnMIB,
       "frameRelayIsdnGroup": frameRelayIsdnGroup,
       "frameRelayIsdnGroupBD": frameRelayIsdnGroupBD,
       "frameRelayIsdnGroupBD02": frameRelayIsdnGroupBD02,
       "frameRelayIsdnGroupBD02A": frameRelayIsdnGroupBD02A,
       "frameRelayIsdnCapabilities": frameRelayIsdnCapabilities,
       "frameRelayIsdnCapabilitiesBD": frameRelayIsdnCapabilitiesBD,
       "frameRelayIsdnCapabilitiesBD02": frameRelayIsdnCapabilitiesBD02,
       "frameRelayIsdnCapabilitiesBD02A": frameRelayIsdnCapabilitiesBD02A}
)
