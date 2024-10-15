# SNMP MIB module (S5-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:14 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

(s5Chassis,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5Chassis")

(AttId,
 LocChan) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "AttId",
    "LocChan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

s5ChasMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 10)
)
s5ChasMib.setRevisions(
        ("2015-04-07 00:00",
         "2013-11-26 00:00",
         "2013-10-18 00:00",
         "2013-10-16 00:00",
         "2013-10-10 00:00",
         "2013-09-09 00:00",
         "2013-08-27 00:00",
         "2012-12-20 00:00",
         "2012-06-01 00:00",
         "2012-02-21 00:00",
         "2011-10-11 00:00",
         "2011-04-22 00:00",
         "2010-10-18 00:00",
         "2008-05-22 00:00",
         "2008-02-20 00:00",
         "2005-05-11 00:00",
         "2005-05-05 00:00",
         "2004-10-29 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5ChasGen_ObjectIdentity = ObjectIdentity
s5ChasGen = _S5ChasGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1)
)
_S5ChasType_Type = ObjectIdentifier
_S5ChasType_Object = MibScalar
s5ChasType = _S5ChasType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 1),
    _S5ChasType_Type()
)
s5ChasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasType.setStatus("current")


class _S5ChasDescr_Type(DisplayString):
    """Custom type s5ChasDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_S5ChasDescr_Type.__name__ = "DisplayString"
_S5ChasDescr_Object = MibScalar
s5ChasDescr = _S5ChasDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 2),
    _S5ChasDescr_Type()
)
s5ChasDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasDescr.setStatus("current")


class _S5ChasLocation_Type(DisplayString):
    """Custom type s5ChasLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_S5ChasLocation_Type.__name__ = "DisplayString"
_S5ChasLocation_Object = MibScalar
s5ChasLocation = _S5ChasLocation_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 3),
    _S5ChasLocation_Type()
)
s5ChasLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasLocation.setStatus("current")


class _S5ChasContact_Type(DisplayString):
    """Custom type s5ChasContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_S5ChasContact_Type.__name__ = "DisplayString"
_S5ChasContact_Object = MibScalar
s5ChasContact = _S5ChasContact_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 4),
    _S5ChasContact_Type()
)
s5ChasContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasContact.setStatus("current")


class _S5ChasVer_Type(DisplayString):
    """Custom type s5ChasVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5ChasVer_Type.__name__ = "DisplayString"
_S5ChasVer_Object = MibScalar
s5ChasVer = _S5ChasVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 5),
    _S5ChasVer_Type()
)
s5ChasVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasVer.setStatus("current")


class _S5ChasSerNum_Type(DisplayString):
    """Custom type s5ChasSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5ChasSerNum_Type.__name__ = "DisplayString"
_S5ChasSerNum_Object = MibScalar
s5ChasSerNum = _S5ChasSerNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 6),
    _S5ChasSerNum_Type()
)
s5ChasSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasSerNum.setStatus("current")
_S5ChasGblPhysChngs_Type = Counter32
_S5ChasGblPhysChngs_Object = MibScalar
s5ChasGblPhysChngs = _S5ChasGblPhysChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 7),
    _S5ChasGblPhysChngs_Type()
)
s5ChasGblPhysChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGblPhysChngs.setStatus("current")
_S5ChasGblPhysLstChng_Type = TimeTicks
_S5ChasGblPhysLstChng_Object = MibScalar
s5ChasGblPhysLstChng = _S5ChasGblPhysLstChng_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 8),
    _S5ChasGblPhysLstChng_Type()
)
s5ChasGblPhysLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGblPhysLstChng.setStatus("current")
_S5ChasGblAttChngs_Type = Counter32
_S5ChasGblAttChngs_Object = MibScalar
s5ChasGblAttChngs = _S5ChasGblAttChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 9),
    _S5ChasGblAttChngs_Type()
)
s5ChasGblAttChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGblAttChngs.setStatus("current")
_S5ChasGblAttLstChng_Type = TimeTicks
_S5ChasGblAttLstChng_Object = MibScalar
s5ChasGblAttLstChng = _S5ChasGblAttLstChng_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 10),
    _S5ChasGblAttLstChng_Type()
)
s5ChasGblAttLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGblAttLstChng.setStatus("current")
_S5ChasGblConfChngs_Type = Counter32
_S5ChasGblConfChngs_Object = MibScalar
s5ChasGblConfChngs = _S5ChasGblConfChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 11),
    _S5ChasGblConfChngs_Type()
)
s5ChasGblConfChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGblConfChngs.setStatus("current")
_S5ChasGblConfLstChng_Type = TimeTicks
_S5ChasGblConfLstChng_Object = MibScalar
s5ChasGblConfLstChng = _S5ChasGblConfLstChng_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 12),
    _S5ChasGblConfLstChng_Type()
)
s5ChasGblConfLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGblConfLstChng.setStatus("current")
_S5ChasGrp_ObjectIdentity = ObjectIdentity
s5ChasGrp = _S5ChasGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2)
)
_S5ChasGrpTable_Object = MibTable
s5ChasGrpTable = _S5ChasGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    s5ChasGrpTable.setStatus("current")
_S5ChasGrpEntry_Object = MibTableRow
s5ChasGrpEntry = _S5ChasGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1)
)
s5ChasGrpEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasGrpIndx"),
)
if mibBuilder.loadTexts:
    s5ChasGrpEntry.setStatus("current")


class _S5ChasGrpIndx_Type(Integer32):
    """Custom type s5ChasGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasGrpIndx_Type.__name__ = "Integer32"
_S5ChasGrpIndx_Object = MibTableColumn
s5ChasGrpIndx = _S5ChasGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 1),
    _S5ChasGrpIndx_Type()
)
s5ChasGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpIndx.setStatus("current")
_S5ChasGrpType_Type = ObjectIdentifier
_S5ChasGrpType_Object = MibTableColumn
s5ChasGrpType = _S5ChasGrpType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 2),
    _S5ChasGrpType_Type()
)
s5ChasGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpType.setStatus("current")


class _S5ChasGrpDescr_Type(DisplayString):
    """Custom type s5ChasGrpDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5ChasGrpDescr_Type.__name__ = "DisplayString"
_S5ChasGrpDescr_Object = MibTableColumn
s5ChasGrpDescr = _S5ChasGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 3),
    _S5ChasGrpDescr_Type()
)
s5ChasGrpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpDescr.setStatus("current")


class _S5ChasGrpMaxEnts_Type(Integer32):
    """Custom type s5ChasGrpMaxEnts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_S5ChasGrpMaxEnts_Type.__name__ = "Integer32"
_S5ChasGrpMaxEnts_Object = MibTableColumn
s5ChasGrpMaxEnts = _S5ChasGrpMaxEnts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 4),
    _S5ChasGrpMaxEnts_Type()
)
s5ChasGrpMaxEnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpMaxEnts.setStatus("current")


class _S5ChasGrpNumEnts_Type(Integer32):
    """Custom type s5ChasGrpNumEnts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_S5ChasGrpNumEnts_Type.__name__ = "Integer32"
_S5ChasGrpNumEnts_Object = MibTableColumn
s5ChasGrpNumEnts = _S5ChasGrpNumEnts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 5),
    _S5ChasGrpNumEnts_Type()
)
s5ChasGrpNumEnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpNumEnts.setStatus("current")
_S5ChasGrpPhysChngs_Type = Counter32
_S5ChasGrpPhysChngs_Object = MibTableColumn
s5ChasGrpPhysChngs = _S5ChasGrpPhysChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 6),
    _S5ChasGrpPhysChngs_Type()
)
s5ChasGrpPhysChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpPhysChngs.setStatus("current")
_S5ChasGrpPhysLstChng_Type = TimeTicks
_S5ChasGrpPhysLstChng_Object = MibTableColumn
s5ChasGrpPhysLstChng = _S5ChasGrpPhysLstChng_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 7),
    _S5ChasGrpPhysLstChng_Type()
)
s5ChasGrpPhysLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpPhysLstChng.setStatus("current")
_S5ChasGrpEncodeFactor_Type = Integer32
_S5ChasGrpEncodeFactor_Object = MibTableColumn
s5ChasGrpEncodeFactor = _S5ChasGrpEncodeFactor_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 8),
    _S5ChasGrpEncodeFactor_Type()
)
s5ChasGrpEncodeFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGrpEncodeFactor.setStatus("current")
_S5ChasCom_ObjectIdentity = ObjectIdentity
s5ChasCom = _S5ChasCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3)
)
_S5ChasComTable_Object = MibTable
s5ChasComTable = _S5ChasComTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    s5ChasComTable.setStatus("current")
_S5ChasComEntry_Object = MibTableRow
s5ChasComEntry = _S5ChasComEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1)
)
s5ChasComEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasComGrpIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasComIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasComSubIndx"),
)
if mibBuilder.loadTexts:
    s5ChasComEntry.setStatus("current")


class _S5ChasComGrpIndx_Type(Integer32):
    """Custom type s5ChasComGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasComGrpIndx_Type.__name__ = "Integer32"
