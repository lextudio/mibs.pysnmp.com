# SNMP MIB module (CISCO-DMN-DSG-DPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-DPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:21 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGDPM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36)
)
ciscoDSGDPM.setRevisions(
        ("2012-03-12 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpmInfo_ObjectIdentity = ObjectIdentity
dpmInfo = _DpmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 1)
)


class _DpmRegenerate_Type(Integer32):
    """Custom type dpmRegenerate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("asNeeded", 2))
    )


_DpmRegenerate_Type.__name__ = "Integer32"
_DpmRegenerate_Object = MibScalar
dpmRegenerate = _DpmRegenerate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 1, 1),
    _DpmRegenerate_Type()
)
dpmRegenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmRegenerate.setStatus("current")
_DpmTable_ObjectIdentity = ObjectIdentity
dpmTable = _DpmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2)
)
_DpmGblCfgTable_Object = MibTable
dpmGblCfgTable = _DpmGblCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1)
)
if mibBuilder.loadTexts:
    dpmGblCfgTable.setStatus("current")
_DpmGblCfgEntry_Object = MibTableRow
dpmGblCfgEntry = _DpmGblCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1)
)
dpmGblCfgEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DPM-MIB", "dpmGblCfgInstanceID"),
)
if mibBuilder.loadTexts:
    dpmGblCfgEntry.setStatus("current")


class _DpmGblCfgInstanceID_Type(Integer32):
    """Custom type dpmGblCfgInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DpmGblCfgInstanceID_Type.__name__ = "Integer32"
_DpmGblCfgInstanceID_Object = MibTableColumn
dpmGblCfgInstanceID = _DpmGblCfgInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 1),
    _DpmGblCfgInstanceID_Type()
)
dpmGblCfgInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmGblCfgInstanceID.setStatus("current")


class _DpmGblCfgInstanceName_Type(DisplayString):
    """Custom type dpmGblCfgInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpmGblCfgInstanceName_Type.__name__ = "DisplayString"
_DpmGblCfgInstanceName_Object = MibTableColumn
dpmGblCfgInstanceName = _DpmGblCfgInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 2),
    _DpmGblCfgInstanceName_Type()
)
dpmGblCfgInstanceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgInstanceName.setStatus("current")


class _DpmGblCfgMapMode_Type(Integer32):
    """Custom type dpmGblCfgMapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("svcID", 1),
          ("svcIDAndPID", 2))
    )


_DpmGblCfgMapMode_Type.__name__ = "Integer32"
_DpmGblCfgMapMode_Object = MibTableColumn
dpmGblCfgMapMode = _DpmGblCfgMapMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 3),
    _DpmGblCfgMapMode_Type()
)
dpmGblCfgMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgMapMode.setStatus("current")


class _DpmGblCfgDupMethod_Type(Integer32):
    """Custom type dpmGblCfgDupMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packetCopy", 2),
          ("psiRemap", 1))
    )


_DpmGblCfgDupMethod_Type.__name__ = "Integer32"
_DpmGblCfgDupMethod_Object = MibTableColumn
dpmGblCfgDupMethod = _DpmGblCfgDupMethod_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 4),
    _DpmGblCfgDupMethod_Type()
)
dpmGblCfgDupMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgDupMethod.setStatus("current")


class _DpmGblCfgRegenRate_Type(Integer32):
    """Custom type dpmGblCfgRegenRate based on Integer32"""
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
          ("mpegMinimum", 2),
          ("saStandard", 1))
    )


_DpmGblCfgRegenRate_Type.__name__ = "Integer32"
_DpmGblCfgRegenRate_Object = MibTableColumn
dpmGblCfgRegenRate = _DpmGblCfgRegenRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 5),
    _DpmGblCfgRegenRate_Type()
)
dpmGblCfgRegenRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgRegenRate.setStatus("current")


class _DpmGblCfgUnrefContent_Type(Integer32):
    """Custom type dpmGblCfgUnrefContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("modeI", 3),
          ("pass", 2))
    )


