# SNMP MIB module (A3COM-HUAWEI-VODIGITALIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VODIGITALIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:21 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

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

h3cVoiceDigitalInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4)
)
h3cVoiceDigitalInterface.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoDigitalIfCommonObjects_ObjectIdentity = ObjectIdentity
h3cVoDigitalIfCommonObjects = _H3cVoDigitalIfCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1)
)
_H3cVoDigitalIfCommonCfgTable_Object = MibTable
h3cVoDigitalIfCommonCfgTable = _H3cVoDigitalIfCommonCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfCommonCfgTable.setStatus("current")
_H3cVoDigitalIfCommonCfgEntry_Object = MibTableRow
h3cVoDigitalIfCommonCfgEntry = _H3cVoDigitalIfCommonCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1, 1)
)
h3cVoDigitalIfCommonCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfCfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfCfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfCommonCfgEntry.setStatus("current")
_H3cVoDIfCfgPort_Type = Integer32
_H3cVoDIfCfgPort_Object = MibTableColumn
h3cVoDIfCfgPort = _H3cVoDIfCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1, 1, 1),
    _H3cVoDIfCfgPort_Type()
)
h3cVoDIfCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfCfgPort.setStatus("current")
_H3cVoDIfCfgGroup_Type = Integer32
_H3cVoDIfCfgGroup_Object = MibTableColumn
h3cVoDIfCfgGroup = _H3cVoDIfCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1, 1, 2),
    _H3cVoDIfCfgGroup_Type()
)
h3cVoDIfCfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfCfgGroup.setStatus("current")


class _H3cVoDIfCfgBoardType_Type(Integer32):
    """Custom type h3cVoDIfCfgBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1vi", 1),
          ("t1vi", 2))
    )


_H3cVoDIfCfgBoardType_Type.__name__ = "Integer32"
_H3cVoDIfCfgBoardType_Object = MibTableColumn
h3cVoDIfCfgBoardType = _H3cVoDIfCfgBoardType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1, 1, 3),
    _H3cVoDIfCfgBoardType_Type()
)
h3cVoDIfCfgBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfCfgBoardType.setStatus("current")


class _H3cVoDIfCfgSignalType_Type(Integer32):
    """Custom type h3cVoDIfCfgSignalType based on Integer32"""
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
        *(("emDelayStart", 4),
          ("emImmediateStart", 3),
          ("emWinkStart", 5),
          ("pri", 2),
          ("r2", 1))
    )


_H3cVoDIfCfgSignalType_Type.__name__ = "Integer32"
_H3cVoDIfCfgSignalType_Object = MibTableColumn
h3cVoDIfCfgSignalType = _H3cVoDIfCfgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1, 1, 4),
    _H3cVoDIfCfgSignalType_Type()
)
h3cVoDIfCfgSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfCfgSignalType.setStatus("current")
_H3cVoDIfCfgTsInformation_Type = OctetString
_H3cVoDIfCfgTsInformation_Object = MibTableColumn
h3cVoDIfCfgTsInformation = _H3cVoDIfCfgTsInformation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1, 1, 5),
    _H3cVoDIfCfgTsInformation_Type()
)
h3cVoDIfCfgTsInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfCfgTsInformation.setStatus("current")
_H3cVoDIfCfgPortSubLine_Type = OctetString
_H3cVoDIfCfgPortSubLine_Object = MibTableColumn
h3cVoDIfCfgPortSubLine = _H3cVoDIfCfgPortSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 1, 1, 1, 6),
    _H3cVoDIfCfgPortSubLine_Type()
)
h3cVoDIfCfgPortSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfCfgPortSubLine.setStatus("current")
_H3cVoDigitalIfEMObjects_ObjectIdentity = ObjectIdentity
h3cVoDigitalIfEMObjects = _H3cVoDigitalIfEMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2)
)
_H3cVoDigitalIfEMCfgTable_Object = MibTable
h3cVoDigitalIfEMCfgTable = _H3cVoDigitalIfEMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfEMCfgTable.setStatus("current")
_H3cVoDigitalIfEMCfgEntry_Object = MibTableRow
h3cVoDigitalIfEMCfgEntry = _H3cVoDigitalIfEMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1, 1)
)
h3cVoDigitalIfEMCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfEMCfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfEMCfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfEMCfgEntry.setStatus("current")
_H3cVoDIfEMCfgPort_Type = Integer32
_H3cVoDIfEMCfgPort_Object = MibTableColumn
h3cVoDIfEMCfgPort = _H3cVoDIfEMCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1, 1, 1),
    _H3cVoDIfEMCfgPort_Type()
)
h3cVoDIfEMCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfEMCfgPort.setStatus("current")
_H3cVoDIfEMCfgGroup_Type = Integer32
_H3cVoDIfEMCfgGroup_Object = MibTableColumn
h3cVoDIfEMCfgGroup = _H3cVoDIfEMCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1, 1, 2),
    _H3cVoDIfEMCfgGroup_Type()
)
h3cVoDIfEMCfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfEMCfgGroup.setStatus("current")
_H3cVoDIfEMCfgTimeoutInterDigit_Type = Integer32
_H3cVoDIfEMCfgTimeoutInterDigit_Object = MibTableColumn
h3cVoDIfEMCfgTimeoutInterDigit = _H3cVoDIfEMCfgTimeoutInterDigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1, 1, 3),
    _H3cVoDIfEMCfgTimeoutInterDigit_Type()
)
h3cVoDIfEMCfgTimeoutInterDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMCfgTimeoutInterDigit.setStatus("current")
_H3cVoDIfEMCfgTimeoutRinging_Type = Integer32
_H3cVoDIfEMCfgTimeoutRinging_Object = MibTableColumn
h3cVoDIfEMCfgTimeoutRinging = _H3cVoDIfEMCfgTimeoutRinging_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1, 1, 4),
    _H3cVoDIfEMCfgTimeoutRinging_Type()
)
h3cVoDIfEMCfgTimeoutRinging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMCfgTimeoutRinging.setStatus("current")
_H3cVoDIfEMCfgTimeoutWaitDigit_Type = Integer32
_H3cVoDIfEMCfgTimeoutWaitDigit_Object = MibTableColumn
h3cVoDIfEMCfgTimeoutWaitDigit = _H3cVoDIfEMCfgTimeoutWaitDigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1, 1, 5),
    _H3cVoDIfEMCfgTimeoutWaitDigit_Type()
)
h3cVoDIfEMCfgTimeoutWaitDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMCfgTimeoutWaitDigit.setStatus("current")
_H3cVoDIfEMCfgPortSubLine_Type = OctetString
_H3cVoDIfEMCfgPortSubLine_Object = MibTableColumn
h3cVoDIfEMCfgPortSubLine = _H3cVoDIfEMCfgPortSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 1, 1, 6),
    _H3cVoDIfEMCfgPortSubLine_Type()
)
h3cVoDIfEMCfgPortSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfEMCfgPortSubLine.setStatus("current")
_H3cVoDigitalIfEMABCDCfgTable_Object = MibTable
h3cVoDigitalIfEMABCDCfgTable = _H3cVoDigitalIfEMABCDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfEMABCDCfgTable.setStatus("current")
_H3cVoDigitalIfEMABCDCfgEntry_Object = MibTableRow
h3cVoDigitalIfEMABCDCfgEntry = _H3cVoDigitalIfEMABCDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1)
)
h3cVoDigitalIfEMABCDCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfEMABCDCfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfEMABCDCfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfEMABCDCfgEntry.setStatus("current")
_H3cVoDIfEMABCDCfgPort_Type = Integer32
_H3cVoDIfEMABCDCfgPort_Object = MibTableColumn
h3cVoDIfEMABCDCfgPort = _H3cVoDIfEMABCDCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1, 1),
    _H3cVoDIfEMABCDCfgPort_Type()
)
h3cVoDIfEMABCDCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfEMABCDCfgPort.setStatus("current")
_H3cVoDIfEMABCDCfgGroup_Type = Integer32
_H3cVoDIfEMABCDCfgGroup_Object = MibTableColumn
h3cVoDIfEMABCDCfgGroup = _H3cVoDIfEMABCDCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1, 2),
    _H3cVoDIfEMABCDCfgGroup_Type()
)
h3cVoDIfEMABCDCfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfEMABCDCfgGroup.setStatus("current")


class _H3cVoDIfEMABCDRxIdle_Type(OctetString):
    """Custom type h3cVoDIfEMABCDRxIdle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfEMABCDRxIdle_Type.__name__ = "OctetString"
_H3cVoDIfEMABCDRxIdle_Object = MibTableColumn
h3cVoDIfEMABCDRxIdle = _H3cVoDIfEMABCDRxIdle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1, 3),
    _H3cVoDIfEMABCDRxIdle_Type()
)
h3cVoDIfEMABCDRxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMABCDRxIdle.setStatus("current")


class _H3cVoDIfEMABCDRxSeizure_Type(OctetString):
    """Custom type h3cVoDIfEMABCDRxSeizure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfEMABCDRxSeizure_Type.__name__ = "OctetString"
_H3cVoDIfEMABCDRxSeizure_Object = MibTableColumn
h3cVoDIfEMABCDRxSeizure = _H3cVoDIfEMABCDRxSeizure_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1, 4),
    _H3cVoDIfEMABCDRxSeizure_Type()
)
h3cVoDIfEMABCDRxSeizure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMABCDRxSeizure.setStatus("current")


class _H3cVoDIfEMABCDTxIdle_Type(OctetString):
    """Custom type h3cVoDIfEMABCDTxIdle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfEMABCDTxIdle_Type.__name__ = "OctetString"