_S5ChasComGrpIndx_Object = MibTableColumn
s5ChasComGrpIndx = _S5ChasComGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 1),
    _S5ChasComGrpIndx_Type()
)
s5ChasComGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComGrpIndx.setStatus("current")


class _S5ChasComIndx_Type(Integer32):
    """Custom type s5ChasComIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasComIndx_Type.__name__ = "Integer32"
_S5ChasComIndx_Object = MibTableColumn
s5ChasComIndx = _S5ChasComIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 2),
    _S5ChasComIndx_Type()
)
s5ChasComIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComIndx.setStatus("current")


class _S5ChasComSubIndx_Type(Integer32):
    """Custom type s5ChasComSubIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasComSubIndx_Type.__name__ = "Integer32"
_S5ChasComSubIndx_Object = MibTableColumn
s5ChasComSubIndx = _S5ChasComSubIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 3),
    _S5ChasComSubIndx_Type()
)
s5ChasComSubIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComSubIndx.setStatus("current")
_S5ChasComType_Type = ObjectIdentifier
_S5ChasComType_Object = MibTableColumn
s5ChasComType = _S5ChasComType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 4),
    _S5ChasComType_Type()
)
s5ChasComType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComType.setStatus("current")


class _S5ChasComDescr_Type(DisplayString):
    """Custom type s5ChasComDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5ChasComDescr_Type.__name__ = "DisplayString"
_S5ChasComDescr_Object = MibTableColumn
s5ChasComDescr = _S5ChasComDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 5),
    _S5ChasComDescr_Type()
)
s5ChasComDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComDescr.setStatus("current")


class _S5ChasComVer_Type(DisplayString):
    """Custom type s5ChasComVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5ChasComVer_Type.__name__ = "DisplayString"
_S5ChasComVer_Object = MibTableColumn
s5ChasComVer = _S5ChasComVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 6),
    _S5ChasComVer_Type()
)
s5ChasComVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComVer.setStatus("current")


class _S5ChasComSerNum_Type(DisplayString):
    """Custom type s5ChasComSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5ChasComSerNum_Type.__name__ = "DisplayString"
_S5ChasComSerNum_Object = MibTableColumn
s5ChasComSerNum = _S5ChasComSerNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 7),
    _S5ChasComSerNum_Type()
)
s5ChasComSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComSerNum.setStatus("current")
_S5ChasComLstChng_Type = TimeTicks
_S5ChasComLstChng_Object = MibTableColumn
s5ChasComLstChng = _S5ChasComLstChng_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 8),
    _S5ChasComLstChng_Type()
)
s5ChasComLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComLstChng.setStatus("current")


class _S5ChasComAdminState_Type(Integer32):
    """Custom type s5ChasComAdminState based on Integer32"""
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
        *(("disable", 3),
          ("enable", 4),
          ("notAvail", 2),
          ("other", 1),
          ("reset", 5),
          ("test", 6))
    )


_S5ChasComAdminState_Type.__name__ = "Integer32"
_S5ChasComAdminState_Object = MibTableColumn
s5ChasComAdminState = _S5ChasComAdminState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 9),
    _S5ChasComAdminState_Type()
)
s5ChasComAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComAdminState.setStatus("current")


class _S5ChasComOperState_Type(Integer32):
    """Custom type s5ChasComOperState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("fatalErr", 10),
          ("nonFatalErr", 9),
          ("normal", 5),
          ("notAvail", 2),
          ("notConfig", 11),
          ("obsoleted", 12),
          ("other", 1),
          ("removed", 3),
          ("resetInProg", 6),
          ("testing", 7),
          ("warning", 8))
    )


_S5ChasComOperState_Type.__name__ = "Integer32"
_S5ChasComOperState_Object = MibTableColumn
s5ChasComOperState = _S5ChasComOperState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 10),
    _S5ChasComOperState_Type()
)
s5ChasComOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComOperState.setStatus("current")


class _S5ChasComMaxSubs_Type(Integer32):
    """Custom type s5ChasComMaxSubs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_S5ChasComMaxSubs_Type.__name__ = "Integer32"
_S5ChasComMaxSubs_Object = MibTableColumn
s5ChasComMaxSubs = _S5ChasComMaxSubs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 11),
    _S5ChasComMaxSubs_Type()
)
s5ChasComMaxSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComMaxSubs.setStatus("current")


class _S5ChasComNumSubs_Type(Integer32):
    """Custom type s5ChasComNumSubs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_S5ChasComNumSubs_Type.__name__ = "Integer32"
_S5ChasComNumSubs_Object = MibTableColumn
s5ChasComNumSubs = _S5ChasComNumSubs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 12),
    _S5ChasComNumSubs_Type()
)
s5ChasComNumSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComNumSubs.setStatus("current")


class _S5ChasComRelPos_Type(Integer32):
    """Custom type s5ChasComRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasComRelPos_Type.__name__ = "Integer32"
_S5ChasComRelPos_Object = MibTableColumn
s5ChasComRelPos = _S5ChasComRelPos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 13),
    _S5ChasComRelPos_Type()
)
s5ChasComRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComRelPos.setStatus("current")


class _S5ChasComLocation_Type(DisplayString):
    """Custom type s5ChasComLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5ChasComLocation_Type.__name__ = "DisplayString"
_S5ChasComLocation_Object = MibTableColumn
s5ChasComLocation = _S5ChasComLocation_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 14),
    _S5ChasComLocation_Type()
)
s5ChasComLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComLocation.setStatus("current")


class _S5ChasComGroupMap_Type(Integer32):
    """Custom type s5ChasComGroupMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasComGroupMap_Type.__name__ = "Integer32"
_S5ChasComGroupMap_Object = MibTableColumn
s5ChasComGroupMap = _S5ChasComGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 15),
    _S5ChasComGroupMap_Type()
)
s5ChasComGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComGroupMap.setStatus("current")


class _S5ChasComBaseNumPorts_Type(Integer32):
    """Custom type s5ChasComBaseNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasComBaseNumPorts_Type.__name__ = "Integer32"
_S5ChasComBaseNumPorts_Object = MibTableColumn
s5ChasComBaseNumPorts = _S5ChasComBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 16),
    _S5ChasComBaseNumPorts_Type()
)
s5ChasComBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComBaseNumPorts.setStatus("current")


class _S5ChasComTotalNumPorts_Type(Integer32):
    """Custom type s5ChasComTotalNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasComTotalNumPorts_Type.__name__ = "Integer32"
_S5ChasComTotalNumPorts_Object = MibTableColumn
s5ChasComTotalNumPorts = _S5ChasComTotalNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 17),
    _S5ChasComTotalNumPorts_Type()
)
s5ChasComTotalNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComTotalNumPorts.setStatus("current")
_S5ChasComIpAddress_Type = IpAddress
_S5ChasComIpAddress_Object = MibTableColumn
s5ChasComIpAddress = _S5ChasComIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 18),
    _S5ChasComIpAddress_Type()
)
s5ChasComIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpAddress.setStatus("current")


class _S5ChasComRunningSoftwareVer_Type(DisplayString):
    """Custom type s5ChasComRunningSoftwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5ChasComRunningSoftwareVer_Type.__name__ = "DisplayString"
