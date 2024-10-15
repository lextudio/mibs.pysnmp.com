# SNMP MIB module (AMIMEGARAIDMIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AMIMEGARAIDMIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:50 2024
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



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ami_ObjectIdentity = ObjectIdentity
ami = _Ami_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16)
)
_Megaraid_ObjectIdentity = ObjectIdentity
megaraid = _Megaraid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 1)
)
_Mifmib_ObjectIdentity = ObjectIdentity
mifmib = _Mifmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 1, 2)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vTheVerifyIsNotSupported", 2),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TControllerInformation_Object = MibTable
tControllerInformation = _TControllerInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tControllerInformation.setStatus("mandatory")
_EControllerInformation_Object = MibTableRow
eControllerInformation = _EControllerInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1)
)
eControllerInformation.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
    (0, "AMIMEGARAIDMIF-MIB", "a2Adpadapternumber"),
)
if mibBuilder.loadTexts:
    eControllerInformation.setStatus("mandatory")
_A2Adpadapternumber_Type = DmiInteger
_A2Adpadapternumber_Object = MibTableColumn
a2Adpadapternumber = _A2Adpadapternumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 1),
    _A2Adpadapternumber_Type()
)
a2Adpadapternumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Adpadapternumber.setStatus("mandatory")
_A2Firmwareversion_Type = DmiDisplaystring
_A2Firmwareversion_Object = MibTableColumn
a2Firmwareversion = _A2Firmwareversion_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 2),
    _A2Firmwareversion_Type()
)
a2Firmwareversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Firmwareversion.setStatus("mandatory")
_A2Biosversion_Type = DmiDisplaystring
_A2Biosversion_Object = MibTableColumn
a2Biosversion = _A2Biosversion_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 3),
    _A2Biosversion_Type()
)
a2Biosversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Biosversion.setStatus("mandatory")
_A2Numlogicaldrives_Type = DmiInteger
_A2Numlogicaldrives_Object = MibTableColumn
a2Numlogicaldrives = _A2Numlogicaldrives_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 4),
    _A2Numlogicaldrives_Type()
)
a2Numlogicaldrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Numlogicaldrives.setStatus("mandatory")
_A2Dramsizeinmb_Type = DmiInteger
_A2Dramsizeinmb_Object = MibTableColumn
a2Dramsizeinmb = _A2Dramsizeinmb_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 5),
    _A2Dramsizeinmb_Type()
)
a2Dramsizeinmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Dramsizeinmb.setStatus("mandatory")


class _A2Chipsettype_Type(Integer32):
    """Custom type a2Chipsettype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(97,
              225,
              226)
        )
    )
    namedValues = NamedValues(
        *(("vIntelneptuneormercury", 225),
          ("vOthers", 97),
          ("vTriton", 226))
    )


_A2Chipsettype_Type.__name__ = "Integer32"
_A2Chipsettype_Object = MibTableColumn
a2Chipsettype = _A2Chipsettype_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 6),
    _A2Chipsettype_Type()
)
a2Chipsettype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Chipsettype.setStatus("mandatory")
_A2Rebuildrateinpercent_Type = DmiInteger
_A2Rebuildrateinpercent_Object = MibTableColumn
a2Rebuildrateinpercent = _A2Rebuildrateinpercent_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 7),
    _A2Rebuildrateinpercent_Type()
)
a2Rebuildrateinpercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Rebuildrateinpercent.setStatus("mandatory")


class _A2Flushinterval_Type(Integer32):
    """Custom type a2Flushinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("vEightsec", 8),
          ("vFoursec", 4),
          ("vSixsec", 6),
          ("vTensec", 10),
          ("vTwosec", 2))
    )