_H3cVoDIfEMABCDTxIdle_Object = MibTableColumn
h3cVoDIfEMABCDTxIdle = _H3cVoDIfEMABCDTxIdle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1, 5),
    _H3cVoDIfEMABCDTxIdle_Type()
)
h3cVoDIfEMABCDTxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMABCDTxIdle.setStatus("current")


class _H3cVoDIfEMABCDTxSeizure_Type(OctetString):
    """Custom type h3cVoDIfEMABCDTxSeizure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfEMABCDTxSeizure_Type.__name__ = "OctetString"
_H3cVoDIfEMABCDTxSeizure_Object = MibTableColumn
h3cVoDIfEMABCDTxSeizure = _H3cVoDIfEMABCDTxSeizure_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1, 6),
    _H3cVoDIfEMABCDTxSeizure_Type()
)
h3cVoDIfEMABCDTxSeizure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMABCDTxSeizure.setStatus("current")
_H3cVoDIFEMABCDSubLine_Type = OctetString
_H3cVoDIFEMABCDSubLine_Object = MibTableColumn
h3cVoDIFEMABCDSubLine = _H3cVoDIFEMABCDSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 2, 1, 7),
    _H3cVoDIFEMABCDSubLine_Type()
)
h3cVoDIFEMABCDSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIFEMABCDSubLine.setStatus("current")
_H3cVoDigitalIfEMTimerTable_Object = MibTable
h3cVoDigitalIfEMTimerTable = _H3cVoDigitalIfEMTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfEMTimerTable.setStatus("current")
_H3cVoDigitalIfEMTimerEntry_Object = MibTableRow
h3cVoDigitalIfEMTimerEntry = _H3cVoDigitalIfEMTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1)
)
h3cVoDigitalIfEMTimerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfEMTimerPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfEMTimerGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfEMTimerEntry.setStatus("current")
_H3cVoDIfEMTimerPort_Type = Integer32
_H3cVoDIfEMTimerPort_Object = MibTableColumn
h3cVoDIfEMTimerPort = _H3cVoDIfEMTimerPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 1),
    _H3cVoDIfEMTimerPort_Type()
)
h3cVoDIfEMTimerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerPort.setStatus("current")
_H3cVoDIfEMTimerGroup_Type = Integer32
_H3cVoDIfEMTimerGroup_Object = MibTableColumn
h3cVoDIfEMTimerGroup = _H3cVoDIfEMTimerGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 2),
    _H3cVoDIfEMTimerGroup_Type()
)
h3cVoDIfEMTimerGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerGroup.setStatus("current")


class _H3cVoDIfEMTimerSendWink_Type(Integer32):
    """Custom type h3cVoDIfEMTimerSendWink based on Integer32"""
    defaultValue = 200


_H3cVoDIfEMTimerSendWink_Object = MibTableColumn
h3cVoDIfEMTimerSendWink = _H3cVoDIfEMTimerSendWink_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 4),
    _H3cVoDIfEMTimerSendWink_Type()
)
h3cVoDIfEMTimerSendWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerSendWink.setStatus("current")
_H3cVoDIfEMTimerWinkRising_Type = Integer32
_H3cVoDIfEMTimerWinkRising_Object = MibTableColumn
h3cVoDIfEMTimerWinkRising = _H3cVoDIfEMTimerWinkRising_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 5),
    _H3cVoDIfEMTimerWinkRising_Type()
)
h3cVoDIfEMTimerWinkRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerWinkRising.setStatus("current")
_H3cVoDIfEMTimerWinkHold_Type = Integer32
_H3cVoDIfEMTimerWinkHold_Object = MibTableColumn
h3cVoDIfEMTimerWinkHold = _H3cVoDIfEMTimerWinkHold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 6),
    _H3cVoDIfEMTimerWinkHold_Type()
)
h3cVoDIfEMTimerWinkHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerWinkHold.setStatus("current")
_H3cVoDIfEMTimerDialoutDelay_Type = Integer32
_H3cVoDIfEMTimerDialoutDelay_Object = MibTableColumn
h3cVoDIfEMTimerDialoutDelay = _H3cVoDIfEMTimerDialoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 7),
    _H3cVoDIfEMTimerDialoutDelay_Type()
)
h3cVoDIfEMTimerDialoutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerDialoutDelay.setStatus("current")
_H3cVoDIfEMTimerDelayRising_Type = Integer32
_H3cVoDIfEMTimerDelayRising_Object = MibTableColumn
h3cVoDIfEMTimerDelayRising = _H3cVoDIfEMTimerDelayRising_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 8),
    _H3cVoDIfEMTimerDelayRising_Type()
)
h3cVoDIfEMTimerDelayRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerDelayRising.setStatus("current")
_H3cVoDIfEMTimerDelayHold_Type = Integer32
_H3cVoDIfEMTimerDelayHold_Object = MibTableColumn
h3cVoDIfEMTimerDelayHold = _H3cVoDIfEMTimerDelayHold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 9),
    _H3cVoDIfEMTimerDelayHold_Type()
)
h3cVoDIfEMTimerDelayHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerDelayHold.setStatus("current")
_H3cVoDIfEMTimerDtmf_Type = Integer32
_H3cVoDIfEMTimerDtmf_Object = MibTableColumn
h3cVoDIfEMTimerDtmf = _H3cVoDIfEMTimerDtmf_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 10),
    _H3cVoDIfEMTimerDtmf_Type()
)
h3cVoDIfEMTimerDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerDtmf.setStatus("current")
_H3cVoDIfEMTimerDtmfInterval_Type = Integer32
_H3cVoDIfEMTimerDtmfInterval_Object = MibTableColumn
h3cVoDIfEMTimerDtmfInterval = _H3cVoDIfEMTimerDtmfInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 11),
    _H3cVoDIfEMTimerDtmfInterval_Type()
)
h3cVoDIfEMTimerDtmfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerDtmfInterval.setStatus("current")
_H3cVoDIfEMTimerPortSubLine_Type = OctetString
_H3cVoDIfEMTimerPortSubLine_Object = MibTableColumn
h3cVoDIfEMTimerPortSubLine = _H3cVoDIfEMTimerPortSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 2, 4, 1, 12),
    _H3cVoDIfEMTimerPortSubLine_Type()
)
h3cVoDIfEMTimerPortSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfEMTimerPortSubLine.setStatus("current")
_H3cVoDigitalIfR2Objects_ObjectIdentity = ObjectIdentity
h3cVoDigitalIfR2Objects = _H3cVoDigitalIfR2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3)
)
_H3cVoDigitalIfR2CfgTable_Object = MibTable
h3cVoDigitalIfR2CfgTable = _H3cVoDigitalIfR2CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2CfgTable.setStatus("current")
_H3cVoDigitalIfR2CfgEntry_Object = MibTableRow
h3cVoDigitalIfR2CfgEntry = _H3cVoDigitalIfR2CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1)
)
h3cVoDigitalIfR2CfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2CfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2CfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2CfgEntry.setStatus("current")
_H3cVoDIfR2CfgPort_Type = Integer32
_H3cVoDIfR2CfgPort_Object = MibTableColumn
h3cVoDIfR2CfgPort = _H3cVoDIfR2CfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1, 1),
    _H3cVoDIfR2CfgPort_Type()
)
h3cVoDIfR2CfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgPort.setStatus("current")
_H3cVoDIfR2CfgGroup_Type = Integer32
_H3cVoDIfR2CfgGroup_Object = MibTableColumn
h3cVoDIfR2CfgGroup = _H3cVoDIfR2CfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1, 2),
    _H3cVoDIfR2CfgGroup_Type()
)
h3cVoDIfR2CfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgGroup.setStatus("current")


class _H3cVoDIfR2CfgCountryMode_Type(Integer32):
    """Custom type h3cVoDIfR2CfgCountryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("argentina", 2),
          ("australia", 3),
          ("bengal", 4),
          ("brazil", 5),
          ("china", 6),
          ("customer", 1),
          ("hongkong", 7),
          ("india", 8),
          ("indonesia", 9),
          ("itut", 10),
          ("korea", 11),
          ("malaysia", 12),
          ("mexico", 13),
          ("newzealand", 14),
          ("singapore", 15),
          ("thailand", 16))
    )


_H3cVoDIfR2CfgCountryMode_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgCountryMode_Object = MibTableColumn
h3cVoDIfR2CfgCountryMode = _H3cVoDIfR2CfgCountryMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1, 3),
    _H3cVoDIfR2CfgCountryMode_Type()
)
h3cVoDIfR2CfgCountryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgCountryMode.setStatus("current")


class _H3cVoDIfR2CfgSpecialChar_Type(Integer32):
    """Custom type h3cVoDIfR2CfgSpecialChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              35,
              42,
              65,
              66,
              67,
              68)
        )
    )
    namedValues = NamedValues(
        *(("a", 65),
          ("asterisk", 42),
          ("b", 66),
          ("c", 67),
          ("d", 68),
          ("null", 0),
          ("pound", 35))
    )


_H3cVoDIfR2CfgSpecialChar_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgSpecialChar_Object = MibTableColumn
h3cVoDIfR2CfgSpecialChar = _H3cVoDIfR2CfgSpecialChar_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1, 4),
    _H3cVoDIfR2CfgSpecialChar_Type()
)
h3cVoDIfR2CfgSpecialChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgSpecialChar.setStatus("current")


class _H3cVoDIfR2CfgSpecialSignal_Type(Integer32):
    """Custom type h3cVoDIfR2CfgSpecialSignal based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(11, 16),
    )