_S5ChasComRunningSoftwareVer_Object = MibTableColumn
s5ChasComRunningSoftwareVer = _S5ChasComRunningSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 19),
    _S5ChasComRunningSoftwareVer_Type()
)
s5ChasComRunningSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComRunningSoftwareVer.setStatus("current")
_S5ChasComIpv6Address_Type = Ipv6Address
_S5ChasComIpv6Address_Object = MibTableColumn
s5ChasComIpv6Address = _S5ChasComIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 20),
    _S5ChasComIpv6Address_Type()
)
s5ChasComIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpv6Address.setStatus("current")
_S5ChasComIpv6NetMask_Type = Ipv6AddressPrefix
_S5ChasComIpv6NetMask_Object = MibTableColumn
s5ChasComIpv6NetMask = _S5ChasComIpv6NetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 21),
    _S5ChasComIpv6NetMask_Type()
)
s5ChasComIpv6NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpv6NetMask.setStatus("current")
_S5ChasComIpMgmtAddress_Type = IpAddress
_S5ChasComIpMgmtAddress_Object = MibTableColumn
s5ChasComIpMgmtAddress = _S5ChasComIpMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 22),
    _S5ChasComIpMgmtAddress_Type()
)
s5ChasComIpMgmtAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtAddress.setStatus("current")
_S5ChasComIpMgmtNetMask_Type = IpAddress
_S5ChasComIpMgmtNetMask_Object = MibTableColumn
s5ChasComIpMgmtNetMask = _S5ChasComIpMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 23),
    _S5ChasComIpMgmtNetMask_Type()
)
s5ChasComIpMgmtNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtNetMask.setStatus("current")
_S5ChasComIpMgmtGateway_Type = IpAddress
_S5ChasComIpMgmtGateway_Object = MibTableColumn
s5ChasComIpMgmtGateway = _S5ChasComIpMgmtGateway_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 24),
    _S5ChasComIpMgmtGateway_Type()
)
s5ChasComIpMgmtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtGateway.setStatus("current")
_S5ChasComIpv6MgmtAddress_Type = Ipv6Address
_S5ChasComIpv6MgmtAddress_Object = MibTableColumn
s5ChasComIpv6MgmtAddress = _S5ChasComIpv6MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 25),
    _S5ChasComIpv6MgmtAddress_Type()
)
s5ChasComIpv6MgmtAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpv6MgmtAddress.setStatus("current")
_S5ChasComIpv6MgmtNetMask_Type = Ipv6AddressPrefix
_S5ChasComIpv6MgmtNetMask_Object = MibTableColumn
s5ChasComIpv6MgmtNetMask = _S5ChasComIpv6MgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 26),
    _S5ChasComIpv6MgmtNetMask_Type()
)
s5ChasComIpv6MgmtNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpv6MgmtNetMask.setStatus("current")


class _S5ChasComIpMgmtLimit_Type(Integer32):
    """Custom type s5ChasComIpMgmtLimit based on Integer32"""
    defaultValue = 7000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_S5ChasComIpMgmtLimit_Type.__name__ = "Integer32"
_S5ChasComIpMgmtLimit_Object = MibTableColumn
s5ChasComIpMgmtLimit = _S5ChasComIpMgmtLimit_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 27),
    _S5ChasComIpMgmtLimit_Type()
)
s5ChasComIpMgmtLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtLimit.setStatus("current")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtLimit.setUnits("packets per second")


class _S5ChasComIpMgmtTimeout_Type(Integer32):
    """Custom type s5ChasComIpMgmtTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_S5ChasComIpMgmtTimeout_Type.__name__ = "Integer32"
_S5ChasComIpMgmtTimeout_Object = MibTableColumn
s5ChasComIpMgmtTimeout = _S5ChasComIpMgmtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 28),
    _S5ChasComIpMgmtTimeout_Type()
)
s5ChasComIpMgmtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtTimeout.setStatus("current")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtTimeout.setUnits("seconds")


class _S5ChasComIpMgmtShutdown_Type(TruthValue):
    """Custom type s5ChasComIpMgmtShutdown based on TruthValue"""


_S5ChasComIpMgmtShutdown_Object = MibTableColumn
s5ChasComIpMgmtShutdown = _S5ChasComIpMgmtShutdown_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 29),
    _S5ChasComIpMgmtShutdown_Type()
)
s5ChasComIpMgmtShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasComIpMgmtShutdown.setStatus("current")
_S5ChasComUpTime_Type = TimeTicks
_S5ChasComUpTime_Object = MibTableColumn
s5ChasComUpTime = _S5ChasComUpTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 30),
    _S5ChasComUpTime_Type()
)
s5ChasComUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasComUpTime.setStatus("current")
_S5ChasBrd_ObjectIdentity = ObjectIdentity
s5ChasBrd = _S5ChasBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4)
)
_S5ChasBrdTable_Object = MibTable
s5ChasBrdTable = _S5ChasBrdTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1)
)
if mibBuilder.loadTexts:
    s5ChasBrdTable.setStatus("current")
_S5ChasBrdEntry_Object = MibTableRow
s5ChasBrdEntry = _S5ChasBrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1)
)
s5ChasBrdEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasBrdIndx"),
)
if mibBuilder.loadTexts:
    s5ChasBrdEntry.setStatus("current")


class _S5ChasBrdIndx_Type(Integer32):
    """Custom type s5ChasBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5ChasBrdIndx_Type.__name__ = "Integer32"
_S5ChasBrdIndx_Object = MibTableColumn
s5ChasBrdIndx = _S5ChasBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 1),
    _S5ChasBrdIndx_Type()
)
s5ChasBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdIndx.setStatus("current")
_S5ChasBrdLeds_Type = OctetString
_S5ChasBrdLeds_Object = MibTableColumn
s5ChasBrdLeds = _S5ChasBrdLeds_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 2),
    _S5ChasBrdLeds_Type()
)
s5ChasBrdLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdLeds.setStatus("current")


class _S5ChasBrdNumAtt_Type(Integer32):
    """Custom type s5ChasBrdNumAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5ChasBrdNumAtt_Type.__name__ = "Integer32"
_S5ChasBrdNumAtt_Object = MibTableColumn
s5ChasBrdNumAtt = _S5ChasBrdNumAtt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 3),
    _S5ChasBrdNumAtt_Type()
)
s5ChasBrdNumAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdNumAtt.setStatus("current")
_S5ChasBrdAttChngs_Type = Counter32
_S5ChasBrdAttChngs_Object = MibTableColumn
s5ChasBrdAttChngs = _S5ChasBrdAttChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 4),
    _S5ChasBrdAttChngs_Type()
)
s5ChasBrdAttChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdAttChngs.setStatus("current")
_S5ChasBrdAttLstChng_Type = TimeTicks
_S5ChasBrdAttLstChng_Object = MibTableColumn
s5ChasBrdAttLstChng = _S5ChasBrdAttLstChng_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 5),
    _S5ChasBrdAttLstChng_Type()
)
s5ChasBrdAttLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdAttLstChng.setStatus("current")


class _S5ChasBrdStatusDsply_Type(DisplayString):
    """Custom type s5ChasBrdStatusDsply based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_S5ChasBrdStatusDsply_Type.__name__ = "DisplayString"
_S5ChasBrdStatusDsply_Object = MibTableColumn
s5ChasBrdStatusDsply = _S5ChasBrdStatusDsply_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 6),
    _S5ChasBrdStatusDsply_Type()
)
s5ChasBrdStatusDsply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdStatusDsply.setStatus("current")


class _S5ChasBrdDateCode_Type(DisplayString):
    """Custom type s5ChasBrdDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_S5ChasBrdDateCode_Type.__name__ = "DisplayString"
_S5ChasBrdDateCode_Object = MibTableColumn
s5ChasBrdDateCode = _S5ChasBrdDateCode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 7),
    _S5ChasBrdDateCode_Type()
)
s5ChasBrdDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdDateCode.setStatus("current")


class _S5ChasBrdCfgSrc_Type(Integer32):
    """Custom type s5ChasBrdCfgSrc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("brdCfg", 4),
          ("dfltJmpr", 2),
          ("other", 1),
          ("prmMem", 3),
          ("sm", 5),
          ("smBrdCfg", 8),
          ("smDfltJmpr", 6),
          ("smPrmMem", 7))
    )


_S5ChasBrdCfgSrc_Type.__name__ = "Integer32"
_S5ChasBrdCfgSrc_Object = MibTableColumn
s5ChasBrdCfgSrc = _S5ChasBrdCfgSrc_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 8),
    _S5ChasBrdCfgSrc_Type()
)
s5ChasBrdCfgSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdCfgSrc.setStatus("current")
_S5ChasBrdCfgChngs_Type = Counter32
_S5ChasBrdCfgChngs_Object = MibTableColumn
s5ChasBrdCfgChngs = _S5ChasBrdCfgChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 9),
    _S5ChasBrdCfgChngs_Type()
)
s5ChasBrdCfgChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdCfgChngs.setStatus("current")
_S5ChasBrdFanLeds_Type = OctetString
_S5ChasBrdFanLeds_Object = MibTableColumn
s5ChasBrdFanLeds = _S5ChasBrdFanLeds_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 10),
    _S5ChasBrdFanLeds_Type()
)
s5ChasBrdFanLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasBrdFanLeds.setStatus("current")
_S5ChasAttTable_Object = MibTable
s5ChasAttTable = _S5ChasAttTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2)
)
if mibBuilder.loadTexts:
    s5ChasAttTable.setStatus("current")
