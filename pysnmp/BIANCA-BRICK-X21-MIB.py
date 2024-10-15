# SNMP MIB module (BIANCA-BRICK-X21-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-X21-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:51 2024
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



class Date(Integer32):
    """Custom type Date based on Integer32"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_X21_ObjectIdentity = ObjectIdentity
x21 = _X21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 10)
)
_X21IfTable_Object = MibTable
x21IfTable = _X21IfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1)
)
if mibBuilder.loadTexts:
    x21IfTable.setStatus("mandatory")
_X21IfEntry_Object = MibTableRow
x21IfEntry = _X21IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1)
)
x21IfEntry.setIndexNames(
    (0, "BIANCA-BRICK-X21-MIB", "x21IfIndex"),
)
if mibBuilder.loadTexts:
    x21IfEntry.setStatus("mandatory")
_X21IfIndex_Type = Integer32
_X21IfIndex_Object = MibTableColumn
x21IfIndex = _X21IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 1),
    _X21IfIndex_Type()
)
x21IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfIndex.setStatus("mandatory")


class _X21IfL1State_Type(Integer32):
    """Custom type x21IfL1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dn", 1),
          ("up", 2))
    )


_X21IfL1State_Type.__name__ = "Integer32"
_X21IfL1State_Object = MibTableColumn
x21IfL1State = _X21IfL1State_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 2),
    _X21IfL1State_Type()
)
x21IfL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfL1State.setStatus("mandatory")


class _X21IfL1Mode_Type(Integer32):
    """Custom type x21IfL1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_X21IfL1Mode_Type.__name__ = "Integer32"
_X21IfL1Mode_Object = MibTableColumn
x21IfL1Mode = _X21IfL1Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 3),
    _X21IfL1Mode_Type()
)
x21IfL1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21IfL1Mode.setStatus("mandatory")


class _X21IfIfLeads_Type(Integer32):
    """Custom type x21IfIfLeads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_X21IfIfLeads_Type.__name__ = "Integer32"
_X21IfIfLeads_Object = MibTableColumn
x21IfIfLeads = _X21IfIfLeads_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 4),
    _X21IfIfLeads_Type()
)
x21IfIfLeads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21IfIfLeads.setStatus("mandatory")


class _X21IfSpeed_Type(Integer32):
    """Custom type x21IfSpeed based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("s1024k", 2),
          ("s128k", 5),
          ("s14400", 9),
          ("s19200", 8),
          ("s2048k", 1),
          ("s2400", 11),
          ("s256k", 4),
          ("s38400", 7),
          ("s512k", 3),
          ("s64000", 6),
          ("s9600", 10))
    )


_X21IfSpeed_Type.__name__ = "Integer32"
_X21IfSpeed_Object = MibTableColumn
x21IfSpeed = _X21IfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 5),
    _X21IfSpeed_Type()
)
x21IfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21IfSpeed.setStatus("mandatory")


class _X21IfL2Mode_Type(Integer32):
    """Custom type x21IfL2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("dce", 2),
          ("dte", 1))
    )