_A2Flushinterval_Type.__name__ = "Integer32"
_A2Flushinterval_Object = MibTableColumn
a2Flushinterval = _A2Flushinterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 8),
    _A2Flushinterval_Type()
)
a2Flushinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Flushinterval.setStatus("mandatory")
_A2Maxconcurrentcmds_Type = DmiInteger
_A2Maxconcurrentcmds_Object = MibTableColumn
a2Maxconcurrentcmds = _A2Maxconcurrentcmds_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 9),
    _A2Maxconcurrentcmds_Type()
)
a2Maxconcurrentcmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Maxconcurrentcmds.setStatus("mandatory")
_A2Spinupdelay_Type = DmiInteger
_A2Spinupdelay_Object = MibTableColumn
a2Spinupdelay = _A2Spinupdelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 10),
    _A2Spinupdelay_Type()
)
a2Spinupdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Spinupdelay.setStatus("mandatory")
_A2Spinupcount_Type = DmiInteger
_A2Spinupcount_Object = MibTableColumn
a2Spinupcount = _A2Spinupcount_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 11),
    _A2Spinupcount_Type()
)
a2Spinupcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Spinupcount.setStatus("mandatory")
_A2Adpioreadspersec_Type = DmiInteger
_A2Adpioreadspersec_Object = MibTableColumn
a2Adpioreadspersec = _A2Adpioreadspersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 12),
    _A2Adpioreadspersec_Type()
)
a2Adpioreadspersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Adpioreadspersec.setStatus("mandatory")
_A2Adpiowritespersec_Type = DmiInteger
_A2Adpiowritespersec_Object = MibTableColumn
a2Adpiowritespersec = _A2Adpiowritespersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 13),
    _A2Adpiowritespersec_Type()
)
a2Adpiowritespersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Adpiowritespersec.setStatus("mandatory")
_A2Adpreadkbspersec_Type = DmiInteger
_A2Adpreadkbspersec_Object = MibTableColumn
a2Adpreadkbspersec = _A2Adpreadkbspersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 14),
    _A2Adpreadkbspersec_Type()
)
a2Adpreadkbspersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Adpreadkbspersec.setStatus("mandatory")
_A2Adpwritekbspersec_Type = DmiInteger
_A2Adpwritekbspersec_Object = MibTableColumn
a2Adpwritekbspersec = _A2Adpwritekbspersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 15),
    _A2Adpwritekbspersec_Type()
)
a2Adpwritekbspersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Adpwritekbspersec.setStatus("mandatory")
_A2Adpreadfailurespersec_Type = DmiInteger
_A2Adpreadfailurespersec_Object = MibTableColumn
a2Adpreadfailurespersec = _A2Adpreadfailurespersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 16),
    _A2Adpreadfailurespersec_Type()
)
a2Adpreadfailurespersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Adpreadfailurespersec.setStatus("mandatory")
_A2Adpwritefailurespersec_Type = DmiInteger
_A2Adpwritefailurespersec_Object = MibTableColumn
a2Adpwritefailurespersec = _A2Adpwritefailurespersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 17),
    _A2Adpwritefailurespersec_Type()
)
a2Adpwritefailurespersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Adpwritefailurespersec.setStatus("mandatory")


class _A2Scanchannels_Type(Integer32):
    """Custom type a2Scanchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vScaninprog", 3),
          ("vScanover", 1),
          ("vStartscan", 2))
    )


_A2Scanchannels_Type.__name__ = "Integer32"
_A2Scanchannels_Object = MibTableColumn
a2Scanchannels = _A2Scanchannels_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 18),
    _A2Scanchannels_Type()
)
a2Scanchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Scanchannels.setStatus("mandatory")
_A2Logicalview_Type = DmiOctetstring
_A2Logicalview_Object = MibTableColumn
a2Logicalview = _A2Logicalview_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 19),
    _A2Logicalview_Type()
)
a2Logicalview.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Logicalview.setStatus("mandatory")
_A2Physicalview_Type = DmiOctetstring
_A2Physicalview_Object = MibTableColumn
a2Physicalview = _A2Physicalview_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 20),
    _A2Physicalview_Type()
)
a2Physicalview.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Physicalview.setStatus("mandatory")
_TLogicalDriveInformation_Object = MibTable
tLogicalDriveInformation = _TLogicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tLogicalDriveInformation.setStatus("mandatory")
_ELogicalDriveInformation_Object = MibTableRow
eLogicalDriveInformation = _ELogicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1)
)
eLogicalDriveInformation.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
    (0, "AMIMEGARAIDMIF-MIB", "a3Ldadapternumber"),
    (0, "AMIMEGARAIDMIF-MIB", "a3Logicaldrivenumber"),
)
if mibBuilder.loadTexts:
    eLogicalDriveInformation.setStatus("mandatory")
_A3Ldadapternumber_Type = DmiInteger
_A3Ldadapternumber_Object = MibTableColumn
a3Ldadapternumber = _A3Ldadapternumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 1),
    _A3Ldadapternumber_Type()
)
a3Ldadapternumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Ldadapternumber.setStatus("mandatory")
_A3Logicaldrivenumber_Type = DmiInteger
_A3Logicaldrivenumber_Object = MibTableColumn
a3Logicaldrivenumber = _A3Logicaldrivenumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 2),
    _A3Logicaldrivenumber_Type()
)
a3Logicaldrivenumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Logicaldrivenumber.setStatus("mandatory")


class _A3Raidlevel_Type(Integer32):
    """Custom type a3Raidlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vRaid0", 0),
          ("vRaid1", 1),
          ("vRaid3", 3),
          ("vRaid5", 5))
    )


_A3Raidlevel_Type.__name__ = "Integer32"
_A3Raidlevel_Object = MibTableColumn
a3Raidlevel = _A3Raidlevel_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 3),
    _A3Raidlevel_Type()
)
a3Raidlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Raidlevel.setStatus("mandatory")


class _A3Status_Type(Integer32):
    """Custom type a3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vCheckconsistency", 4),
          ("vDegraded", 1),
          ("vInitialize", 3),
          ("vOffline", 0),
          ("vOptimal", 2))
    )


_A3Status_Type.__name__ = "Integer32"
_A3Status_Object = MibTableColumn
a3Status = _A3Status_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 4),
    _A3Status_Type()
)
a3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3Status.setStatus("mandatory")
_A3Sizeinmb_Type = DmiInteger
_A3Sizeinmb_Object = MibTableColumn
a3Sizeinmb = _A3Sizeinmb_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 5),
    _A3Sizeinmb_Type()
)
a3Sizeinmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Sizeinmb.setStatus("mandatory")


class _A3Stripesize_Type(Integer32):
    """Custom type a3Stripesize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              16,
              32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("vEightkb", 16),
          ("vFourkb", 8),
          ("vOnekb", 2),
          ("vOnetwentyeightkb", 256),
          ("vSixteenkb", 32),
          ("vSixtyfourkb", 128),
          ("vThirtytwokb", 64),
          ("vTwokb", 4))
    )