_S5ChasAttEntry_Object = MibTableRow
s5ChasAttEntry = _S5ChasAttEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1)
)
s5ChasAttEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasAttBrdIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasAttIndx"),
)
if mibBuilder.loadTexts:
    s5ChasAttEntry.setStatus("current")


class _S5ChasAttBrdIndx_Type(Integer32):
    """Custom type s5ChasAttBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5ChasAttBrdIndx_Type.__name__ = "Integer32"
_S5ChasAttBrdIndx_Object = MibTableColumn
s5ChasAttBrdIndx = _S5ChasAttBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 1),
    _S5ChasAttBrdIndx_Type()
)
s5ChasAttBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasAttBrdIndx.setStatus("current")


class _S5ChasAttIndx_Type(Integer32):
    """Custom type s5ChasAttIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5ChasAttIndx_Type.__name__ = "Integer32"
_S5ChasAttIndx_Object = MibTableColumn
s5ChasAttIndx = _S5ChasAttIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 2),
    _S5ChasAttIndx_Type()
)
s5ChasAttIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasAttIndx.setStatus("current")
_S5ChasAttDfltAtt_Type = AttId
_S5ChasAttDfltAtt_Object = MibTableColumn
s5ChasAttDfltAtt = _S5ChasAttDfltAtt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 3),
    _S5ChasAttDfltAtt_Type()
)
s5ChasAttDfltAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasAttDfltAtt.setStatus("current")
_S5ChasAttCurAtt_Type = AttId
_S5ChasAttCurAtt_Object = MibTableColumn
s5ChasAttCurAtt = _S5ChasAttCurAtt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 4),
    _S5ChasAttCurAtt_Type()
)
s5ChasAttCurAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasAttCurAtt.setStatus("current")
_S5ChasAttChngs_Type = Counter32
_S5ChasAttChngs_Object = MibTableColumn
s5ChasAttChngs = _S5ChasAttChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 5),
    _S5ChasAttChngs_Type()
)
s5ChasAttChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasAttChngs.setStatus("current")
_S5ChasAttLstChng_Type = TimeTicks
_S5ChasAttLstChng_Object = MibTableColumn
s5ChasAttLstChng = _S5ChasAttLstChng_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 6),
    _S5ChasAttLstChng_Type()
)
s5ChasAttLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasAttLstChng.setStatus("current")


class _S5ChasAttClusterConnCapability_Type(OctetString):
    """Custom type s5ChasAttClusterConnCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_S5ChasAttClusterConnCapability_Type.__name__ = "OctetString"
_S5ChasAttClusterConnCapability_Object = MibTableColumn
s5ChasAttClusterConnCapability = _S5ChasAttClusterConnCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 7),
    _S5ChasAttClusterConnCapability_Type()
)
s5ChasAttClusterConnCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasAttClusterConnCapability.setStatus("current")
_S5ChasLocChanTable_Object = MibTable
s5ChasLocChanTable = _S5ChasLocChanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3)
)
if mibBuilder.loadTexts:
    s5ChasLocChanTable.setStatus("current")
_S5ChasLocChanEntry_Object = MibTableRow
s5ChasLocChanEntry = _S5ChasLocChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1)
)
s5ChasLocChanEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasLocChanBrdIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasLocChanIndx"),
)
if mibBuilder.loadTexts:
    s5ChasLocChanEntry.setStatus("current")


class _S5ChasLocChanBrdIndx_Type(Integer32):
    """Custom type s5ChasLocChanBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5ChasLocChanBrdIndx_Type.__name__ = "Integer32"
_S5ChasLocChanBrdIndx_Object = MibTableColumn
s5ChasLocChanBrdIndx = _S5ChasLocChanBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1, 1),
    _S5ChasLocChanBrdIndx_Type()
)
s5ChasLocChanBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasLocChanBrdIndx.setStatus("current")
_S5ChasLocChanIndx_Type = LocChan
_S5ChasLocChanIndx_Object = MibTableColumn
s5ChasLocChanIndx = _S5ChasLocChanIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1, 2),
    _S5ChasLocChanIndx_Type()
)
s5ChasLocChanIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasLocChanIndx.setStatus("current")


class _S5ChasLocChanBkplMode_Type(Integer32):
    """Custom type s5ChasLocChanBkplMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("notConnected", 3),
          ("other", 1))
    )


_S5ChasLocChanBkplMode_Type.__name__ = "Integer32"
_S5ChasLocChanBkplMode_Object = MibTableColumn
s5ChasLocChanBkplMode = _S5ChasLocChanBkplMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1, 3),
    _S5ChasLocChanBkplMode_Type()
)
s5ChasLocChanBkplMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasLocChanBkplMode.setStatus("current")
_S5ChasStore_ObjectIdentity = ObjectIdentity
s5ChasStore = _S5ChasStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5)
)
_S5ChasStoreTable_Object = MibTable
s5ChasStoreTable = _S5ChasStoreTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1)
)
if mibBuilder.loadTexts:
    s5ChasStoreTable.setStatus("current")
_S5ChasStoreEntry_Object = MibTableRow
s5ChasStoreEntry = _S5ChasStoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1)
)
s5ChasStoreEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasStoreGrpIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasStoreComIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasStoreSubIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasStoreIndx"),
)
if mibBuilder.loadTexts:
    s5ChasStoreEntry.setStatus("current")


class _S5ChasStoreGrpIndx_Type(Integer32):
    """Custom type s5ChasStoreGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasStoreGrpIndx_Type.__name__ = "Integer32"
_S5ChasStoreGrpIndx_Object = MibTableColumn
s5ChasStoreGrpIndx = _S5ChasStoreGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 1),
    _S5ChasStoreGrpIndx_Type()
)
s5ChasStoreGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreGrpIndx.setStatus("current")


class _S5ChasStoreComIndx_Type(Integer32):
    """Custom type s5ChasStoreComIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasStoreComIndx_Type.__name__ = "Integer32"
_S5ChasStoreComIndx_Object = MibTableColumn
s5ChasStoreComIndx = _S5ChasStoreComIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 2),
    _S5ChasStoreComIndx_Type()
)
s5ChasStoreComIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreComIndx.setStatus("current")


class _S5ChasStoreSubIndx_Type(Integer32):
    """Custom type s5ChasStoreSubIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasStoreSubIndx_Type.__name__ = "Integer32"
_S5ChasStoreSubIndx_Object = MibTableColumn
s5ChasStoreSubIndx = _S5ChasStoreSubIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 3),
    _S5ChasStoreSubIndx_Type()
)
s5ChasStoreSubIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreSubIndx.setStatus("current")


class _S5ChasStoreIndx_Type(Integer32):
    """Custom type s5ChasStoreIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5ChasStoreIndx_Type.__name__ = "Integer32"
_S5ChasStoreIndx_Object = MibTableColumn
s5ChasStoreIndx = _S5ChasStoreIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 4),
    _S5ChasStoreIndx_Type()
)
s5ChasStoreIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreIndx.setStatus("current")
_S5ChasStoreType_Type = ObjectIdentifier
_S5ChasStoreType_Object = MibTableColumn
s5ChasStoreType = _S5ChasStoreType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 5),
    _S5ChasStoreType_Type()
)
s5ChasStoreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreType.setStatus("current")


class _S5ChasStoreCurSize_Type(Integer32):
    """Custom type s5ChasStoreCurSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_S5ChasStoreCurSize_Type.__name__ = "Integer32"
_S5ChasStoreCurSize_Object = MibTableColumn
s5ChasStoreCurSize = _S5ChasStoreCurSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 6),
    _S5ChasStoreCurSize_Type()
)
s5ChasStoreCurSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreCurSize.setStatus("current")


class _S5ChasStoreCntntVer_Type(DisplayString):
    """Custom type s5ChasStoreCntntVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_S5ChasStoreCntntVer_Type.__name__ = "DisplayString"
_S5ChasStoreCntntVer_Object = MibTableColumn
s5ChasStoreCntntVer = _S5ChasStoreCntntVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 7),
    _S5ChasStoreCntntVer_Type()
)
s5ChasStoreCntntVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreCntntVer.setStatus("current")


class _S5ChasStoreFilename_Type(DisplayString):
    """Custom type s5ChasStoreFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5ChasStoreFilename_Type.__name__ = "DisplayString"
