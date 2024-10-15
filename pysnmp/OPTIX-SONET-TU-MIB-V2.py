# SNMP MIB module (OPTIX-SONET-TU-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-TU-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:34 2024
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

(optixProvisionSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionSonet")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

optixsonetFacilityMgt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LpbkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("crs", 3),
          ("ds1feac", 4),
          ("ds3feac", 5),
          ("fac2ni", 6),
          ("facility", 2),
          ("noloop", 255),
          ("terminal", 1))
    )



class IntfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              12,
              13,
              17,
              65,
              100,
              254)
        )
    )
    namedValues = NamedValues(
        *(("ds1-asyn-vt1", 1),
          ("ds3-asyn-sts1", 10),
          ("ds3-srv-ds1", 17),
          ("ds3-tmux-ds1", 13),
          ("ec", 12),
          ("invalid", 254),
          ("mix", 100),
          ("uas", 65))
    )



# MIB Managed Objects in the order of their OIDs

_Ds3PortAttribTable_Object = MibTable
ds3PortAttribTable = _Ds3PortAttribTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1)
)
if mibBuilder.loadTexts:
    ds3PortAttribTable.setStatus("current")
_Ds3PortAttribEntry_Object = MibTableRow
ds3PortAttribEntry = _Ds3PortAttribEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1)
)
ds3PortAttribEntry.setIndexNames(
    (0, "OPTIX-SONET-TU-MIB-V2", "ds3PortIndexSlotId"),
    (0, "OPTIX-SONET-TU-MIB-V2", "ds3PortIndexPortId"),
)
if mibBuilder.loadTexts:
    ds3PortAttribEntry.setStatus("current")
_Ds3PortIndexSlotId_Type = Gauge32
_Ds3PortIndexSlotId_Object = MibTableColumn
ds3PortIndexSlotId = _Ds3PortIndexSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 1),
    _Ds3PortIndexSlotId_Type()
)
ds3PortIndexSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PortIndexSlotId.setStatus("current")
_Ds3PortIndexPortId_Type = Gauge32
_Ds3PortIndexPortId_Object = MibTableColumn
ds3PortIndexPortId = _Ds3PortIndexPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 2),
    _Ds3PortIndexPortId_Type()
)
ds3PortIndexPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PortIndexPortId.setStatus("current")


class _Ds3PortAttribReq_Type(Integer32):
    """Custom type ds3PortAttribReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("invalid", 254),
          ("low", 2))
    )


_Ds3PortAttribReq_Type.__name__ = "Integer32"
_Ds3PortAttribReq_Object = MibTableColumn
ds3PortAttribReq = _Ds3PortAttribReq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 3),
    _Ds3PortAttribReq_Type()
)
ds3PortAttribReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribReq.setStatus("current")


class _Ds3PortAttribLbo_Type(Integer32):
    """Custom type ds3PortAttribLbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ds3PortAttribLbo_Type.__name__ = "Integer32"
_Ds3PortAttribLbo_Object = MibTableColumn
ds3PortAttribLbo = _Ds3PortAttribLbo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 4),
    _Ds3PortAttribLbo_Type()
)
ds3PortAttribLbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribLbo.setStatus("current")


class _Ds3PortAttribLineCde_Type(Integer32):
    """Custom type ds3PortAttribLineCde based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("b3zs", 3),
          ("invalid", 254))
    )


_Ds3PortAttribLineCde_Type.__name__ = "Integer32"
_Ds3PortAttribLineCde_Object = MibTableColumn
ds3PortAttribLineCde = _Ds3PortAttribLineCde_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 5),
    _Ds3PortAttribLineCde_Type()
)
ds3PortAttribLineCde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PortAttribLineCde.setStatus("current")


class _Ds3PortAttribFmt_Type(Integer32):
    """Custom type ds3PortAttribFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cbit", 3),
          ("m23", 4),
          ("unframed", 255))
    )


_Ds3PortAttribFmt_Type.__name__ = "Integer32"
_Ds3PortAttribFmt_Object = MibTableColumn
ds3PortAttribFmt = _Ds3PortAttribFmt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 6),
    _Ds3PortAttribFmt_Type()
)
ds3PortAttribFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribFmt.setStatus("current")