_DpmGblCfgUnrefContent_Type.__name__ = "Integer32"
_DpmGblCfgUnrefContent_Object = MibTableColumn
dpmGblCfgUnrefContent = _DpmGblCfgUnrefContent_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 6),
    _DpmGblCfgUnrefContent_Type()
)
dpmGblCfgUnrefContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgUnrefContent.setStatus("current")


class _DpmGblCfgPSIOutput_Type(Integer32):
    """Custom type dpmGblCfgPSIOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctlByTable", 3),
          ("dropAll", 1),
          ("passAll", 2))
    )


_DpmGblCfgPSIOutput_Type.__name__ = "Integer32"
_DpmGblCfgPSIOutput_Object = MibTableColumn
dpmGblCfgPSIOutput = _DpmGblCfgPSIOutput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 7),
    _DpmGblCfgPSIOutput_Type()
)
dpmGblCfgPSIOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIOutput.setStatus("current")


class _DpmGblCfgSVCIDOutput_Type(Integer32):
    """Custom type dpmGblCfgSVCIDOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allChannel", 2),
          ("validChannel", 1))
    )


_DpmGblCfgSVCIDOutput_Type.__name__ = "Integer32"
_DpmGblCfgSVCIDOutput_Object = MibTableColumn
dpmGblCfgSVCIDOutput = _DpmGblCfgSVCIDOutput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 8),
    _DpmGblCfgSVCIDOutput_Type()
)
dpmGblCfgSVCIDOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgSVCIDOutput.setStatus("current")


class _DpmGblCfgPSIPAT_Type(Integer32):
    """Custom type dpmGblCfgPSIPAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2),
          ("regeneration", 3))
    )


_DpmGblCfgPSIPAT_Type.__name__ = "Integer32"
_DpmGblCfgPSIPAT_Object = MibTableColumn
dpmGblCfgPSIPAT = _DpmGblCfgPSIPAT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 9),
    _DpmGblCfgPSIPAT_Type()
)
dpmGblCfgPSIPAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIPAT.setStatus("current")


class _DpmGblCfgPSICAT_Type(Integer32):
    """Custom type dpmGblCfgPSICAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2),
          ("regeneration", 3))
    )


_DpmGblCfgPSICAT_Type.__name__ = "Integer32"
_DpmGblCfgPSICAT_Object = MibTableColumn
dpmGblCfgPSICAT = _DpmGblCfgPSICAT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 10),
    _DpmGblCfgPSICAT_Type()
)
dpmGblCfgPSICAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSICAT.setStatus("current")


class _DpmGblCfgPSIPMT_Type(Integer32):
    """Custom type dpmGblCfgPSIPMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2),
          ("regeneration", 3))
    )


_DpmGblCfgPSIPMT_Type.__name__ = "Integer32"
_DpmGblCfgPSIPMT_Object = MibTableColumn
dpmGblCfgPSIPMT = _DpmGblCfgPSIPMT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 11),
    _DpmGblCfgPSIPMT_Type()
)
dpmGblCfgPSIPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIPMT.setStatus("current")


class _DpmGblCfgPSITSDT_Type(Integer32):
    """Custom type dpmGblCfgPSITSDT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSITSDT_Type.__name__ = "Integer32"
_DpmGblCfgPSITSDT_Object = MibTableColumn
dpmGblCfgPSITSDT = _DpmGblCfgPSITSDT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 12),
    _DpmGblCfgPSITSDT_Type()
)
dpmGblCfgPSITSDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSITSDT.setStatus("current")


class _DpmGblCfgPSINIT_Type(Integer32):
    """Custom type dpmGblCfgPSINIT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2),
          ("regeneration", 3))
    )


_DpmGblCfgPSINIT_Type.__name__ = "Integer32"
_DpmGblCfgPSINIT_Object = MibTableColumn
dpmGblCfgPSINIT = _DpmGblCfgPSINIT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 13),
    _DpmGblCfgPSINIT_Type()
)
dpmGblCfgPSINIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSINIT.setStatus("current")


class _DpmGblCfgPSINITO_Type(Integer32):
    """Custom type dpmGblCfgPSINITO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2),
          ("pwRC", 4))
    )