_S5ChasStoreFilename_Object = MibTableColumn
s5ChasStoreFilename = _S5ChasStoreFilename_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 8),
    _S5ChasStoreFilename_Type()
)
s5ChasStoreFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasStoreFilename.setStatus("current")


class _S5ChasStoreUsedSize_Type(Integer32):
    """Custom type s5ChasStoreUsedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_S5ChasStoreUsedSize_Type.__name__ = "Integer32"
_S5ChasStoreUsedSize_Object = MibTableColumn
s5ChasStoreUsedSize = _S5ChasStoreUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 9),
    _S5ChasStoreUsedSize_Type()
)
s5ChasStoreUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreUsedSize.setStatus("current")


class _S5ChasStoreDescription_Type(DisplayString):
    """Custom type s5ChasStoreDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5ChasStoreDescription_Type.__name__ = "DisplayString"
_S5ChasStoreDescription_Object = MibTableColumn
s5ChasStoreDescription = _S5ChasStoreDescription_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 10),
    _S5ChasStoreDescription_Type()
)
s5ChasStoreDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreDescription.setStatus("current")


class _S5ChasStoreAge_Type(Integer32):
    """Custom type s5ChasStoreAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_S5ChasStoreAge_Type.__name__ = "Integer32"
_S5ChasStoreAge_Object = MibTableColumn
s5ChasStoreAge = _S5ChasStoreAge_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 11),
    _S5ChasStoreAge_Type()
)
s5ChasStoreAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasStoreAge.setStatus("current")
_S5ChasSm_ObjectIdentity = ObjectIdentity
s5ChasSm = _S5ChasSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 6)
)
_S5ChasSmLeds_Type = OctetString
_S5ChasSmLeds_Object = MibScalar
s5ChasSmLeds = _S5ChasSmLeds_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 6, 1),
    _S5ChasSmLeds_Type()
)
s5ChasSmLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasSmLeds.setStatus("current")


class _S5ChasSmDateCode_Type(DisplayString):
    """Custom type s5ChasSmDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_S5ChasSmDateCode_Type.__name__ = "DisplayString"
_S5ChasSmDateCode_Object = MibScalar
s5ChasSmDateCode = _S5ChasSmDateCode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 6, 2),
    _S5ChasSmDateCode_Type()
)
s5ChasSmDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasSmDateCode.setStatus("current")
_S5ChasTmpSnr_ObjectIdentity = ObjectIdentity
s5ChasTmpSnr = _S5ChasTmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7)
)
_S5ChasTmpSnrTable_Object = MibTable
s5ChasTmpSnrTable = _S5ChasTmpSnrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1)
)
if mibBuilder.loadTexts:
    s5ChasTmpSnrTable.setStatus("current")
_S5ChasTmpSnrEntry_Object = MibTableRow
s5ChasTmpSnrEntry = _S5ChasTmpSnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1)
)
s5ChasTmpSnrEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasTmpSnrGrpIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasTmpSnrIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasTmpSnrSubIndx"),
)
if mibBuilder.loadTexts:
    s5ChasTmpSnrEntry.setStatus("current")


class _S5ChasTmpSnrGrpIndx_Type(Integer32):
    """Custom type s5ChasTmpSnrGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasTmpSnrGrpIndx_Type.__name__ = "Integer32"
_S5ChasTmpSnrGrpIndx_Object = MibTableColumn
s5ChasTmpSnrGrpIndx = _S5ChasTmpSnrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 1),
    _S5ChasTmpSnrGrpIndx_Type()
)
s5ChasTmpSnrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasTmpSnrGrpIndx.setStatus("current")


class _S5ChasTmpSnrIndx_Type(Integer32):
    """Custom type s5ChasTmpSnrIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasTmpSnrIndx_Type.__name__ = "Integer32"
_S5ChasTmpSnrIndx_Object = MibTableColumn
s5ChasTmpSnrIndx = _S5ChasTmpSnrIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 2),
    _S5ChasTmpSnrIndx_Type()
)
s5ChasTmpSnrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasTmpSnrIndx.setStatus("current")


class _S5ChasTmpSnrSubIndx_Type(Integer32):
    """Custom type s5ChasTmpSnrSubIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasTmpSnrSubIndx_Type.__name__ = "Integer32"
_S5ChasTmpSnrSubIndx_Object = MibTableColumn
s5ChasTmpSnrSubIndx = _S5ChasTmpSnrSubIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 3),
    _S5ChasTmpSnrSubIndx_Type()
)
s5ChasTmpSnrSubIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasTmpSnrSubIndx.setStatus("current")
_S5ChasTmpSnrValue_Type = Gauge32
_S5ChasTmpSnrValue_Object = MibTableColumn
s5ChasTmpSnrValue = _S5ChasTmpSnrValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 4),
    _S5ChasTmpSnrValue_Type()
)
s5ChasTmpSnrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasTmpSnrValue.setStatus("deprecated")


class _S5ChasTmpSnrTmpValue_Type(Integer32):
    """Custom type s5ChasTmpSnrTmpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_S5ChasTmpSnrTmpValue_Type.__name__ = "Integer32"
_S5ChasTmpSnrTmpValue_Object = MibTableColumn
s5ChasTmpSnrTmpValue = _S5ChasTmpSnrTmpValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 5),
    _S5ChasTmpSnrTmpValue_Type()
)
s5ChasTmpSnrTmpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasTmpSnrTmpValue.setStatus("current")
_S5ChasUtil_ObjectIdentity = ObjectIdentity
s5ChasUtil = _S5ChasUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8)
)
_S5ChasUtilTable_Object = MibTable
s5ChasUtilTable = _S5ChasUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1)
)
if mibBuilder.loadTexts:
    s5ChasUtilTable.setStatus("current")
_S5ChasUtilEntry_Object = MibTableRow
s5ChasUtilEntry = _S5ChasUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1)
)
s5ChasUtilEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasUtilGrpIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasUtilIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasUtilSubIndx"),
)
if mibBuilder.loadTexts:
    s5ChasUtilEntry.setStatus("current")


class _S5ChasUtilGrpIndx_Type(Integer32):
    """Custom type s5ChasUtilGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasUtilGrpIndx_Type.__name__ = "Integer32"
_S5ChasUtilGrpIndx_Object = MibTableColumn
s5ChasUtilGrpIndx = _S5ChasUtilGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 1),
    _S5ChasUtilGrpIndx_Type()
)
s5ChasUtilGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilGrpIndx.setStatus("current")


class _S5ChasUtilIndx_Type(Integer32):
    """Custom type s5ChasUtilIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasUtilIndx_Type.__name__ = "Integer32"
_S5ChasUtilIndx_Object = MibTableColumn
s5ChasUtilIndx = _S5ChasUtilIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 2),
    _S5ChasUtilIndx_Type()
)
s5ChasUtilIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilIndx.setStatus("current")


class _S5ChasUtilSubIndx_Type(Integer32):
    """Custom type s5ChasUtilSubIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasUtilSubIndx_Type.__name__ = "Integer32"
_S5ChasUtilSubIndx_Object = MibTableColumn
s5ChasUtilSubIndx = _S5ChasUtilSubIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 3),
    _S5ChasUtilSubIndx_Type()
)
s5ChasUtilSubIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilSubIndx.setStatus("current")


class _S5ChasUtilTotalCPUUsage_Type(Gauge32):
    """Custom type s5ChasUtilTotalCPUUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilTotalCPUUsage_Type.__name__ = "Gauge32"
_S5ChasUtilTotalCPUUsage_Object = MibTableColumn
s5ChasUtilTotalCPUUsage = _S5ChasUtilTotalCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 4),
    _S5ChasUtilTotalCPUUsage_Type()
)
s5ChasUtilTotalCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilTotalCPUUsage.setStatus("current")


class _S5ChasUtilCPUUsageLast1Minute_Type(Gauge32):
    """Custom type s5ChasUtilCPUUsageLast1Minute based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilCPUUsageLast1Minute_Type.__name__ = "Gauge32"
_S5ChasUtilCPUUsageLast1Minute_Object = MibTableColumn
s5ChasUtilCPUUsageLast1Minute = _S5ChasUtilCPUUsageLast1Minute_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 5),
    _S5ChasUtilCPUUsageLast1Minute_Type()
)
s5ChasUtilCPUUsageLast1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilCPUUsageLast1Minute.setStatus("current")


class _S5ChasUtilCPUUsageLast10Minutes_Type(Gauge32):
    """Custom type s5ChasUtilCPUUsageLast10Minutes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilCPUUsageLast10Minutes_Type.__name__ = "Gauge32"
