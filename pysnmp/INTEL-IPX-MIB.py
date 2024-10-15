# SNMP MIB module (INTEL-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:49 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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



class FltDirection(Integer32):
    """Custom type FltDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )





class IpxAddr(OctetString):
    """Custom type IpxAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )





class FltAction(Integer32):
    """Custom type FltAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("discard", 2),
          ("pass", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 22)
)
_IpxControl_ObjectIdentity = ObjectIdentity
ipxControl = _IpxControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 1)
)


class _IpxControlCommand_Type(Integer32):
    """Custom type ipxControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushRipSap", 1),
          ("updateRipSap", 2))
    )


_IpxControlCommand_Type.__name__ = "Integer32"
_IpxControlCommand_Object = MibScalar
ipxControlCommand = _IpxControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 1, 1),
    _IpxControlCommand_Type()
)
ipxControlCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ipxControlCommand.setStatus("mandatory")
_IpxConf_ObjectIdentity = ObjectIdentity
ipxConf = _IpxConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2)
)
_IpxLinkConfTable_Object = MibTable
ipxLinkConfTable = _IpxLinkConfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1)
)
if mibBuilder.loadTexts:
    ipxLinkConfTable.setStatus("mandatory")
_IpxLinkConfEntry_Object = MibTableRow
ipxLinkConfEntry = _IpxLinkConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1)
)
ipxLinkConfEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxLinkConfIpxLinkIndex"),
)
if mibBuilder.loadTexts:
    ipxLinkConfEntry.setStatus("mandatory")
_IpxLinkConfIpxLinkIndex_Type = Integer32
_IpxLinkConfIpxLinkIndex_Object = MibTableColumn
ipxLinkConfIpxLinkIndex = _IpxLinkConfIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 1),
    _IpxLinkConfIpxLinkIndex_Type()
)
ipxLinkConfIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkConfIpxLinkIndex.setStatus("mandatory")


class _IpxLinkConfRoutingProtocol_Type(Integer32):
    """Custom type ipxLinkConfRoutingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripAndSap", 1),
          ("staticOrNone", 2))
    )


_IpxLinkConfRoutingProtocol_Type.__name__ = "Integer32"
_IpxLinkConfRoutingProtocol_Object = MibTableColumn
ipxLinkConfRoutingProtocol = _IpxLinkConfRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 2),
    _IpxLinkConfRoutingProtocol_Type()
)
ipxLinkConfRoutingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfRoutingProtocol.setStatus("mandatory")


class _IpxLinkConfNumbered_Type(Integer32):
    """Custom type ipxLinkConfNumbered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxLinkConfNumbered_Type.__name__ = "Integer32"
_IpxLinkConfNumbered_Object = MibTableColumn
ipxLinkConfNumbered = _IpxLinkConfNumbered_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 3),
    _IpxLinkConfNumbered_Type()
)
ipxLinkConfNumbered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfNumbered.setStatus("mandatory")


class _IpxLinkConfNet_Type(OctetString):
    """Custom type ipxLinkConfNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxLinkConfNet_Type.__name__ = "OctetString"
_IpxLinkConfNet_Object = MibTableColumn
ipxLinkConfNet = _IpxLinkConfNet_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 4),
    _IpxLinkConfNet_Type()
)
ipxLinkConfNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfNet.setStatus("mandatory")


class _IpxLinkConfFrameType_Type(Integer32):
    """Custom type ipxLinkConfFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ieee8022", 2),
          ("ieee8023", 5),
          ("snap", 4),
          ("type", 1),
          ("wan", 16))
    )


_IpxLinkConfFrameType_Type.__name__ = "Integer32"
_IpxLinkConfFrameType_Object = MibTableColumn
ipxLinkConfFrameType = _IpxLinkConfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 5),
    _IpxLinkConfFrameType_Type()
)
ipxLinkConfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfFrameType.setStatus("mandatory")


class _IpxLinkConfFrameParam_Type(OctetString):
    """Custom type ipxLinkConfFrameParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IpxLinkConfFrameParam_Type.__name__ = "OctetString"
_IpxLinkConfFrameParam_Object = MibTableColumn
ipxLinkConfFrameParam = _IpxLinkConfFrameParam_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 6),
    _IpxLinkConfFrameParam_Type()
)
ipxLinkConfFrameParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkConfFrameParam.setStatus("mandatory")


class _IpxLinkConfIpxWanNegotiation_Type(Integer32):
    """Custom type ipxLinkConfIpxWanNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxLinkConfIpxWanNegotiation_Type.__name__ = "Integer32"
_IpxLinkConfIpxWanNegotiation_Object = MibTableColumn
ipxLinkConfIpxWanNegotiation = _IpxLinkConfIpxWanNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 7),
    _IpxLinkConfIpxWanNegotiation_Type()
)
ipxLinkConfIpxWanNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfIpxWanNegotiation.setStatus("mandatory")
_IpxLinkConfRipUpdateInterval_Type = Integer32
_IpxLinkConfRipUpdateInterval_Object = MibTableColumn
ipxLinkConfRipUpdateInterval = _IpxLinkConfRipUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 8),
    _IpxLinkConfRipUpdateInterval_Type()
)
ipxLinkConfRipUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfRipUpdateInterval.setStatus("mandatory")


class _IpxLinkConfRipTrigger_Type(Integer32):
    """Custom type ipxLinkConfRipTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxLinkConfRipTrigger_Type.__name__ = "Integer32"
_IpxLinkConfRipTrigger_Object = MibTableColumn
ipxLinkConfRipTrigger = _IpxLinkConfRipTrigger_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 9),
    _IpxLinkConfRipTrigger_Type()
)
ipxLinkConfRipTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfRipTrigger.setStatus("mandatory")
_IpxLinkConfSapUpdateInterval_Type = Integer32
_IpxLinkConfSapUpdateInterval_Object = MibTableColumn
ipxLinkConfSapUpdateInterval = _IpxLinkConfSapUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 10),
    _IpxLinkConfSapUpdateInterval_Type()
)
ipxLinkConfSapUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfSapUpdateInterval.setStatus("mandatory")


class _IpxLinkConfSapTrigger_Type(Integer32):
    """Custom type ipxLinkConfSapTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxLinkConfSapTrigger_Type.__name__ = "Integer32"
_IpxLinkConfSapTrigger_Object = MibTableColumn
ipxLinkConfSapTrigger = _IpxLinkConfSapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 11),
    _IpxLinkConfSapTrigger_Type()
)
ipxLinkConfSapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfSapTrigger.setStatus("mandatory")


class _IpxLinkConfAutomaticDelay_Type(Integer32):
    """Custom type ipxLinkConfAutomaticDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxLinkConfAutomaticDelay_Type.__name__ = "Integer32"
_IpxLinkConfAutomaticDelay_Object = MibTableColumn
ipxLinkConfAutomaticDelay = _IpxLinkConfAutomaticDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 12),
    _IpxLinkConfAutomaticDelay_Type()
)
ipxLinkConfAutomaticDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfAutomaticDelay.setStatus("mandatory")
_IpxLinkConfDelay_Type = Integer32
_IpxLinkConfDelay_Object = MibTableColumn
ipxLinkConfDelay = _IpxLinkConfDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 13),
    _IpxLinkConfDelay_Type()
)
ipxLinkConfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfDelay.setStatus("mandatory")


class _IpxLinkConfSpxSpoofing_Type(Integer32):
    """Custom type ipxLinkConfSpxSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxLinkConfSpxSpoofing_Type.__name__ = "Integer32"
_IpxLinkConfSpxSpoofing_Object = MibTableColumn
ipxLinkConfSpxSpoofing = _IpxLinkConfSpxSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 14),
    _IpxLinkConfSpxSpoofing_Type()
)
ipxLinkConfSpxSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfSpxSpoofing.setStatus("mandatory")
_IpxLinkConfSpxSessionTimeout_Type = Integer32
_IpxLinkConfSpxSessionTimeout_Object = MibTableColumn
ipxLinkConfSpxSessionTimeout = _IpxLinkConfSpxSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 15),
    _IpxLinkConfSpxSessionTimeout_Type()
)
ipxLinkConfSpxSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfSpxSessionTimeout.setStatus("mandatory")


class _IpxLinkConfType20Broadcast_Type(Integer32):
    """Custom type ipxLinkConfType20Broadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxLinkConfType20Broadcast_Type.__name__ = "Integer32"
_IpxLinkConfType20Broadcast_Object = MibTableColumn
ipxLinkConfType20Broadcast = _IpxLinkConfType20Broadcast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 16),
    _IpxLinkConfType20Broadcast_Type()
)
ipxLinkConfType20Broadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfType20Broadcast.setStatus("mandatory")


class _IpxLinkConfWatchdogSpoofing_Type(Integer32):
    """Custom type ipxLinkConfWatchdogSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxLinkConfWatchdogSpoofing_Type.__name__ = "Integer32"