_H3cVoDIfR2CfgSpecialSignal_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgSpecialSignal_Object = MibTableColumn
h3cVoDIfR2CfgSpecialSignal = _H3cVoDIfR2CfgSpecialSignal_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1, 5),
    _H3cVoDIfR2CfgSpecialSignal_Type()
)
h3cVoDIfR2CfgSpecialSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgSpecialSignal.setStatus("current")


class _H3cVoDIfR2CfgSelectMode_Type(Integer32):
    """Custom type h3cVoDIfR2CfgSelectMode based on Integer32"""
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
        *(("max", 2),
          ("maxpoll", 4),
          ("min", 1),
          ("minpoll", 3))
    )


_H3cVoDIfR2CfgSelectMode_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgSelectMode_Object = MibTableColumn
h3cVoDIfR2CfgSelectMode = _H3cVoDIfR2CfgSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1, 6),
    _H3cVoDIfR2CfgSelectMode_Type()
)
h3cVoDIfR2CfgSelectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgSelectMode.setStatus("current")
_H3cVoDIFR2CfgSubLine_Type = OctetString
_H3cVoDIFR2CfgSubLine_Object = MibTableColumn
h3cVoDIFR2CfgSubLine = _H3cVoDIFR2CfgSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 1, 1, 7),
    _H3cVoDIFR2CfgSubLine_Type()
)
h3cVoDIFR2CfgSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIFR2CfgSubLine.setStatus("current")
_H3cVoDigitalIfR2ABCDCfgTable_Object = MibTable
h3cVoDigitalIfR2ABCDCfgTable = _H3cVoDigitalIfR2ABCDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2ABCDCfgTable.setStatus("current")
_H3cVoDigitalIfR2ABCDCfgEntry_Object = MibTableRow
h3cVoDigitalIfR2ABCDCfgEntry = _H3cVoDigitalIfR2ABCDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1)
)
h3cVoDigitalIfR2ABCDCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2ABCDCfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2ABCDCfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2ABCDCfgEntry.setStatus("current")
_H3cVoDIfR2ABCDCfgPort_Type = Integer32
_H3cVoDIfR2ABCDCfgPort_Object = MibTableColumn
h3cVoDIfR2ABCDCfgPort = _H3cVoDIfR2ABCDCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 1),
    _H3cVoDIfR2ABCDCfgPort_Type()
)
h3cVoDIfR2ABCDCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDCfgPort.setStatus("current")
_H3cVoDIfR2ABCDCfgGroup_Type = Integer32
_H3cVoDIfR2ABCDCfgGroup_Object = MibTableColumn
h3cVoDIfR2ABCDCfgGroup = _H3cVoDIfR2ABCDCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 2),
    _H3cVoDIfR2ABCDCfgGroup_Type()
)
h3cVoDIfR2ABCDCfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDCfgGroup.setStatus("current")


class _H3cVoDIfR2ABCDReverseABCD_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDReverseABCD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDReverseABCD_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDReverseABCD_Object = MibTableColumn
h3cVoDIfR2ABCDReverseABCD = _H3cVoDIfR2ABCDReverseABCD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 3),
    _H3cVoDIfR2ABCDReverseABCD_Type()
)
h3cVoDIfR2ABCDReverseABCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDReverseABCD.setStatus("current")


class _H3cVoDIfR2ABCDRenewABCD_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRenewABCD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRenewABCD_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRenewABCD_Object = MibTableColumn
h3cVoDIfR2ABCDRenewABCD = _H3cVoDIfR2ABCDRenewABCD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 4),
    _H3cVoDIfR2ABCDRenewABCD_Type()
)
h3cVoDIfR2ABCDRenewABCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRenewABCD.setStatus("current")


class _H3cVoDIfR2ABCDRxIdle_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxIdle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxIdle_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxIdle_Object = MibTableColumn
h3cVoDIfR2ABCDRxIdle = _H3cVoDIfR2ABCDRxIdle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 5),
    _H3cVoDIfR2ABCDRxIdle_Type()
)
h3cVoDIfR2ABCDRxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxIdle.setStatus("current")


class _H3cVoDIfR2ABCDTxIdle_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxIdle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxIdle_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxIdle_Object = MibTableColumn
h3cVoDIfR2ABCDTxIdle = _H3cVoDIfR2ABCDTxIdle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 6),
    _H3cVoDIfR2ABCDTxIdle_Type()
)
h3cVoDIfR2ABCDTxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxIdle.setStatus("current")


class _H3cVoDIfR2ABCDRxSeizure_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxSeizure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxSeizure_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxSeizure_Object = MibTableColumn
h3cVoDIfR2ABCDRxSeizure = _H3cVoDIfR2ABCDRxSeizure_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 7),
    _H3cVoDIfR2ABCDRxSeizure_Type()
)
h3cVoDIfR2ABCDRxSeizure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxSeizure.setStatus("current")


class _H3cVoDIfR2ABCDTxSeizure_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxSeizure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxSeizure_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxSeizure_Object = MibTableColumn
h3cVoDIfR2ABCDTxSeizure = _H3cVoDIfR2ABCDTxSeizure_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 8),
    _H3cVoDIfR2ABCDTxSeizure_Type()
)
h3cVoDIfR2ABCDTxSeizure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxSeizure.setStatus("current")


class _H3cVoDIfR2ABCDRxSeizureAck_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxSeizureAck based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxSeizureAck_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxSeizureAck_Object = MibTableColumn
h3cVoDIfR2ABCDRxSeizureAck = _H3cVoDIfR2ABCDRxSeizureAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 9),
    _H3cVoDIfR2ABCDRxSeizureAck_Type()
)
h3cVoDIfR2ABCDRxSeizureAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxSeizureAck.setStatus("current")


class _H3cVoDIfR2ABCDTxSeizureAck_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxSeizureAck based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxSeizureAck_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxSeizureAck_Object = MibTableColumn
h3cVoDIfR2ABCDTxSeizureAck = _H3cVoDIfR2ABCDTxSeizureAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 10),
    _H3cVoDIfR2ABCDTxSeizureAck_Type()
)
h3cVoDIfR2ABCDTxSeizureAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxSeizureAck.setStatus("current")


class _H3cVoDIfR2ABCDRxAnswer_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxAnswer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxAnswer_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxAnswer_Object = MibTableColumn
h3cVoDIfR2ABCDRxAnswer = _H3cVoDIfR2ABCDRxAnswer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 11),
    _H3cVoDIfR2ABCDRxAnswer_Type()
)
h3cVoDIfR2ABCDRxAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxAnswer.setStatus("current")


class _H3cVoDIfR2ABCDTxAnswer_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxAnswer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxAnswer_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxAnswer_Object = MibTableColumn
h3cVoDIfR2ABCDTxAnswer = _H3cVoDIfR2ABCDTxAnswer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 12),
    _H3cVoDIfR2ABCDTxAnswer_Type()
)
h3cVoDIfR2ABCDTxAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxAnswer.setStatus("current")


class _H3cVoDIfR2ABCDRxClearForward_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxClearForward based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxClearForward_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxClearForward_Object = MibTableColumn
h3cVoDIfR2ABCDRxClearForward = _H3cVoDIfR2ABCDRxClearForward_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 13),
    _H3cVoDIfR2ABCDRxClearForward_Type()
)
h3cVoDIfR2ABCDRxClearForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxClearForward.setStatus("current")


class _H3cVoDIfR2ABCDTxClearForward_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxClearForward based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxClearForward_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxClearForward_Object = MibTableColumn
h3cVoDIfR2ABCDTxClearForward = _H3cVoDIfR2ABCDTxClearForward_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 14),
    _H3cVoDIfR2ABCDTxClearForward_Type()
)
h3cVoDIfR2ABCDTxClearForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxClearForward.setStatus("current")


class _H3cVoDIfR2ABCDRxClearBack_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxClearBack based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxClearBack_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxClearBack_Object = MibTableColumn
h3cVoDIfR2ABCDRxClearBack = _H3cVoDIfR2ABCDRxClearBack_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 15),
    _H3cVoDIfR2ABCDRxClearBack_Type()
)
h3cVoDIfR2ABCDRxClearBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxClearBack.setStatus("current")


class _H3cVoDIfR2ABCDTxClearBack_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxClearBack based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxClearBack_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxClearBack_Object = MibTableColumn
h3cVoDIfR2ABCDTxClearBack = _H3cVoDIfR2ABCDTxClearBack_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 16),
    _H3cVoDIfR2ABCDTxClearBack_Type()
)
h3cVoDIfR2ABCDTxClearBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxClearBack.setStatus("current")


class _H3cVoDIfR2ABCDRxReleaseGuard_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxReleaseGuard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxReleaseGuard_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxReleaseGuard_Object = MibTableColumn
h3cVoDIfR2ABCDRxReleaseGuard = _H3cVoDIfR2ABCDRxReleaseGuard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 17),
    _H3cVoDIfR2ABCDRxReleaseGuard_Type()
)
h3cVoDIfR2ABCDRxReleaseGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxReleaseGuard.setStatus("current")