_DpmGblCfgPSINITO_Type.__name__ = "Integer32"
_DpmGblCfgPSINITO_Object = MibTableColumn
dpmGblCfgPSINITO = _DpmGblCfgPSINITO_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 14),
    _DpmGblCfgPSINITO_Type()
)
dpmGblCfgPSINITO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSINITO.setStatus("current")


class _DpmGblCfgPSISDT_Type(Integer32):
    """Custom type dpmGblCfgPSISDT based on Integer32"""
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
        *(("drop", 1),
          ("pass", 2),
          ("pwRC", 4),
          ("regeneration", 3))
    )


_DpmGblCfgPSISDT_Type.__name__ = "Integer32"
_DpmGblCfgPSISDT_Object = MibTableColumn
dpmGblCfgPSISDT = _DpmGblCfgPSISDT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 15),
    _DpmGblCfgPSISDT_Type()
)
dpmGblCfgPSISDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSISDT.setStatus("current")


class _DpmGblCfgPSISDTO_Type(Integer32):
    """Custom type dpmGblCfgPSISDTO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2),
          ("pwRC", 4))
    )


_DpmGblCfgPSISDTO_Type.__name__ = "Integer32"
_DpmGblCfgPSISDTO_Object = MibTableColumn
dpmGblCfgPSISDTO = _DpmGblCfgPSISDTO_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 16),
    _DpmGblCfgPSISDTO_Type()
)
dpmGblCfgPSISDTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSISDTO.setStatus("current")


class _DpmGblCfgPSIBAT_Type(Integer32):
    """Custom type dpmGblCfgPSIBAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2),
          ("pwRC", 4))
    )


_DpmGblCfgPSIBAT_Type.__name__ = "Integer32"
_DpmGblCfgPSIBAT_Object = MibTableColumn
dpmGblCfgPSIBAT = _DpmGblCfgPSIBAT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 17),
    _DpmGblCfgPSIBAT_Type()
)
dpmGblCfgPSIBAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIBAT.setStatus("current")


class _DpmGblCfgPSIEIT_Type(Integer32):
    """Custom type dpmGblCfgPSIEIT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSIEIT_Type.__name__ = "Integer32"
_DpmGblCfgPSIEIT_Object = MibTableColumn
dpmGblCfgPSIEIT = _DpmGblCfgPSIEIT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 18),
    _DpmGblCfgPSIEIT_Type()
)
dpmGblCfgPSIEIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIEIT.setStatus("current")


class _DpmGblCfgPSITDT_Type(Integer32):
    """Custom type dpmGblCfgPSITDT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSITDT_Type.__name__ = "Integer32"
_DpmGblCfgPSITDT_Object = MibTableColumn
dpmGblCfgPSITDT = _DpmGblCfgPSITDT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 19),
    _DpmGblCfgPSITDT_Type()
)
dpmGblCfgPSITDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSITDT.setStatus("current")


class _DpmGblCfgPSIST_Type(Integer32):
    """Custom type dpmGblCfgPSIST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSIST_Type.__name__ = "Integer32"
_DpmGblCfgPSIST_Object = MibTableColumn
dpmGblCfgPSIST = _DpmGblCfgPSIST_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 20),
    _DpmGblCfgPSIST_Type()
)
dpmGblCfgPSIST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIST.setStatus("current")


class _DpmGblCfgPSIRST_Type(Integer32):
    """Custom type dpmGblCfgPSIRST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSIRST_Type.__name__ = "Integer32"
_DpmGblCfgPSIRST_Object = MibTableColumn
dpmGblCfgPSIRST = _DpmGblCfgPSIRST_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 21),
    _DpmGblCfgPSIRST_Type()
)
dpmGblCfgPSIRST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIRST.setStatus("current")


