# SNMP MIB module (INTEL-AMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-AMOD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:31 2024
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



class ModemState(Integer32):
    """Custom type ModemState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("acceptingCall", 9),
          ("connected", 10),
          ("dialing", 12),
          ("hangingUp", 6),
          ("initializingModem", 3),
          ("noConfiguration", 1),
          ("noValidModem", 2),
          ("other", 14),
          ("reserved", 11),
          ("resettingModem", 4),
          ("standBy", 8),
          ("waitingForAnswer", 13),
          ("waitingForHangupAck", 7),
          ("waitingForResetAck", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Amod_ObjectIdentity = ObjectIdentity
amod = _Amod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 24)
)
_AmodModem_ObjectIdentity = ObjectIdentity
amodModem = _AmodModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 1)
)
_AmodModemTable_Object = MibTable
amodModemTable = _AmodModemTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 1, 1)
)
if mibBuilder.loadTexts:
    amodModemTable.setStatus("mandatory")
_AmodModemEntry_Object = MibTableRow
amodModemEntry = _AmodModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 1, 1, 1)
)
amodModemEntry.setIndexNames(
    (0, "INTEL-AMOD-MIB", "amodModemIfIndex"),
)
if mibBuilder.loadTexts:
    amodModemEntry.setStatus("mandatory")
_AmodModemIfIndex_Type = Integer32
_AmodModemIfIndex_Object = MibTableColumn
amodModemIfIndex = _AmodModemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 1, 1, 1, 1),
    _AmodModemIfIndex_Type()
)
amodModemIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodModemIfIndex.setStatus("mandatory")
_AmodModemState_Type = ModemState
_AmodModemState_Object = MibTableColumn
amodModemState = _AmodModemState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 1, 1, 1, 2),
    _AmodModemState_Type()
)
amodModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodModemState.setStatus("mandatory")


class _AmodModemManufactureName_Type(DisplayString):
    """Custom type amodModemManufactureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AmodModemManufactureName_Type.__name__ = "DisplayString"
_AmodModemManufactureName_Object = MibTableColumn
amodModemManufactureName = _AmodModemManufactureName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 1, 1, 1, 3),
    _AmodModemManufactureName_Type()
)
amodModemManufactureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodModemManufactureName.setStatus("mandatory")