class _H3cVoDIfR2ABCDTxReleaseGuard_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxReleaseGuard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxReleaseGuard_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxReleaseGuard_Object = MibTableColumn
h3cVoDIfR2ABCDTxReleaseGuard = _H3cVoDIfR2ABCDTxReleaseGuard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 18),
    _H3cVoDIfR2ABCDTxReleaseGuard_Type()
)
h3cVoDIfR2ABCDTxReleaseGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxReleaseGuard.setStatus("current")


class _H3cVoDIfR2ABCDRxBlocking_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDRxBlocking based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDRxBlocking_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDRxBlocking_Object = MibTableColumn
h3cVoDIfR2ABCDRxBlocking = _H3cVoDIfR2ABCDRxBlocking_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 19),
    _H3cVoDIfR2ABCDRxBlocking_Type()
)
h3cVoDIfR2ABCDRxBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDRxBlocking.setStatus("current")


class _H3cVoDIfR2ABCDTxBlocking_Type(OctetString):
    """Custom type h3cVoDIfR2ABCDTxBlocking based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cVoDIfR2ABCDTxBlocking_Type.__name__ = "OctetString"
_H3cVoDIfR2ABCDTxBlocking_Object = MibTableColumn
h3cVoDIfR2ABCDTxBlocking = _H3cVoDIfR2ABCDTxBlocking_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 20),
    _H3cVoDIfR2ABCDTxBlocking_Type()
)
h3cVoDIfR2ABCDTxBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDTxBlocking.setStatus("current")
_H3cVoDIfR2ABCDSubLine_Type = OctetString
_H3cVoDIfR2ABCDSubLine_Object = MibTableColumn
h3cVoDIfR2ABCDSubLine = _H3cVoDIfR2ABCDSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 2, 1, 21),
    _H3cVoDIfR2ABCDSubLine_Type()
)
h3cVoDIfR2ABCDSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfR2ABCDSubLine.setStatus("current")
_H3cVoDigitalIfR2MfcCfgTable_Object = MibTable
h3cVoDigitalIfR2MfcCfgTable = _H3cVoDigitalIfR2MfcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2MfcCfgTable.setStatus("current")
_H3cVoDigitalIfR2MfcCfgEntry_Object = MibTableRow
h3cVoDigitalIfR2MfcCfgEntry = _H3cVoDigitalIfR2MfcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1)
)
h3cVoDigitalIfR2MfcCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2MfcCfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2MfcCfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2MfcCfgEntry.setStatus("current")
_H3cVoDIfR2MfcCfgPort_Type = Integer32
_H3cVoDIfR2MfcCfgPort_Object = MibTableColumn
h3cVoDIfR2MfcCfgPort = _H3cVoDIfR2MfcCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 1),
    _H3cVoDIfR2MfcCfgPort_Type()
)
h3cVoDIfR2MfcCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2MfcCfgPort.setStatus("current")
_H3cVoDIfR2MfcCfgGroup_Type = Integer32
_H3cVoDIfR2MfcCfgGroup_Object = MibTableColumn
h3cVoDIfR2MfcCfgGroup = _H3cVoDIfR2MfcCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 2),
    _H3cVoDIfR2MfcCfgGroup_Type()
)
h3cVoDIfR2MfcCfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2MfcCfgGroup.setStatus("current")


class _H3cVoDIfR2BillingCategory_Type(Integer32):
    """Custom type h3cVoDIfR2BillingCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2BillingCategory_Type.__name__ = "Integer32"
_H3cVoDIfR2BillingCategory_Object = MibTableColumn
h3cVoDIfR2BillingCategory = _H3cVoDIfR2BillingCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 3),
    _H3cVoDIfR2BillingCategory_Type()
)
h3cVoDIfR2BillingCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2BillingCategory.setStatus("current")


class _H3cVoDIfR2CallingCategory_Type(Integer32):
    """Custom type h3cVoDIfR2CallingCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2CallingCategory_Type.__name__ = "Integer32"
_H3cVoDIfR2CallingCategory_Object = MibTableColumn
h3cVoDIfR2CallingCategory = _H3cVoDIfR2CallingCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 4),
    _H3cVoDIfR2CallingCategory_Type()
)
h3cVoDIfR2CallingCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CallingCategory.setStatus("current")


class _H3cVoDIfR2Congestion_Type(Integer32):
    """Custom type h3cVoDIfR2Congestion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2Congestion_Type.__name__ = "Integer32"
_H3cVoDIfR2Congestion_Object = MibTableColumn
h3cVoDIfR2Congestion = _H3cVoDIfR2Congestion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 5),
    _H3cVoDIfR2Congestion_Type()
)
h3cVoDIfR2Congestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2Congestion.setStatus("current")


class _H3cVoDIfR2DemandRefused_Type(Integer32):
    """Custom type h3cVoDIfR2DemandRefused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2DemandRefused_Type.__name__ = "Integer32"
_H3cVoDIfR2DemandRefused_Object = MibTableColumn
h3cVoDIfR2DemandRefused = _H3cVoDIfR2DemandRefused_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 6),
    _H3cVoDIfR2DemandRefused_Type()
)
h3cVoDIfR2DemandRefused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2DemandRefused.setStatus("current")


class _H3cVoDIfR2DigitEnd_Type(Integer32):
    """Custom type h3cVoDIfR2DigitEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2DigitEnd_Type.__name__ = "Integer32"
_H3cVoDIfR2DigitEnd_Object = MibTableColumn
h3cVoDIfR2DigitEnd = _H3cVoDIfR2DigitEnd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 7),
    _H3cVoDIfR2DigitEnd_Type()
)
h3cVoDIfR2DigitEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2DigitEnd.setStatus("current")


class _H3cVoDIfR2Nullnum_Type(Integer32):
    """Custom type h3cVoDIfR2Nullnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2Nullnum_Type.__name__ = "Integer32"
_H3cVoDIfR2Nullnum_Object = MibTableColumn
h3cVoDIfR2Nullnum = _H3cVoDIfR2Nullnum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 8),
    _H3cVoDIfR2Nullnum_Type()
)
h3cVoDIfR2Nullnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2Nullnum.setStatus("current")


class _H3cVoDIfR2ReqBillingCategory_Type(Integer32):
    """Custom type h3cVoDIfR2ReqBillingCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqBillingCategory_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqBillingCategory_Object = MibTableColumn
h3cVoDIfR2ReqBillingCategory = _H3cVoDIfR2ReqBillingCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 9),
    _H3cVoDIfR2ReqBillingCategory_Type()
)
h3cVoDIfR2ReqBillingCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqBillingCategory.setStatus("current")


class _H3cVoDIfR2ReqCallingCategory_Type(Integer32):
    """Custom type h3cVoDIfR2ReqCallingCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqCallingCategory_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqCallingCategory_Object = MibTableColumn
h3cVoDIfR2ReqCallingCategory = _H3cVoDIfR2ReqCallingCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 10),
    _H3cVoDIfR2ReqCallingCategory_Type()
)
h3cVoDIfR2ReqCallingCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqCallingCategory.setStatus("current")


class _H3cVoDIfR2ReqCurrentdigit_Type(Integer32):
    """Custom type h3cVoDIfR2ReqCurrentdigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqCurrentdigit_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqCurrentdigit_Object = MibTableColumn
h3cVoDIfR2ReqCurrentdigit = _H3cVoDIfR2ReqCurrentdigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 11),
    _H3cVoDIfR2ReqCurrentdigit_Type()
)
h3cVoDIfR2ReqCurrentdigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqCurrentdigit.setStatus("current")


class _H3cVoDIfR2ReqFirstCallingnum_Type(Integer32):
    """Custom type h3cVoDIfR2ReqFirstCallingnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqFirstCallingnum_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqFirstCallingnum_Object = MibTableColumn
h3cVoDIfR2ReqFirstCallingnum = _H3cVoDIfR2ReqFirstCallingnum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 12),
    _H3cVoDIfR2ReqFirstCallingnum_Type()
)
h3cVoDIfR2ReqFirstCallingnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqFirstCallingnum.setStatus("current")


class _H3cVoDIfR2ReqFirstDigit_Type(Integer32):
    """Custom type h3cVoDIfR2ReqFirstDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqFirstDigit_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqFirstDigit_Object = MibTableColumn
h3cVoDIfR2ReqFirstDigit = _H3cVoDIfR2ReqFirstDigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 13),
    _H3cVoDIfR2ReqFirstDigit_Type()
)
h3cVoDIfR2ReqFirstDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqFirstDigit.setStatus("current")


class _H3cVoDIfR2ReqNextCallednum_Type(Integer32):
    """Custom type h3cVoDIfR2ReqNextCallednum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqNextCallednum_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqNextCallednum_Object = MibTableColumn
h3cVoDIfR2ReqNextCallednum = _H3cVoDIfR2ReqNextCallednum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 14),
    _H3cVoDIfR2ReqNextCallednum_Type()
)
h3cVoDIfR2ReqNextCallednum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqNextCallednum.setStatus("current")


class _H3cVoDIfR2ReqNextCallingnum_Type(Integer32):
    """Custom type h3cVoDIfR2ReqNextCallingnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqNextCallingnum_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqNextCallingnum_Object = MibTableColumn