_S5ChasUtilCPUUsageLast10Minutes_Object = MibTableColumn
s5ChasUtilCPUUsageLast10Minutes = _S5ChasUtilCPUUsageLast10Minutes_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 6),
    _S5ChasUtilCPUUsageLast10Minutes_Type()
)
s5ChasUtilCPUUsageLast10Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilCPUUsageLast10Minutes.setStatus("current")


class _S5ChasUtilCPUUsageLast1Hour_Type(Gauge32):
    """Custom type s5ChasUtilCPUUsageLast1Hour based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilCPUUsageLast1Hour_Type.__name__ = "Gauge32"
_S5ChasUtilCPUUsageLast1Hour_Object = MibTableColumn
s5ChasUtilCPUUsageLast1Hour = _S5ChasUtilCPUUsageLast1Hour_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 7),
    _S5ChasUtilCPUUsageLast1Hour_Type()
)
s5ChasUtilCPUUsageLast1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilCPUUsageLast1Hour.setStatus("current")


class _S5ChasUtilCPUUsageLast24Hours_Type(Gauge32):
    """Custom type s5ChasUtilCPUUsageLast24Hours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilCPUUsageLast24Hours_Type.__name__ = "Gauge32"
_S5ChasUtilCPUUsageLast24Hours_Object = MibTableColumn
s5ChasUtilCPUUsageLast24Hours = _S5ChasUtilCPUUsageLast24Hours_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 8),
    _S5ChasUtilCPUUsageLast24Hours_Type()
)
s5ChasUtilCPUUsageLast24Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilCPUUsageLast24Hours.setStatus("current")


class _S5ChasUtilMemoryAvailable_Type(Gauge32):
    """Custom type s5ChasUtilMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilMemoryAvailable_Type.__name__ = "Gauge32"
_S5ChasUtilMemoryAvailable_Object = MibTableColumn
s5ChasUtilMemoryAvailable = _S5ChasUtilMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 9),
    _S5ChasUtilMemoryAvailable_Type()
)
s5ChasUtilMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilMemoryAvailable.setStatus("current")


class _S5ChasUtilMemoryMinAvailable_Type(Gauge32):
    """Custom type s5ChasUtilMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilMemoryMinAvailable_Type.__name__ = "Gauge32"
_S5ChasUtilMemoryMinAvailable_Object = MibTableColumn
s5ChasUtilMemoryMinAvailable = _S5ChasUtilMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 10),
    _S5ChasUtilMemoryMinAvailable_Type()
)
s5ChasUtilMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilMemoryMinAvailable.setStatus("current")


class _S5ChasUtilCPUUsageLast10Seconds_Type(Gauge32):
    """Custom type s5ChasUtilCPUUsageLast10Seconds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5ChasUtilCPUUsageLast10Seconds_Type.__name__ = "Gauge32"
_S5ChasUtilCPUUsageLast10Seconds_Object = MibTableColumn
s5ChasUtilCPUUsageLast10Seconds = _S5ChasUtilCPUUsageLast10Seconds_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 11),
    _S5ChasUtilCPUUsageLast10Seconds_Type()
)
s5ChasUtilCPUUsageLast10Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilCPUUsageLast10Seconds.setStatus("current")


class _S5ChasUtilMemoryTotalMB_Type(Gauge32):
    """Custom type s5ChasUtilMemoryTotalMB based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_S5ChasUtilMemoryTotalMB_Type.__name__ = "Gauge32"
_S5ChasUtilMemoryTotalMB_Object = MibTableColumn
s5ChasUtilMemoryTotalMB = _S5ChasUtilMemoryTotalMB_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 12),
    _S5ChasUtilMemoryTotalMB_Type()
)
s5ChasUtilMemoryTotalMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilMemoryTotalMB.setStatus("current")
if mibBuilder.loadTexts:
    s5ChasUtilMemoryTotalMB.setUnits("MegaBytes")


class _S5ChasUtilMemoryAvailableMB_Type(Gauge32):
    """Custom type s5ChasUtilMemoryAvailableMB based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_S5ChasUtilMemoryAvailableMB_Type.__name__ = "Gauge32"
_S5ChasUtilMemoryAvailableMB_Object = MibTableColumn
s5ChasUtilMemoryAvailableMB = _S5ChasUtilMemoryAvailableMB_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 13),
    _S5ChasUtilMemoryAvailableMB_Type()
)
s5ChasUtilMemoryAvailableMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasUtilMemoryAvailableMB.setStatus("current")
if mibBuilder.loadTexts:
    s5ChasUtilMemoryAvailableMB.setUnits("MegaBytes")
_S5ChasPs_ObjectIdentity = ObjectIdentity
s5ChasPs = _S5ChasPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9)
)
_S5ChasPsRpsuTable_Object = MibTable
s5ChasPsRpsuTable = _S5ChasPsRpsuTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1)
)
if mibBuilder.loadTexts:
    s5ChasPsRpsuTable.setStatus("current")
_S5ChasPsRpsuEntry_Object = MibTableRow
s5ChasPsRpsuEntry = _S5ChasPsRpsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1)
)
s5ChasPsRpsuEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasPsRpsuGrpIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasPsRpsuIndx"),
    (0, "S5-CHASSIS-MIB", "s5ChasPsRpsuSubIndx"),
)
if mibBuilder.loadTexts:
    s5ChasPsRpsuEntry.setStatus("current")


class _S5ChasPsRpsuGrpIndx_Type(Integer32):
    """Custom type s5ChasPsRpsuGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasPsRpsuGrpIndx_Type.__name__ = "Integer32"
_S5ChasPsRpsuGrpIndx_Object = MibTableColumn
s5ChasPsRpsuGrpIndx = _S5ChasPsRpsuGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 1),
    _S5ChasPsRpsuGrpIndx_Type()
)
s5ChasPsRpsuGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasPsRpsuGrpIndx.setStatus("current")


class _S5ChasPsRpsuIndx_Type(Integer32):
    """Custom type s5ChasPsRpsuIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5ChasPsRpsuIndx_Type.__name__ = "Integer32"
_S5ChasPsRpsuIndx_Object = MibTableColumn
s5ChasPsRpsuIndx = _S5ChasPsRpsuIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 2),
    _S5ChasPsRpsuIndx_Type()
)
s5ChasPsRpsuIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasPsRpsuIndx.setStatus("current")


class _S5ChasPsRpsuSubIndx_Type(Integer32):
    """Custom type s5ChasPsRpsuSubIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_S5ChasPsRpsuSubIndx_Type.__name__ = "Integer32"
_S5ChasPsRpsuSubIndx_Object = MibTableColumn
s5ChasPsRpsuSubIndx = _S5ChasPsRpsuSubIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 3),
    _S5ChasPsRpsuSubIndx_Type()
)
s5ChasPsRpsuSubIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasPsRpsuSubIndx.setStatus("current")


class _S5ChasPsRpsuType_Type(Integer32):
    """Custom type s5ChasPsRpsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bayStack10", 1),
          ("bayStack15", 3),
          ("nes", 2))
    )


_S5ChasPsRpsuType_Type.__name__ = "Integer32"
_S5ChasPsRpsuType_Object = MibTableColumn
s5ChasPsRpsuType = _S5ChasPsRpsuType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 4),
    _S5ChasPsRpsuType_Type()
)
s5ChasPsRpsuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasPsRpsuType.setStatus("current")


class _S5ChasPsRpsuSourceConfig_Type(Integer32):
    """Custom type s5ChasPsRpsuSourceConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powerSharing", 3),
          ("rpsu", 2),
          ("ups", 1))
    )


_S5ChasPsRpsuSourceConfig_Type.__name__ = "Integer32"
_S5ChasPsRpsuSourceConfig_Object = MibTableColumn
s5ChasPsRpsuSourceConfig = _S5ChasPsRpsuSourceConfig_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 5),
    _S5ChasPsRpsuSourceConfig_Type()
)
s5ChasPsRpsuSourceConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5ChasPsRpsuSourceConfig.setStatus("current")
_S5ChasNotify_ObjectIdentity = ObjectIdentity
s5ChasNotify = _S5ChasNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 11)
)