class _Ds3PortAttribTACC_Type(Integer32):
    """Custom type ds3PortAttribTACC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Ds3PortAttribTACC_Type.__name__ = "Integer32"
_Ds3PortAttribTACC_Object = MibTableColumn
ds3PortAttribTACC = _Ds3PortAttribTACC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 7),
    _Ds3PortAttribTACC_Type()
)
ds3PortAttribTACC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribTACC.setStatus("current")


class _Ds3PortAttribLof2ais_Type(Integer32):
    """Custom type ds3PortAttribLof2ais based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 254),
          ("no", 2),
          ("yes", 1))
    )


_Ds3PortAttribLof2ais_Type.__name__ = "Integer32"
_Ds3PortAttribLof2ais_Object = MibTableColumn
ds3PortAttribLof2ais = _Ds3PortAttribLof2ais_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 8),
    _Ds3PortAttribLof2ais_Type()
)
ds3PortAttribLof2ais.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribLof2ais.setStatus("current")


class _Ds3PortAttribSvtimer_Type(OctetString):
    """Custom type ds3PortAttribSvtimer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Ds3PortAttribSvtimer_Type.__name__ = "OctetString"
_Ds3PortAttribSvtimer_Object = MibTableColumn
ds3PortAttribSvtimer = _Ds3PortAttribSvtimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 9),
    _Ds3PortAttribSvtimer_Type()
)
ds3PortAttribSvtimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribSvtimer.setStatus("current")


class _Ds3PortAttribPST_Type(OctetString):
    """Custom type ds3PortAttribPST based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ds3PortAttribPST_Type.__name__ = "OctetString"
_Ds3PortAttribPST_Object = MibTableColumn
ds3PortAttribPST = _Ds3PortAttribPST_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 10),
    _Ds3PortAttribPST_Type()
)
ds3PortAttribPST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribPST.setStatus("current")


class _Ds3PortAttribSST_Type(OctetString):
    """Custom type ds3PortAttribSST based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ds3PortAttribSST_Type.__name__ = "OctetString"
_Ds3PortAttribSST_Object = MibTableColumn
ds3PortAttribSST = _Ds3PortAttribSST_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 11),
    _Ds3PortAttribSST_Type()
)
ds3PortAttribSST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PortAttribSST.setStatus("current")
_Ds3LoopbackStatus_Type = LpbkType
_Ds3LoopbackStatus_Object = MibTableColumn
ds3LoopbackStatus = _Ds3LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 12),
    _Ds3LoopbackStatus_Type()
)
ds3LoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LoopbackStatus.setStatus("current")
_Ds3LoopbackTimeout_Type = Gauge32
_Ds3LoopbackTimeout_Object = MibTableColumn
ds3LoopbackTimeout = _Ds3LoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 13),
    _Ds3LoopbackTimeout_Type()
)
ds3LoopbackTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LoopbackTimeout.setStatus("current")


class _Ds3RemoteALWFELPBK_Type(Integer32):
    """Custom type ds3RemoteALWFELPBK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("invalid", 254))
    )


_Ds3RemoteALWFELPBK_Type.__name__ = "Integer32"
_Ds3RemoteALWFELPBK_Object = MibTableColumn
ds3RemoteALWFELPBK = _Ds3RemoteALWFELPBK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 1, 1, 14),
    _Ds3RemoteALWFELPBK_Type()
)
ds3RemoteALWFELPBK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3RemoteALWFELPBK.setStatus("current")
_Ds1PortAttribTable_Object = MibTable
ds1PortAttribTable = _Ds1PortAttribTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2)
)
if mibBuilder.loadTexts:
    ds1PortAttribTable.setStatus("current")
_Ds1PortAttribEntry_Object = MibTableRow
ds1PortAttribEntry = _Ds1PortAttribEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1)
)
ds1PortAttribEntry.setIndexNames(
    (0, "OPTIX-SONET-TU-MIB-V2", "ds1PortIndexSlotId"),
    (0, "OPTIX-SONET-TU-MIB-V2", "ds1PortIndexPortId"),
    (0, "OPTIX-SONET-TU-MIB-V2", "ds1PortIndexPath"),
)
if mibBuilder.loadTexts:
    ds1PortAttribEntry.setStatus("current")