h3cVoDIfR2ReqNextCallingnum = _H3cVoDIfR2ReqNextCallingnum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 15),
    _H3cVoDIfR2ReqNextCallingnum_Type()
)
h3cVoDIfR2ReqNextCallingnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqNextCallingnum.setStatus("current")


class _H3cVoDIfR2ReqLastFirstDigit_Type(Integer32):
    """Custom type h3cVoDIfR2ReqLastFirstDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqLastFirstDigit_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqLastFirstDigit_Object = MibTableColumn
h3cVoDIfR2ReqLastFirstDigit = _H3cVoDIfR2ReqLastFirstDigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 16),
    _H3cVoDIfR2ReqLastFirstDigit_Type()
)
h3cVoDIfR2ReqLastFirstDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqLastFirstDigit.setStatus("current")


class _H3cVoDIfR2ReqLastSecondDigit_Type(Integer32):
    """Custom type h3cVoDIfR2ReqLastSecondDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqLastSecondDigit_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqLastSecondDigit_Object = MibTableColumn
h3cVoDIfR2ReqLastSecondDigit = _H3cVoDIfR2ReqLastSecondDigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 17),
    _H3cVoDIfR2ReqLastSecondDigit_Type()
)
h3cVoDIfR2ReqLastSecondDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqLastSecondDigit.setStatus("current")


class _H3cVoDIfR2ReqLastThirdDigit_Type(Integer32):
    """Custom type h3cVoDIfR2ReqLastThirdDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqLastThirdDigit_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqLastThirdDigit_Object = MibTableColumn
h3cVoDIfR2ReqLastThirdDigit = _H3cVoDIfR2ReqLastThirdDigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 18),
    _H3cVoDIfR2ReqLastThirdDigit_Type()
)
h3cVoDIfR2ReqLastThirdDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqLastThirdDigit.setStatus("current")


class _H3cVoDIfR2ReqSwitchGroupB_Type(Integer32):
    """Custom type h3cVoDIfR2ReqSwitchGroupB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqSwitchGroupB_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqSwitchGroupB_Object = MibTableColumn
h3cVoDIfR2ReqSwitchGroupB = _H3cVoDIfR2ReqSwitchGroupB_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 19),
    _H3cVoDIfR2ReqSwitchGroupB_Type()
)
h3cVoDIfR2ReqSwitchGroupB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqSwitchGroupB.setStatus("current")


class _H3cVoDIfR2SubscriberIdle_Type(Integer32):
    """Custom type h3cVoDIfR2SubscriberIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2SubscriberIdle_Type.__name__ = "Integer32"
_H3cVoDIfR2SubscriberIdle_Object = MibTableColumn
h3cVoDIfR2SubscriberIdle = _H3cVoDIfR2SubscriberIdle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 20),
    _H3cVoDIfR2SubscriberIdle_Type()
)
h3cVoDIfR2SubscriberIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2SubscriberIdle.setStatus("current")


class _H3cVoDIfR2SubscriberBusy_Type(Integer32):
    """Custom type h3cVoDIfR2SubscriberBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2SubscriberBusy_Type.__name__ = "Integer32"
_H3cVoDIfR2SubscriberBusy_Object = MibTableColumn
h3cVoDIfR2SubscriberBusy = _H3cVoDIfR2SubscriberBusy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 21),
    _H3cVoDIfR2SubscriberBusy_Type()
)
h3cVoDIfR2SubscriberBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2SubscriberBusy.setStatus("current")


class _H3cVoDIfR2ReqCallingnumOffset_Type(Integer32):
    """Custom type h3cVoDIfR2ReqCallingnumOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cVoDIfR2ReqCallingnumOffset_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqCallingnumOffset_Object = MibTableColumn
h3cVoDIfR2ReqCallingnumOffset = _H3cVoDIfR2ReqCallingnumOffset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 22),
    _H3cVoDIfR2ReqCallingnumOffset_Type()
)
h3cVoDIfR2ReqCallingnumOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqCallingnumOffset.setStatus("current")


class _H3cVoDIfR2CallCreateInA_Type(Integer32):
    """Custom type h3cVoDIfR2CallCreateInA based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2CallCreateInA_Type.__name__ = "Integer32"
_H3cVoDIfR2CallCreateInA_Object = MibTableColumn
h3cVoDIfR2CallCreateInA = _H3cVoDIfR2CallCreateInA_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 23),
    _H3cVoDIfR2CallCreateInA_Type()
)
h3cVoDIfR2CallCreateInA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CallCreateInA.setStatus("current")


class _H3cVoDIfR2ReqFirstCalledNumInC_Type(Integer32):
    """Custom type h3cVoDIfR2ReqFirstCalledNumInC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqFirstCalledNumInC_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqFirstCalledNumInC_Object = MibTableColumn
h3cVoDIfR2ReqFirstCalledNumInC = _H3cVoDIfR2ReqFirstCalledNumInC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 24),
    _H3cVoDIfR2ReqFirstCalledNumInC_Type()
)
h3cVoDIfR2ReqFirstCalledNumInC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqFirstCalledNumInC.setStatus("current")


class _H3cVoDIfR2ReqCurCalledNumInC_Type(Integer32):
    """Custom type h3cVoDIfR2ReqCurCalledNumInC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqCurCalledNumInC_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqCurCalledNumInC_Object = MibTableColumn
h3cVoDIfR2ReqCurCalledNumInC = _H3cVoDIfR2ReqCurCalledNumInC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 25),
    _H3cVoDIfR2ReqCurCalledNumInC_Type()
)
h3cVoDIfR2ReqCurCalledNumInC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqCurCalledNumInC.setStatus("current")


class _H3cVoDIfR2ReqCalledNumSwitchA_Type(Integer32):
    """Custom type h3cVoDIfR2ReqCalledNumSwitchA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqCalledNumSwitchA_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqCalledNumSwitchA_Object = MibTableColumn
h3cVoDIfR2ReqCalledNumSwitchA = _H3cVoDIfR2ReqCalledNumSwitchA_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 26),
    _H3cVoDIfR2ReqCalledNumSwitchA_Type()
)
h3cVoDIfR2ReqCalledNumSwitchA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqCalledNumSwitchA.setStatus("current")


class _H3cVoDIfR2ReqSpecialSignal_Type(Integer32):
    """Custom type h3cVoDIfR2ReqSpecialSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2ReqSpecialSignal_Type.__name__ = "Integer32"
_H3cVoDIfR2ReqSpecialSignal_Object = MibTableColumn
h3cVoDIfR2ReqSpecialSignal = _H3cVoDIfR2ReqSpecialSignal_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 27),
    _H3cVoDIfR2ReqSpecialSignal_Type()
)
h3cVoDIfR2ReqSpecialSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2ReqSpecialSignal.setStatus("current")


class _H3cVoDIfR2SubscriberCharge_Type(Integer32):
    """Custom type h3cVoDIfR2SubscriberCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2SubscriberCharge_Type.__name__ = "Integer32"
_H3cVoDIfR2SubscriberCharge_Object = MibTableColumn
h3cVoDIfR2SubscriberCharge = _H3cVoDIfR2SubscriberCharge_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 28),
    _H3cVoDIfR2SubscriberCharge_Type()
)
h3cVoDIfR2SubscriberCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2SubscriberCharge.setStatus("current")


class _H3cVoDIfR2SubscriberAbnormal_Type(Integer32):
    """Custom type h3cVoDIfR2SubscriberAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoDIfR2SubscriberAbnormal_Type.__name__ = "Integer32"
_H3cVoDIfR2SubscriberAbnormal_Object = MibTableColumn
h3cVoDIfR2SubscriberAbnormal = _H3cVoDIfR2SubscriberAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 29),
    _H3cVoDIfR2SubscriberAbnormal_Type()
)
h3cVoDIfR2SubscriberAbnormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2SubscriberAbnormal.setStatus("current")