class _DpmGblCfgPSITOT_Type(Integer32):
    """Custom type dpmGblCfgPSITOT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSITOT_Type.__name__ = "Integer32"
_DpmGblCfgPSITOT_Object = MibTableColumn
dpmGblCfgPSITOT = _DpmGblCfgPSITOT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 22),
    _DpmGblCfgPSITOT_Type()
)
dpmGblCfgPSITOT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSITOT.setStatus("current")


class _DpmGblCfgPSIDIT_Type(Integer32):
    """Custom type dpmGblCfgPSIDIT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSIDIT_Type.__name__ = "Integer32"
_DpmGblCfgPSIDIT_Object = MibTableColumn
dpmGblCfgPSIDIT = _DpmGblCfgPSIDIT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 23),
    _DpmGblCfgPSIDIT_Type()
)
dpmGblCfgPSIDIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIDIT.setStatus("current")


class _DpmGblCfgPSISIT_Type(Integer32):
    """Custom type dpmGblCfgPSISIT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSISIT_Type.__name__ = "Integer32"
_DpmGblCfgPSISIT_Object = MibTableColumn
dpmGblCfgPSISIT = _DpmGblCfgPSISIT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 24),
    _DpmGblCfgPSISIT_Type()
)
dpmGblCfgPSISIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSISIT.setStatus("current")


class _DpmGblCfgPSIECM_Type(Integer32):
    """Custom type dpmGblCfgPSIECM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSIECM_Type.__name__ = "Integer32"
_DpmGblCfgPSIECM_Object = MibTableColumn
dpmGblCfgPSIECM = _DpmGblCfgPSIECM_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 25),
    _DpmGblCfgPSIECM_Type()
)
dpmGblCfgPSIECM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIECM.setStatus("current")


class _DpmGblCfgPSIEMM_Type(Integer32):
    """Custom type dpmGblCfgPSIEMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSIEMM_Type.__name__ = "Integer32"
_DpmGblCfgPSIEMM_Object = MibTableColumn
dpmGblCfgPSIEMM = _DpmGblCfgPSIEMM_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 26),
    _DpmGblCfgPSIEMM_Type()
)
dpmGblCfgPSIEMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIEMM.setStatus("current")


class _DpmGblCfgPSIDRT_Type(Integer32):
    """Custom type dpmGblCfgPSIDRT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSIDRT_Type.__name__ = "Integer32"
_DpmGblCfgPSIDRT_Object = MibTableColumn
dpmGblCfgPSIDRT = _DpmGblCfgPSIDRT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 27),
    _DpmGblCfgPSIDRT_Type()
)
dpmGblCfgPSIDRT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSIDRT.setStatus("current")


class _DpmGblCfgPSICDT_Type(Integer32):
    """Custom type dpmGblCfgPSICDT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_DpmGblCfgPSICDT_Type.__name__ = "Integer32"
_DpmGblCfgPSICDT_Object = MibTableColumn
dpmGblCfgPSICDT = _DpmGblCfgPSICDT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 28),
    _DpmGblCfgPSICDT_Type()
)
dpmGblCfgPSICDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPSICDT.setStatus("current")


class _DpmGblCfgPATPMTOffset_Type(Integer32):
    """Custom type dpmGblCfgPATPMTOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_DpmGblCfgPATPMTOffset_Type.__name__ = "Integer32"
_DpmGblCfgPATPMTOffset_Object = MibTableColumn
dpmGblCfgPATPMTOffset = _DpmGblCfgPATPMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 29),
    _DpmGblCfgPATPMTOffset_Type()
)
dpmGblCfgPATPMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgPATPMTOffset.setStatus("current")