class _S5ChasNotifyFanDirection_Type(Integer32):
    """Custom type s5ChasNotifyFanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("right", 2))
    )


_S5ChasNotifyFanDirection_Type.__name__ = "Integer32"
_S5ChasNotifyFanDirection_Object = MibScalar
s5ChasNotifyFanDirection = _S5ChasNotifyFanDirection_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 11, 1),
    _S5ChasNotifyFanDirection_Type()
)
s5ChasNotifyFanDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    s5ChasNotifyFanDirection.setStatus("current")
_S5ChasPluggables_ObjectIdentity = ObjectIdentity
s5ChasPluggables = _S5ChasPluggables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12)
)
_S5ChasGbicInfoTable_Object = MibTable
s5ChasGbicInfoTable = _S5ChasGbicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1)
)
if mibBuilder.loadTexts:
    s5ChasGbicInfoTable.setStatus("current")
_S5ChasGbicInfoEntry_Object = MibTableRow
s5ChasGbicInfoEntry = _S5ChasGbicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1)
)
s5ChasGbicInfoEntry.setIndexNames(
    (0, "S5-CHASSIS-MIB", "s5ChasGbicInfoIfIndex"),
)
if mibBuilder.loadTexts:
    s5ChasGbicInfoEntry.setStatus("current")
_S5ChasGbicInfoIfIndex_Type = InterfaceIndex
_S5ChasGbicInfoIfIndex_Object = MibTableColumn
s5ChasGbicInfoIfIndex = _S5ChasGbicInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 1),
    _S5ChasGbicInfoIfIndex_Type()
)
s5ChasGbicInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoIfIndex.setStatus("current")
_S5ChasGbicInfoGbicType_Type = DisplayString
_S5ChasGbicInfoGbicType_Object = MibTableColumn
s5ChasGbicInfoGbicType = _S5ChasGbicInfoGbicType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 2),
    _S5ChasGbicInfoGbicType_Type()
)
s5ChasGbicInfoGbicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoGbicType.setStatus("current")
_S5ChasGbicInfoWavelength_Type = Integer32
_S5ChasGbicInfoWavelength_Object = MibTableColumn
s5ChasGbicInfoWavelength = _S5ChasGbicInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 3),
    _S5ChasGbicInfoWavelength_Type()
)
s5ChasGbicInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoWavelength.setStatus("current")
_S5ChasGbicInfoVendorName_Type = DisplayString
_S5ChasGbicInfoVendorName_Object = MibTableColumn
s5ChasGbicInfoVendorName = _S5ChasGbicInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 4),
    _S5ChasGbicInfoVendorName_Type()
)
s5ChasGbicInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoVendorName.setStatus("current")


class _S5ChasGbicInfoVendorOui_Type(OctetString):
    """Custom type s5ChasGbicInfoVendorOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_S5ChasGbicInfoVendorOui_Type.__name__ = "OctetString"
_S5ChasGbicInfoVendorOui_Object = MibTableColumn
s5ChasGbicInfoVendorOui = _S5ChasGbicInfoVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 5),
    _S5ChasGbicInfoVendorOui_Type()
)
s5ChasGbicInfoVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoVendorOui.setStatus("current")
_S5ChasGbicInfoVendorPartNo_Type = DisplayString
_S5ChasGbicInfoVendorPartNo_Object = MibTableColumn
s5ChasGbicInfoVendorPartNo = _S5ChasGbicInfoVendorPartNo_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 6),
    _S5ChasGbicInfoVendorPartNo_Type()
)
s5ChasGbicInfoVendorPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoVendorPartNo.setStatus("current")
_S5ChasGbicInfoVendorRevision_Type = DisplayString
_S5ChasGbicInfoVendorRevision_Object = MibTableColumn
s5ChasGbicInfoVendorRevision = _S5ChasGbicInfoVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 7),
    _S5ChasGbicInfoVendorRevision_Type()
)
s5ChasGbicInfoVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoVendorRevision.setStatus("current")
_S5ChasGbicInfoVendorSerial_Type = DisplayString
_S5ChasGbicInfoVendorSerial_Object = MibTableColumn
s5ChasGbicInfoVendorSerial = _S5ChasGbicInfoVendorSerial_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 8),
    _S5ChasGbicInfoVendorSerial_Type()
)
s5ChasGbicInfoVendorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoVendorSerial.setStatus("current")


class _S5ChasGbicInfoHwOptions_Type(Bits):
    """Custom type s5ChasGbicInfoHwOptions based on Bits"""
    namedValues = NamedValues(
        *(("rxLoss", 0),
          ("txDisable", 2),
          ("txFault", 1))
    )