_IpxLinkConfWatchdogSpoofing_Object = MibTableColumn
ipxLinkConfWatchdogSpoofing = _IpxLinkConfWatchdogSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 17),
    _IpxLinkConfWatchdogSpoofing_Type()
)
ipxLinkConfWatchdogSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfWatchdogSpoofing.setStatus("mandatory")
_IpxLinkConfRipFltRxDefaultAction_Type = FltAction
_IpxLinkConfRipFltRxDefaultAction_Object = MibTableColumn
ipxLinkConfRipFltRxDefaultAction = _IpxLinkConfRipFltRxDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 18),
    _IpxLinkConfRipFltRxDefaultAction_Type()
)
ipxLinkConfRipFltRxDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfRipFltRxDefaultAction.setStatus("mandatory")
_IpxLinkConfRipFltTxDefaultAction_Type = FltAction
_IpxLinkConfRipFltTxDefaultAction_Object = MibTableColumn
ipxLinkConfRipFltTxDefaultAction = _IpxLinkConfRipFltTxDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 19),
    _IpxLinkConfRipFltTxDefaultAction_Type()
)
ipxLinkConfRipFltTxDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfRipFltTxDefaultAction.setStatus("mandatory")
_IpxLinkConfSapFltRxDefaultAction_Type = FltAction
_IpxLinkConfSapFltRxDefaultAction_Object = MibTableColumn
ipxLinkConfSapFltRxDefaultAction = _IpxLinkConfSapFltRxDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 20),
    _IpxLinkConfSapFltRxDefaultAction_Type()
)
ipxLinkConfSapFltRxDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfSapFltRxDefaultAction.setStatus("mandatory")
_IpxLinkConfSapFltTxDefaultAction_Type = FltAction
_IpxLinkConfSapFltTxDefaultAction_Object = MibTableColumn
ipxLinkConfSapFltTxDefaultAction = _IpxLinkConfSapFltTxDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 21),
    _IpxLinkConfSapFltTxDefaultAction_Type()
)
ipxLinkConfSapFltTxDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfSapFltTxDefaultAction.setStatus("mandatory")
_IpxLinkConfDataFltRxDefaultAction_Type = FltAction
_IpxLinkConfDataFltRxDefaultAction_Object = MibTableColumn
ipxLinkConfDataFltRxDefaultAction = _IpxLinkConfDataFltRxDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 22),
    _IpxLinkConfDataFltRxDefaultAction_Type()
)
ipxLinkConfDataFltRxDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfDataFltRxDefaultAction.setStatus("mandatory")
_IpxLinkConfDataFltTxDefaultAction_Type = FltAction
_IpxLinkConfDataFltTxDefaultAction_Object = MibTableColumn
ipxLinkConfDataFltTxDefaultAction = _IpxLinkConfDataFltTxDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 23),
    _IpxLinkConfDataFltTxDefaultAction_Type()
)
ipxLinkConfDataFltTxDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfDataFltTxDefaultAction.setStatus("mandatory")


class _IpxLinkConfDataFilters_Type(Integer32):
    """Custom type ipxLinkConfDataFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxLinkConfDataFilters_Type.__name__ = "Integer32"
_IpxLinkConfDataFilters_Object = MibTableColumn
ipxLinkConfDataFilters = _IpxLinkConfDataFilters_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 24),
    _IpxLinkConfDataFilters_Type()
)
ipxLinkConfDataFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfDataFilters.setStatus("mandatory")


class _IpxLinkConfCreateObj_Type(OctetString):
    """Custom type ipxLinkConfCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(34, 34),
    )


_IpxLinkConfCreateObj_Type.__name__ = "OctetString"
_IpxLinkConfCreateObj_Object = MibTableColumn
ipxLinkConfCreateObj = _IpxLinkConfCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 25),
    _IpxLinkConfCreateObj_Type()
)
ipxLinkConfCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfCreateObj.setStatus("mandatory")


class _IpxLinkConfDeleteObj_Type(Integer32):
    """Custom type ipxLinkConfDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_IpxLinkConfDeleteObj_Type.__name__ = "Integer32"
_IpxLinkConfDeleteObj_Object = MibTableColumn
ipxLinkConfDeleteObj = _IpxLinkConfDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 1, 1, 26),
    _IpxLinkConfDeleteObj_Type()
)
ipxLinkConfDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkConfDeleteObj.setStatus("mandatory")
_IpxRipFltTable_Object = MibTable
ipxRipFltTable = _IpxRipFltTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2)
)
if mibBuilder.loadTexts:
    ipxRipFltTable.setStatus("mandatory")
_IpxRipFltEntry_Object = MibTableRow
ipxRipFltEntry = _IpxRipFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2, 1)
)
ipxRipFltEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxRipFltIpxLinkIndex"),
    (0, "INTEL-IPX-MIB", "ipxRipFltDirection"),
    (0, "INTEL-IPX-MIB", "ipxRipFltNumber"),
)
if mibBuilder.loadTexts:
    ipxRipFltEntry.setStatus("mandatory")
_IpxRipFltIpxLinkIndex_Type = Integer32
_IpxRipFltIpxLinkIndex_Object = MibTableColumn
ipxRipFltIpxLinkIndex = _IpxRipFltIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2, 1, 1),
    _IpxRipFltIpxLinkIndex_Type()
)
ipxRipFltIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipFltIpxLinkIndex.setStatus("mandatory")
_IpxRipFltDirection_Type = FltDirection
_IpxRipFltDirection_Object = MibTableColumn
ipxRipFltDirection = _IpxRipFltDirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2, 1, 2),
    _IpxRipFltDirection_Type()
)
ipxRipFltDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipFltDirection.setStatus("mandatory")
_IpxRipFltNumber_Type = Integer32
_IpxRipFltNumber_Object = MibTableColumn
ipxRipFltNumber = _IpxRipFltNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2, 1, 3),
    _IpxRipFltNumber_Type()
)
ipxRipFltNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipFltNumber.setStatus("mandatory")
_IpxRipFltAction_Type = FltAction
_IpxRipFltAction_Object = MibTableColumn
ipxRipFltAction = _IpxRipFltAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2, 1, 4),
    _IpxRipFltAction_Type()
)
ipxRipFltAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipFltAction.setStatus("mandatory")


class _IpxRipFltNetworkAddress_Type(OctetString):
    """Custom type ipxRipFltNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRipFltNetworkAddress_Type.__name__ = "OctetString"
_IpxRipFltNetworkAddress_Object = MibTableColumn
ipxRipFltNetworkAddress = _IpxRipFltNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2, 1, 5),
    _IpxRipFltNetworkAddress_Type()
)
ipxRipFltNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipFltNetworkAddress.setStatus("mandatory")


class _IpxRipFltNetworkMask_Type(OctetString):
    """Custom type ipxRipFltNetworkMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRipFltNetworkMask_Type.__name__ = "OctetString"
_IpxRipFltNetworkMask_Object = MibTableColumn
ipxRipFltNetworkMask = _IpxRipFltNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 2, 1, 6),
    _IpxRipFltNetworkMask_Type()
)
ipxRipFltNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipFltNetworkMask.setStatus("mandatory")
_IpxSapFltTable_Object = MibTable
ipxSapFltTable = _IpxSapFltTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3)
)
if mibBuilder.loadTexts:
    ipxSapFltTable.setStatus("mandatory")
_IpxSapFltEntry_Object = MibTableRow
ipxSapFltEntry = _IpxSapFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1)
)
ipxSapFltEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxSapFltIpxLinkIndex"),
    (0, "INTEL-IPX-MIB", "ipxSapFltDirection"),
    (0, "INTEL-IPX-MIB", "ipxSapFltNumber"),
)
if mibBuilder.loadTexts:
    ipxSapFltEntry.setStatus("mandatory")
_IpxSapFltIpxLinkIndex_Type = Integer32
_IpxSapFltIpxLinkIndex_Object = MibTableColumn
ipxSapFltIpxLinkIndex = _IpxSapFltIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 1),
    _IpxSapFltIpxLinkIndex_Type()
)
ipxSapFltIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltIpxLinkIndex.setStatus("mandatory")
_IpxSapFltDirection_Type = FltDirection
_IpxSapFltDirection_Object = MibTableColumn
ipxSapFltDirection = _IpxSapFltDirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 2),
    _IpxSapFltDirection_Type()
)
ipxSapFltDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltDirection.setStatus("mandatory")
_IpxSapFltNumber_Type = Integer32
_IpxSapFltNumber_Object = MibTableColumn
ipxSapFltNumber = _IpxSapFltNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 3),
    _IpxSapFltNumber_Type()
)
ipxSapFltNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltNumber.setStatus("mandatory")
_IpxSapFltAction_Type = FltAction
_IpxSapFltAction_Object = MibTableColumn
ipxSapFltAction = _IpxSapFltAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 4),
    _IpxSapFltAction_Type()
)
ipxSapFltAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltAction.setStatus("mandatory")


class _IpxSapFltNetworkAddress_Type(OctetString):
    """Custom type ipxSapFltNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxSapFltNetworkAddress_Type.__name__ = "OctetString"
_IpxSapFltNetworkAddress_Object = MibTableColumn
ipxSapFltNetworkAddress = _IpxSapFltNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 5),
    _IpxSapFltNetworkAddress_Type()
)
ipxSapFltNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltNetworkAddress.setStatus("mandatory")


class _IpxSapFltNetworkMask_Type(OctetString):
    """Custom type ipxSapFltNetworkMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxSapFltNetworkMask_Type.__name__ = "OctetString"
_IpxSapFltNetworkMask_Object = MibTableColumn
ipxSapFltNetworkMask = _IpxSapFltNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 6),
    _IpxSapFltNetworkMask_Type()
)
ipxSapFltNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltNetworkMask.setStatus("mandatory")


class _IpxSapFltNodeAddress_Type(OctetString):
    """Custom type ipxSapFltNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxSapFltNodeAddress_Type.__name__ = "OctetString"
_IpxSapFltNodeAddress_Object = MibTableColumn
ipxSapFltNodeAddress = _IpxSapFltNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 7),
    _IpxSapFltNodeAddress_Type()
)
ipxSapFltNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltNodeAddress.setStatus("mandatory")
_IpxSapFltServiceType_Type = Integer32
_IpxSapFltServiceType_Object = MibTableColumn
ipxSapFltServiceType = _IpxSapFltServiceType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 8),
    _IpxSapFltServiceType_Type()
)
ipxSapFltServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltServiceType.setStatus("mandatory")


