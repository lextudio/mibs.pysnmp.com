# SNMP MIB module (BIANCA-BRICK-PPPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PPPOA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:40 2024
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Pppoa_ObjectIdentity = ObjectIdentity
pppoa = _Pppoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 28)
)
_PppoaCallTable_Object = MibTable
pppoaCallTable = _PppoaCallTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1)
)
if mibBuilder.loadTexts:
    pppoaCallTable.setStatus("mandatory")
_PppoaCallEntry_Object = MibTableRow
pppoaCallEntry = _PppoaCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1)
)
pppoaCallEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPPOA-MIB", "pppoaCallId"),
)
if mibBuilder.loadTexts:
    pppoaCallEntry.setStatus("mandatory")
_PppoaCallId_Type = Integer32
_PppoaCallId_Object = MibTableColumn
pppoaCallId = _PppoaCallId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 1),
    _PppoaCallId_Type()
)
pppoaCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallId.setStatus("mandatory")


class _PppoaCallState_Type(Integer32):
    """Custom type pppoaCallState based on Integer32"""
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
        *(("established", 2),
          ("idle", 1),
          ("terminated", 3))
    )


_PppoaCallState_Type.__name__ = "Integer32"
_PppoaCallState_Object = MibTableColumn
pppoaCallState = _PppoaCallState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 2),
    _PppoaCallState_Type()
)
pppoaCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaCallState.setStatus("mandatory")
_PppoaCallReceivedPackets_Type = Counter32
_PppoaCallReceivedPackets_Object = MibTableColumn
pppoaCallReceivedPackets = _PppoaCallReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 3),
    _PppoaCallReceivedPackets_Type()
)
pppoaCallReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallReceivedPackets.setStatus("mandatory")
_PppoaCallReceivedOctets_Type = Counter32
_PppoaCallReceivedOctets_Object = MibTableColumn
pppoaCallReceivedOctets = _PppoaCallReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 4),
    _PppoaCallReceivedOctets_Type()
)
pppoaCallReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallReceivedOctets.setStatus("mandatory")
_PppoaCallReceivedErrors_Type = Counter32
_PppoaCallReceivedErrors_Object = MibTableColumn
pppoaCallReceivedErrors = _PppoaCallReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 5),
    _PppoaCallReceivedErrors_Type()
)
pppoaCallReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallReceivedErrors.setStatus("mandatory")
_PppoaCallTransmitPackets_Type = Counter32
_PppoaCallTransmitPackets_Object = MibTableColumn
pppoaCallTransmitPackets = _PppoaCallTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 6),
    _PppoaCallTransmitPackets_Type()
)
pppoaCallTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallTransmitPackets.setStatus("mandatory")
_PppoaCallTransmitOctets_Type = Counter32
_PppoaCallTransmitOctets_Object = MibTableColumn
pppoaCallTransmitOctets = _PppoaCallTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 7),
    _PppoaCallTransmitOctets_Type()
)
pppoaCallTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallTransmitOctets.setStatus("mandatory")
_PppoaCallTransmitErrors_Type = Counter32
_PppoaCallTransmitErrors_Object = MibTableColumn
pppoaCallTransmitErrors = _PppoaCallTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 8),
    _PppoaCallTransmitErrors_Type()
)
pppoaCallTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallTransmitErrors.setStatus("mandatory")
_PppoaCallInfo_Type = DisplayString
_PppoaCallInfo_Object = MibTableColumn
pppoaCallInfo = _PppoaCallInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 28, 1, 1, 9),
    _PppoaCallInfo_Type()
)
pppoaCallInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaCallInfo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PPPOA-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "pppoa": pppoa,
       "pppoaCallTable": pppoaCallTable,
       "pppoaCallEntry": pppoaCallEntry,
       "pppoaCallId": pppoaCallId,
       "pppoaCallState": pppoaCallState,
       "pppoaCallReceivedPackets": pppoaCallReceivedPackets,
       "pppoaCallReceivedOctets": pppoaCallReceivedOctets,
       "pppoaCallReceivedErrors": pppoaCallReceivedErrors,
       "pppoaCallTransmitPackets": pppoaCallTransmitPackets,
       "pppoaCallTransmitOctets": pppoaCallTransmitOctets,
       "pppoaCallTransmitErrors": pppoaCallTransmitErrors,
       "pppoaCallInfo": pppoaCallInfo}
)
