# SNMP MIB module (BAS-TG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-TG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:34 2024
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

(basTrafGen,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basTrafGen")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

basTrafGenMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasTrafGenTable_Object = MibTable
basTrafGenTable = _BasTrafGenTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    basTrafGenTable.setStatus("current")
_BasTrafGenEntry_Object = MibTableRow
basTrafGenEntry = _BasTrafGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1)
)
basTrafGenEntry.setIndexNames(
    (0, "BAS-TG-MIB", "basTrafGenIndex"),
)
if mibBuilder.loadTexts:
    basTrafGenEntry.setStatus("current")
_BasTrafGenIndex_Type = Integer32
_BasTrafGenIndex_Object = MibTableColumn
basTrafGenIndex = _BasTrafGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 1),
    _BasTrafGenIndex_Type()
)
basTrafGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTrafGenIndex.setStatus("current")


class _BasTrafGenTransport_Type(Integer32):
    """Custom type basTrafGenTransport based on Integer32"""
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
        *(("basTrafIp", 1),
          ("basTrafTcp", 3),
          ("basTrafUdp", 2))
    )


_BasTrafGenTransport_Type.__name__ = "Integer32"
_BasTrafGenTransport_Object = MibTableColumn
basTrafGenTransport = _BasTrafGenTransport_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 2),
    _BasTrafGenTransport_Type()
)
basTrafGenTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenTransport.setStatus("current")


class _BasTrafGenPort_Type(Integer32):
    """Custom type basTrafGenPort based on Integer32"""
    defaultValue = 99


_BasTrafGenPort_Object = MibTableColumn
basTrafGenPort = _BasTrafGenPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 3),
    _BasTrafGenPort_Type()
)
basTrafGenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenPort.setStatus("current")


class _BasTrafGenStart_Type(Integer32):
    """Custom type basTrafGenStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basTrafStart", 1),
          ("basTrafStop", 2))
    )


_BasTrafGenStart_Type.__name__ = "Integer32"
_BasTrafGenStart_Object = MibTableColumn
basTrafGenStart = _BasTrafGenStart_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 4),
    _BasTrafGenStart_Type()
)
basTrafGenStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenStart.setStatus("current")


class _BasTrafGenRate_Type(Integer32):
    """Custom type basTrafGenRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basTran1sec", 2),
          ("basTranMax", 1))
    )


_BasTrafGenRate_Type.__name__ = "Integer32"
_BasTrafGenRate_Object = MibTableColumn
basTrafGenRate = _BasTrafGenRate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 5),
    _BasTrafGenRate_Type()
)
basTrafGenRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenRate.setStatus("current")
_BasTrafGenDest_Type = IpAddress
_BasTrafGenDest_Object = MibTableColumn
basTrafGenDest = _BasTrafGenDest_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 6),
    _BasTrafGenDest_Type()
)
basTrafGenDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenDest.setStatus("current")
_BasTrafGenSrc_Type = IpAddress
_BasTrafGenSrc_Object = MibTableColumn
basTrafGenSrc = _BasTrafGenSrc_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 7),
    _BasTrafGenSrc_Type()
)
basTrafGenSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenSrc.setStatus("current")
_BasTrafGenIn_Type = Counter32
_BasTrafGenIn_Object = MibTableColumn
basTrafGenIn = _BasTrafGenIn_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 8),
    _BasTrafGenIn_Type()
)
basTrafGenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTrafGenIn.setStatus("current")
_BasTrafGenOut_Type = Counter32
_BasTrafGenOut_Object = MibTableColumn
basTrafGenOut = _BasTrafGenOut_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 9),
    _BasTrafGenOut_Type()
)
basTrafGenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTrafGenOut.setStatus("current")
_BasTrafGenSeqError_Type = Counter32
_BasTrafGenSeqError_Object = MibTableColumn
basTrafGenSeqError = _BasTrafGenSeqError_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 10),
    _BasTrafGenSeqError_Type()
)
basTrafGenSeqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTrafGenSeqError.setStatus("current")
_BasTrafGenSize_Type = Integer32
_BasTrafGenSize_Object = MibTableColumn
basTrafGenSize = _BasTrafGenSize_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 11),
    _BasTrafGenSize_Type()
)
basTrafGenSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenSize.setStatus("current")
_BasTrafGenPattern_Type = Integer32
_BasTrafGenPattern_Object = MibTableColumn
basTrafGenPattern = _BasTrafGenPattern_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 12),
    _BasTrafGenPattern_Type()
)
basTrafGenPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenPattern.setStatus("current")
_BasTrafGenReset_Type = Integer32
_BasTrafGenReset_Object = MibTableColumn
basTrafGenReset = _BasTrafGenReset_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 13),
    _BasTrafGenReset_Type()
)
basTrafGenReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenReset.setStatus("current")
_BasTrafGenStatus_Type = RowStatus
_BasTrafGenStatus_Object = MibTableColumn
basTrafGenStatus = _BasTrafGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13, 1, 1, 1, 14),
    _BasTrafGenStatus_Type()
)
basTrafGenStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrafGenStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-TG-MIB",
    **{"basTrafGenMIB": basTrafGenMIB,
       "basTrafGenTable": basTrafGenTable,
       "basTrafGenEntry": basTrafGenEntry,
       "basTrafGenIndex": basTrafGenIndex,
       "basTrafGenTransport": basTrafGenTransport,
       "basTrafGenPort": basTrafGenPort,
       "basTrafGenStart": basTrafGenStart,
       "basTrafGenRate": basTrafGenRate,
       "basTrafGenDest": basTrafGenDest,
       "basTrafGenSrc": basTrafGenSrc,
       "basTrafGenIn": basTrafGenIn,
       "basTrafGenOut": basTrafGenOut,
       "basTrafGenSeqError": basTrafGenSeqError,
       "basTrafGenSize": basTrafGenSize,
       "basTrafGenPattern": basTrafGenPattern,
       "basTrafGenReset": basTrafGenReset,
       "basTrafGenStatus": basTrafGenStatus}
)