_A3Stripesize_Type.__name__ = "Integer32"
_A3Stripesize_Object = MibTableColumn
a3Stripesize = _A3Stripesize_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 6),
    _A3Stripesize_Type()
)
a3Stripesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Stripesize.setStatus("mandatory")


class _A3Readpolicy_Type(Integer32):
    """Custom type a3Readpolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vAdaptive", 2),
          ("vNormal", 0),
          ("vReadahead", 1))
    )


_A3Readpolicy_Type.__name__ = "Integer32"
_A3Readpolicy_Object = MibTableColumn
a3Readpolicy = _A3Readpolicy_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 7),
    _A3Readpolicy_Type()
)
a3Readpolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3Readpolicy.setStatus("mandatory")


class _A3Writepolicy_Type(Integer32):
    """Custom type a3Writepolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vWriteback", 1),
          ("vWritethru", 0))
    )


_A3Writepolicy_Type.__name__ = "Integer32"
_A3Writepolicy_Object = MibTableColumn
a3Writepolicy = _A3Writepolicy_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 8),
    _A3Writepolicy_Type()
)
a3Writepolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3Writepolicy.setStatus("mandatory")


class _A3Cachepolicy_Type(Integer32):
    """Custom type a3Cachepolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vCachedio", 0),
          ("vDirectio", 1))
    )


_A3Cachepolicy_Type.__name__ = "Integer32"
_A3Cachepolicy_Object = MibTableColumn
a3Cachepolicy = _A3Cachepolicy_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 9),
    _A3Cachepolicy_Type()
)
a3Cachepolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3Cachepolicy.setStatus("mandatory")
_A3Numberofspans_Type = DmiInteger
_A3Numberofspans_Object = MibTableColumn
a3Numberofspans = _A3Numberofspans_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 10),
    _A3Numberofspans_Type()
)
a3Numberofspans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Numberofspans.setStatus("mandatory")
_A3Numberofstripes_Type = DmiInteger
_A3Numberofstripes_Object = MibTableColumn
a3Numberofstripes = _A3Numberofstripes_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 11),
    _A3Numberofstripes_Type()
)
a3Numberofstripes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Numberofstripes.setStatus("mandatory")
_A3Ldioreadspersec_Type = DmiInteger
_A3Ldioreadspersec_Object = MibTableColumn
a3Ldioreadspersec = _A3Ldioreadspersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 12),
    _A3Ldioreadspersec_Type()
)
a3Ldioreadspersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Ldioreadspersec.setStatus("mandatory")
_A3Ldiowritespersec_Type = DmiInteger
_A3Ldiowritespersec_Object = MibTableColumn
a3Ldiowritespersec = _A3Ldiowritespersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 13),
    _A3Ldiowritespersec_Type()
)
a3Ldiowritespersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Ldiowritespersec.setStatus("mandatory")
_A3Ldreadskbspersec_Type = DmiInteger
_A3Ldreadskbspersec_Object = MibTableColumn
a3Ldreadskbspersec = _A3Ldreadskbspersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 14),
    _A3Ldreadskbspersec_Type()
)
a3Ldreadskbspersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Ldreadskbspersec.setStatus("mandatory")
_A3Ldwritekbspersec_Type = DmiInteger
_A3Ldwritekbspersec_Object = MibTableColumn
a3Ldwritekbspersec = _A3Ldwritekbspersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 15),
    _A3Ldwritekbspersec_Type()
)
a3Ldwritekbspersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Ldwritekbspersec.setStatus("mandatory")
_A3Ldioreadfailurespersec_Type = DmiInteger
_A3Ldioreadfailurespersec_Object = MibTableColumn
a3Ldioreadfailurespersec = _A3Ldioreadfailurespersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 16),
    _A3Ldioreadfailurespersec_Type()
)
a3Ldioreadfailurespersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Ldioreadfailurespersec.setStatus("mandatory")
_A3Ldwritefailurespersec_Type = DmiInteger
_A3Ldwritefailurespersec_Object = MibTableColumn
a3Ldwritefailurespersec = _A3Ldwritefailurespersec_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 17),
    _A3Ldwritefailurespersec_Type()
)
a3Ldwritefailurespersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Ldwritefailurespersec.setStatus("mandatory")
_A3Progress_Type = DmiInteger
_A3Progress_Object = MibTableColumn
a3Progress = _A3Progress_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 18),
    _A3Progress_Type()
)
a3Progress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3Progress.setStatus("mandatory")
_A3Allattributes_Type = DmiOctetstring
_A3Allattributes_Object = MibTableColumn
a3Allattributes = _A3Allattributes_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 19),
    _A3Allattributes_Type()
)
a3Allattributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Allattributes.setStatus("mandatory")
_TPhysicalDeviceInformation_Object = MibTable
tPhysicalDeviceInformation = _TPhysicalDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tPhysicalDeviceInformation.setStatus("mandatory")
_EPhysicalDeviceInformation_Object = MibTableRow
ePhysicalDeviceInformation = _EPhysicalDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1)
)
ePhysicalDeviceInformation.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
    (0, "AMIMEGARAIDMIF-MIB", "a4Physadapternumber"),
    (0, "AMIMEGARAIDMIF-MIB", "a4Physchannel"),
    (0, "AMIMEGARAIDMIF-MIB", "a4Targetid"),
)
if mibBuilder.loadTexts:
    ePhysicalDeviceInformation.setStatus("mandatory")
_A4Physadapternumber_Type = DmiInteger
_A4Physadapternumber_Object = MibTableColumn
a4Physadapternumber = _A4Physadapternumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 1),
    _A4Physadapternumber_Type()
)
a4Physadapternumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Physadapternumber.setStatus("mandatory")
_A4Physchannel_Type = DmiInteger
_A4Physchannel_Object = MibTableColumn
a4Physchannel = _A4Physchannel_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 2),
    _A4Physchannel_Type()
)
a4Physchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Physchannel.setStatus("mandatory")
_A4Targetid_Type = DmiInteger
_A4Targetid_Object = MibTableColumn
a4Targetid = _A4Targetid_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 3),
    _A4Targetid_Type()
)
a4Targetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Targetid.setStatus("mandatory")


class _A4State_Type(Integer32):
    """Custom type a4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vFailed", 4),
          ("vHotspare", 6),
          ("vNotResponding", 7),
          ("vOnline", 3),
          ("vReady", 1),
          ("vRebuild", 5))
    )