class _H3cVoDIfR2Ani_Type(Integer32):
    """Custom type h3cVoDIfR2Ani based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("disable", 1),
          ("ka", 3))
    )


_H3cVoDIfR2Ani_Type.__name__ = "Integer32"
_H3cVoDIfR2Ani_Object = MibTableColumn
h3cVoDIfR2Ani = _H3cVoDIfR2Ani_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 30),
    _H3cVoDIfR2Ani_Type()
)
h3cVoDIfR2Ani.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2Ani.setStatus("current")
_H3cVoDIfR2SubLine_Type = OctetString
_H3cVoDIfR2SubLine_Object = MibTableColumn
h3cVoDIfR2SubLine = _H3cVoDIfR2SubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 3, 1, 31),
    _H3cVoDIfR2SubLine_Type()
)
h3cVoDIfR2SubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfR2SubLine.setStatus("current")
_H3cVoDigitalIfR2TimerCfgTable_Object = MibTable
h3cVoDigitalIfR2TimerCfgTable = _H3cVoDigitalIfR2TimerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4)
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2TimerCfgTable.setStatus("current")
_H3cVoDigitalIfR2TimerCfgEntry_Object = MibTableRow
h3cVoDigitalIfR2TimerCfgEntry = _H3cVoDigitalIfR2TimerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1)
)
h3cVoDigitalIfR2TimerCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2TimeCfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2TimeCfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDigitalIfR2TimerCfgEntry.setStatus("current")
_H3cVoDIfR2TimeCfgPort_Type = Integer32
_H3cVoDIfR2TimeCfgPort_Object = MibTableColumn
h3cVoDIfR2TimeCfgPort = _H3cVoDIfR2TimeCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 1),
    _H3cVoDIfR2TimeCfgPort_Type()
)
h3cVoDIfR2TimeCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2TimeCfgPort.setStatus("current")
_H3cVoDIfR2TimeCfgGroup_Type = Integer32
_H3cVoDIfR2TimeCfgGroup_Object = MibTableColumn
h3cVoDIfR2TimeCfgGroup = _H3cVoDIfR2TimeCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 2),
    _H3cVoDIfR2TimeCfgGroup_Type()
)
h3cVoDIfR2TimeCfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2TimeCfgGroup.setStatus("current")
_H3cVoDIfR2CfgDebounceTime_Type = Integer32
_H3cVoDIfR2CfgDebounceTime_Object = MibTableColumn
h3cVoDIfR2CfgDebounceTime = _H3cVoDIfR2CfgDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 3),
    _H3cVoDIfR2CfgDebounceTime_Type()
)
h3cVoDIfR2CfgDebounceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDebounceTime.setStatus("current")
_H3cVoDIfR2CfgSendringBackTime_Type = Integer32
_H3cVoDIfR2CfgSendringBackTime_Object = MibTableColumn
h3cVoDIfR2CfgSendringBackTime = _H3cVoDIfR2CfgSendringBackTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 4),
    _H3cVoDIfR2CfgSendringBackTime_Type()
)
h3cVoDIfR2CfgSendringBackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgSendringBackTime.setStatus("current")
_H3cVoDIfR2CfgSendringBusyTime_Type = Integer32
_H3cVoDIfR2CfgSendringBusyTime_Object = MibTableColumn
h3cVoDIfR2CfgSendringBusyTime = _H3cVoDIfR2CfgSendringBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 5),
    _H3cVoDIfR2CfgSendringBusyTime_Type()
)
h3cVoDIfR2CfgSendringBusyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgSendringBusyTime.setStatus("current")
_H3cVoDIfR2PulseSignalPersistT_Type = Integer32
_H3cVoDIfR2PulseSignalPersistT_Object = MibTableColumn
h3cVoDIfR2PulseSignalPersistT = _H3cVoDIfR2PulseSignalPersistT_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 6),
    _H3cVoDIfR2PulseSignalPersistT_Type()
)
h3cVoDIfR2PulseSignalPersistT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2PulseSignalPersistT.setStatus("current")
_H3cVoDIfR2CfgDlAnswerTime_Type = Integer32
_H3cVoDIfR2CfgDlAnswerTime_Object = MibTableColumn
h3cVoDIfR2CfgDlAnswerTime = _H3cVoDIfR2CfgDlAnswerTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 7),
    _H3cVoDIfR2CfgDlAnswerTime_Type()
)
h3cVoDIfR2CfgDlAnswerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDlAnswerTime.setStatus("current")
_H3cVoDIfR2CfgDlClearBackTime_Type = Integer32
_H3cVoDIfR2CfgDlClearBackTime_Object = MibTableColumn
h3cVoDIfR2CfgDlClearBackTime = _H3cVoDIfR2CfgDlClearBackTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 8),
    _H3cVoDIfR2CfgDlClearBackTime_Type()
)
h3cVoDIfR2CfgDlClearBackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDlClearBackTime.setStatus("current")
_H3cVoDIfR2CfgDlClearForwardT_Type = Integer32
_H3cVoDIfR2CfgDlClearForwardT_Object = MibTableColumn
h3cVoDIfR2CfgDlClearForwardT = _H3cVoDIfR2CfgDlClearForwardT_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 9),
    _H3cVoDIfR2CfgDlClearForwardT_Type()
)
h3cVoDIfR2CfgDlClearForwardT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDlClearForwardT.setStatus("current")
_H3cVoDIfR2CfgDlSeizureTime_Type = Integer32
_H3cVoDIfR2CfgDlSeizureTime_Object = MibTableColumn
h3cVoDIfR2CfgDlSeizureTime = _H3cVoDIfR2CfgDlSeizureTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 10),
    _H3cVoDIfR2CfgDlSeizureTime_Type()
)
h3cVoDIfR2CfgDlSeizureTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDlSeizureTime.setStatus("current")
_H3cVoDIfR2CfgDlReanswerTime_Type = Integer32
_H3cVoDIfR2CfgDlReanswerTime_Object = MibTableColumn
h3cVoDIfR2CfgDlReanswerTime = _H3cVoDIfR2CfgDlReanswerTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 11),
    _H3cVoDIfR2CfgDlReanswerTime_Type()
)
h3cVoDIfR2CfgDlReanswerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDlReanswerTime.setStatus("current")
_H3cVoDIfR2CfgDlRelGuardTime_Type = Integer32
_H3cVoDIfR2CfgDlRelGuardTime_Object = MibTableColumn
h3cVoDIfR2CfgDlRelGuardTime = _H3cVoDIfR2CfgDlRelGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 12),
    _H3cVoDIfR2CfgDlRelGuardTime_Type()
)
h3cVoDIfR2CfgDlRelGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDlRelGuardTime.setStatus("current")
_H3cVoDIfR2CfgMfcGroupBTime_Type = Integer32
_H3cVoDIfR2CfgMfcGroupBTime_Object = MibTableColumn
h3cVoDIfR2CfgMfcGroupBTime = _H3cVoDIfR2CfgMfcGroupBTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 13),
    _H3cVoDIfR2CfgMfcGroupBTime_Type()
)
h3cVoDIfR2CfgMfcGroupBTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgMfcGroupBTime.setStatus("current")
_H3cVoDIfR2CfgDTMFTime_Type = Integer32
_H3cVoDIfR2CfgDTMFTime_Object = MibTableColumn
h3cVoDIfR2CfgDTMFTime = _H3cVoDIfR2CfgDTMFTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 14),
    _H3cVoDIfR2CfgDTMFTime_Type()
)
h3cVoDIfR2CfgDTMFTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDTMFTime.setStatus("current")
_H3cVoDIfR2TimeCfgSubLine_Type = OctetString
_H3cVoDIfR2TimeCfgSubLine_Object = MibTableColumn
h3cVoDIfR2TimeCfgSubLine = _H3cVoDIfR2TimeCfgSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 4, 1, 15),
    _H3cVoDIfR2TimeCfgSubLine_Type()
)
h3cVoDIfR2TimeCfgSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfR2TimeCfgSubLine.setStatus("current")
_H3cVoDIfR2CapabilityCfgTable_Object = MibTable
h3cVoDIfR2CapabilityCfgTable = _H3cVoDIfR2CapabilityCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5)
)
if mibBuilder.loadTexts:
    h3cVoDIfR2CapabilityCfgTable.setStatus("current")
_H3cVoDIfR2CapabilityCfgEntry_Object = MibTableRow
h3cVoDIfR2CapabilityCfgEntry = _H3cVoDIfR2CapabilityCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1)
)
h3cVoDIfR2CapabilityCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2CapCfgPort"),
    (0, "A3COM-HUAWEI-VODIGITALIF-MIB", "h3cVoDIfR2CapCfgGroup"),
)
if mibBuilder.loadTexts:
    h3cVoDIfR2CapabilityCfgEntry.setStatus("current")
_H3cVoDIfR2CapCfgPort_Type = Integer32
_H3cVoDIfR2CapCfgPort_Object = MibTableColumn
h3cVoDIfR2CapCfgPort = _H3cVoDIfR2CapCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 1),
    _H3cVoDIfR2CapCfgPort_Type()
)
h3cVoDIfR2CapCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2CapCfgPort.setStatus("current")
_H3cVoDIfR2CapCfgGroup_Type = Integer32
_H3cVoDIfR2CapCfgGroup_Object = MibTableColumn
h3cVoDIfR2CapCfgGroup = _H3cVoDIfR2CapCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 2),
    _H3cVoDIfR2CapCfgGroup_Type()
)
h3cVoDIfR2CapCfgGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoDIfR2CapCfgGroup.setStatus("current")


class _H3cVoDIfR2CfgGroupB_Type(Integer32):
    """Custom type h3cVoDIfR2CfgGroupB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgGroupB_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgGroupB_Object = MibTableColumn
h3cVoDIfR2CfgGroupB = _H3cVoDIfR2CfgGroupB_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 3),
    _H3cVoDIfR2CfgGroupB_Type()
)
h3cVoDIfR2CfgGroupB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgGroupB.setStatus("current")


class _H3cVoDIfR2CfgClearForwardAck_Type(Integer32):
    """Custom type h3cVoDIfR2CfgClearForwardAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgClearForwardAck_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgClearForwardAck_Object = MibTableColumn
h3cVoDIfR2CfgClearForwardAck = _H3cVoDIfR2CfgClearForwardAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 4),
    _H3cVoDIfR2CfgClearForwardAck_Type()
)
h3cVoDIfR2CfgClearForwardAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgClearForwardAck.setStatus("current")


class _H3cVoDIfR2CfgDlSeizureAck_Type(Integer32):
    """Custom type h3cVoDIfR2CfgDlSeizureAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgDlSeizureAck_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgDlSeizureAck_Object = MibTableColumn