_Ds1PortIndexSlotId_Type = Gauge32
_Ds1PortIndexSlotId_Object = MibTableColumn
ds1PortIndexSlotId = _Ds1PortIndexSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 1),
    _Ds1PortIndexSlotId_Type()
)
ds1PortIndexSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PortIndexSlotId.setStatus("current")
_Ds1PortIndexPortId_Type = Gauge32
_Ds1PortIndexPortId_Object = MibTableColumn
ds1PortIndexPortId = _Ds1PortIndexPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 2),
    _Ds1PortIndexPortId_Type()
)
ds1PortIndexPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PortIndexPortId.setStatus("current")
_Ds1PortIndexPath_Type = Gauge32
_Ds1PortIndexPath_Object = MibTableColumn
ds1PortIndexPath = _Ds1PortIndexPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 3),
    _Ds1PortIndexPath_Type()
)
ds1PortIndexPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PortIndexPath.setStatus("current")


class _Ds1PortAttribLbo_Type(Integer32):
    """Custom type ds1PortAttribLbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Ds1PortAttribLbo_Type.__name__ = "Integer32"
_Ds1PortAttribLbo_Object = MibTableColumn
ds1PortAttribLbo = _Ds1PortAttribLbo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 4),
    _Ds1PortAttribLbo_Type()
)
ds1PortAttribLbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribLbo.setStatus("current")


class _Ds1PortAttribLineCde_Type(Integer32):
    """Custom type ds1PortAttribLineCde based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1),
          ("invalid", 254))
    )


_Ds1PortAttribLineCde_Type.__name__ = "Integer32"
_Ds1PortAttribLineCde_Object = MibTableColumn
ds1PortAttribLineCde = _Ds1PortAttribLineCde_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 5),
    _Ds1PortAttribLineCde_Type()
)
ds1PortAttribLineCde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribLineCde.setStatus("current")


class _Ds1PortAttribFmt_Type(Integer32):
    """Custom type ds1PortAttribFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("esf", 2),
          ("sf", 1),
          ("unframed", 255))
    )


_Ds1PortAttribFmt_Type.__name__ = "Integer32"
_Ds1PortAttribFmt_Object = MibTableColumn
ds1PortAttribFmt = _Ds1PortAttribFmt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 6),
    _Ds1PortAttribFmt_Type()
)
ds1PortAttribFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribFmt.setStatus("current")


class _Ds1PortAttribTACC_Type(Integer32):
    """Custom type ds1PortAttribTACC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Ds1PortAttribTACC_Type.__name__ = "Integer32"
_Ds1PortAttribTACC_Object = MibTableColumn
ds1PortAttribTACC = _Ds1PortAttribTACC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 7),
    _Ds1PortAttribTACC_Type()
)
ds1PortAttribTACC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribTACC.setStatus("current")


class _Ds1PortAttribLof2ais_Type(Integer32):
    """Custom type ds1PortAttribLof2ais based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 254),
          ("no", 2),
          ("yes", 1))
    )


_Ds1PortAttribLof2ais_Type.__name__ = "Integer32"
_Ds1PortAttribLof2ais_Object = MibTableColumn
ds1PortAttribLof2ais = _Ds1PortAttribLof2ais_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 8),
    _Ds1PortAttribLof2ais_Type()
)
ds1PortAttribLof2ais.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribLof2ais.setStatus("current")


class _Ds1PortAttribSvtimer_Type(OctetString):
    """Custom type ds1PortAttribSvtimer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Ds1PortAttribSvtimer_Type.__name__ = "OctetString"
_Ds1PortAttribSvtimer_Object = MibTableColumn
ds1PortAttribSvtimer = _Ds1PortAttribSvtimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 9),
    _Ds1PortAttribSvtimer_Type()
)
ds1PortAttribSvtimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribSvtimer.setStatus("current")