class _DpmGblCfgNITOffset_Type(Integer32):
    """Custom type dpmGblCfgNITOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_DpmGblCfgNITOffset_Type.__name__ = "Integer32"
_DpmGblCfgNITOffset_Object = MibTableColumn
dpmGblCfgNITOffset = _DpmGblCfgNITOffset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 30),
    _DpmGblCfgNITOffset_Type()
)
dpmGblCfgNITOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmGblCfgNITOffset.setStatus("current")
_DpmPeMappingTable_Object = MibTable
dpmPeMappingTable = _DpmPeMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2)
)
if mibBuilder.loadTexts:
    dpmPeMappingTable.setStatus("current")
_DpmPeMappingEntry_Object = MibTableRow
dpmPeMappingEntry = _DpmPeMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1)
)
dpmPeMappingEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DPM-MIB", "dpmPeMappingInstanceID"),
    (0, "CISCO-DMN-DSG-DPM-MIB", "dpmPeMappingPEID"),
)
if mibBuilder.loadTexts:
    dpmPeMappingEntry.setStatus("current")


class _DpmPeMappingInstanceID_Type(Integer32):
    """Custom type dpmPeMappingInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DpmPeMappingInstanceID_Type.__name__ = "Integer32"
_DpmPeMappingInstanceID_Object = MibTableColumn
dpmPeMappingInstanceID = _DpmPeMappingInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 1),
    _DpmPeMappingInstanceID_Type()
)
dpmPeMappingInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmPeMappingInstanceID.setStatus("current")


class _DpmPeMappingPEID_Type(Integer32):
    """Custom type dpmPeMappingPEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DpmPeMappingPEID_Type.__name__ = "Integer32"
_DpmPeMappingPEID_Object = MibTableColumn
dpmPeMappingPEID = _DpmPeMappingPEID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 2),
    _DpmPeMappingPEID_Type()
)
dpmPeMappingPEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmPeMappingPEID.setStatus("current")


class _DpmPeMappingAction_Type(Integer32):
    """Custom type dpmPeMappingAction based on Integer32"""
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
        *(("drop", 1),
          ("map", 3),
          ("pass", 2),
          ("xcode", 4))
    )


_DpmPeMappingAction_Type.__name__ = "Integer32"
_DpmPeMappingAction_Object = MibTableColumn
dpmPeMappingAction = _DpmPeMappingAction_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 3),
    _DpmPeMappingAction_Type()
)
dpmPeMappingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPeMappingAction.setStatus("current")


class _DpmPeMappingPMTPID_Type(Integer32):
    """Custom type dpmPeMappingPMTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_DpmPeMappingPMTPID_Type.__name__ = "Integer32"
_DpmPeMappingPMTPID_Object = MibTableColumn
dpmPeMappingPMTPID = _DpmPeMappingPMTPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 4),
    _DpmPeMappingPMTPID_Type()
)
dpmPeMappingPMTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPeMappingPMTPID.setStatus("current")


class _DpmPeMappingOpChannel_Type(Integer32):
    """Custom type dpmPeMappingOpChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpmPeMappingOpChannel_Type.__name__ = "Integer32"
_DpmPeMappingOpChannel_Object = MibTableColumn
dpmPeMappingOpChannel = _DpmPeMappingOpChannel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 5),
    _DpmPeMappingOpChannel_Type()
)
dpmPeMappingOpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPeMappingOpChannel.setStatus("current")
_DpmPIDMapTable_Object = MibTable
dpmPIDMapTable = _DpmPIDMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3)
)
if mibBuilder.loadTexts:
    dpmPIDMapTable.setStatus("current")
_DpmPIDMapEntry_Object = MibTableRow
dpmPIDMapEntry = _DpmPIDMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1)
)
dpmPIDMapEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DPM-MIB", "dpmPIDMapIndex"),
)
if mibBuilder.loadTexts:
    dpmPIDMapEntry.setStatus("current")


class _DpmPIDMapIndex_Type(Integer32):
    """Custom type dpmPIDMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_DpmPIDMapIndex_Type.__name__ = "Integer32"
_DpmPIDMapIndex_Object = MibTableColumn
dpmPIDMapIndex = _DpmPIDMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 1),
    _DpmPIDMapIndex_Type()
)
dpmPIDMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmPIDMapIndex.setStatus("current")