_A4State_Type.__name__ = "Integer32"
_A4State_Object = MibTableColumn
a4State = _A4State_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 4),
    _A4State_Type()
)
a4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4State.setStatus("mandatory")
_A4Arrayposition_Type = DmiDisplaystring
_A4Arrayposition_Object = MibTableColumn
a4Arrayposition = _A4Arrayposition_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 5),
    _A4Arrayposition_Type()
)
a4Arrayposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Arrayposition.setStatus("mandatory")
_A4Sizemb_Type = DmiInteger
_A4Sizemb_Object = MibTableColumn
a4Sizemb = _A4Sizemb_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 6),
    _A4Sizemb_Type()
)
a4Sizemb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Sizemb.setStatus("mandatory")


class _A4Devicetype_Type(Integer32):
    """Custom type a4Devicetype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("vAsynchronoushigh", 11),
          ("vAsynchronouslow", 10),
          ("vChanger", 8),
          ("vCommunication", 9),
          ("vDisk", 0),
          ("vNotResponding", 13),
          ("vOptical", 7),
          ("vPrinter", 2),
          ("vProcessor", 3),
          ("vReservedlow", 12),
          ("vScanner", 6),
          ("vTape", 1),
          ("vWorm", 4))
    )


_A4Devicetype_Type.__name__ = "Integer32"
_A4Devicetype_Object = MibTableColumn
a4Devicetype = _A4Devicetype_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 7),
    _A4Devicetype_Type()
)
a4Devicetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Devicetype.setStatus("mandatory")
_A4Inquirystring_Type = DmiDisplaystring
_A4Inquirystring_Object = MibTableColumn
a4Inquirystring = _A4Inquirystring_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 8),
    _A4Inquirystring_Type()
)
a4Inquirystring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Inquirystring.setStatus("mandatory")


class _A4Scsilevel_Type(Integer32):
    """Custom type a4Scsilevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vScsi1", 1),
          ("vScsi2", 2),
          ("vUnknown", 3))
    )


_A4Scsilevel_Type.__name__ = "Integer32"
_A4Scsilevel_Object = MibTableColumn
a4Scsilevel = _A4Scsilevel_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 9),
    _A4Scsilevel_Type()
)
a4Scsilevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Scsilevel.setStatus("mandatory")