class _Ds1PortAttribPST_Type(OctetString):
    """Custom type ds1PortAttribPST based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ds1PortAttribPST_Type.__name__ = "OctetString"
_Ds1PortAttribPST_Object = MibTableColumn
ds1PortAttribPST = _Ds1PortAttribPST_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 10),
    _Ds1PortAttribPST_Type()
)
ds1PortAttribPST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribPST.setStatus("current")


class _Ds1PortAttribSST_Type(OctetString):
    """Custom type ds1PortAttribSST based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ds1PortAttribSST_Type.__name__ = "OctetString"
_Ds1PortAttribSST_Object = MibTableColumn
ds1PortAttribSST = _Ds1PortAttribSST_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 11),
    _Ds1PortAttribSST_Type()
)
ds1PortAttribSST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortAttribSST.setStatus("current")
_Ds1LoopbackStatus_Type = LpbkType
_Ds1LoopbackStatus_Object = MibTableColumn
ds1LoopbackStatus = _Ds1LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 12),
    _Ds1LoopbackStatus_Type()
)
ds1LoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1LoopbackStatus.setStatus("current")
_Ds1LoopbackTimeout_Type = Gauge32
_Ds1LoopbackTimeout_Object = MibTableColumn
ds1LoopbackTimeout = _Ds1LoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 13),
    _Ds1LoopbackTimeout_Type()
)
ds1LoopbackTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LoopbackTimeout.setStatus("current")