class _DpmPIDMapInstanceID_Type(Integer32):
    """Custom type dpmPIDMapInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DpmPIDMapInstanceID_Type.__name__ = "Integer32"
_DpmPIDMapInstanceID_Object = MibTableColumn
dpmPIDMapInstanceID = _DpmPIDMapInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 2),
    _DpmPIDMapInstanceID_Type()
)
dpmPIDMapInstanceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapInstanceID.setStatus("current")


class _DpmPIDMapPEID_Type(Integer32):
    """Custom type dpmPIDMapPEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DpmPIDMapPEID_Type.__name__ = "Integer32"
_DpmPIDMapPEID_Object = MibTableColumn
dpmPIDMapPEID = _DpmPIDMapPEID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 3),
    _DpmPIDMapPEID_Type()
)
dpmPIDMapPEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapPEID.setStatus("current")


class _DpmPIDMapRow_Type(Integer32):
    """Custom type dpmPIDMapRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DpmPIDMapRow_Type.__name__ = "Integer32"
_DpmPIDMapRow_Object = MibTableColumn
dpmPIDMapRow = _DpmPIDMapRow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 4),
    _DpmPIDMapRow_Type()
)
dpmPIDMapRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapRow.setStatus("current")


class _DpmPIDMapStreamType_Type(Integer32):
    """Custom type dpmPIDMapStreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DpmPIDMapStreamType_Type.__name__ = "Integer32"
_DpmPIDMapStreamType_Object = MibTableColumn
dpmPIDMapStreamType = _DpmPIDMapStreamType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 5),
    _DpmPIDMapStreamType_Type()
)
dpmPIDMapStreamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapStreamType.setStatus("current")


class _DpmPIDMapStreamCategory_Type(Integer32):
    """Custom type dpmPIDMapStreamCategory based on Integer32"""
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
        *(("aud", 4),
          ("cdt", 12),
          ("data", 10),
          ("dpi", 7),
          ("etv", 13),
          ("invl", 1),
          ("lsdt", 11),
          ("mpe", 8),
          ("pcr", 2),
          ("subt", 5),
          ("ttx", 9),
          ("ukn", 14),
          ("vbi", 6),
          ("vid", 3))
    )


_DpmPIDMapStreamCategory_Type.__name__ = "Integer32"
_DpmPIDMapStreamCategory_Object = MibTableColumn
dpmPIDMapStreamCategory = _DpmPIDMapStreamCategory_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 6),
    _DpmPIDMapStreamCategory_Type()
)
dpmPIDMapStreamCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapStreamCategory.setStatus("current")


class _DpmPIDMapStreamInstance_Type(Integer32):
    """Custom type dpmPIDMapStreamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DpmPIDMapStreamInstance_Type.__name__ = "Integer32"
_DpmPIDMapStreamInstance_Object = MibTableColumn
dpmPIDMapStreamInstance = _DpmPIDMapStreamInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 7),
    _DpmPIDMapStreamInstance_Type()
)
dpmPIDMapStreamInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapStreamInstance.setStatus("current")


class _DpmPIDMapAction_Type(Integer32):
    """Custom type dpmPIDMapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("map", 3))
    )


_DpmPIDMapAction_Type.__name__ = "Integer32"
_DpmPIDMapAction_Object = MibTableColumn
dpmPIDMapAction = _DpmPIDMapAction_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 8),
    _DpmPIDMapAction_Type()
)
dpmPIDMapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapAction.setStatus("current")