class _IpxSapFltServerName_Type(OctetString):
    """Custom type ipxSapFltServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_IpxSapFltServerName_Type.__name__ = "OctetString"
_IpxSapFltServerName_Object = MibTableColumn
ipxSapFltServerName = _IpxSapFltServerName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 3, 1, 9),
    _IpxSapFltServerName_Type()
)
ipxSapFltServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFltServerName.setStatus("mandatory")
_IpxDataFltTable_Object = MibTable
ipxDataFltTable = _IpxDataFltTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4)
)
if mibBuilder.loadTexts:
    ipxDataFltTable.setStatus("mandatory")
_IpxDataFltEntry_Object = MibTableRow
ipxDataFltEntry = _IpxDataFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1)
)
ipxDataFltEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxDataFltIpxLinkIndex"),
    (0, "INTEL-IPX-MIB", "ipxDataFltDirection"),
    (0, "INTEL-IPX-MIB", "ipxDataFltNumber"),
)
if mibBuilder.loadTexts:
    ipxDataFltEntry.setStatus("mandatory")
_IpxDataFltIpxLinkIndex_Type = Integer32
_IpxDataFltIpxLinkIndex_Object = MibTableColumn
ipxDataFltIpxLinkIndex = _IpxDataFltIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 1),
    _IpxDataFltIpxLinkIndex_Type()
)
ipxDataFltIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltIpxLinkIndex.setStatus("mandatory")
_IpxDataFltDirection_Type = FltDirection
_IpxDataFltDirection_Object = MibTableColumn
ipxDataFltDirection = _IpxDataFltDirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 2),
    _IpxDataFltDirection_Type()
)
ipxDataFltDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltDirection.setStatus("mandatory")
_IpxDataFltNumber_Type = Integer32
_IpxDataFltNumber_Object = MibTableColumn
ipxDataFltNumber = _IpxDataFltNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 3),
    _IpxDataFltNumber_Type()
)
ipxDataFltNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltNumber.setStatus("mandatory")
_IpxDataFltAction_Type = FltAction
_IpxDataFltAction_Object = MibTableColumn
ipxDataFltAction = _IpxDataFltAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 4),
    _IpxDataFltAction_Type()
)
ipxDataFltAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltAction.setStatus("mandatory")


class _IpxDataFltDstNetworkAddress_Type(OctetString):
    """Custom type ipxDataFltDstNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxDataFltDstNetworkAddress_Type.__name__ = "OctetString"
_IpxDataFltDstNetworkAddress_Object = MibTableColumn
ipxDataFltDstNetworkAddress = _IpxDataFltDstNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 5),
    _IpxDataFltDstNetworkAddress_Type()
)
ipxDataFltDstNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltDstNetworkAddress.setStatus("mandatory")


class _IpxDataFltDstNetworkMask_Type(OctetString):
    """Custom type ipxDataFltDstNetworkMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxDataFltDstNetworkMask_Type.__name__ = "OctetString"
_IpxDataFltDstNetworkMask_Object = MibTableColumn
ipxDataFltDstNetworkMask = _IpxDataFltDstNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 6),
    _IpxDataFltDstNetworkMask_Type()
)
ipxDataFltDstNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltDstNetworkMask.setStatus("mandatory")


class _IpxDataFltDstNodeAddress_Type(OctetString):
    """Custom type ipxDataFltDstNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxDataFltDstNodeAddress_Type.__name__ = "OctetString"
_IpxDataFltDstNodeAddress_Object = MibTableColumn
ipxDataFltDstNodeAddress = _IpxDataFltDstNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 7),
    _IpxDataFltDstNodeAddress_Type()
)
ipxDataFltDstNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltDstNodeAddress.setStatus("mandatory")


class _IpxDataFltDstSocketFilter_Type(Integer32):
    """Custom type ipxDataFltDstSocketFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxDataFltDstSocketFilter_Type.__name__ = "Integer32"
_IpxDataFltDstSocketFilter_Object = MibTableColumn
ipxDataFltDstSocketFilter = _IpxDataFltDstSocketFilter_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 8),
    _IpxDataFltDstSocketFilter_Type()
)
ipxDataFltDstSocketFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltDstSocketFilter.setStatus("mandatory")
_IpxDataFltDstSocket_Type = Integer32
_IpxDataFltDstSocket_Object = MibTableColumn
ipxDataFltDstSocket = _IpxDataFltDstSocket_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 9),
    _IpxDataFltDstSocket_Type()
)
ipxDataFltDstSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltDstSocket.setStatus("mandatory")


class _IpxDataFltSrcNetworkAddress_Type(OctetString):
    """Custom type ipxDataFltSrcNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxDataFltSrcNetworkAddress_Type.__name__ = "OctetString"
_IpxDataFltSrcNetworkAddress_Object = MibTableColumn
ipxDataFltSrcNetworkAddress = _IpxDataFltSrcNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 10),
    _IpxDataFltSrcNetworkAddress_Type()
)
ipxDataFltSrcNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltSrcNetworkAddress.setStatus("mandatory")


class _IpxDataFltSrcNetworkMask_Type(OctetString):
    """Custom type ipxDataFltSrcNetworkMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxDataFltSrcNetworkMask_Type.__name__ = "OctetString"
_IpxDataFltSrcNetworkMask_Object = MibTableColumn
ipxDataFltSrcNetworkMask = _IpxDataFltSrcNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 11),
    _IpxDataFltSrcNetworkMask_Type()
)
ipxDataFltSrcNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltSrcNetworkMask.setStatus("mandatory")


class _IpxDataFltSrcNodeAddress_Type(OctetString):
    """Custom type ipxDataFltSrcNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxDataFltSrcNodeAddress_Type.__name__ = "OctetString"
_IpxDataFltSrcNodeAddress_Object = MibTableColumn
ipxDataFltSrcNodeAddress = _IpxDataFltSrcNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 12),
    _IpxDataFltSrcNodeAddress_Type()
)
ipxDataFltSrcNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltSrcNodeAddress.setStatus("mandatory")


class _IpxDataFltSrcSocketFilter_Type(Integer32):
    """Custom type ipxDataFltSrcSocketFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxDataFltSrcSocketFilter_Type.__name__ = "Integer32"
_IpxDataFltSrcSocketFilter_Object = MibTableColumn
ipxDataFltSrcSocketFilter = _IpxDataFltSrcSocketFilter_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 13),
    _IpxDataFltSrcSocketFilter_Type()
)
ipxDataFltSrcSocketFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltSrcSocketFilter.setStatus("mandatory")
_IpxDataFltSrcSocket_Type = Integer32
_IpxDataFltSrcSocket_Object = MibTableColumn
ipxDataFltSrcSocket = _IpxDataFltSrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 14),
    _IpxDataFltSrcSocket_Type()
)
ipxDataFltSrcSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltSrcSocket.setStatus("mandatory")


class _IpxDataFltPacketTypeFilter_Type(Integer32):
    """Custom type ipxDataFltPacketTypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxDataFltPacketTypeFilter_Type.__name__ = "Integer32"
_IpxDataFltPacketTypeFilter_Object = MibTableColumn
ipxDataFltPacketTypeFilter = _IpxDataFltPacketTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 15),
    _IpxDataFltPacketTypeFilter_Type()
)
ipxDataFltPacketTypeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltPacketTypeFilter.setStatus("mandatory")
_IpxDataFltPacketType_Type = Integer32
_IpxDataFltPacketType_Object = MibTableColumn
ipxDataFltPacketType = _IpxDataFltPacketType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 16),
    _IpxDataFltPacketType_Type()
)
ipxDataFltPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltPacketType.setStatus("mandatory")
_IpxDataFltHits_Type = Counter32
_IpxDataFltHits_Object = MibTableColumn
ipxDataFltHits = _IpxDataFltHits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 4, 1, 17),
    _IpxDataFltHits_Type()
)
ipxDataFltHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDataFltHits.setStatus("mandatory")


class _IpxConfAutoIntNetNumber_Type(Integer32):
    """Custom type ipxConfAutoIntNetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxConfAutoIntNetNumber_Type.__name__ = "Integer32"
_IpxConfAutoIntNetNumber_Object = MibScalar
ipxConfAutoIntNetNumber = _IpxConfAutoIntNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 5),
    _IpxConfAutoIntNetNumber_Type()
)
ipxConfAutoIntNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxConfAutoIntNetNumber.setStatus("mandatory")


class _IpxConfIntNetNumber_Type(OctetString):
    """Custom type ipxConfIntNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxConfIntNetNumber_Type.__name__ = "OctetString"
_IpxConfIntNetNumber_Object = MibScalar
ipxConfIntNetNumber = _IpxConfIntNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 2, 6),
    _IpxConfIntNetNumber_Type()
)
ipxConfIntNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxConfIntNetNumber.setStatus("mandatory")
_IpxStatus_ObjectIdentity = ObjectIdentity
ipxStatus = _IpxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3)
)
_IpxLinkMonTable_Object = MibTable
ipxLinkMonTable = _IpxLinkMonTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 1)
)
if mibBuilder.loadTexts:
    ipxLinkMonTable.setStatus("mandatory")
_IpxLinkMonEntry_Object = MibTableRow
ipxLinkMonEntry = _IpxLinkMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 1, 1)
)
ipxLinkMonEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxLinkMonIpxLinkIndex"),
)
if mibBuilder.loadTexts:
    ipxLinkMonEntry.setStatus("mandatory")
_IpxLinkMonIpxLinkIndex_Type = Counter32
_IpxLinkMonIpxLinkIndex_Object = MibTableColumn
ipxLinkMonIpxLinkIndex = _IpxLinkMonIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 1, 1, 1),
    _IpxLinkMonIpxLinkIndex_Type()
)
ipxLinkMonIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkMonIpxLinkIndex.setStatus("mandatory")
_IpxLinkMonIfIndex_Type = Integer32
_IpxLinkMonIfIndex_Object = MibTableColumn
ipxLinkMonIfIndex = _IpxLinkMonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 1, 1, 2),
    _IpxLinkMonIfIndex_Type()
)
ipxLinkMonIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkMonIfIndex.setStatus("mandatory")