class _A4Syncnegotiation_Type(Integer32):
    """Custom type a4Syncnegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vDisable", 2),
          ("vEnable", 1),
          ("vUnknown", 3))
    )


_A4Syncnegotiation_Type.__name__ = "Integer32"
_A4Syncnegotiation_Object = MibTableColumn
a4Syncnegotiation = _A4Syncnegotiation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 10),
    _A4Syncnegotiation_Type()
)
a4Syncnegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Syncnegotiation.setStatus("mandatory")


class _A4Qtags_Type(Integer32):
    """Custom type a4Qtags based on Integer32"""
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
        *(("vEnhancedqtagscheduling", 5),
          ("vFour", 4),
          ("vOne", 1),
          ("vThree", 3),
          ("vTwo", 2),
          ("vUnknown", 6))
    )


_A4Qtags_Type.__name__ = "Integer32"
_A4Qtags_Object = MibTableColumn
a4Qtags = _A4Qtags_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 11),
    _A4Qtags_Type()
)
a4Qtags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Qtags.setStatus("mandatory")
_A4Rebuildprogress_Type = DmiInteger
_A4Rebuildprogress_Object = MibTableColumn
a4Rebuildprogress = _A4Rebuildprogress_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 12),
    _A4Rebuildprogress_Type()
)
a4Rebuildprogress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4Rebuildprogress.setStatus("mandatory")
_A4Mediumerrors_Type = DmiInteger
_A4Mediumerrors_Object = MibTableColumn
a4Mediumerrors = _A4Mediumerrors_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 13),
    _A4Mediumerrors_Type()
)
a4Mediumerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Mediumerrors.setStatus("mandatory")
_A4Othererrors_Type = DmiInteger
_A4Othererrors_Object = MibTableColumn
a4Othererrors = _A4Othererrors_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 14),
    _A4Othererrors_Type()
)
a4Othererrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Othererrors.setStatus("mandatory")
_A4Allattributes_Type = DmiOctetstring
_A4Allattributes_Object = MibTableColumn
a4Allattributes = _A4Allattributes_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 15),
    _A4Allattributes_Type()
)
a4Allattributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Allattributes.setStatus("mandatory")
_TChannels_Object = MibTable
tChannels = _TChannels_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tChannels.setStatus("mandatory")
_EChannels_Object = MibTableRow
eChannels = _EChannels_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1)
)
eChannels.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
    (0, "AMIMEGARAIDMIF-MIB", "a5Chanadapternumber"),
    (0, "AMIMEGARAIDMIF-MIB", "a5Channel"),
)
if mibBuilder.loadTexts:
    eChannels.setStatus("mandatory")
_A5Chanadapternumber_Type = DmiInteger
_A5Chanadapternumber_Object = MibTableColumn
a5Chanadapternumber = _A5Chanadapternumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 1),
    _A5Chanadapternumber_Type()
)
a5Chanadapternumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Chanadapternumber.setStatus("mandatory")
_A5Channel_Type = DmiInteger
_A5Channel_Object = MibTableColumn
a5Channel = _A5Channel_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 2),
    _A5Channel_Type()
)
a5Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Channel.setStatus("mandatory")


class _A5Terminations_Type(Integer32):
    """Custom type a5Terminations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 0),
          ("vHigher8bits", 1),
          ("vWideterminations", 2))
    )


_A5Terminations_Type.__name__ = "Integer32"
_A5Terminations_Object = MibTableColumn
a5Terminations = _A5Terminations_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 3),
    _A5Terminations_Type()
)
a5Terminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Terminations.setStatus("mandatory")


class _A5Channelstatus_Type(Integer32):
    """Custom type a5Channelstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vActive", 1),
          ("vQuit", 0))
    )


_A5Channelstatus_Type.__name__ = "Integer32"
_A5Channelstatus_Object = MibTableColumn
a5Channelstatus = _A5Channelstatus_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 4),
    _A5Channelstatus_Type()
)
a5Channelstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Channelstatus.setStatus("mandatory")
_TAlertManagementInformation_Object = MibTable
tAlertManagementInformation = _TAlertManagementInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tAlertManagementInformation.setStatus("mandatory")
_EAlertManagementInformation_Object = MibTableRow
eAlertManagementInformation = _EAlertManagementInformation_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1)
)
eAlertManagementInformation.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eAlertManagementInformation.setStatus("mandatory")


class _A6Dmiindication_Type(Integer32):
    """Custom type a6Dmiindication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 0),
          ("vEnabled", 1))
    )


_A6Dmiindication_Type.__name__ = "Integer32"
_A6Dmiindication_Object = MibTableColumn
a6Dmiindication = _A6Dmiindication_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1, 1),
    _A6Dmiindication_Type()
)
a6Dmiindication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a6Dmiindication.setStatus("mandatory")


class _A6Ams2alerts_Type(Integer32):
    """Custom type a6Ams2alerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 0),
          ("vEnabled", 1))
    )


_A6Ams2alerts_Type.__name__ = "Integer32"
_A6Ams2alerts_Object = MibTableColumn
a6Ams2alerts = _A6Ams2alerts_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1, 2),
    _A6Ams2alerts_Type()
)
a6Ams2alerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a6Ams2alerts.setStatus("mandatory")


class _A6Eventlog_Type(Integer32):
    """Custom type a6Eventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 0),
          ("vEnabled", 1))
    )


_A6Eventlog_Type.__name__ = "Integer32"
_A6Eventlog_Object = MibTableColumn
a6Eventlog = _A6Eventlog_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1, 3),
    _A6Eventlog_Type()
)
a6Eventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a6Eventlog.setStatus("mandatory")
_TGlobalinfo_Object = MibTable
tGlobalinfo = _TGlobalinfo_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tGlobalinfo.setStatus("mandatory")
_EGlobalinfo_Object = MibTableRow
eGlobalinfo = _EGlobalinfo_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 7, 1)
)
eGlobalinfo.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eGlobalinfo.setStatus("mandatory")
_A7Globalcltrinfo_Type = DmiOctetstring
_A7Globalcltrinfo_Object = MibTableColumn
a7Globalcltrinfo = _A7Globalcltrinfo_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 7, 1, 1),
    _A7Globalcltrinfo_Type()
)
a7Globalcltrinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Globalcltrinfo.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99AmiMegaraidMib_Type = DmiDisplaystring
_A99AmiMegaraidMib_Object = MibTableColumn
a99AmiMegaraidMib = _A99AmiMegaraidMib_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1, 1),
    _A99AmiMegaraidMib_Type()
)
a99AmiMegaraidMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99AmiMegaraidMib.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTraps_Type = DmiInteger
_A99DisableTraps_Object = MibTableColumn
a99DisableTraps = _A99DisableTraps_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1, 3),
    _A99DisableTraps_Type()
)
a99DisableTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99DisableTraps.setStatus("mandatory")
_TCompositeDriveAlerts_Object = MibTable
tCompositeDriveAlerts = _TCompositeDriveAlerts_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103)
)
if mibBuilder.loadTexts:
    tCompositeDriveAlerts.setStatus("mandatory")