h3cVoDIfR2CfgDlSeizureAck = _H3cVoDIfR2CfgDlSeizureAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 5),
    _H3cVoDIfR2CfgDlSeizureAck_Type()
)
h3cVoDIfR2CfgDlSeizureAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDlSeizureAck.setStatus("current")


class _H3cVoDIfR2CfgDTMF_Type(Integer32):
    """Custom type h3cVoDIfR2CfgDTMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgDTMF_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgDTMF_Object = MibTableColumn
h3cVoDIfR2CfgDTMF = _H3cVoDIfR2CfgDTMF_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 6),
    _H3cVoDIfR2CfgDTMF_Type()
)
h3cVoDIfR2CfgDTMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgDTMF.setStatus("current")


class _H3cVoDIfR2CfgAnswer_Type(Integer32):
    """Custom type h3cVoDIfR2CfgAnswer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgAnswer_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgAnswer_Object = MibTableColumn
h3cVoDIfR2CfgAnswer = _H3cVoDIfR2CfgAnswer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 7),
    _H3cVoDIfR2CfgAnswer_Type()
)
h3cVoDIfR2CfgAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgAnswer.setStatus("current")


class _H3cVoDIfR2CfgReanswer_Type(Integer32):
    """Custom type h3cVoDIfR2CfgReanswer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgReanswer_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgReanswer_Object = MibTableColumn
h3cVoDIfR2CfgReanswer = _H3cVoDIfR2CfgReanswer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 8),
    _H3cVoDIfR2CfgReanswer_Type()
)
h3cVoDIfR2CfgReanswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgReanswer.setStatus("current")


class _H3cVoDIfR2CfgFinalCallnum_Type(Integer32):
    """Custom type h3cVoDIfR2CfgFinalCallnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgFinalCallnum_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgFinalCallnum_Object = MibTableColumn
h3cVoDIfR2CfgFinalCallnum = _H3cVoDIfR2CfgFinalCallnum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 9),
    _H3cVoDIfR2CfgFinalCallnum_Type()
)
h3cVoDIfR2CfgFinalCallnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgFinalCallnum.setStatus("current")


class _H3cVoDIfR2CfgForceMetering_Type(Integer32):
    """Custom type h3cVoDIfR2CfgForceMetering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgForceMetering_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgForceMetering_Object = MibTableColumn
h3cVoDIfR2CfgForceMetering = _H3cVoDIfR2CfgForceMetering_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 10),
    _H3cVoDIfR2CfgForceMetering_Type()
)
h3cVoDIfR2CfgForceMetering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgForceMetering.setStatus("current")


class _H3cVoDIfR2CfgSendRingBack_Type(Integer32):
    """Custom type h3cVoDIfR2CfgSendRingBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgSendRingBack_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgSendRingBack_Object = MibTableColumn
h3cVoDIfR2CfgSendRingBack = _H3cVoDIfR2CfgSendRingBack_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 11),
    _H3cVoDIfR2CfgSendRingBack_Type()
)
h3cVoDIfR2CfgSendRingBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgSendRingBack.setStatus("current")