class _IpxLinkMonState_Type(Integer32):
    """Custom type ipxLinkMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("negotiating", 3),
          ("up", 2))
    )


_IpxLinkMonState_Type.__name__ = "Integer32"
_IpxLinkMonState_Object = MibTableColumn
ipxLinkMonState = _IpxLinkMonState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 1, 1, 3),
    _IpxLinkMonState_Type()
)
ipxLinkMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkMonState.setStatus("mandatory")
_IpxLinkMonDelay_Type = Integer32
_IpxLinkMonDelay_Object = MibTableColumn
ipxLinkMonDelay = _IpxLinkMonDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 1, 1, 4),
    _IpxLinkMonDelay_Type()
)
ipxLinkMonDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkMonDelay.setStatus("mandatory")
_IpxLinkMonMtuSize_Type = Integer32
_IpxLinkMonMtuSize_Object = MibTableColumn
ipxLinkMonMtuSize = _IpxLinkMonMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 1, 1, 5),
    _IpxLinkMonMtuSize_Type()
)
ipxLinkMonMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkMonMtuSize.setStatus("mandatory")
_IpxStatusConfigTimeStamp_Type = TimeTicks
_IpxStatusConfigTimeStamp_Object = MibScalar
ipxStatusConfigTimeStamp = _IpxStatusConfigTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 2),
    _IpxStatusConfigTimeStamp_Type()
)
ipxStatusConfigTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStatusConfigTimeStamp.setStatus("mandatory")
_IpxStatusReachableNets_Type = Counter32
_IpxStatusReachableNets_Object = MibScalar
ipxStatusReachableNets = _IpxStatusReachableNets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 3),
    _IpxStatusReachableNets_Type()
)
ipxStatusReachableNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStatusReachableNets.setStatus("mandatory")
_IpxStatusDeadNets_Type = Counter32
_IpxStatusDeadNets_Object = MibScalar
ipxStatusDeadNets = _IpxStatusDeadNets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 4),
    _IpxStatusDeadNets_Type()
)
ipxStatusDeadNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStatusDeadNets.setStatus("mandatory")
_IpxStatusReachableServices_Type = Counter32
_IpxStatusReachableServices_Object = MibScalar
ipxStatusReachableServices = _IpxStatusReachableServices_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 5),
    _IpxStatusReachableServices_Type()
)
ipxStatusReachableServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStatusReachableServices.setStatus("mandatory")
_IpxStatusDeadServices_Type = Counter32
_IpxStatusDeadServices_Object = MibScalar
ipxStatusDeadServices = _IpxStatusDeadServices_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 6),
    _IpxStatusDeadServices_Type()
)
ipxStatusDeadServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStatusDeadServices.setStatus("mandatory")
_IpxStatusLinkTimeStamp_Type = TimeTicks
_IpxStatusLinkTimeStamp_Object = MibScalar
ipxStatusLinkTimeStamp = _IpxStatusLinkTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 3, 7),
    _IpxStatusLinkTimeStamp_Type()
)
ipxStatusLinkTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStatusLinkTimeStamp.setStatus("mandatory")
_IpxCount_ObjectIdentity = ObjectIdentity
ipxCount = _IpxCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4)
)
_IpxLinkCntTable_Object = MibTable
ipxLinkCntTable = _IpxLinkCntTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1)
)
if mibBuilder.loadTexts:
    ipxLinkCntTable.setStatus("mandatory")
_IpxLinkCntEntry_Object = MibTableRow
ipxLinkCntEntry = _IpxLinkCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1)
)
ipxLinkCntEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxLinkCntIpxLinkIndex"),
)
if mibBuilder.loadTexts:
    ipxLinkCntEntry.setStatus("mandatory")
_IpxLinkCntIpxLinkIndex_Type = Integer32
_IpxLinkCntIpxLinkIndex_Object = MibTableColumn
ipxLinkCntIpxLinkIndex = _IpxLinkCntIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 1),
    _IpxLinkCntIpxLinkIndex_Type()
)
ipxLinkCntIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntIpxLinkIndex.setStatus("mandatory")
_IpxLinkCntRxTotal_Type = Counter32
_IpxLinkCntRxTotal_Object = MibTableColumn
ipxLinkCntRxTotal = _IpxLinkCntRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 2),
    _IpxLinkCntRxTotal_Type()
)
ipxLinkCntRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxTotal.setStatus("mandatory")
_IpxLinkCntTxTotal_Type = Counter32
_IpxLinkCntTxTotal_Object = MibTableColumn
ipxLinkCntTxTotal = _IpxLinkCntTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 3),
    _IpxLinkCntTxTotal_Type()
)
ipxLinkCntTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxTotal.setStatus("mandatory")
_IpxLinkCntTxFailed_Type = Counter32
_IpxLinkCntTxFailed_Object = MibTableColumn
ipxLinkCntTxFailed = _IpxLinkCntTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 4),
    _IpxLinkCntTxFailed_Type()
)
ipxLinkCntTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxFailed.setStatus("mandatory")
_IpxLinkCntRxFiltered_Type = Counter32
_IpxLinkCntRxFiltered_Object = MibTableColumn
ipxLinkCntRxFiltered = _IpxLinkCntRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 5),
    _IpxLinkCntRxFiltered_Type()
)
ipxLinkCntRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxFiltered.setStatus("mandatory")
_IpxLinkCntTxFiltered_Type = Counter32
_IpxLinkCntTxFiltered_Object = MibTableColumn
ipxLinkCntTxFiltered = _IpxLinkCntTxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 6),
    _IpxLinkCntTxFiltered_Type()
)
ipxLinkCntTxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxFiltered.setStatus("mandatory")
_IpxLinkCntRxTooManyHops_Type = Counter32
_IpxLinkCntRxTooManyHops_Object = MibTableColumn
ipxLinkCntRxTooManyHops = _IpxLinkCntRxTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 7),
    _IpxLinkCntRxTooManyHops_Type()
)
ipxLinkCntRxTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxTooManyHops.setStatus("mandatory")
_IpxLinkCntRxHeaderErr_Type = Counter32
_IpxLinkCntRxHeaderErr_Object = MibTableColumn
ipxLinkCntRxHeaderErr = _IpxLinkCntRxHeaderErr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 8),
    _IpxLinkCntRxHeaderErr_Type()
)
ipxLinkCntRxHeaderErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxHeaderErr.setStatus("mandatory")
_IpxLinkCntRxSapReq_Type = Counter32
_IpxLinkCntRxSapReq_Object = MibTableColumn
ipxLinkCntRxSapReq = _IpxLinkCntRxSapReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 9),
    _IpxLinkCntRxSapReq_Type()
)
ipxLinkCntRxSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxSapReq.setStatus("mandatory")
_IpxLinkCntTxSapReq_Type = Counter32
_IpxLinkCntTxSapReq_Object = MibTableColumn
ipxLinkCntTxSapReq = _IpxLinkCntTxSapReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 10),
    _IpxLinkCntTxSapReq_Type()
)
ipxLinkCntTxSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxSapReq.setStatus("mandatory")
_IpxLinkCntRxSapResp_Type = Counter32
_IpxLinkCntRxSapResp_Object = MibTableColumn
ipxLinkCntRxSapResp = _IpxLinkCntRxSapResp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 11),
    _IpxLinkCntRxSapResp_Type()
)
ipxLinkCntRxSapResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxSapResp.setStatus("mandatory")
_IpxLinkCntTxSapReply_Type = Counter32
_IpxLinkCntTxSapReply_Object = MibTableColumn
ipxLinkCntTxSapReply = _IpxLinkCntTxSapReply_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 12),
    _IpxLinkCntTxSapReply_Type()
)
ipxLinkCntTxSapReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxSapReply.setStatus("mandatory")
_IpxLinkCntRxSapInvalid_Type = Counter32
_IpxLinkCntRxSapInvalid_Object = MibTableColumn
ipxLinkCntRxSapInvalid = _IpxLinkCntRxSapInvalid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 13),
    _IpxLinkCntRxSapInvalid_Type()
)
ipxLinkCntRxSapInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxSapInvalid.setStatus("mandatory")
_IpxLinkCntRxRipReq_Type = Counter32
_IpxLinkCntRxRipReq_Object = MibTableColumn
ipxLinkCntRxRipReq = _IpxLinkCntRxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 14),
    _IpxLinkCntRxRipReq_Type()
)
ipxLinkCntRxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxRipReq.setStatus("mandatory")
_IpxLinkCntTxRipReq_Type = Counter32
_IpxLinkCntTxRipReq_Object = MibTableColumn
ipxLinkCntTxRipReq = _IpxLinkCntTxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 15),
    _IpxLinkCntTxRipReq_Type()
)
ipxLinkCntTxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxRipReq.setStatus("mandatory")
_IpxLinkCntRxRipResp_Type = Counter32
_IpxLinkCntRxRipResp_Object = MibTableColumn
ipxLinkCntRxRipResp = _IpxLinkCntRxRipResp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 16),
    _IpxLinkCntRxRipResp_Type()
)
ipxLinkCntRxRipResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxRipResp.setStatus("mandatory")
_IpxLinkCntTxRipReply_Type = Counter32
_IpxLinkCntTxRipReply_Object = MibTableColumn
ipxLinkCntTxRipReply = _IpxLinkCntTxRipReply_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 17),
    _IpxLinkCntTxRipReply_Type()
)
ipxLinkCntTxRipReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxRipReply.setStatus("mandatory")
_IpxLinkCntRxRipInvalid_Type = Counter32
_IpxLinkCntRxRipInvalid_Object = MibTableColumn
ipxLinkCntRxRipInvalid = _IpxLinkCntRxRipInvalid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 18),
    _IpxLinkCntRxRipInvalid_Type()
)
ipxLinkCntRxRipInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxRipInvalid.setStatus("mandatory")
_IpxLinkCntRxType20_Type = Counter32
_IpxLinkCntRxType20_Object = MibTableColumn
ipxLinkCntRxType20 = _IpxLinkCntRxType20_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 19),
    _IpxLinkCntRxType20_Type()
)
ipxLinkCntRxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxType20.setStatus("mandatory")
_IpxLinkCntTxType20_Type = Counter32
_IpxLinkCntTxType20_Object = MibTableColumn
ipxLinkCntTxType20 = _IpxLinkCntTxType20_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 20),
    _IpxLinkCntTxType20_Type()
)
ipxLinkCntTxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxType20.setStatus("mandatory")
_IpxLinkCntType20Disc_Type = Counter32
_IpxLinkCntType20Disc_Object = MibTableColumn
ipxLinkCntType20Disc = _IpxLinkCntType20Disc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 21),
    _IpxLinkCntType20Disc_Type()
)
ipxLinkCntType20Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntType20Disc.setStatus("mandatory")
_IpxLinkCntNoRoute_Type = Counter32
_IpxLinkCntNoRoute_Object = MibTableColumn
ipxLinkCntNoRoute = _IpxLinkCntNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 22),
    _IpxLinkCntNoRoute_Type()
)
ipxLinkCntNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntNoRoute.setStatus("mandatory")
_IpxLinkCntRxDiscarded_Type = Counter32
_IpxLinkCntRxDiscarded_Object = MibTableColumn
ipxLinkCntRxDiscarded = _IpxLinkCntRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 23),
    _IpxLinkCntRxDiscarded_Type()
)
ipxLinkCntRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxDiscarded.setStatus("mandatory")
_IpxLinkCntSpxSpoofed_Type = Counter32
_IpxLinkCntSpxSpoofed_Object = MibTableColumn
ipxLinkCntSpxSpoofed = _IpxLinkCntSpxSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 24),
    _IpxLinkCntSpxSpoofed_Type()
)
ipxLinkCntSpxSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntSpxSpoofed.setStatus("mandatory")
_IpxLinkCntWatchdogSpoofed_Type = Counter32
_IpxLinkCntWatchdogSpoofed_Object = MibTableColumn
ipxLinkCntWatchdogSpoofed = _IpxLinkCntWatchdogSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 25),
    _IpxLinkCntWatchdogSpoofed_Type()
)
ipxLinkCntWatchdogSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntWatchdogSpoofed.setStatus("mandatory")
_IpxLinkCntForwarded_Type = Counter32
_IpxLinkCntForwarded_Object = MibTableColumn
ipxLinkCntForwarded = _IpxLinkCntForwarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 26),
    _IpxLinkCntForwarded_Type()
)
ipxLinkCntForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntForwarded.setStatus("mandatory")
_IpxLinkCntCacheHits_Type = Counter32
_IpxLinkCntCacheHits_Object = MibTableColumn
ipxLinkCntCacheHits = _IpxLinkCntCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 27),
    _IpxLinkCntCacheHits_Type()
)
ipxLinkCntCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntCacheHits.setStatus("mandatory")
_IpxLinkCntSPXCacheHits_Type = Counter32
_IpxLinkCntSPXCacheHits_Object = MibTableColumn
ipxLinkCntSPXCacheHits = _IpxLinkCntSPXCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 28),
    _IpxLinkCntSPXCacheHits_Type()
)
ipxLinkCntSPXCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntSPXCacheHits.setStatus("mandatory")
_IpxLinkCntRxDefDataFltHits_Type = Counter32
_IpxLinkCntRxDefDataFltHits_Object = MibTableColumn
ipxLinkCntRxDefDataFltHits = _IpxLinkCntRxDefDataFltHits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 29),
    _IpxLinkCntRxDefDataFltHits_Type()
)
ipxLinkCntRxDefDataFltHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxDefDataFltHits.setStatus("mandatory")
_IpxLinkCntTxDefDataFltHits_Type = Counter32
_IpxLinkCntTxDefDataFltHits_Object = MibTableColumn
ipxLinkCntTxDefDataFltHits = _IpxLinkCntTxDefDataFltHits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 1, 1, 30),
    _IpxLinkCntTxDefDataFltHits_Type()
)
ipxLinkCntTxDefDataFltHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxDefDataFltHits.setStatus("mandatory")
_IpxLinkByteCntTable_Object = MibTable
ipxLinkByteCntTable = _IpxLinkByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2)
)
if mibBuilder.loadTexts:
    ipxLinkByteCntTable.setStatus("mandatory")
_IpxLinkByteCntEntry_Object = MibTableRow
ipxLinkByteCntEntry = _IpxLinkByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1)
)
ipxLinkByteCntEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxLinkByteCntIpxLinkIndex"),
)
if mibBuilder.loadTexts:
    ipxLinkByteCntEntry.setStatus("mandatory")
_IpxLinkByteCntIpxLinkIndex_Type = Integer32
_IpxLinkByteCntIpxLinkIndex_Object = MibTableColumn
ipxLinkByteCntIpxLinkIndex = _IpxLinkByteCntIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 1),
    _IpxLinkByteCntIpxLinkIndex_Type()
)
ipxLinkByteCntIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntIpxLinkIndex.setStatus("mandatory")
_IpxLinkByteCntRxTotal_Type = Counter32
_IpxLinkByteCntRxTotal_Object = MibTableColumn
ipxLinkByteCntRxTotal = _IpxLinkByteCntRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 2),
    _IpxLinkByteCntRxTotal_Type()
)
ipxLinkByteCntRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntRxTotal.setStatus("mandatory")
_IpxLinkByteCntTxTotal_Type = Counter32
_IpxLinkByteCntTxTotal_Object = MibTableColumn
ipxLinkByteCntTxTotal = _IpxLinkByteCntTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 3),
    _IpxLinkByteCntTxTotal_Type()
)
ipxLinkByteCntTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntTxTotal.setStatus("mandatory")
_IpxLinkByteCntRxOther_Type = Counter32
_IpxLinkByteCntRxOther_Object = MibTableColumn
ipxLinkByteCntRxOther = _IpxLinkByteCntRxOther_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 4),
    _IpxLinkByteCntRxOther_Type()
)
ipxLinkByteCntRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntRxOther.setStatus("mandatory")
_IpxLinkByteCntTxOther_Type = Counter32
_IpxLinkByteCntTxOther_Object = MibTableColumn
ipxLinkByteCntTxOther = _IpxLinkByteCntTxOther_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 5),
    _IpxLinkByteCntTxOther_Type()
)
ipxLinkByteCntTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntTxOther.setStatus("mandatory")
_IpxLinkByteCntRxNcp_Type = Counter32
_IpxLinkByteCntRxNcp_Object = MibTableColumn
ipxLinkByteCntRxNcp = _IpxLinkByteCntRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 6),
    _IpxLinkByteCntRxNcp_Type()
)
ipxLinkByteCntRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntRxNcp.setStatus("mandatory")
_IpxLinkByteCntTxNcp_Type = Counter32
_IpxLinkByteCntTxNcp_Object = MibTableColumn
ipxLinkByteCntTxNcp = _IpxLinkByteCntTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 7),
    _IpxLinkByteCntTxNcp_Type()
)
ipxLinkByteCntTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntTxNcp.setStatus("mandatory")
_IpxLinkByteCntRxSpx_Type = Counter32
_IpxLinkByteCntRxSpx_Object = MibTableColumn
ipxLinkByteCntRxSpx = _IpxLinkByteCntRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 8),
    _IpxLinkByteCntRxSpx_Type()
)
ipxLinkByteCntRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntRxSpx.setStatus("mandatory")
_IpxLinkByteCntTxSpx_Type = Counter32
_IpxLinkByteCntTxSpx_Object = MibTableColumn
ipxLinkByteCntTxSpx = _IpxLinkByteCntTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 9),
    _IpxLinkByteCntTxSpx_Type()
)
ipxLinkByteCntTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntTxSpx.setStatus("mandatory")
_IpxLinkByteCntRxRip_Type = Counter32
_IpxLinkByteCntRxRip_Object = MibTableColumn
ipxLinkByteCntRxRip = _IpxLinkByteCntRxRip_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 10),
    _IpxLinkByteCntRxRip_Type()
)
ipxLinkByteCntRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntRxRip.setStatus("mandatory")
_IpxLinkByteCntTxRip_Type = Counter32
_IpxLinkByteCntTxRip_Object = MibTableColumn
ipxLinkByteCntTxRip = _IpxLinkByteCntTxRip_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 11),
    _IpxLinkByteCntTxRip_Type()
)
ipxLinkByteCntTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntTxRip.setStatus("mandatory")
_IpxLinkByteCntRxSap_Type = Counter32
_IpxLinkByteCntRxSap_Object = MibTableColumn
ipxLinkByteCntRxSap = _IpxLinkByteCntRxSap_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 12),
    _IpxLinkByteCntRxSap_Type()
)
ipxLinkByteCntRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntRxSap.setStatus("mandatory")
_IpxLinkByteCntTxSap_Type = Counter32
_IpxLinkByteCntTxSap_Object = MibTableColumn
ipxLinkByteCntTxSap = _IpxLinkByteCntTxSap_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 13),
    _IpxLinkByteCntTxSap_Type()
)
ipxLinkByteCntTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntTxSap.setStatus("mandatory")
_IpxLinkByteCntRxType20_Type = Counter32
_IpxLinkByteCntRxType20_Object = MibTableColumn
ipxLinkByteCntRxType20 = _IpxLinkByteCntRxType20_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 14),
    _IpxLinkByteCntRxType20_Type()
)
ipxLinkByteCntRxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntRxType20.setStatus("mandatory")
_IpxLinkByteCntTxType20_Type = Counter32
_IpxLinkByteCntTxType20_Object = MibTableColumn
ipxLinkByteCntTxType20 = _IpxLinkByteCntTxType20_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 2, 1, 15),
    _IpxLinkByteCntTxType20_Type()
)
ipxLinkByteCntTxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkByteCntTxType20.setStatus("mandatory")
_IpxCountRxTotal_Type = Counter32
_IpxCountRxTotal_Object = MibScalar
ipxCountRxTotal = _IpxCountRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 3),
    _IpxCountRxTotal_Type()
)
ipxCountRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxTotal.setStatus("mandatory")
_IpxCountTxTotal_Type = Counter32
_IpxCountTxTotal_Object = MibScalar
ipxCountTxTotal = _IpxCountTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 4),
    _IpxCountTxTotal_Type()
)
ipxCountTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxTotal.setStatus("mandatory")
_IpxCountTxFailed_Type = Counter32
_IpxCountTxFailed_Object = MibScalar
ipxCountTxFailed = _IpxCountTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 5),
    _IpxCountTxFailed_Type()
)
ipxCountTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxFailed.setStatus("mandatory")
_IpxCountRxFiltered_Type = Counter32
_IpxCountRxFiltered_Object = MibScalar
ipxCountRxFiltered = _IpxCountRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 6),
    _IpxCountRxFiltered_Type()
)
ipxCountRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxFiltered.setStatus("mandatory")
_IpxCountTxFiltered_Type = Counter32
_IpxCountTxFiltered_Object = MibScalar
ipxCountTxFiltered = _IpxCountTxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 7),
    _IpxCountTxFiltered_Type()
)
ipxCountTxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxFiltered.setStatus("mandatory")
_IpxCountRxTooManyHops_Type = Counter32
_IpxCountRxTooManyHops_Object = MibScalar
ipxCountRxTooManyHops = _IpxCountRxTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 8),
    _IpxCountRxTooManyHops_Type()
)
ipxCountRxTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxTooManyHops.setStatus("mandatory")
_IpxCountRxHeaderErr_Type = Counter32
_IpxCountRxHeaderErr_Object = MibScalar
ipxCountRxHeaderErr = _IpxCountRxHeaderErr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 9),
    _IpxCountRxHeaderErr_Type()
)
ipxCountRxHeaderErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxHeaderErr.setStatus("mandatory")
_IpxCountRxSapReq_Type = Counter32
_IpxCountRxSapReq_Object = MibScalar
ipxCountRxSapReq = _IpxCountRxSapReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 10),
    _IpxCountRxSapReq_Type()
)
ipxCountRxSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxSapReq.setStatus("mandatory")
_IpxCountTxSapReq_Type = Counter32
_IpxCountTxSapReq_Object = MibScalar
ipxCountTxSapReq = _IpxCountTxSapReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 11),
    _IpxCountTxSapReq_Type()
)
ipxCountTxSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxSapReq.setStatus("mandatory")
_IpxCountRxSapResp_Type = Counter32
_IpxCountRxSapResp_Object = MibScalar
ipxCountRxSapResp = _IpxCountRxSapResp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 12),
    _IpxCountRxSapResp_Type()
)
ipxCountRxSapResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxSapResp.setStatus("mandatory")
_IpxCountTxSapReply_Type = Counter32
_IpxCountTxSapReply_Object = MibScalar
ipxCountTxSapReply = _IpxCountTxSapReply_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 13),
    _IpxCountTxSapReply_Type()
)
ipxCountTxSapReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxSapReply.setStatus("mandatory")
_IpxCountRxSapInvalid_Type = Counter32
_IpxCountRxSapInvalid_Object = MibScalar
ipxCountRxSapInvalid = _IpxCountRxSapInvalid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 14),
    _IpxCountRxSapInvalid_Type()
)
ipxCountRxSapInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxSapInvalid.setStatus("mandatory")
_IpxCountRxRipReq_Type = Counter32
_IpxCountRxRipReq_Object = MibScalar
ipxCountRxRipReq = _IpxCountRxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 15),
    _IpxCountRxRipReq_Type()
)
ipxCountRxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxRipReq.setStatus("mandatory")
_IpxCountTxRipReq_Type = Counter32
_IpxCountTxRipReq_Object = MibScalar
ipxCountTxRipReq = _IpxCountTxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 16),
    _IpxCountTxRipReq_Type()
)
ipxCountTxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxRipReq.setStatus("mandatory")
_IpxCountRxRipResp_Type = Counter32
_IpxCountRxRipResp_Object = MibScalar
ipxCountRxRipResp = _IpxCountRxRipResp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 17),
    _IpxCountRxRipResp_Type()
)
ipxCountRxRipResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxRipResp.setStatus("mandatory")
_IpxCountTxRipReply_Type = Counter32
_IpxCountTxRipReply_Object = MibScalar
ipxCountTxRipReply = _IpxCountTxRipReply_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 18),
    _IpxCountTxRipReply_Type()
)
ipxCountTxRipReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxRipReply.setStatus("mandatory")
_IpxCountRxRipInvalid_Type = Counter32
_IpxCountRxRipInvalid_Object = MibScalar
ipxCountRxRipInvalid = _IpxCountRxRipInvalid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 19),
    _IpxCountRxRipInvalid_Type()
)
ipxCountRxRipInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxRipInvalid.setStatus("mandatory")
_IpxCountRxType20_Type = Counter32
_IpxCountRxType20_Object = MibScalar
ipxCountRxType20 = _IpxCountRxType20_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 20),
    _IpxCountRxType20_Type()
)
ipxCountRxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxType20.setStatus("mandatory")
_IpxCountTxType20_Type = Counter32
_IpxCountTxType20_Object = MibScalar
ipxCountTxType20 = _IpxCountTxType20_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 21),
    _IpxCountTxType20_Type()
)
ipxCountTxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountTxType20.setStatus("mandatory")
_IpxCountType20Disc_Type = Counter32
_IpxCountType20Disc_Object = MibScalar
ipxCountType20Disc = _IpxCountType20Disc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 22),
    _IpxCountType20Disc_Type()
)
ipxCountType20Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountType20Disc.setStatus("mandatory")
_IpxCountNoRoute_Type = Counter32
_IpxCountNoRoute_Object = MibScalar
ipxCountNoRoute = _IpxCountNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 23),
    _IpxCountNoRoute_Type()
)
ipxCountNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountNoRoute.setStatus("mandatory")
_IpxCountRxDiscarded_Type = Counter32
_IpxCountRxDiscarded_Object = MibScalar
ipxCountRxDiscarded = _IpxCountRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 24),
    _IpxCountRxDiscarded_Type()
)
ipxCountRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountRxDiscarded.setStatus("mandatory")
_IpxCountSpxSpoofed_Type = Counter32
_IpxCountSpxSpoofed_Object = MibScalar
ipxCountSpxSpoofed = _IpxCountSpxSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 25),
    _IpxCountSpxSpoofed_Type()
)
ipxCountSpxSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountSpxSpoofed.setStatus("mandatory")
_IpxCountWatchdogSpoofed_Type = Counter32
_IpxCountWatchdogSpoofed_Object = MibScalar
ipxCountWatchdogSpoofed = _IpxCountWatchdogSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 26),
    _IpxCountWatchdogSpoofed_Type()
)
ipxCountWatchdogSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountWatchdogSpoofed.setStatus("mandatory")
_IpxCountForwarded_Type = Counter32
_IpxCountForwarded_Object = MibScalar
ipxCountForwarded = _IpxCountForwarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 27),
    _IpxCountForwarded_Type()
)
ipxCountForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountForwarded.setStatus("mandatory")
_IpxCountCacheHits_Type = Counter32
_IpxCountCacheHits_Object = MibScalar
ipxCountCacheHits = _IpxCountCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 28),
    _IpxCountCacheHits_Type()
)
ipxCountCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountCacheHits.setStatus("mandatory")
_IpxCountSPXCacheHits_Type = Counter32
_IpxCountSPXCacheHits_Object = MibScalar
ipxCountSPXCacheHits = _IpxCountSPXCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 4, 29),
    _IpxCountSPXCacheHits_Type()
)
ipxCountSPXCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCountSPXCacheHits.setStatus("mandatory")
_IpxRip_ObjectIdentity = ObjectIdentity
ipxRip = _IpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5)
)
_IpxRipTable_Object = MibTable
ipxRipTable = _IpxRipTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1)
)
if mibBuilder.loadTexts:
    ipxRipTable.setStatus("mandatory")
_IpxRipEntry_Object = MibTableRow
ipxRipEntry = _IpxRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1)
)
ipxRipEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxRipNetwork"),
)
if mibBuilder.loadTexts:
    ipxRipEntry.setStatus("mandatory")


class _IpxRipNetwork_Type(OctetString):
    """Custom type ipxRipNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRipNetwork_Type.__name__ = "OctetString"
