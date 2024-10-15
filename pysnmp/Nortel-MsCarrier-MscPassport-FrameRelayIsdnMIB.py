# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayIsdnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayIsdnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:27 2024
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

(mscFrUni,
 mscFrUniIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB",
    "mscFrUni",
    "mscFrUniIndex")

(Counter32,
 DisplayString,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(DigitString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "DigitString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscFrUniIsdn_ObjectIdentity = ObjectIdentity
mscFrUniIsdn = _MscFrUniIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100)
)
_MscFrUniIsdnRowStatusTable_Object = MibTable
mscFrUniIsdnRowStatusTable = _MscFrUniIsdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 1)
)
if mibBuilder.loadTexts:
    mscFrUniIsdnRowStatusTable.setStatus("mandatory")
_MscFrUniIsdnRowStatusEntry_Object = MibTableRow
mscFrUniIsdnRowStatusEntry = _MscFrUniIsdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 1, 1)
)
mscFrUniIsdnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayIsdnMIB", "mscFrUniIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniIsdnRowStatusEntry.setStatus("mandatory")
_MscFrUniIsdnRowStatus_Type = RowStatus
_MscFrUniIsdnRowStatus_Object = MibTableColumn
mscFrUniIsdnRowStatus = _MscFrUniIsdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 1, 1, 1),
    _MscFrUniIsdnRowStatus_Type()
)
mscFrUniIsdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniIsdnRowStatus.setStatus("mandatory")
_MscFrUniIsdnComponentName_Type = DisplayString
_MscFrUniIsdnComponentName_Object = MibTableColumn
mscFrUniIsdnComponentName = _MscFrUniIsdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 1, 1, 2),
    _MscFrUniIsdnComponentName_Type()
)
mscFrUniIsdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIsdnComponentName.setStatus("mandatory")
_MscFrUniIsdnStorageType_Type = StorageType
_MscFrUniIsdnStorageType_Object = MibTableColumn
mscFrUniIsdnStorageType = _MscFrUniIsdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 1, 1, 4),
    _MscFrUniIsdnStorageType_Type()
)
mscFrUniIsdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIsdnStorageType.setStatus("mandatory")
_MscFrUniIsdnIndex_Type = NonReplicated
_MscFrUniIsdnIndex_Object = MibTableColumn
mscFrUniIsdnIndex = _MscFrUniIsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 1, 1, 10),
    _MscFrUniIsdnIndex_Type()
)
mscFrUniIsdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniIsdnIndex.setStatus("mandatory")
_MscFrUniIsdnProvTable_Object = MibTable
mscFrUniIsdnProvTable = _MscFrUniIsdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 11)
)
if mibBuilder.loadTexts:
    mscFrUniIsdnProvTable.setStatus("mandatory")
_MscFrUniIsdnProvEntry_Object = MibTableRow
mscFrUniIsdnProvEntry = _MscFrUniIsdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 11, 1)
)
mscFrUniIsdnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayIsdnMIB", "mscFrUniIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniIsdnProvEntry.setStatus("mandatory")


class _MscFrUniIsdnT320_Type(Unsigned32):
    """Custom type mscFrUniIsdnT320 based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniIsdnT320_Type.__name__ = "Unsigned32"
_MscFrUniIsdnT320_Object = MibTableColumn
mscFrUniIsdnT320 = _MscFrUniIsdnT320_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 11, 1, 1),
    _MscFrUniIsdnT320_Type()
)
mscFrUniIsdnT320.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniIsdnT320.setStatus("mandatory")


class _MscFrUniIsdnAddressSignalling_Type(Integer32):
    """Custom type mscFrUniIsdnAddressSignalling based on Integer32"""
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


_MscFrUniIsdnAddressSignalling_Type.__name__ = "Integer32"
_MscFrUniIsdnAddressSignalling_Object = MibTableColumn
mscFrUniIsdnAddressSignalling = _MscFrUniIsdnAddressSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 11, 1, 2),
    _MscFrUniIsdnAddressSignalling_Type()
)
mscFrUniIsdnAddressSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniIsdnAddressSignalling.setStatus("mandatory")
_MscFrUniIsdnOperTable_Object = MibTable
mscFrUniIsdnOperTable = _MscFrUniIsdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 12)
)
if mibBuilder.loadTexts:
    mscFrUniIsdnOperTable.setStatus("mandatory")
_MscFrUniIsdnOperEntry_Object = MibTableRow
mscFrUniIsdnOperEntry = _MscFrUniIsdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 12, 1)
)
mscFrUniIsdnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayIsdnMIB", "mscFrUniIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniIsdnOperEntry.setStatus("mandatory")


class _MscFrUniIsdnDataSigChan_Type(Integer32):
    """Custom type mscFrUniIsdnDataSigChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniIsdnDataSigChan_Type.__name__ = "Integer32"
_MscFrUniIsdnDataSigChan_Object = MibTableColumn
mscFrUniIsdnDataSigChan = _MscFrUniIsdnDataSigChan_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 12, 1, 1),
    _MscFrUniIsdnDataSigChan_Type()
)
mscFrUniIsdnDataSigChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIsdnDataSigChan.setStatus("mandatory")


class _MscFrUniIsdnBChannelState_Type(Integer32):
    """Custom type mscFrUniIsdnBChannelState based on Integer32"""
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