class _DpmPIDMapOutputPID_Type(Integer32):
    """Custom type dpmPIDMapOutputPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_DpmPIDMapOutputPID_Type.__name__ = "Integer32"
_DpmPIDMapOutputPID_Object = MibTableColumn
dpmPIDMapOutputPID = _DpmPIDMapOutputPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 9),
    _DpmPIDMapOutputPID_Type()
)
dpmPIDMapOutputPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapOutputPID.setStatus("current")
_DpmPIDMapInuse_Type = RowStatus
_DpmPIDMapInuse_Object = MibTableColumn
dpmPIDMapInuse = _DpmPIDMapInuse_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 10),
    _DpmPIDMapInuse_Type()
)
dpmPIDMapInuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpmPIDMapInuse.setStatus("current")
_DpmAlignedPMTTable_Object = MibTable
dpmAlignedPMTTable = _DpmAlignedPMTTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4)
)
if mibBuilder.loadTexts:
    dpmAlignedPMTTable.setStatus("current")
_DpmAlignedPMTEntry_Object = MibTableRow
dpmAlignedPMTEntry = _DpmAlignedPMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1)
)
dpmAlignedPMTEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DPM-MIB", "dpmAlignedPMTInstanceID"),
    (0, "CISCO-DMN-DSG-DPM-MIB", "dpmAlignedPMTPEID"),
    (0, "CISCO-DMN-DSG-DPM-MIB", "dpmAlignedPMTRow"),
)
if mibBuilder.loadTexts:
    dpmAlignedPMTEntry.setStatus("current")


class _DpmAlignedPMTInstanceID_Type(Integer32):
    """Custom type dpmAlignedPMTInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DpmAlignedPMTInstanceID_Type.__name__ = "Integer32"
_DpmAlignedPMTInstanceID_Object = MibTableColumn
dpmAlignedPMTInstanceID = _DpmAlignedPMTInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 1),
    _DpmAlignedPMTInstanceID_Type()
)
dpmAlignedPMTInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmAlignedPMTInstanceID.setStatus("current")


class _DpmAlignedPMTPEID_Type(Integer32):
    """Custom type dpmAlignedPMTPEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DpmAlignedPMTPEID_Type.__name__ = "Integer32"
_DpmAlignedPMTPEID_Object = MibTableColumn
dpmAlignedPMTPEID = _DpmAlignedPMTPEID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 2),
    _DpmAlignedPMTPEID_Type()
)
dpmAlignedPMTPEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmAlignedPMTPEID.setStatus("current")


class _DpmAlignedPMTRow_Type(Integer32):
    """Custom type dpmAlignedPMTRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DpmAlignedPMTRow_Type.__name__ = "Integer32"
_DpmAlignedPMTRow_Object = MibTableColumn
dpmAlignedPMTRow = _DpmAlignedPMTRow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 3),
    _DpmAlignedPMTRow_Type()
)
dpmAlignedPMTRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmAlignedPMTRow.setStatus("current")


class _DpmAlignedPMTStreamTypeTxt_Type(DisplayString):
    """Custom type dpmAlignedPMTStreamTypeTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DpmAlignedPMTStreamTypeTxt_Type.__name__ = "DisplayString"
_DpmAlignedPMTStreamTypeTxt_Object = MibTableColumn
dpmAlignedPMTStreamTypeTxt = _DpmAlignedPMTStreamTypeTxt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 4),
    _DpmAlignedPMTStreamTypeTxt_Type()
)
dpmAlignedPMTStreamTypeTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmAlignedPMTStreamTypeTxt.setStatus("current")


class _DpmAlignedPMTInputPID_Type(Integer32):
    """Custom type dpmAlignedPMTInputPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_DpmAlignedPMTInputPID_Type.__name__ = "Integer32"