_IpxRipNetwork_Object = MibTableColumn
ipxRipNetwork = _IpxRipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 1),
    _IpxRipNetwork_Type()
)
ipxRipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipNetwork.setStatus("mandatory")
_IpxRipIpxLinkIndex_Type = Integer32
_IpxRipIpxLinkIndex_Object = MibTableColumn
ipxRipIpxLinkIndex = _IpxRipIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 2),
    _IpxRipIpxLinkIndex_Type()
)
ipxRipIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipIpxLinkIndex.setStatus("mandatory")
_IpxRipIfIndex_Type = Integer32
_IpxRipIfIndex_Object = MibTableColumn
ipxRipIfIndex = _IpxRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 3),
    _IpxRipIfIndex_Type()
)
ipxRipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipIfIndex.setStatus("mandatory")


class _IpxRipProtocol_Type(Integer32):
    """Custom type ipxRipProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5),
          ("staticBackup", 6))
    )


_IpxRipProtocol_Type.__name__ = "Integer32"
_IpxRipProtocol_Object = MibTableColumn
ipxRipProtocol = _IpxRipProtocol_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 4),
    _IpxRipProtocol_Type()
)
ipxRipProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipProtocol.setStatus("mandatory")
_IpxRipDelay_Type = Integer32
_IpxRipDelay_Object = MibTableColumn
ipxRipDelay = _IpxRipDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 5),
    _IpxRipDelay_Type()
)
ipxRipDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipDelay.setStatus("mandatory")
_IpxRipHops_Type = Integer32
_IpxRipHops_Object = MibTableColumn
ipxRipHops = _IpxRipHops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 6),
    _IpxRipHops_Type()
)
ipxRipHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipHops.setStatus("mandatory")
_IpxRipAge_Type = Integer32
_IpxRipAge_Object = MibTableColumn
ipxRipAge = _IpxRipAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 7),
    _IpxRipAge_Type()
)
ipxRipAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipAge.setStatus("mandatory")
_IpxRipIpxAddr_Type = IpxAddr
_IpxRipIpxAddr_Object = MibTableColumn
ipxRipIpxAddr = _IpxRipIpxAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 8),
    _IpxRipIpxAddr_Type()
)
ipxRipIpxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipIpxAddr.setStatus("mandatory")
_IpxRipStaticCount_Type = Integer32
_IpxRipStaticCount_Object = MibTableColumn
ipxRipStaticCount = _IpxRipStaticCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 5, 1, 1, 9),
    _IpxRipStaticCount_Type()
)
ipxRipStaticCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipStaticCount.setStatus("mandatory")
_IpxSap_ObjectIdentity = ObjectIdentity
ipxSap = _IpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6)
)
_IpxSapTable_Object = MibTable
ipxSapTable = _IpxSapTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1)
)
if mibBuilder.loadTexts:
    ipxSapTable.setStatus("mandatory")
_IpxSapEntry_Object = MibTableRow
ipxSapEntry = _IpxSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1)
)
ipxSapEntry.setIndexNames(
    (0, "INTEL-IPX-MIB", "ipxSapServerAddr"),
    (0, "INTEL-IPX-MIB", "ipxSapServerType"),
)
if mibBuilder.loadTexts:
    ipxSapEntry.setStatus("mandatory")
_IpxSapServerAddr_Type = IpxAddr
_IpxSapServerAddr_Object = MibTableColumn
ipxSapServerAddr = _IpxSapServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 1),
    _IpxSapServerAddr_Type()
)
ipxSapServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapServerAddr.setStatus("mandatory")
_IpxSapServerType_Type = Integer32
_IpxSapServerType_Object = MibTableColumn
ipxSapServerType = _IpxSapServerType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 2),
    _IpxSapServerType_Type()
)
ipxSapServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapServerType.setStatus("mandatory")


class _IpxSapServerName_Type(OctetString):
    """Custom type ipxSapServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_IpxSapServerName_Type.__name__ = "OctetString"