_ECompositeDriveAlerts_Object = MibTableRow
eCompositeDriveAlerts = _ECompositeDriveAlerts_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1)
)
eCompositeDriveAlerts.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
    (0, "AMIMEGARAIDMIF-MIB", "a103AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eCompositeDriveAlerts.setStatus("mandatory")


class _A103EventType_Type(Integer32):
    """Custom type a103EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vCompositeDriveRecoveryCompleted", 3),
          ("vCompositeDriveRecoveryStarted", 2),
          ("vCompositeDriveStatusChange", 1))
    )


_A103EventType_Type.__name__ = "Integer32"
_A103EventType_Object = MibTableColumn
a103EventType = _A103EventType_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 1),
    _A103EventType_Type()
)
a103EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventType.setStatus("mandatory")


class _A103EventSeverity_Type(Integer32):
    """Custom type a103EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A103EventSeverity_Type.__name__ = "Integer32"
_A103EventSeverity_Object = MibTableColumn
a103EventSeverity = _A103EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 2),
    _A103EventSeverity_Type()
)
a103EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSeverity.setStatus("mandatory")


class _A103IsEventStateBased_Type(Integer32):
    """Custom type a103IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A103IsEventStateBased_Type.__name__ = "Integer32"
_A103IsEventStateBased_Object = MibTableColumn
a103IsEventStateBased = _A103IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 3),
    _A103IsEventStateBased_Type()
)
a103IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103IsEventStateBased.setStatus("mandatory")
_A103EventStateKey_Type = DmiInteger
_A103EventStateKey_Object = MibTableColumn
a103EventStateKey = _A103EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 4),
    _A103EventStateKey_Type()
)
a103EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventStateKey.setStatus("mandatory")
_A103AssociatedGroup_Type = DmiDisplaystring
_A103AssociatedGroup_Object = MibTableColumn
a103AssociatedGroup = _A103AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 5),
    _A103AssociatedGroup_Type()
)
a103AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103AssociatedGroup.setStatus("mandatory")
_A103EventSystem_Type = DmiInteger
_A103EventSystem_Object = MibTableColumn
a103EventSystem = _A103EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 6),
    _A103EventSystem_Type()
)
a103EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSystem.setStatus("mandatory")
_A103EventSubsystem_Type = DmiInteger
_A103EventSubsystem_Object = MibTableColumn
a103EventSubsystem = _A103EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 7),
    _A103EventSubsystem_Type()
)
a103EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSubsystem.setStatus("mandatory")


class _A103EventSolution_Type(Integer32):
    """Custom type a103EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A103EventSolution_Type.__name__ = "Integer32"
_A103EventSolution_Object = MibTableColumn
a103EventSolution = _A103EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 8),
    _A103EventSolution_Type()
)
a103EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSolution.setStatus("mandatory")


class _A103InstanceDataPresent_Type(Integer32):
    """Custom type a103InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A103InstanceDataPresent_Type.__name__ = "Integer32"
_A103InstanceDataPresent_Object = MibTableColumn
a103InstanceDataPresent = _A103InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 9),
    _A103InstanceDataPresent_Type()
)
a103InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103InstanceDataPresent.setStatus("mandatory")
_A103VendorSpecificMessage_Type = DmiOctetstring
_A103VendorSpecificMessage_Object = MibTableColumn
a103VendorSpecificMessage = _A103VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 10),
    _A103VendorSpecificMessage_Type()
)
a103VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103VendorSpecificMessage.setStatus("mandatory")
_A103VendorSpecificData_Type = DmiOctetstring
_A103VendorSpecificData_Object = MibTableColumn
a103VendorSpecificData = _A103VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 11),
    _A103VendorSpecificData_Type()
)
a103VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103VendorSpecificData.setStatus("mandatory")
_A103VendorTrapNumber_Type = DmiInteger
_A103VendorTrapNumber_Object = MibTableColumn
a103VendorTrapNumber = _A103VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 12),
    _A103VendorTrapNumber_Type()
)
a103VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103VendorTrapNumber.setStatus("mandatory")
_TPhysicalDriveAlerts_Object = MibTable
tPhysicalDriveAlerts = _TPhysicalDriveAlerts_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104)
)
if mibBuilder.loadTexts:
    tPhysicalDriveAlerts.setStatus("mandatory")
_EPhysicalDriveAlerts_Object = MibTableRow
ePhysicalDriveAlerts = _EPhysicalDriveAlerts_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1)
)
ePhysicalDriveAlerts.setIndexNames(
    (0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"),
    (0, "AMIMEGARAIDMIF-MIB", "a104AssociatedGroup"),
)
if mibBuilder.loadTexts:
    ePhysicalDriveAlerts.setStatus("mandatory")


class _A104EventType_Type(Integer32):
    """Custom type a104EventType based on Integer32"""
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
        *(("vHotSpareCreated", 4),
          ("vPhysicalDriveAppeared", 3),
          ("vPhysicalDriveRemoved", 2),
          ("vPhysicalDriveStatusChange", 1))
    )


_A104EventType_Type.__name__ = "Integer32"
_A104EventType_Object = MibTableColumn
a104EventType = _A104EventType_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 1),
    _A104EventType_Type()
)
a104EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventType.setStatus("mandatory")


class _A104EventSeverity_Type(Integer32):
    """Custom type a104EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A104EventSeverity_Type.__name__ = "Integer32"