_DpmAlignedPMTInputPID_Object = MibTableColumn
dpmAlignedPMTInputPID = _DpmAlignedPMTInputPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 5),
    _DpmAlignedPMTInputPID_Type()
)
dpmAlignedPMTInputPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpmAlignedPMTInputPID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-DPM-MIB",
    **{"ciscoDSGDPM": ciscoDSGDPM,
       "dpmInfo": dpmInfo,
       "dpmRegenerate": dpmRegenerate,
       "dpmTable": dpmTable,
       "dpmGblCfgTable": dpmGblCfgTable,
       "dpmGblCfgEntry": dpmGblCfgEntry,
       "dpmGblCfgInstanceID": dpmGblCfgInstanceID,
       "dpmGblCfgInstanceName": dpmGblCfgInstanceName,
       "dpmGblCfgMapMode": dpmGblCfgMapMode,
       "dpmGblCfgDupMethod": dpmGblCfgDupMethod,
       "dpmGblCfgRegenRate": dpmGblCfgRegenRate,
       "dpmGblCfgUnrefContent": dpmGblCfgUnrefContent,
       "dpmGblCfgPSIOutput": dpmGblCfgPSIOutput,
       "dpmGblCfgSVCIDOutput": dpmGblCfgSVCIDOutput,
       "dpmGblCfgPSIPAT": dpmGblCfgPSIPAT,
       "dpmGblCfgPSICAT": dpmGblCfgPSICAT,
       "dpmGblCfgPSIPMT": dpmGblCfgPSIPMT,
       "dpmGblCfgPSITSDT": dpmGblCfgPSITSDT,
       "dpmGblCfgPSINIT": dpmGblCfgPSINIT,
       "dpmGblCfgPSINITO": dpmGblCfgPSINITO,
       "dpmGblCfgPSISDT": dpmGblCfgPSISDT,
       "dpmGblCfgPSISDTO": dpmGblCfgPSISDTO,
       "dpmGblCfgPSIBAT": dpmGblCfgPSIBAT,
       "dpmGblCfgPSIEIT": dpmGblCfgPSIEIT,
       "dpmGblCfgPSITDT": dpmGblCfgPSITDT,
       "dpmGblCfgPSIST": dpmGblCfgPSIST,
       "dpmGblCfgPSIRST": dpmGblCfgPSIRST,
       "dpmGblCfgPSITOT": dpmGblCfgPSITOT,
       "dpmGblCfgPSIDIT": dpmGblCfgPSIDIT,
       "dpmGblCfgPSISIT": dpmGblCfgPSISIT,
       "dpmGblCfgPSIECM": dpmGblCfgPSIECM,
       "dpmGblCfgPSIEMM": dpmGblCfgPSIEMM,
       "dpmGblCfgPSIDRT": dpmGblCfgPSIDRT,
       "dpmGblCfgPSICDT": dpmGblCfgPSICDT,
       "dpmGblCfgPATPMTOffset": dpmGblCfgPATPMTOffset,
       "dpmGblCfgNITOffset": dpmGblCfgNITOffset,
       "dpmPeMappingTable": dpmPeMappingTable,
       "dpmPeMappingEntry": dpmPeMappingEntry,
       "dpmPeMappingInstanceID": dpmPeMappingInstanceID,
       "dpmPeMappingPEID": dpmPeMappingPEID,
       "dpmPeMappingAction": dpmPeMappingAction,
       "dpmPeMappingPMTPID": dpmPeMappingPMTPID,
       "dpmPeMappingOpChannel": dpmPeMappingOpChannel,
       "dpmPIDMapTable": dpmPIDMapTable,
       "dpmPIDMapEntry": dpmPIDMapEntry,
       "dpmPIDMapIndex": dpmPIDMapIndex,
       "dpmPIDMapInstanceID": dpmPIDMapInstanceID,
       "dpmPIDMapPEID": dpmPIDMapPEID,
       "dpmPIDMapRow": dpmPIDMapRow,
       "dpmPIDMapStreamType": dpmPIDMapStreamType,
       "dpmPIDMapStreamCategory": dpmPIDMapStreamCategory,
       "dpmPIDMapStreamInstance": dpmPIDMapStreamInstance,
       "dpmPIDMapAction": dpmPIDMapAction,
       "dpmPIDMapOutputPID": dpmPIDMapOutputPID,
       "dpmPIDMapInuse": dpmPIDMapInuse,
       "dpmAlignedPMTTable": dpmAlignedPMTTable,
       "dpmAlignedPMTEntry": dpmAlignedPMTEntry,
       "dpmAlignedPMTInstanceID": dpmAlignedPMTInstanceID,
       "dpmAlignedPMTPEID": dpmAlignedPMTPEID,
       "dpmAlignedPMTRow": dpmAlignedPMTRow,
       "dpmAlignedPMTStreamTypeTxt": dpmAlignedPMTStreamTypeTxt,
       "dpmAlignedPMTInputPID": dpmAlignedPMTInputPID}
)