_IpxSapServerName_Object = MibTableColumn
ipxSapServerName = _IpxSapServerName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 3),
    _IpxSapServerName_Type()
)
ipxSapServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapServerName.setStatus("mandatory")
_IpxSapIpxLinkIndex_Type = Integer32
_IpxSapIpxLinkIndex_Object = MibTableColumn
ipxSapIpxLinkIndex = _IpxSapIpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 4),
    _IpxSapIpxLinkIndex_Type()
)
ipxSapIpxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapIpxLinkIndex.setStatus("mandatory")
_IpxSapIfIndex_Type = Integer32
_IpxSapIfIndex_Object = MibTableColumn
ipxSapIfIndex = _IpxSapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 5),
    _IpxSapIfIndex_Type()
)
ipxSapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapIfIndex.setStatus("mandatory")
_IpxSapAge_Type = Integer32
_IpxSapAge_Object = MibTableColumn
ipxSapAge = _IpxSapAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 6),
    _IpxSapAge_Type()
)
ipxSapAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapAge.setStatus("mandatory")


class _IpxSapProtocol_Type(Integer32):
    """Custom type ipxSapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sap", 6),
          ("static", 5))
    )


_IpxSapProtocol_Type.__name__ = "Integer32"
_IpxSapProtocol_Object = MibTableColumn
ipxSapProtocol = _IpxSapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 7),
    _IpxSapProtocol_Type()
)
ipxSapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapProtocol.setStatus("mandatory")
_IpxSapHops_Type = Integer32
_IpxSapHops_Object = MibTableColumn
ipxSapHops = _IpxSapHops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 8),
    _IpxSapHops_Type()
)
ipxSapHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapHops.setStatus("mandatory")
_IpxSapStaticCount_Type = Integer32
_IpxSapStaticCount_Object = MibTableColumn
ipxSapStaticCount = _IpxSapStaticCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 22, 6, 1, 1, 9),
    _IpxSapStaticCount_Type()
)
ipxSapStaticCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapStaticCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-IPX-MIB",
    **{"FltDirection": FltDirection,
       "IpxAddr": IpxAddr,
       "FltAction": FltAction,
       "ipx": ipx,
       "ipxControl": ipxControl,
       "ipxControlCommand": ipxControlCommand,
       "ipxConf": ipxConf,
       "ipxLinkConfTable": ipxLinkConfTable,
       "ipxLinkConfEntry": ipxLinkConfEntry,
       "ipxLinkConfIpxLinkIndex": ipxLinkConfIpxLinkIndex,
       "ipxLinkConfRoutingProtocol": ipxLinkConfRoutingProtocol,
       "ipxLinkConfNumbered": ipxLinkConfNumbered,
       "ipxLinkConfNet": ipxLinkConfNet,
       "ipxLinkConfFrameType": ipxLinkConfFrameType,
       "ipxLinkConfFrameParam": ipxLinkConfFrameParam,
       "ipxLinkConfIpxWanNegotiation": ipxLinkConfIpxWanNegotiation,
       "ipxLinkConfRipUpdateInterval": ipxLinkConfRipUpdateInterval,
       "ipxLinkConfRipTrigger": ipxLinkConfRipTrigger,
       "ipxLinkConfSapUpdateInterval": ipxLinkConfSapUpdateInterval,
       "ipxLinkConfSapTrigger": ipxLinkConfSapTrigger,
       "ipxLinkConfAutomaticDelay": ipxLinkConfAutomaticDelay,
       "ipxLinkConfDelay": ipxLinkConfDelay,
       "ipxLinkConfSpxSpoofing": ipxLinkConfSpxSpoofing,
       "ipxLinkConfSpxSessionTimeout": ipxLinkConfSpxSessionTimeout,
       "ipxLinkConfType20Broadcast": ipxLinkConfType20Broadcast,
       "ipxLinkConfWatchdogSpoofing": ipxLinkConfWatchdogSpoofing,
       "ipxLinkConfRipFltRxDefaultAction": ipxLinkConfRipFltRxDefaultAction,
       "ipxLinkConfRipFltTxDefaultAction": ipxLinkConfRipFltTxDefaultAction,
       "ipxLinkConfSapFltRxDefaultAction": ipxLinkConfSapFltRxDefaultAction,
       "ipxLinkConfSapFltTxDefaultAction": ipxLinkConfSapFltTxDefaultAction,
       "ipxLinkConfDataFltRxDefaultAction": ipxLinkConfDataFltRxDefaultAction,
       "ipxLinkConfDataFltTxDefaultAction": ipxLinkConfDataFltTxDefaultAction,
       "ipxLinkConfDataFilters": ipxLinkConfDataFilters,
       "ipxLinkConfCreateObj": ipxLinkConfCreateObj,
       "ipxLinkConfDeleteObj": ipxLinkConfDeleteObj,
       "ipxRipFltTable": ipxRipFltTable,
       "ipxRipFltEntry": ipxRipFltEntry,
       "ipxRipFltIpxLinkIndex": ipxRipFltIpxLinkIndex,
       "ipxRipFltDirection": ipxRipFltDirection,
       "ipxRipFltNumber": ipxRipFltNumber,
       "ipxRipFltAction": ipxRipFltAction,
       "ipxRipFltNetworkAddress": ipxRipFltNetworkAddress,
       "ipxRipFltNetworkMask": ipxRipFltNetworkMask,
       "ipxSapFltTable": ipxSapFltTable,
       "ipxSapFltEntry": ipxSapFltEntry,
       "ipxSapFltIpxLinkIndex": ipxSapFltIpxLinkIndex,
       "ipxSapFltDirection": ipxSapFltDirection,
       "ipxSapFltNumber": ipxSapFltNumber,
       "ipxSapFltAction": ipxSapFltAction,
       "ipxSapFltNetworkAddress": ipxSapFltNetworkAddress,
       "ipxSapFltNetworkMask": ipxSapFltNetworkMask,
       "ipxSapFltNodeAddress": ipxSapFltNodeAddress,
       "ipxSapFltServiceType": ipxSapFltServiceType,
       "ipxSapFltServerName": ipxSapFltServerName,
       "ipxDataFltTable": ipxDataFltTable,
       "ipxDataFltEntry": ipxDataFltEntry,
       "ipxDataFltIpxLinkIndex": ipxDataFltIpxLinkIndex,
       "ipxDataFltDirection": ipxDataFltDirection,
       "ipxDataFltNumber": ipxDataFltNumber,
       "ipxDataFltAction": ipxDataFltAction,
       "ipxDataFltDstNetworkAddress": ipxDataFltDstNetworkAddress,
       "ipxDataFltDstNetworkMask": ipxDataFltDstNetworkMask,
       "ipxDataFltDstNodeAddress": ipxDataFltDstNodeAddress,
       "ipxDataFltDstSocketFilter": ipxDataFltDstSocketFilter,
       "ipxDataFltDstSocket": ipxDataFltDstSocket,
       "ipxDataFltSrcNetworkAddress": ipxDataFltSrcNetworkAddress,
       "ipxDataFltSrcNetworkMask": ipxDataFltSrcNetworkMask,
       "ipxDataFltSrcNodeAddress": ipxDataFltSrcNodeAddress,
       "ipxDataFltSrcSocketFilter": ipxDataFltSrcSocketFilter,
       "ipxDataFltSrcSocket": ipxDataFltSrcSocket,
       "ipxDataFltPacketTypeFilter": ipxDataFltPacketTypeFilter,
       "ipxDataFltPacketType": ipxDataFltPacketType,
       "ipxDataFltHits": ipxDataFltHits,
       "ipxConfAutoIntNetNumber": ipxConfAutoIntNetNumber,
       "ipxConfIntNetNumber": ipxConfIntNetNumber,
       "ipxStatus": ipxStatus,
       "ipxLinkMonTable": ipxLinkMonTable,
       "ipxLinkMonEntry": ipxLinkMonEntry,
       "ipxLinkMonIpxLinkIndex": ipxLinkMonIpxLinkIndex,
       "ipxLinkMonIfIndex": ipxLinkMonIfIndex,
       "ipxLinkMonState": ipxLinkMonState,
       "ipxLinkMonDelay": ipxLinkMonDelay,
       "ipxLinkMonMtuSize": ipxLinkMonMtuSize,
       "ipxStatusConfigTimeStamp": ipxStatusConfigTimeStamp,
       "ipxStatusReachableNets": ipxStatusReachableNets,
       "ipxStatusDeadNets": ipxStatusDeadNets,
       "ipxStatusReachableServices": ipxStatusReachableServices,
       "ipxStatusDeadServices": ipxStatusDeadServices,
       "ipxStatusLinkTimeStamp": ipxStatusLinkTimeStamp,
       "ipxCount": ipxCount,
       "ipxLinkCntTable": ipxLinkCntTable,
       "ipxLinkCntEntry": ipxLinkCntEntry,
       "ipxLinkCntIpxLinkIndex": ipxLinkCntIpxLinkIndex,
       "ipxLinkCntRxTotal": ipxLinkCntRxTotal,
       "ipxLinkCntTxTotal": ipxLinkCntTxTotal,
       "ipxLinkCntTxFailed": ipxLinkCntTxFailed,
       "ipxLinkCntRxFiltered": ipxLinkCntRxFiltered,
       "ipxLinkCntTxFiltered": ipxLinkCntTxFiltered,
       "ipxLinkCntRxTooManyHops": ipxLinkCntRxTooManyHops,
       "ipxLinkCntRxHeaderErr": ipxLinkCntRxHeaderErr,
       "ipxLinkCntRxSapReq": ipxLinkCntRxSapReq,
       "ipxLinkCntTxSapReq": ipxLinkCntTxSapReq,
       "ipxLinkCntRxSapResp": ipxLinkCntRxSapResp,
       "ipxLinkCntTxSapReply": ipxLinkCntTxSapReply,
       "ipxLinkCntRxSapInvalid": ipxLinkCntRxSapInvalid,
       "ipxLinkCntRxRipReq": ipxLinkCntRxRipReq,
       "ipxLinkCntTxRipReq": ipxLinkCntTxRipReq,
       "ipxLinkCntRxRipResp": ipxLinkCntRxRipResp,
       "ipxLinkCntTxRipReply": ipxLinkCntTxRipReply,
       "ipxLinkCntRxRipInvalid": ipxLinkCntRxRipInvalid,
       "ipxLinkCntRxType20": ipxLinkCntRxType20,
       "ipxLinkCntTxType20": ipxLinkCntTxType20,
       "ipxLinkCntType20Disc": ipxLinkCntType20Disc,
       "ipxLinkCntNoRoute": ipxLinkCntNoRoute,
       "ipxLinkCntRxDiscarded": ipxLinkCntRxDiscarded,
       "ipxLinkCntSpxSpoofed": ipxLinkCntSpxSpoofed,
       "ipxLinkCntWatchdogSpoofed": ipxLinkCntWatchdogSpoofed,
       "ipxLinkCntForwarded": ipxLinkCntForwarded,
       "ipxLinkCntCacheHits": ipxLinkCntCacheHits,
       "ipxLinkCntSPXCacheHits": ipxLinkCntSPXCacheHits,
       "ipxLinkCntRxDefDataFltHits": ipxLinkCntRxDefDataFltHits,
       "ipxLinkCntTxDefDataFltHits": ipxLinkCntTxDefDataFltHits,
       "ipxLinkByteCntTable": ipxLinkByteCntTable,
       "ipxLinkByteCntEntry": ipxLinkByteCntEntry,
       "ipxLinkByteCntIpxLinkIndex": ipxLinkByteCntIpxLinkIndex,
       "ipxLinkByteCntRxTotal": ipxLinkByteCntRxTotal,
       "ipxLinkByteCntTxTotal": ipxLinkByteCntTxTotal,
       "ipxLinkByteCntRxOther": ipxLinkByteCntRxOther,
       "ipxLinkByteCntTxOther": ipxLinkByteCntTxOther,
       "ipxLinkByteCntRxNcp": ipxLinkByteCntRxNcp,
       "ipxLinkByteCntTxNcp": ipxLinkByteCntTxNcp,
       "ipxLinkByteCntRxSpx": ipxLinkByteCntRxSpx,
       "ipxLinkByteCntTxSpx": ipxLinkByteCntTxSpx,
       "ipxLinkByteCntRxRip": ipxLinkByteCntRxRip,
       "ipxLinkByteCntTxRip": ipxLinkByteCntTxRip,
       "ipxLinkByteCntRxSap": ipxLinkByteCntRxSap,
       "ipxLinkByteCntTxSap": ipxLinkByteCntTxSap,
       "ipxLinkByteCntRxType20": ipxLinkByteCntRxType20,
       "ipxLinkByteCntTxType20": ipxLinkByteCntTxType20,
       "ipxCountRxTotal": ipxCountRxTotal,
       "ipxCountTxTotal": ipxCountTxTotal,
       "ipxCountTxFailed": ipxCountTxFailed,
       "ipxCountRxFiltered": ipxCountRxFiltered,
       "ipxCountTxFiltered": ipxCountTxFiltered,
       "ipxCountRxTooManyHops": ipxCountRxTooManyHops,
       "ipxCountRxHeaderErr": ipxCountRxHeaderErr,
       "ipxCountRxSapReq": ipxCountRxSapReq,
       "ipxCountTxSapReq": ipxCountTxSapReq,
       "ipxCountRxSapResp": ipxCountRxSapResp,
       "ipxCountTxSapReply": ipxCountTxSapReply,
       "ipxCountRxSapInvalid": ipxCountRxSapInvalid,
       "ipxCountRxRipReq": ipxCountRxRipReq,
       "ipxCountTxRipReq": ipxCountTxRipReq,
       "ipxCountRxRipResp": ipxCountRxRipResp,
       "ipxCountTxRipReply": ipxCountTxRipReply,
       "ipxCountRxRipInvalid": ipxCountRxRipInvalid,
       "ipxCountRxType20": ipxCountRxType20,
       "ipxCountTxType20": ipxCountTxType20,
       "ipxCountType20Disc": ipxCountType20Disc,
       "ipxCountNoRoute": ipxCountNoRoute,
       "ipxCountRxDiscarded": ipxCountRxDiscarded,
       "ipxCountSpxSpoofed": ipxCountSpxSpoofed,
       "ipxCountWatchdogSpoofed": ipxCountWatchdogSpoofed,
       "ipxCountForwarded": ipxCountForwarded,
       "ipxCountCacheHits": ipxCountCacheHits,
       "ipxCountSPXCacheHits": ipxCountSPXCacheHits,
       "ipxRip": ipxRip,
       "ipxRipTable": ipxRipTable,
       "ipxRipEntry": ipxRipEntry,
       "ipxRipNetwork": ipxRipNetwork,
       "ipxRipIpxLinkIndex": ipxRipIpxLinkIndex,
       "ipxRipIfIndex": ipxRipIfIndex,
       "ipxRipProtocol": ipxRipProtocol,
       "ipxRipDelay": ipxRipDelay,
       "ipxRipHops": ipxRipHops,
       "ipxRipAge": ipxRipAge,
       "ipxRipIpxAddr": ipxRipIpxAddr,
       "ipxRipStaticCount": ipxRipStaticCount,
       "ipxSap": ipxSap,
       "ipxSapTable": ipxSapTable,
       "ipxSapEntry": ipxSapEntry,
       "ipxSapServerAddr": ipxSapServerAddr,
       "ipxSapServerType": ipxSapServerType,
       "ipxSapServerName": ipxSapServerName,
       "ipxSapIpxLinkIndex": ipxSapIpxLinkIndex,
       "ipxSapIfIndex": ipxSapIfIndex,
       "ipxSapAge": ipxSapAge,
       "ipxSapProtocol": ipxSapProtocol,
       "ipxSapHops": ipxSapHops,
       "ipxSapStaticCount": ipxSapStaticCount}
)