_A104EventSeverity_Object = MibTableColumn
a104EventSeverity = _A104EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 2),
    _A104EventSeverity_Type()
)
a104EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSeverity.setStatus("mandatory")


class _A104IsEventStateBased_Type(Integer32):
    """Custom type a104IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A104IsEventStateBased_Type.__name__ = "Integer32"
_A104IsEventStateBased_Object = MibTableColumn
a104IsEventStateBased = _A104IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 3),
    _A104IsEventStateBased_Type()
)
a104IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104IsEventStateBased.setStatus("mandatory")
_A104EventStateKey_Type = DmiInteger
_A104EventStateKey_Object = MibTableColumn
a104EventStateKey = _A104EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 4),
    _A104EventStateKey_Type()
)
a104EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventStateKey.setStatus("mandatory")
_A104AssociatedGroup_Type = DmiDisplaystring
_A104AssociatedGroup_Object = MibTableColumn
a104AssociatedGroup = _A104AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 5),
    _A104AssociatedGroup_Type()
)
a104AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104AssociatedGroup.setStatus("mandatory")
_A104EventSystem_Type = DmiInteger
_A104EventSystem_Object = MibTableColumn
a104EventSystem = _A104EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 6),
    _A104EventSystem_Type()
)
a104EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSystem.setStatus("mandatory")
_A104EventSubsystem_Type = DmiInteger
_A104EventSubsystem_Object = MibTableColumn
a104EventSubsystem = _A104EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 7),
    _A104EventSubsystem_Type()
)
a104EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSubsystem.setStatus("mandatory")


class _A104EventSolution_Type(Integer32):
    """Custom type a104EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A104EventSolution_Type.__name__ = "Integer32"
_A104EventSolution_Object = MibTableColumn
a104EventSolution = _A104EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 8),
    _A104EventSolution_Type()
)
a104EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSolution.setStatus("mandatory")