class _AmodModemProductNameAndVer_Type(DisplayString):
    """Custom type amodModemProductNameAndVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_AmodModemProductNameAndVer_Type.__name__ = "DisplayString"
_AmodModemProductNameAndVer_Object = MibTableColumn
amodModemProductNameAndVer = _AmodModemProductNameAndVer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 1, 1, 1, 4),
    _AmodModemProductNameAndVer_Type()
)
amodModemProductNameAndVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodModemProductNameAndVer.setStatus("mandatory")
_AmodLink_ObjectIdentity = ObjectIdentity
amodLink = _AmodLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2)
)
_AmodLinkTable_Object = MibTable
amodLinkTable = _AmodLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1)
)
if mibBuilder.loadTexts:
    amodLinkTable.setStatus("mandatory")
_AmodLinkEntry_Object = MibTableRow
amodLinkEntry = _AmodLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1)
)
amodLinkEntry.setIndexNames(
    (0, "INTEL-AMOD-MIB", "amodLinkIfIndex"),
)
if mibBuilder.loadTexts:
    amodLinkEntry.setStatus("mandatory")
_AmodLinkIfIndex_Type = Integer32
_AmodLinkIfIndex_Object = MibTableColumn
amodLinkIfIndex = _AmodLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 1),
    _AmodLinkIfIndex_Type()
)
amodLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkIfIndex.setStatus("mandatory")
_AmodLinkHdlcRxChecksumErrors_Type = Counter32
_AmodLinkHdlcRxChecksumErrors_Object = MibTableColumn
amodLinkHdlcRxChecksumErrors = _AmodLinkHdlcRxChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 2),
    _AmodLinkHdlcRxChecksumErrors_Type()
)
amodLinkHdlcRxChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkHdlcRxChecksumErrors.setStatus("mandatory")
_AmodLinkHdlcRxLong_Type = Counter32
_AmodLinkHdlcRxLong_Object = MibTableColumn
amodLinkHdlcRxLong = _AmodLinkHdlcRxLong_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 3),
    _AmodLinkHdlcRxLong_Type()
)
amodLinkHdlcRxLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkHdlcRxLong.setStatus("mandatory")
_AmodLinkHdlcRxShort_Type = Counter32
_AmodLinkHdlcRxShort_Object = MibTableColumn
amodLinkHdlcRxShort = _AmodLinkHdlcRxShort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 4),
    _AmodLinkHdlcRxShort_Type()
)
amodLinkHdlcRxShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkHdlcRxShort.setStatus("mandatory")
_AmodLinkHdlcStuffingErrors_Type = Counter32
_AmodLinkHdlcStuffingErrors_Object = MibTableColumn
amodLinkHdlcStuffingErrors = _AmodLinkHdlcStuffingErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 5),
    _AmodLinkHdlcStuffingErrors_Type()
)
amodLinkHdlcStuffingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkHdlcStuffingErrors.setStatus("mandatory")
_AmodLinkHdlcLostEndMarkers_Type = Counter32
_AmodLinkHdlcLostEndMarkers_Object = MibTableColumn
amodLinkHdlcLostEndMarkers = _AmodLinkHdlcLostEndMarkers_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 6),
    _AmodLinkHdlcLostEndMarkers_Type()
)
amodLinkHdlcLostEndMarkers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkHdlcLostEndMarkers.setStatus("mandatory")
_AmodLinkHdlcRxOverflow_Type = Counter32
_AmodLinkHdlcRxOverflow_Object = MibTableColumn
amodLinkHdlcRxOverflow = _AmodLinkHdlcRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 7),
    _AmodLinkHdlcRxOverflow_Type()
)
amodLinkHdlcRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkHdlcRxOverflow.setStatus("mandatory")
_AmodLinkTxCalls_Type = Counter32
_AmodLinkTxCalls_Object = MibTableColumn
amodLinkTxCalls = _AmodLinkTxCalls_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 8),
    _AmodLinkTxCalls_Type()
)
amodLinkTxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkTxCalls.setStatus("mandatory")
_AmodLinkTxCallsFailed_Type = Counter32
_AmodLinkTxCallsFailed_Object = MibTableColumn
amodLinkTxCallsFailed = _AmodLinkTxCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 9),
    _AmodLinkTxCallsFailed_Type()
)
amodLinkTxCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkTxCallsFailed.setStatus("mandatory")
_AmodLinkRxCalls_Type = Counter32
_AmodLinkRxCalls_Object = MibTableColumn
amodLinkRxCalls = _AmodLinkRxCalls_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 24, 2, 1, 1, 10),
    _AmodLinkRxCalls_Type()
)
amodLinkRxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amodLinkRxCalls.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-AMOD-MIB",
    **{"ModemState": ModemState,
       "amod": amod,
       "amodModem": amodModem,
       "amodModemTable": amodModemTable,
       "amodModemEntry": amodModemEntry,
       "amodModemIfIndex": amodModemIfIndex,
       "amodModemState": amodModemState,
       "amodModemManufactureName": amodModemManufactureName,
       "amodModemProductNameAndVer": amodModemProductNameAndVer,
       "amodLink": amodLink,
       "amodLinkTable": amodLinkTable,
       "amodLinkEntry": amodLinkEntry,
       "amodLinkIfIndex": amodLinkIfIndex,
       "amodLinkHdlcRxChecksumErrors": amodLinkHdlcRxChecksumErrors,
       "amodLinkHdlcRxLong": amodLinkHdlcRxLong,
       "amodLinkHdlcRxShort": amodLinkHdlcRxShort,
       "amodLinkHdlcStuffingErrors": amodLinkHdlcStuffingErrors,
       "amodLinkHdlcLostEndMarkers": amodLinkHdlcLostEndMarkers,
       "amodLinkHdlcRxOverflow": amodLinkHdlcRxOverflow,
       "amodLinkTxCalls": amodLinkTxCalls,
       "amodLinkTxCallsFailed": amodLinkTxCallsFailed,
       "amodLinkRxCalls": amodLinkRxCalls}
)