class _Ds1RemoteALWFELPBK_Type(Integer32):
    """Custom type ds1RemoteALWFELPBK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("invalid", 254))
    )


_Ds1RemoteALWFELPBK_Type.__name__ = "Integer32"
_Ds1RemoteALWFELPBK_Object = MibTableColumn
ds1RemoteALWFELPBK = _Ds1RemoteALWFELPBK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 14),
    _Ds1RemoteALWFELPBK_Type()
)
ds1RemoteALWFELPBK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1RemoteALWFELPBK.setStatus("current")
_Ds1PortLpbkAutomaticTime_Type = Gauge32
_Ds1PortLpbkAutomaticTime_Object = MibTableColumn
ds1PortLpbkAutomaticTime = _Ds1PortLpbkAutomaticTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 2, 1, 15),
    _Ds1PortLpbkAutomaticTime_Type()
)
ds1PortLpbkAutomaticTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1PortLpbkAutomaticTime.setStatus("current")
_PortTypeTable_Object = MibTable
portTypeTable = _PortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 3)
)
if mibBuilder.loadTexts:
    portTypeTable.setStatus("current")
_PortTypeEntry_Object = MibTableRow
portTypeEntry = _PortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 3, 1)
)
portTypeEntry.setIndexNames(
    (0, "OPTIX-SONET-TU-MIB-V2", "portIndexSlotId"),
    (0, "OPTIX-SONET-TU-MIB-V2", "portIndexPortId"),
)
if mibBuilder.loadTexts:
    portTypeEntry.setStatus("current")
_PortIndexSlotId_Type = Gauge32
_PortIndexSlotId_Object = MibTableColumn
portIndexSlotId = _PortIndexSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 3, 1, 1),
    _PortIndexSlotId_Type()
)
portIndexSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndexSlotId.setStatus("current")
_PortIndexPortId_Type = Gauge32
_PortIndexPortId_Object = MibTableColumn
portIndexPortId = _PortIndexPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 3, 1, 2),
    _PortIndexPortId_Type()
)
portIndexPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndexPortId.setStatus("current")
_PortType_Type = IntfType
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 3, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portType.setStatus("current")
_OptixsonetFacilityMgtConformance_ObjectIdentity = ObjectIdentity
optixsonetFacilityMgtConformance = _OptixsonetFacilityMgtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 4)
)
_OptixsonetFacilityMgtGroups_ObjectIdentity = ObjectIdentity
optixsonetFacilityMgtGroups = _OptixsonetFacilityMgtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 4, 1)
)
_OptixsonetFacilityMgtCompliances_ObjectIdentity = ObjectIdentity
optixsonetFacilityMgtCompliances = _OptixsonetFacilityMgtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 4, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 4, 1, 1)
)
currentObjectGroup.setObjects(
      *(("OPTIX-SONET-TU-MIB-V2", "ds3PortIndexSlotId"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortIndexPortId"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribReq"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribLbo"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribLineCde"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribFmt"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribTACC"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribLof2ais"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribSvtimer"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribPST"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3PortAttribSST"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3LoopbackStatus"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3LoopbackTimeout"),
        ("OPTIX-SONET-TU-MIB-V2", "ds3RemoteALWFELPBK"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortIndexSlotId"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortIndexPortId"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortIndexPath"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribLbo"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribLineCde"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribFmt"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribTACC"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribLof2ais"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribSvtimer"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribPST"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortAttribSST"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1LoopbackStatus"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1LoopbackTimeout"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1RemoteALWFELPBK"),
        ("OPTIX-SONET-TU-MIB-V2", "ds1PortLpbkAutomaticTime"),
        ("OPTIX-SONET-TU-MIB-V2", "portIndexSlotId"),
        ("OPTIX-SONET-TU-MIB-V2", "portIndexPortId"),
        ("OPTIX-SONET-TU-MIB-V2", "portType"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-TU-MIB-V2",
    **{"LpbkType": LpbkType,
       "IntfType": IntfType,
       "optixsonetFacilityMgt": optixsonetFacilityMgt,
       "ds3PortAttribTable": ds3PortAttribTable,
       "ds3PortAttribEntry": ds3PortAttribEntry,
       "ds3PortIndexSlotId": ds3PortIndexSlotId,
       "ds3PortIndexPortId": ds3PortIndexPortId,
       "ds3PortAttribReq": ds3PortAttribReq,
       "ds3PortAttribLbo": ds3PortAttribLbo,
       "ds3PortAttribLineCde": ds3PortAttribLineCde,
       "ds3PortAttribFmt": ds3PortAttribFmt,
       "ds3PortAttribTACC": ds3PortAttribTACC,
       "ds3PortAttribLof2ais": ds3PortAttribLof2ais,
       "ds3PortAttribSvtimer": ds3PortAttribSvtimer,
       "ds3PortAttribPST": ds3PortAttribPST,
       "ds3PortAttribSST": ds3PortAttribSST,
       "ds3LoopbackStatus": ds3LoopbackStatus,
       "ds3LoopbackTimeout": ds3LoopbackTimeout,
       "ds3RemoteALWFELPBK": ds3RemoteALWFELPBK,
       "ds1PortAttribTable": ds1PortAttribTable,
       "ds1PortAttribEntry": ds1PortAttribEntry,
       "ds1PortIndexSlotId": ds1PortIndexSlotId,
       "ds1PortIndexPortId": ds1PortIndexPortId,
       "ds1PortIndexPath": ds1PortIndexPath,
       "ds1PortAttribLbo": ds1PortAttribLbo,
       "ds1PortAttribLineCde": ds1PortAttribLineCde,
       "ds1PortAttribFmt": ds1PortAttribFmt,
       "ds1PortAttribTACC": ds1PortAttribTACC,
       "ds1PortAttribLof2ais": ds1PortAttribLof2ais,
       "ds1PortAttribSvtimer": ds1PortAttribSvtimer,
       "ds1PortAttribPST": ds1PortAttribPST,
       "ds1PortAttribSST": ds1PortAttribSST,
       "ds1LoopbackStatus": ds1LoopbackStatus,
       "ds1LoopbackTimeout": ds1LoopbackTimeout,
       "ds1RemoteALWFELPBK": ds1RemoteALWFELPBK,
       "ds1PortLpbkAutomaticTime": ds1PortLpbkAutomaticTime,
       "portTypeTable": portTypeTable,
       "portTypeEntry": portTypeEntry,
       "portIndexSlotId": portIndexSlotId,
       "portIndexPortId": portIndexPortId,
       "portType": portType,
       "optixsonetFacilityMgtConformance": optixsonetFacilityMgtConformance,
       "optixsonetFacilityMgtGroups": optixsonetFacilityMgtGroups,
       "currentObjectGroup": currentObjectGroup,
       "optixsonetFacilityMgtCompliances": optixsonetFacilityMgtCompliances,
       "basicCompliance": basicCompliance}
)
