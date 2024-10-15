# SNMP MIB module (APTIS-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:06 2024
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

(aptis_generic,) = mibBuilder.importSymbols(
    "APTIS-MIB",
    "aptis-generic")

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



class Index(Integer32):
    """Custom type Index based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AptisHdlc_ObjectIdentity = ObjectIdentity
aptisHdlc = _AptisHdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7)
)
_AptisHdlcTable_Object = MibTable
aptisHdlcTable = _AptisHdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1)
)
if mibBuilder.loadTexts:
    aptisHdlcTable.setStatus("mandatory")
_AptisHdlcEntry_Object = MibTableRow
aptisHdlcEntry = _AptisHdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1)
)
aptisHdlcEntry.setIndexNames(
    (0, "APTIS-HDLC-MIB", "aptisHdlcIfIndex"),
)
if mibBuilder.loadTexts:
    aptisHdlcEntry.setStatus("mandatory")
_AptisHdlcIfIndex_Type = Index
_AptisHdlcIfIndex_Object = MibTableColumn
aptisHdlcIfIndex = _AptisHdlcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 1),
    _AptisHdlcIfIndex_Type()
)
aptisHdlcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcIfIndex.setStatus("mandatory")
_AptisHdlcReceiveDrops_Type = Counter32
_AptisHdlcReceiveDrops_Object = MibTableColumn
aptisHdlcReceiveDrops = _AptisHdlcReceiveDrops_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 2),
    _AptisHdlcReceiveDrops_Type()
)
aptisHdlcReceiveDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcReceiveDrops.setStatus("mandatory")
_AptisHdlcTransmitDrops_Type = Counter32
_AptisHdlcTransmitDrops_Object = MibTableColumn
aptisHdlcTransmitDrops = _AptisHdlcTransmitDrops_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 3),
    _AptisHdlcTransmitDrops_Type()
)
aptisHdlcTransmitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcTransmitDrops.setStatus("mandatory")
_AptisHdlcSysErrors_Type = Counter32
_AptisHdlcSysErrors_Object = MibTableColumn
aptisHdlcSysErrors = _AptisHdlcSysErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 4),
    _AptisHdlcSysErrors_Type()
)
aptisHdlcSysErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcSysErrors.setStatus("mandatory")
_AptisHdlcParityErrors_Type = Counter32
_AptisHdlcParityErrors_Object = MibTableColumn
aptisHdlcParityErrors = _AptisHdlcParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 5),
    _AptisHdlcParityErrors_Type()
)
aptisHdlcParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcParityErrors.setStatus("mandatory")
_AptisHdlcFCSErrors_Type = Counter32
_AptisHdlcFCSErrors_Object = MibTableColumn
aptisHdlcFCSErrors = _AptisHdlcFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 6),
    _AptisHdlcFCSErrors_Type()
)
aptisHdlcFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcFCSErrors.setStatus("mandatory")
_AptisHdlcAborts_Type = Counter32
_AptisHdlcAborts_Object = MibTableColumn
aptisHdlcAborts = _AptisHdlcAborts_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 7),
    _AptisHdlcAborts_Type()
)
aptisHdlcAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcAborts.setStatus("mandatory")
_AptisHdlcFramingErrors_Type = Counter32
_AptisHdlcFramingErrors_Object = MibTableColumn
aptisHdlcFramingErrors = _AptisHdlcFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 8),
    _AptisHdlcFramingErrors_Type()
)
aptisHdlcFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcFramingErrors.setStatus("mandatory")
_AptisHdlcReceiveOverruns_Type = Counter32
_AptisHdlcReceiveOverruns_Object = MibTableColumn
aptisHdlcReceiveOverruns = _AptisHdlcReceiveOverruns_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 9),
    _AptisHdlcReceiveOverruns_Type()
)
aptisHdlcReceiveOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcReceiveOverruns.setStatus("mandatory")
_AptisHdlcTransmitUnderflows_Type = Counter32
_AptisHdlcTransmitUnderflows_Object = MibTableColumn
aptisHdlcTransmitUnderflows = _AptisHdlcTransmitUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 1, 1, 10),
    _AptisHdlcTransmitUnderflows_Type()
)
aptisHdlcTransmitUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcTransmitUnderflows.setStatus("mandatory")
_AptisHdlcChannelTable_Object = MibTable
aptisHdlcChannelTable = _AptisHdlcChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2)
)
if mibBuilder.loadTexts:
    aptisHdlcChannelTable.setStatus("mandatory")
_AptisHdlcChannelEntry_Object = MibTableRow
aptisHdlcChannelEntry = _AptisHdlcChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1)
)
aptisHdlcChannelEntry.setIndexNames(
    (0, "APTIS-HDLC-MIB", "aptisHdlcIfIndex"),
    (0, "APTIS-HDLC-MIB", "aptisHdlcChannelIfIndex"),
)
if mibBuilder.loadTexts:
    aptisHdlcChannelEntry.setStatus("mandatory")
_AptisHdlcChannelIfIndex_Type = Index
_AptisHdlcChannelIfIndex_Object = MibTableColumn
aptisHdlcChannelIfIndex = _AptisHdlcChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 1),
    _AptisHdlcChannelIfIndex_Type()
)
aptisHdlcChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelIfIndex.setStatus("mandatory")


class _AptisHdlcChannelStatus_Type(Integer32):
    """Custom type aptisHdlcChannelStatus based on Integer32"""
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
        *(("disabled", 3),
          ("down", 2),
          ("init", 1),
          ("smconnnectwait", 4),
          ("smdisconnectwait", 6),
          ("up", 5))
    )


_AptisHdlcChannelStatus_Type.__name__ = "Integer32"
_AptisHdlcChannelStatus_Object = MibTableColumn
aptisHdlcChannelStatus = _AptisHdlcChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 2),
    _AptisHdlcChannelStatus_Type()
)
aptisHdlcChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelStatus.setStatus("mandatory")
_AptisHdlcChannelRcvFrames_Type = Counter32
_AptisHdlcChannelRcvFrames_Object = MibTableColumn
aptisHdlcChannelRcvFrames = _AptisHdlcChannelRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 3),
    _AptisHdlcChannelRcvFrames_Type()
)
aptisHdlcChannelRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvFrames.setStatus("mandatory")
_AptisHdlcChannelRcvOctets_Type = Counter32
_AptisHdlcChannelRcvOctets_Object = MibTableColumn
aptisHdlcChannelRcvOctets = _AptisHdlcChannelRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 4),
    _AptisHdlcChannelRcvOctets_Type()
)
aptisHdlcChannelRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvOctets.setStatus("mandatory")
_AptisHdlcChannelRcvDrops_Type = Counter32
_AptisHdlcChannelRcvDrops_Object = MibTableColumn
aptisHdlcChannelRcvDrops = _AptisHdlcChannelRcvDrops_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 5),
    _AptisHdlcChannelRcvDrops_Type()
)
aptisHdlcChannelRcvDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvDrops.setStatus("mandatory")
_AptisHdlcChannelRcvMaxPacket_Type = Counter32
_AptisHdlcChannelRcvMaxPacket_Object = MibTableColumn
aptisHdlcChannelRcvMaxPacket = _AptisHdlcChannelRcvMaxPacket_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 6),
    _AptisHdlcChannelRcvMaxPacket_Type()
)
aptisHdlcChannelRcvMaxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvMaxPacket.setStatus("mandatory")
_AptisHdlcChannelRcvOverruns_Type = Counter32
_AptisHdlcChannelRcvOverruns_Object = MibTableColumn
aptisHdlcChannelRcvOverruns = _AptisHdlcChannelRcvOverruns_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 7),
    _AptisHdlcChannelRcvOverruns_Type()
)
aptisHdlcChannelRcvOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvOverruns.setStatus("mandatory")
_AptisHdlcChannelRcvFCSErrors_Type = Counter32
_AptisHdlcChannelRcvFCSErrors_Object = MibTableColumn
aptisHdlcChannelRcvFCSErrors = _AptisHdlcChannelRcvFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 8),
    _AptisHdlcChannelRcvFCSErrors_Type()
)
aptisHdlcChannelRcvFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvFCSErrors.setStatus("mandatory")
_AptisHdlcChannelRcvByteAlign_Type = Counter32
_AptisHdlcChannelRcvByteAlign_Object = MibTableColumn
aptisHdlcChannelRcvByteAlign = _AptisHdlcChannelRcvByteAlign_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 9),
    _AptisHdlcChannelRcvByteAlign_Type()
)
aptisHdlcChannelRcvByteAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvByteAlign.setStatus("mandatory")
_AptisHdlcChannelRcvAborts_Type = Counter32
_AptisHdlcChannelRcvAborts_Object = MibTableColumn
aptisHdlcChannelRcvAborts = _AptisHdlcChannelRcvAborts_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 10),
    _AptisHdlcChannelRcvAborts_Type()
)
aptisHdlcChannelRcvAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelRcvAborts.setStatus("mandatory")
_AptisHdlcChannelTransmitFrames_Type = Counter32
_AptisHdlcChannelTransmitFrames_Object = MibTableColumn
aptisHdlcChannelTransmitFrames = _AptisHdlcChannelTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 11),
    _AptisHdlcChannelTransmitFrames_Type()
)
aptisHdlcChannelTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelTransmitFrames.setStatus("mandatory")
_AptisHdlcChannelTransmitOctets_Type = Counter32
_AptisHdlcChannelTransmitOctets_Object = MibTableColumn
aptisHdlcChannelTransmitOctets = _AptisHdlcChannelTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 12),
    _AptisHdlcChannelTransmitOctets_Type()
)
aptisHdlcChannelTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelTransmitOctets.setStatus("mandatory")
_AptisHdlcChannelTransmitDrops_Type = Counter32
_AptisHdlcChannelTransmitDrops_Object = MibTableColumn
aptisHdlcChannelTransmitDrops = _AptisHdlcChannelTransmitDrops_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 13),
    _AptisHdlcChannelTransmitDrops_Type()
)
aptisHdlcChannelTransmitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelTransmitDrops.setStatus("mandatory")
_AptisHdlcChannelTransmitUnderflows_Type = Counter32
_AptisHdlcChannelTransmitUnderflows_Object = MibTableColumn
aptisHdlcChannelTransmitUnderflows = _AptisHdlcChannelTransmitUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 14),
    _AptisHdlcChannelTransmitUnderflows_Type()
)
aptisHdlcChannelTransmitUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelTransmitUnderflows.setStatus("mandatory")
_AptisHdlcChannelTransmitBuffer_Type = Counter32
_AptisHdlcChannelTransmitBuffer_Object = MibTableColumn
aptisHdlcChannelTransmitBuffer = _AptisHdlcChannelTransmitBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 7, 2, 1, 15),
    _AptisHdlcChannelTransmitBuffer_Type()
)
aptisHdlcChannelTransmitBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisHdlcChannelTransmitBuffer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-HDLC-MIB",
    **{"Index": Index,
       "aptisHdlc": aptisHdlc,
       "aptisHdlcTable": aptisHdlcTable,
       "aptisHdlcEntry": aptisHdlcEntry,
       "aptisHdlcIfIndex": aptisHdlcIfIndex,
       "aptisHdlcReceiveDrops": aptisHdlcReceiveDrops,
       "aptisHdlcTransmitDrops": aptisHdlcTransmitDrops,
       "aptisHdlcSysErrors": aptisHdlcSysErrors,
       "aptisHdlcParityErrors": aptisHdlcParityErrors,
       "aptisHdlcFCSErrors": aptisHdlcFCSErrors,
       "aptisHdlcAborts": aptisHdlcAborts,
       "aptisHdlcFramingErrors": aptisHdlcFramingErrors,
       "aptisHdlcReceiveOverruns": aptisHdlcReceiveOverruns,
       "aptisHdlcTransmitUnderflows": aptisHdlcTransmitUnderflows,
       "aptisHdlcChannelTable": aptisHdlcChannelTable,
       "aptisHdlcChannelEntry": aptisHdlcChannelEntry,
       "aptisHdlcChannelIfIndex": aptisHdlcChannelIfIndex,
       "aptisHdlcChannelStatus": aptisHdlcChannelStatus,
       "aptisHdlcChannelRcvFrames": aptisHdlcChannelRcvFrames,
       "aptisHdlcChannelRcvOctets": aptisHdlcChannelRcvOctets,
       "aptisHdlcChannelRcvDrops": aptisHdlcChannelRcvDrops,
       "aptisHdlcChannelRcvMaxPacket": aptisHdlcChannelRcvMaxPacket,
       "aptisHdlcChannelRcvOverruns": aptisHdlcChannelRcvOverruns,
       "aptisHdlcChannelRcvFCSErrors": aptisHdlcChannelRcvFCSErrors,
       "aptisHdlcChannelRcvByteAlign": aptisHdlcChannelRcvByteAlign,
       "aptisHdlcChannelRcvAborts": aptisHdlcChannelRcvAborts,
       "aptisHdlcChannelTransmitFrames": aptisHdlcChannelTransmitFrames,
       "aptisHdlcChannelTransmitOctets": aptisHdlcChannelTransmitOctets,
       "aptisHdlcChannelTransmitDrops": aptisHdlcChannelTransmitDrops,
       "aptisHdlcChannelTransmitUnderflows": aptisHdlcChannelTransmitUnderflows,
       "aptisHdlcChannelTransmitBuffer": aptisHdlcChannelTransmitBuffer}
)