class _H3cVoDIfR2CfgSendRingBusy_Type(Integer32):
    """Custom type h3cVoDIfR2CfgSendRingBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoDIfR2CfgSendRingBusy_Type.__name__ = "Integer32"
_H3cVoDIfR2CfgSendRingBusy_Object = MibTableColumn
h3cVoDIfR2CfgSendRingBusy = _H3cVoDIfR2CfgSendRingBusy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 12),
    _H3cVoDIfR2CfgSendRingBusy_Type()
)
h3cVoDIfR2CfgSendRingBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoDIfR2CfgSendRingBusy.setStatus("current")
_H3cVoDIfR2CapCfgSubLine_Type = OctetString
_H3cVoDIfR2CapCfgSubLine_Object = MibTableColumn
h3cVoDIfR2CapCfgSubLine = _H3cVoDIfR2CapCfgSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 4, 3, 5, 1, 15),
    _H3cVoDIfR2CapCfgSubLine_Type()
)
h3cVoDIfR2CapCfgSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoDIfR2CapCfgSubLine.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VODIGITALIF-MIB",
    **{"h3cVoiceDigitalInterface": h3cVoiceDigitalInterface,
       "h3cVoDigitalIfCommonObjects": h3cVoDigitalIfCommonObjects,
       "h3cVoDigitalIfCommonCfgTable": h3cVoDigitalIfCommonCfgTable,
       "h3cVoDigitalIfCommonCfgEntry": h3cVoDigitalIfCommonCfgEntry,
       "h3cVoDIfCfgPort": h3cVoDIfCfgPort,
       "h3cVoDIfCfgGroup": h3cVoDIfCfgGroup,
       "h3cVoDIfCfgBoardType": h3cVoDIfCfgBoardType,
       "h3cVoDIfCfgSignalType": h3cVoDIfCfgSignalType,
       "h3cVoDIfCfgTsInformation": h3cVoDIfCfgTsInformation,
       "h3cVoDIfCfgPortSubLine": h3cVoDIfCfgPortSubLine,
       "h3cVoDigitalIfEMObjects": h3cVoDigitalIfEMObjects,
       "h3cVoDigitalIfEMCfgTable": h3cVoDigitalIfEMCfgTable,
       "h3cVoDigitalIfEMCfgEntry": h3cVoDigitalIfEMCfgEntry,
       "h3cVoDIfEMCfgPort": h3cVoDIfEMCfgPort,
       "h3cVoDIfEMCfgGroup": h3cVoDIfEMCfgGroup,
       "h3cVoDIfEMCfgTimeoutInterDigit": h3cVoDIfEMCfgTimeoutInterDigit,
       "h3cVoDIfEMCfgTimeoutRinging": h3cVoDIfEMCfgTimeoutRinging,
       "h3cVoDIfEMCfgTimeoutWaitDigit": h3cVoDIfEMCfgTimeoutWaitDigit,
       "h3cVoDIfEMCfgPortSubLine": h3cVoDIfEMCfgPortSubLine,
       "h3cVoDigitalIfEMABCDCfgTable": h3cVoDigitalIfEMABCDCfgTable,
       "h3cVoDigitalIfEMABCDCfgEntry": h3cVoDigitalIfEMABCDCfgEntry,
       "h3cVoDIfEMABCDCfgPort": h3cVoDIfEMABCDCfgPort,
       "h3cVoDIfEMABCDCfgGroup": h3cVoDIfEMABCDCfgGroup,
       "h3cVoDIfEMABCDRxIdle": h3cVoDIfEMABCDRxIdle,
       "h3cVoDIfEMABCDRxSeizure": h3cVoDIfEMABCDRxSeizure,
       "h3cVoDIfEMABCDTxIdle": h3cVoDIfEMABCDTxIdle,
       "h3cVoDIfEMABCDTxSeizure": h3cVoDIfEMABCDTxSeizure,
       "h3cVoDIFEMABCDSubLine": h3cVoDIFEMABCDSubLine,
       "h3cVoDigitalIfEMTimerTable": h3cVoDigitalIfEMTimerTable,
       "h3cVoDigitalIfEMTimerEntry": h3cVoDigitalIfEMTimerEntry,
       "h3cVoDIfEMTimerPort": h3cVoDIfEMTimerPort,
       "h3cVoDIfEMTimerGroup": h3cVoDIfEMTimerGroup,
       "h3cVoDIfEMTimerSendWink": h3cVoDIfEMTimerSendWink,
       "h3cVoDIfEMTimerWinkRising": h3cVoDIfEMTimerWinkRising,
       "h3cVoDIfEMTimerWinkHold": h3cVoDIfEMTimerWinkHold,
       "h3cVoDIfEMTimerDialoutDelay": h3cVoDIfEMTimerDialoutDelay,
       "h3cVoDIfEMTimerDelayRising": h3cVoDIfEMTimerDelayRising,
       "h3cVoDIfEMTimerDelayHold": h3cVoDIfEMTimerDelayHold,
       "h3cVoDIfEMTimerDtmf": h3cVoDIfEMTimerDtmf,
       "h3cVoDIfEMTimerDtmfInterval": h3cVoDIfEMTimerDtmfInterval,
       "h3cVoDIfEMTimerPortSubLine": h3cVoDIfEMTimerPortSubLine,
       "h3cVoDigitalIfR2Objects": h3cVoDigitalIfR2Objects,
       "h3cVoDigitalIfR2CfgTable": h3cVoDigitalIfR2CfgTable,
       "h3cVoDigitalIfR2CfgEntry": h3cVoDigitalIfR2CfgEntry,
       "h3cVoDIfR2CfgPort": h3cVoDIfR2CfgPort,
       "h3cVoDIfR2CfgGroup": h3cVoDIfR2CfgGroup,
       "h3cVoDIfR2CfgCountryMode": h3cVoDIfR2CfgCountryMode,
       "h3cVoDIfR2CfgSpecialChar": h3cVoDIfR2CfgSpecialChar,
       "h3cVoDIfR2CfgSpecialSignal": h3cVoDIfR2CfgSpecialSignal,
       "h3cVoDIfR2CfgSelectMode": h3cVoDIfR2CfgSelectMode,
       "h3cVoDIFR2CfgSubLine": h3cVoDIFR2CfgSubLine,
       "h3cVoDigitalIfR2ABCDCfgTable": h3cVoDigitalIfR2ABCDCfgTable,
       "h3cVoDigitalIfR2ABCDCfgEntry": h3cVoDigitalIfR2ABCDCfgEntry,
       "h3cVoDIfR2ABCDCfgPort": h3cVoDIfR2ABCDCfgPort,
       "h3cVoDIfR2ABCDCfgGroup": h3cVoDIfR2ABCDCfgGroup,
       "h3cVoDIfR2ABCDReverseABCD": h3cVoDIfR2ABCDReverseABCD,
       "h3cVoDIfR2ABCDRenewABCD": h3cVoDIfR2ABCDRenewABCD,
       "h3cVoDIfR2ABCDRxIdle": h3cVoDIfR2ABCDRxIdle,
       "h3cVoDIfR2ABCDTxIdle": h3cVoDIfR2ABCDTxIdle,
       "h3cVoDIfR2ABCDRxSeizure": h3cVoDIfR2ABCDRxSeizure,
       "h3cVoDIfR2ABCDTxSeizure": h3cVoDIfR2ABCDTxSeizure,
       "h3cVoDIfR2ABCDRxSeizureAck": h3cVoDIfR2ABCDRxSeizureAck,
       "h3cVoDIfR2ABCDTxSeizureAck": h3cVoDIfR2ABCDTxSeizureAck,
       "h3cVoDIfR2ABCDRxAnswer": h3cVoDIfR2ABCDRxAnswer,
       "h3cVoDIfR2ABCDTxAnswer": h3cVoDIfR2ABCDTxAnswer,
       "h3cVoDIfR2ABCDRxClearForward": h3cVoDIfR2ABCDRxClearForward,
       "h3cVoDIfR2ABCDTxClearForward": h3cVoDIfR2ABCDTxClearForward,
       "h3cVoDIfR2ABCDRxClearBack": h3cVoDIfR2ABCDRxClearBack,
       "h3cVoDIfR2ABCDTxClearBack": h3cVoDIfR2ABCDTxClearBack,
       "h3cVoDIfR2ABCDRxReleaseGuard": h3cVoDIfR2ABCDRxReleaseGuard,
       "h3cVoDIfR2ABCDTxReleaseGuard": h3cVoDIfR2ABCDTxReleaseGuard,
       "h3cVoDIfR2ABCDRxBlocking": h3cVoDIfR2ABCDRxBlocking,
       "h3cVoDIfR2ABCDTxBlocking": h3cVoDIfR2ABCDTxBlocking,
       "h3cVoDIfR2ABCDSubLine": h3cVoDIfR2ABCDSubLine,
       "h3cVoDigitalIfR2MfcCfgTable": h3cVoDigitalIfR2MfcCfgTable,
       "h3cVoDigitalIfR2MfcCfgEntry": h3cVoDigitalIfR2MfcCfgEntry,
       "h3cVoDIfR2MfcCfgPort": h3cVoDIfR2MfcCfgPort,
       "h3cVoDIfR2MfcCfgGroup": h3cVoDIfR2MfcCfgGroup,
       "h3cVoDIfR2BillingCategory": h3cVoDIfR2BillingCategory,
       "h3cVoDIfR2CallingCategory": h3cVoDIfR2CallingCategory,
       "h3cVoDIfR2Congestion": h3cVoDIfR2Congestion,
       "h3cVoDIfR2DemandRefused": h3cVoDIfR2DemandRefused,
       "h3cVoDIfR2DigitEnd": h3cVoDIfR2DigitEnd,
       "h3cVoDIfR2Nullnum": h3cVoDIfR2Nullnum,
       "h3cVoDIfR2ReqBillingCategory": h3cVoDIfR2ReqBillingCategory,
       "h3cVoDIfR2ReqCallingCategory": h3cVoDIfR2ReqCallingCategory,
       "h3cVoDIfR2ReqCurrentdigit": h3cVoDIfR2ReqCurrentdigit,
       "h3cVoDIfR2ReqFirstCallingnum": h3cVoDIfR2ReqFirstCallingnum,
       "h3cVoDIfR2ReqFirstDigit": h3cVoDIfR2ReqFirstDigit,
       "h3cVoDIfR2ReqNextCallednum": h3cVoDIfR2ReqNextCallednum,
       "h3cVoDIfR2ReqNextCallingnum": h3cVoDIfR2ReqNextCallingnum,
       "h3cVoDIfR2ReqLastFirstDigit": h3cVoDIfR2ReqLastFirstDigit,
       "h3cVoDIfR2ReqLastSecondDigit": h3cVoDIfR2ReqLastSecondDigit,
       "h3cVoDIfR2ReqLastThirdDigit": h3cVoDIfR2ReqLastThirdDigit,
       "h3cVoDIfR2ReqSwitchGroupB": h3cVoDIfR2ReqSwitchGroupB,
       "h3cVoDIfR2SubscriberIdle": h3cVoDIfR2SubscriberIdle,
       "h3cVoDIfR2SubscriberBusy": h3cVoDIfR2SubscriberBusy,
       "h3cVoDIfR2ReqCallingnumOffset": h3cVoDIfR2ReqCallingnumOffset,
       "h3cVoDIfR2CallCreateInA": h3cVoDIfR2CallCreateInA,
       "h3cVoDIfR2ReqFirstCalledNumInC": h3cVoDIfR2ReqFirstCalledNumInC,
       "h3cVoDIfR2ReqCurCalledNumInC": h3cVoDIfR2ReqCurCalledNumInC,
       "h3cVoDIfR2ReqCalledNumSwitchA": h3cVoDIfR2ReqCalledNumSwitchA,
       "h3cVoDIfR2ReqSpecialSignal": h3cVoDIfR2ReqSpecialSignal,
       "h3cVoDIfR2SubscriberCharge": h3cVoDIfR2SubscriberCharge,
       "h3cVoDIfR2SubscriberAbnormal": h3cVoDIfR2SubscriberAbnormal,
       "h3cVoDIfR2Ani": h3cVoDIfR2Ani,
       "h3cVoDIfR2SubLine": h3cVoDIfR2SubLine,
       "h3cVoDigitalIfR2TimerCfgTable": h3cVoDigitalIfR2TimerCfgTable,
       "h3cVoDigitalIfR2TimerCfgEntry": h3cVoDigitalIfR2TimerCfgEntry,
       "h3cVoDIfR2TimeCfgPort": h3cVoDIfR2TimeCfgPort,
       "h3cVoDIfR2TimeCfgGroup": h3cVoDIfR2TimeCfgGroup,
       "h3cVoDIfR2CfgDebounceTime": h3cVoDIfR2CfgDebounceTime,
       "h3cVoDIfR2CfgSendringBackTime": h3cVoDIfR2CfgSendringBackTime,
       "h3cVoDIfR2CfgSendringBusyTime": h3cVoDIfR2CfgSendringBusyTime,
       "h3cVoDIfR2PulseSignalPersistT": h3cVoDIfR2PulseSignalPersistT,
       "h3cVoDIfR2CfgDlAnswerTime": h3cVoDIfR2CfgDlAnswerTime,
       "h3cVoDIfR2CfgDlClearBackTime": h3cVoDIfR2CfgDlClearBackTime,
       "h3cVoDIfR2CfgDlClearForwardT": h3cVoDIfR2CfgDlClearForwardT,
       "h3cVoDIfR2CfgDlSeizureTime": h3cVoDIfR2CfgDlSeizureTime,
       "h3cVoDIfR2CfgDlReanswerTime": h3cVoDIfR2CfgDlReanswerTime,
       "h3cVoDIfR2CfgDlRelGuardTime": h3cVoDIfR2CfgDlRelGuardTime,
       "h3cVoDIfR2CfgMfcGroupBTime": h3cVoDIfR2CfgMfcGroupBTime,
       "h3cVoDIfR2CfgDTMFTime": h3cVoDIfR2CfgDTMFTime,
       "h3cVoDIfR2TimeCfgSubLine": h3cVoDIfR2TimeCfgSubLine,
       "h3cVoDIfR2CapabilityCfgTable": h3cVoDIfR2CapabilityCfgTable,
       "h3cVoDIfR2CapabilityCfgEntry": h3cVoDIfR2CapabilityCfgEntry,
       "h3cVoDIfR2CapCfgPort": h3cVoDIfR2CapCfgPort,
       "h3cVoDIfR2CapCfgGroup": h3cVoDIfR2CapCfgGroup,
       "h3cVoDIfR2CfgGroupB": h3cVoDIfR2CfgGroupB,
       "h3cVoDIfR2CfgClearForwardAck": h3cVoDIfR2CfgClearForwardAck,
       "h3cVoDIfR2CfgDlSeizureAck": h3cVoDIfR2CfgDlSeizureAck,
       "h3cVoDIfR2CfgDTMF": h3cVoDIfR2CfgDTMF,
       "h3cVoDIfR2CfgAnswer": h3cVoDIfR2CfgAnswer,
       "h3cVoDIfR2CfgReanswer": h3cVoDIfR2CfgReanswer,
       "h3cVoDIfR2CfgFinalCallnum": h3cVoDIfR2CfgFinalCallnum,
       "h3cVoDIfR2CfgForceMetering": h3cVoDIfR2CfgForceMetering,
       "h3cVoDIfR2CfgSendRingBack": h3cVoDIfR2CfgSendRingBack,
       "h3cVoDIfR2CfgSendRingBusy": h3cVoDIfR2CfgSendRingBusy,
       "h3cVoDIfR2CapCfgSubLine": h3cVoDIfR2CapCfgSubLine}
)