_S5ChasGbicInfoHwOptions_Type.__name__ = "Bits"
_S5ChasGbicInfoHwOptions_Object = MibTableColumn
s5ChasGbicInfoHwOptions = _S5ChasGbicInfoHwOptions_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 9),
    _S5ChasGbicInfoHwOptions_Type()
)
s5ChasGbicInfoHwOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoHwOptions.setStatus("current")
_S5ChasGbicInfoDateCode_Type = DisplayString
_S5ChasGbicInfoDateCode_Object = MibTableColumn
s5ChasGbicInfoDateCode = _S5ChasGbicInfoDateCode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 10),
    _S5ChasGbicInfoDateCode_Type()
)
s5ChasGbicInfoDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoDateCode.setStatus("current")
_S5ChasGbicInfoCleiCode_Type = DisplayString
_S5ChasGbicInfoCleiCode_Object = MibTableColumn
s5ChasGbicInfoCleiCode = _S5ChasGbicInfoCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 11),
    _S5ChasGbicInfoCleiCode_Type()
)
s5ChasGbicInfoCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoCleiCode.setStatus("current")
_S5ChasGbicInfoProductCode_Type = DisplayString
_S5ChasGbicInfoProductCode_Object = MibTableColumn
s5ChasGbicInfoProductCode = _S5ChasGbicInfoProductCode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 12),
    _S5ChasGbicInfoProductCode_Type()
)
s5ChasGbicInfoProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ChasGbicInfoProductCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-CHASSIS-MIB",
    **{"s5ChasGen": s5ChasGen,
       "s5ChasType": s5ChasType,
       "s5ChasDescr": s5ChasDescr,
       "s5ChasLocation": s5ChasLocation,
       "s5ChasContact": s5ChasContact,
       "s5ChasVer": s5ChasVer,
       "s5ChasSerNum": s5ChasSerNum,
       "s5ChasGblPhysChngs": s5ChasGblPhysChngs,
       "s5ChasGblPhysLstChng": s5ChasGblPhysLstChng,
       "s5ChasGblAttChngs": s5ChasGblAttChngs,
       "s5ChasGblAttLstChng": s5ChasGblAttLstChng,
       "s5ChasGblConfChngs": s5ChasGblConfChngs,
       "s5ChasGblConfLstChng": s5ChasGblConfLstChng,
       "s5ChasGrp": s5ChasGrp,
       "s5ChasGrpTable": s5ChasGrpTable,
       "s5ChasGrpEntry": s5ChasGrpEntry,
       "s5ChasGrpIndx": s5ChasGrpIndx,
       "s5ChasGrpType": s5ChasGrpType,
       "s5ChasGrpDescr": s5ChasGrpDescr,
       "s5ChasGrpMaxEnts": s5ChasGrpMaxEnts,
       "s5ChasGrpNumEnts": s5ChasGrpNumEnts,
       "s5ChasGrpPhysChngs": s5ChasGrpPhysChngs,
       "s5ChasGrpPhysLstChng": s5ChasGrpPhysLstChng,
       "s5ChasGrpEncodeFactor": s5ChasGrpEncodeFactor,
       "s5ChasCom": s5ChasCom,
       "s5ChasComTable": s5ChasComTable,
       "s5ChasComEntry": s5ChasComEntry,
       "s5ChasComGrpIndx": s5ChasComGrpIndx,
       "s5ChasComIndx": s5ChasComIndx,
       "s5ChasComSubIndx": s5ChasComSubIndx,
       "s5ChasComType": s5ChasComType,
       "s5ChasComDescr": s5ChasComDescr,
       "s5ChasComVer": s5ChasComVer,
       "s5ChasComSerNum": s5ChasComSerNum,
       "s5ChasComLstChng": s5ChasComLstChng,
       "s5ChasComAdminState": s5ChasComAdminState,
       "s5ChasComOperState": s5ChasComOperState,
       "s5ChasComMaxSubs": s5ChasComMaxSubs,
       "s5ChasComNumSubs": s5ChasComNumSubs,
       "s5ChasComRelPos": s5ChasComRelPos,
       "s5ChasComLocation": s5ChasComLocation,
       "s5ChasComGroupMap": s5ChasComGroupMap,
       "s5ChasComBaseNumPorts": s5ChasComBaseNumPorts,
       "s5ChasComTotalNumPorts": s5ChasComTotalNumPorts,
       "s5ChasComIpAddress": s5ChasComIpAddress,
       "s5ChasComRunningSoftwareVer": s5ChasComRunningSoftwareVer,
       "s5ChasComIpv6Address": s5ChasComIpv6Address,
       "s5ChasComIpv6NetMask": s5ChasComIpv6NetMask,
       "s5ChasComIpMgmtAddress": s5ChasComIpMgmtAddress,
       "s5ChasComIpMgmtNetMask": s5ChasComIpMgmtNetMask,
       "s5ChasComIpMgmtGateway": s5ChasComIpMgmtGateway,
       "s5ChasComIpv6MgmtAddress": s5ChasComIpv6MgmtAddress,
       "s5ChasComIpv6MgmtNetMask": s5ChasComIpv6MgmtNetMask,
       "s5ChasComIpMgmtLimit": s5ChasComIpMgmtLimit,
       "s5ChasComIpMgmtTimeout": s5ChasComIpMgmtTimeout,
       "s5ChasComIpMgmtShutdown": s5ChasComIpMgmtShutdown,
       "s5ChasComUpTime": s5ChasComUpTime,
       "s5ChasBrd": s5ChasBrd,
       "s5ChasBrdTable": s5ChasBrdTable,
       "s5ChasBrdEntry": s5ChasBrdEntry,
       "s5ChasBrdIndx": s5ChasBrdIndx,
       "s5ChasBrdLeds": s5ChasBrdLeds,
       "s5ChasBrdNumAtt": s5ChasBrdNumAtt,
       "s5ChasBrdAttChngs": s5ChasBrdAttChngs,
       "s5ChasBrdAttLstChng": s5ChasBrdAttLstChng,
       "s5ChasBrdStatusDsply": s5ChasBrdStatusDsply,
       "s5ChasBrdDateCode": s5ChasBrdDateCode,
       "s5ChasBrdCfgSrc": s5ChasBrdCfgSrc,
       "s5ChasBrdCfgChngs": s5ChasBrdCfgChngs,
       "s5ChasBrdFanLeds": s5ChasBrdFanLeds,
       "s5ChasAttTable": s5ChasAttTable,
       "s5ChasAttEntry": s5ChasAttEntry,
       "s5ChasAttBrdIndx": s5ChasAttBrdIndx,
       "s5ChasAttIndx": s5ChasAttIndx,
       "s5ChasAttDfltAtt": s5ChasAttDfltAtt,
       "s5ChasAttCurAtt": s5ChasAttCurAtt,
       "s5ChasAttChngs": s5ChasAttChngs,
       "s5ChasAttLstChng": s5ChasAttLstChng,
       "s5ChasAttClusterConnCapability": s5ChasAttClusterConnCapability,
       "s5ChasLocChanTable": s5ChasLocChanTable,
       "s5ChasLocChanEntry": s5ChasLocChanEntry,
       "s5ChasLocChanBrdIndx": s5ChasLocChanBrdIndx,
       "s5ChasLocChanIndx": s5ChasLocChanIndx,
       "s5ChasLocChanBkplMode": s5ChasLocChanBkplMode,
       "s5ChasStore": s5ChasStore,
       "s5ChasStoreTable": s5ChasStoreTable,
       "s5ChasStoreEntry": s5ChasStoreEntry,
       "s5ChasStoreGrpIndx": s5ChasStoreGrpIndx,
       "s5ChasStoreComIndx": s5ChasStoreComIndx,
       "s5ChasStoreSubIndx": s5ChasStoreSubIndx,
       "s5ChasStoreIndx": s5ChasStoreIndx,
       "s5ChasStoreType": s5ChasStoreType,
       "s5ChasStoreCurSize": s5ChasStoreCurSize,
       "s5ChasStoreCntntVer": s5ChasStoreCntntVer,
       "s5ChasStoreFilename": s5ChasStoreFilename,
       "s5ChasStoreUsedSize": s5ChasStoreUsedSize,
       "s5ChasStoreDescription": s5ChasStoreDescription,
       "s5ChasStoreAge": s5ChasStoreAge,
       "s5ChasSm": s5ChasSm,
       "s5ChasSmLeds": s5ChasSmLeds,
       "s5ChasSmDateCode": s5ChasSmDateCode,
       "s5ChasTmpSnr": s5ChasTmpSnr,
       "s5ChasTmpSnrTable": s5ChasTmpSnrTable,
       "s5ChasTmpSnrEntry": s5ChasTmpSnrEntry,
       "s5ChasTmpSnrGrpIndx": s5ChasTmpSnrGrpIndx,
       "s5ChasTmpSnrIndx": s5ChasTmpSnrIndx,
       "s5ChasTmpSnrSubIndx": s5ChasTmpSnrSubIndx,
       "s5ChasTmpSnrValue": s5ChasTmpSnrValue,
       "s5ChasTmpSnrTmpValue": s5ChasTmpSnrTmpValue,
       "s5ChasUtil": s5ChasUtil,
       "s5ChasUtilTable": s5ChasUtilTable,
       "s5ChasUtilEntry": s5ChasUtilEntry,
       "s5ChasUtilGrpIndx": s5ChasUtilGrpIndx,
       "s5ChasUtilIndx": s5ChasUtilIndx,
       "s5ChasUtilSubIndx": s5ChasUtilSubIndx,
       "s5ChasUtilTotalCPUUsage": s5ChasUtilTotalCPUUsage,
       "s5ChasUtilCPUUsageLast1Minute": s5ChasUtilCPUUsageLast1Minute,
       "s5ChasUtilCPUUsageLast10Minutes": s5ChasUtilCPUUsageLast10Minutes,
       "s5ChasUtilCPUUsageLast1Hour": s5ChasUtilCPUUsageLast1Hour,
       "s5ChasUtilCPUUsageLast24Hours": s5ChasUtilCPUUsageLast24Hours,
       "s5ChasUtilMemoryAvailable": s5ChasUtilMemoryAvailable,
       "s5ChasUtilMemoryMinAvailable": s5ChasUtilMemoryMinAvailable,
       "s5ChasUtilCPUUsageLast10Seconds": s5ChasUtilCPUUsageLast10Seconds,
       "s5ChasUtilMemoryTotalMB": s5ChasUtilMemoryTotalMB,
       "s5ChasUtilMemoryAvailableMB": s5ChasUtilMemoryAvailableMB,
       "s5ChasPs": s5ChasPs,
       "s5ChasPsRpsuTable": s5ChasPsRpsuTable,
       "s5ChasPsRpsuEntry": s5ChasPsRpsuEntry,
       "s5ChasPsRpsuGrpIndx": s5ChasPsRpsuGrpIndx,
       "s5ChasPsRpsuIndx": s5ChasPsRpsuIndx,
       "s5ChasPsRpsuSubIndx": s5ChasPsRpsuSubIndx,
       "s5ChasPsRpsuType": s5ChasPsRpsuType,
       "s5ChasPsRpsuSourceConfig": s5ChasPsRpsuSourceConfig,
       "s5ChasMib": s5ChasMib,
       "s5ChasNotify": s5ChasNotify,
       "s5ChasNotifyFanDirection": s5ChasNotifyFanDirection,
       "s5ChasPluggables": s5ChasPluggables,
       "s5ChasGbicInfoTable": s5ChasGbicInfoTable,
       "s5ChasGbicInfoEntry": s5ChasGbicInfoEntry,
       "s5ChasGbicInfoIfIndex": s5ChasGbicInfoIfIndex,
       "s5ChasGbicInfoGbicType": s5ChasGbicInfoGbicType,
       "s5ChasGbicInfoWavelength": s5ChasGbicInfoWavelength,
       "s5ChasGbicInfoVendorName": s5ChasGbicInfoVendorName,
       "s5ChasGbicInfoVendorOui": s5ChasGbicInfoVendorOui,
       "s5ChasGbicInfoVendorPartNo": s5ChasGbicInfoVendorPartNo,
       "s5ChasGbicInfoVendorRevision": s5ChasGbicInfoVendorRevision,
       "s5ChasGbicInfoVendorSerial": s5ChasGbicInfoVendorSerial,
       "s5ChasGbicInfoHwOptions": s5ChasGbicInfoHwOptions,
       "s5ChasGbicInfoDateCode": s5ChasGbicInfoDateCode,
       "s5ChasGbicInfoCleiCode": s5ChasGbicInfoCleiCode,
       "s5ChasGbicInfoProductCode": s5ChasGbicInfoProductCode}
)