_X21IfL2Mode_Type.__name__ = "Integer32"
_X21IfL2Mode_Object = MibTableColumn
x21IfL2Mode = _X21IfL2Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 6),
    _X21IfL2Mode_Type()
)
x21IfL2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21IfL2Mode.setStatus("mandatory")
_X21IfSpeedReal_Type = Counter32
_X21IfSpeedReal_Object = MibTableColumn
x21IfSpeedReal = _X21IfSpeedReal_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 7),
    _X21IfSpeedReal_Type()
)
x21IfSpeedReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfSpeedReal.setStatus("mandatory")
_X21IfRxPackets_Type = Counter32
_X21IfRxPackets_Object = MibTableColumn
x21IfRxPackets = _X21IfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 8),
    _X21IfRxPackets_Type()
)
x21IfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfRxPackets.setStatus("mandatory")
_X21IfRxOctets_Type = Counter32
_X21IfRxOctets_Object = MibTableColumn
x21IfRxOctets = _X21IfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 9),
    _X21IfRxOctets_Type()
)
x21IfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfRxOctets.setStatus("mandatory")
_X21IfTxPackets_Type = Counter32
_X21IfTxPackets_Object = MibTableColumn
x21IfTxPackets = _X21IfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 10),
    _X21IfTxPackets_Type()
)
x21IfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfTxPackets.setStatus("mandatory")
_X21IfTxOctets_Type = Counter32
_X21IfTxOctets_Object = MibTableColumn
x21IfTxOctets = _X21IfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 11),
    _X21IfTxOctets_Type()
)
x21IfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfTxOctets.setStatus("mandatory")
_X21IfRxResets_Type = Counter32
_X21IfRxResets_Object = MibTableColumn
x21IfRxResets = _X21IfRxResets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 12),
    _X21IfRxResets_Type()
)
x21IfRxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfRxResets.setStatus("mandatory")
_X21IfRxAborts_Type = Counter32
_X21IfRxAborts_Object = MibTableColumn
x21IfRxAborts = _X21IfRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 13),
    _X21IfRxAborts_Type()
)
x21IfRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfRxAborts.setStatus("mandatory")
_X21IfRxOverruns_Type = Counter32
_X21IfRxOverruns_Object = MibTableColumn
x21IfRxOverruns = _X21IfRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 14),
    _X21IfRxOverruns_Type()
)
x21IfRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfRxOverruns.setStatus("mandatory")
_X21IfRxCRCErrors_Type = Counter32
_X21IfRxCRCErrors_Object = MibTableColumn
x21IfRxCRCErrors = _X21IfRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 15),
    _X21IfRxCRCErrors_Type()
)
x21IfRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfRxCRCErrors.setStatus("mandatory")
_X21IfRxGiantFrames_Type = Counter32
_X21IfRxGiantFrames_Object = MibTableColumn
x21IfRxGiantFrames = _X21IfRxGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 16),
    _X21IfRxGiantFrames_Type()
)
x21IfRxGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfRxGiantFrames.setStatus("mandatory")
_X21IfTxResets_Type = Counter32
_X21IfTxResets_Object = MibTableColumn
x21IfTxResets = _X21IfTxResets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 17),
    _X21IfTxResets_Type()
)
x21IfTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfTxResets.setStatus("mandatory")
_X21IfTxAborts_Type = Counter32
_X21IfTxAborts_Object = MibTableColumn
x21IfTxAborts = _X21IfTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 18),
    _X21IfTxAborts_Type()
)
x21IfTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfTxAborts.setStatus("mandatory")
_X21IfTxUnderruns_Type = Counter32
_X21IfTxUnderruns_Object = MibTableColumn
x21IfTxUnderruns = _X21IfTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 19),
    _X21IfTxUnderruns_Type()
)
x21IfTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfTxUnderruns.setStatus("mandatory")
_X21IfTxGiantFrames_Type = Counter32
_X21IfTxGiantFrames_Object = MibTableColumn
x21IfTxGiantFrames = _X21IfTxGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 20),
    _X21IfTxGiantFrames_Type()
)
x21IfTxGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21IfTxGiantFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-X21-MIB",
    **{"Date": Date,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "x21": x21,
       "x21IfTable": x21IfTable,
       "x21IfEntry": x21IfEntry,
       "x21IfIndex": x21IfIndex,
       "x21IfL1State": x21IfL1State,
       "x21IfL1Mode": x21IfL1Mode,
       "x21IfIfLeads": x21IfIfLeads,
       "x21IfSpeed": x21IfSpeed,
       "x21IfL2Mode": x21IfL2Mode,
       "x21IfSpeedReal": x21IfSpeedReal,
       "x21IfRxPackets": x21IfRxPackets,
       "x21IfRxOctets": x21IfRxOctets,
       "x21IfTxPackets": x21IfTxPackets,
       "x21IfTxOctets": x21IfTxOctets,
       "x21IfRxResets": x21IfRxResets,
       "x21IfRxAborts": x21IfRxAborts,
       "x21IfRxOverruns": x21IfRxOverruns,
       "x21IfRxCRCErrors": x21IfRxCRCErrors,
       "x21IfRxGiantFrames": x21IfRxGiantFrames,
       "x21IfTxResets": x21IfTxResets,
       "x21IfTxAborts": x21IfTxAborts,
       "x21IfTxUnderruns": x21IfTxUnderruns,
       "x21IfTxGiantFrames": x21IfTxGiantFrames}
)