_MscFrUniIsdnBChannelState_Type.__name__ = "Integer32"
_MscFrUniIsdnBChannelState_Object = MibTableColumn
mscFrUniIsdnBChannelState = _MscFrUniIsdnBChannelState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 12, 1, 2),
    _MscFrUniIsdnBChannelState_Type()
)
mscFrUniIsdnBChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIsdnBChannelState.setStatus("mandatory")


class _MscFrUniIsdnLastUsedCgpn_Type(DigitString):
    """Custom type mscFrUniIsdnLastUsedCgpn based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscFrUniIsdnLastUsedCgpn_Type.__name__ = "DigitString"
_MscFrUniIsdnLastUsedCgpn_Object = MibTableColumn
mscFrUniIsdnLastUsedCgpn = _MscFrUniIsdnLastUsedCgpn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 12, 1, 3),
    _MscFrUniIsdnLastUsedCgpn_Type()
)
mscFrUniIsdnLastUsedCgpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIsdnLastUsedCgpn.setStatus("mandatory")


class _MscFrUniIsdnBChanIntState_Type(Integer32):
    """Custom type mscFrUniIsdnBChanIntState based on Integer32"""
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


_MscFrUniIsdnBChanIntState_Type.__name__ = "Integer32"
_MscFrUniIsdnBChanIntState_Object = MibTableColumn
mscFrUniIsdnBChanIntState = _MscFrUniIsdnBChanIntState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 12, 1, 4),
    _MscFrUniIsdnBChanIntState_Type()
)
mscFrUniIsdnBChanIntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIsdnBChanIntState.setStatus("mandatory")
_MscFrUniIsdnActiveVirtualCircuitsCount_Type = Counter32
_MscFrUniIsdnActiveVirtualCircuitsCount_Object = MibTableColumn
mscFrUniIsdnActiveVirtualCircuitsCount = _MscFrUniIsdnActiveVirtualCircuitsCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 100, 12, 1, 5),
    _MscFrUniIsdnActiveVirtualCircuitsCount_Type()
)
mscFrUniIsdnActiveVirtualCircuitsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIsdnActiveVirtualCircuitsCount.setStatus("mandatory")
_FrameRelayIsdnMIB_ObjectIdentity = ObjectIdentity
frameRelayIsdnMIB = _FrameRelayIsdnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122)
)
_FrameRelayIsdnGroup_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroup = _FrameRelayIsdnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 1)
)
_FrameRelayIsdnGroupCA_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroupCA = _FrameRelayIsdnGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 1, 1)
)
_FrameRelayIsdnGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroupCA02 = _FrameRelayIsdnGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 1, 1, 3)
)
_FrameRelayIsdnGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayIsdnGroupCA02A = _FrameRelayIsdnGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 1, 1, 3, 2)
)
_FrameRelayIsdnCapabilities_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilities = _FrameRelayIsdnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 3)
)
_FrameRelayIsdnCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilitiesCA = _FrameRelayIsdnCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 3, 1)
)
_FrameRelayIsdnCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilitiesCA02 = _FrameRelayIsdnCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 3, 1, 3)
)
_FrameRelayIsdnCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayIsdnCapabilitiesCA02A = _FrameRelayIsdnCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 122, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayIsdnMIB",
    **{"mscFrUniIsdn": mscFrUniIsdn,
       "mscFrUniIsdnRowStatusTable": mscFrUniIsdnRowStatusTable,
       "mscFrUniIsdnRowStatusEntry": mscFrUniIsdnRowStatusEntry,
       "mscFrUniIsdnRowStatus": mscFrUniIsdnRowStatus,
       "mscFrUniIsdnComponentName": mscFrUniIsdnComponentName,
       "mscFrUniIsdnStorageType": mscFrUniIsdnStorageType,
       "mscFrUniIsdnIndex": mscFrUniIsdnIndex,
       "mscFrUniIsdnProvTable": mscFrUniIsdnProvTable,
       "mscFrUniIsdnProvEntry": mscFrUniIsdnProvEntry,
       "mscFrUniIsdnT320": mscFrUniIsdnT320,
       "mscFrUniIsdnAddressSignalling": mscFrUniIsdnAddressSignalling,
       "mscFrUniIsdnOperTable": mscFrUniIsdnOperTable,
       "mscFrUniIsdnOperEntry": mscFrUniIsdnOperEntry,
       "mscFrUniIsdnDataSigChan": mscFrUniIsdnDataSigChan,
       "mscFrUniIsdnBChannelState": mscFrUniIsdnBChannelState,
       "mscFrUniIsdnLastUsedCgpn": mscFrUniIsdnLastUsedCgpn,
       "mscFrUniIsdnBChanIntState": mscFrUniIsdnBChanIntState,
       "mscFrUniIsdnActiveVirtualCircuitsCount": mscFrUniIsdnActiveVirtualCircuitsCount,
       "frameRelayIsdnMIB": frameRelayIsdnMIB,
       "frameRelayIsdnGroup": frameRelayIsdnGroup,
       "frameRelayIsdnGroupCA": frameRelayIsdnGroupCA,
       "frameRelayIsdnGroupCA02": frameRelayIsdnGroupCA02,
       "frameRelayIsdnGroupCA02A": frameRelayIsdnGroupCA02A,
       "frameRelayIsdnCapabilities": frameRelayIsdnCapabilities,
       "frameRelayIsdnCapabilitiesCA": frameRelayIsdnCapabilitiesCA,
       "frameRelayIsdnCapabilitiesCA02": frameRelayIsdnCapabilitiesCA02,
       "frameRelayIsdnCapabilitiesCA02A": frameRelayIsdnCapabilitiesCA02A}
)