class _A104InstanceDataPresent_Type(Integer32):
    """Custom type a104InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A104InstanceDataPresent_Type.__name__ = "Integer32"
_A104InstanceDataPresent_Object = MibTableColumn
a104InstanceDataPresent = _A104InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 9),
    _A104InstanceDataPresent_Type()
)
a104InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104InstanceDataPresent.setStatus("mandatory")
_A104VendorSpecificMessage_Type = DmiOctetstring
_A104VendorSpecificMessage_Object = MibTableColumn
a104VendorSpecificMessage = _A104VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 10),
    _A104VendorSpecificMessage_Type()
)
a104VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104VendorSpecificMessage.setStatus("mandatory")
_A104VendorSpecificData_Type = DmiOctetstring
_A104VendorSpecificData_Object = MibTableColumn
a104VendorSpecificData = _A104VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 11),
    _A104VendorSpecificData_Type()
)
a104VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104VendorSpecificData.setStatus("mandatory")
_A104VendorTrapNumber_Type = DmiInteger
_A104VendorTrapNumber_Object = MibTableColumn
a104VendorTrapNumber = _A104VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 12),
    _A104VendorTrapNumber_Type()
)
a104VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104VendorTrapNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AMIMEGARAIDMIF-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "ami": ami,
       "megaraid": megaraid,
       "mifmib": mifmib,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tControllerInformation": tControllerInformation,
       "eControllerInformation": eControllerInformation,
       "a2Adpadapternumber": a2Adpadapternumber,
       "a2Firmwareversion": a2Firmwareversion,
       "a2Biosversion": a2Biosversion,
       "a2Numlogicaldrives": a2Numlogicaldrives,
       "a2Dramsizeinmb": a2Dramsizeinmb,
       "a2Chipsettype": a2Chipsettype,
       "a2Rebuildrateinpercent": a2Rebuildrateinpercent,
       "a2Flushinterval": a2Flushinterval,
       "a2Maxconcurrentcmds": a2Maxconcurrentcmds,
       "a2Spinupdelay": a2Spinupdelay,
       "a2Spinupcount": a2Spinupcount,
       "a2Adpioreadspersec": a2Adpioreadspersec,
       "a2Adpiowritespersec": a2Adpiowritespersec,
       "a2Adpreadkbspersec": a2Adpreadkbspersec,
       "a2Adpwritekbspersec": a2Adpwritekbspersec,
       "a2Adpreadfailurespersec": a2Adpreadfailurespersec,
       "a2Adpwritefailurespersec": a2Adpwritefailurespersec,
       "a2Scanchannels": a2Scanchannels,
       "a2Logicalview": a2Logicalview,
       "a2Physicalview": a2Physicalview,
       "tLogicalDriveInformation": tLogicalDriveInformation,
       "eLogicalDriveInformation": eLogicalDriveInformation,
       "a3Ldadapternumber": a3Ldadapternumber,
       "a3Logicaldrivenumber": a3Logicaldrivenumber,
       "a3Raidlevel": a3Raidlevel,
       "a3Status": a3Status,
       "a3Sizeinmb": a3Sizeinmb,
       "a3Stripesize": a3Stripesize,
       "a3Readpolicy": a3Readpolicy,
       "a3Writepolicy": a3Writepolicy,
       "a3Cachepolicy": a3Cachepolicy,
       "a3Numberofspans": a3Numberofspans,
       "a3Numberofstripes": a3Numberofstripes,
       "a3Ldioreadspersec": a3Ldioreadspersec,
       "a3Ldiowritespersec": a3Ldiowritespersec,
       "a3Ldreadskbspersec": a3Ldreadskbspersec,
       "a3Ldwritekbspersec": a3Ldwritekbspersec,
       "a3Ldioreadfailurespersec": a3Ldioreadfailurespersec,
       "a3Ldwritefailurespersec": a3Ldwritefailurespersec,
       "a3Progress": a3Progress,
       "a3Allattributes": a3Allattributes,
       "tPhysicalDeviceInformation": tPhysicalDeviceInformation,
       "ePhysicalDeviceInformation": ePhysicalDeviceInformation,
       "a4Physadapternumber": a4Physadapternumber,
       "a4Physchannel": a4Physchannel,
       "a4Targetid": a4Targetid,
       "a4State": a4State,
       "a4Arrayposition": a4Arrayposition,
       "a4Sizemb": a4Sizemb,
       "a4Devicetype": a4Devicetype,
       "a4Inquirystring": a4Inquirystring,
       "a4Scsilevel": a4Scsilevel,
       "a4Syncnegotiation": a4Syncnegotiation,
       "a4Qtags": a4Qtags,
       "a4Rebuildprogress": a4Rebuildprogress,
       "a4Mediumerrors": a4Mediumerrors,
       "a4Othererrors": a4Othererrors,
       "a4Allattributes": a4Allattributes,
       "tChannels": tChannels,
       "eChannels": eChannels,
       "a5Chanadapternumber": a5Chanadapternumber,
       "a5Channel": a5Channel,
       "a5Terminations": a5Terminations,
       "a5Channelstatus": a5Channelstatus,
       "tAlertManagementInformation": tAlertManagementInformation,
       "eAlertManagementInformation": eAlertManagementInformation,
       "a6Dmiindication": a6Dmiindication,
       "a6Ams2alerts": a6Ams2alerts,
       "a6Eventlog": a6Eventlog,
       "tGlobalinfo": tGlobalinfo,
       "eGlobalinfo": eGlobalinfo,
       "a7Globalcltrinfo": a7Globalcltrinfo,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99AmiMegaraidMib": a99AmiMegaraidMib,
       "a99MibOid": a99MibOid,
       "a99DisableTraps": a99DisableTraps,
       "tCompositeDriveAlerts": tCompositeDriveAlerts,
       "eCompositeDriveAlerts": eCompositeDriveAlerts,
       "a103EventType": a103EventType,
       "a103EventSeverity": a103EventSeverity,
       "a103IsEventStateBased": a103IsEventStateBased,
       "a103EventStateKey": a103EventStateKey,
       "a103AssociatedGroup": a103AssociatedGroup,
       "a103EventSystem": a103EventSystem,
       "a103EventSubsystem": a103EventSubsystem,
       "a103EventSolution": a103EventSolution,
       "a103InstanceDataPresent": a103InstanceDataPresent,
       "a103VendorSpecificMessage": a103VendorSpecificMessage,
       "a103VendorSpecificData": a103VendorSpecificData,
       "a103VendorTrapNumber": a103VendorTrapNumber,
       "tPhysicalDriveAlerts": tPhysicalDriveAlerts,
       "ePhysicalDriveAlerts": ePhysicalDriveAlerts,
       "a104EventType": a104EventType,
       "a104EventSeverity": a104EventSeverity,
       "a104IsEventStateBased": a104IsEventStateBased,
       "a104EventStateKey": a104EventStateKey,
       "a104AssociatedGroup": a104AssociatedGroup,
       "a104EventSystem": a104EventSystem,
       "a104EventSubsystem": a104EventSubsystem,
       "a104EventSolution": a104EventSolution,
       "a104InstanceDataPresent": a104InstanceDataPresent,
       "a104VendorSpecificMessage": a104VendorSpecificMessage,
       "a104VendorSpecificData": a104VendorSpecificData,
       "a104VendorTrapNumber": a104VendorTrapNumber}
)
