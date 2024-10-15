# SNMP MIB module (BayNetworks-AHB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BayNetworks-AHB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:17 2024
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

(wfAtmHalfBridgeGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAtmHalfBridgeGroup")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAhb_ObjectIdentity = ObjectIdentity
wfAhb = _WfAhb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1)
)


class _WfAhbDelete_Type(Integer32):
    """Custom type wfAhbDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAhbDelete_Type.__name__ = "Integer32"
_WfAhbDelete_Object = MibScalar
wfAhbDelete = _WfAhbDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 1),
    _WfAhbDelete_Type()
)
wfAhbDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbDelete.setStatus("mandatory")


class _WfAhbDisable_Type(Integer32):
    """Custom type wfAhbDisable based on Integer32"""
    defaultValue = 1

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


_WfAhbDisable_Type.__name__ = "Integer32"
_WfAhbDisable_Object = MibScalar
wfAhbDisable = _WfAhbDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 2),
    _WfAhbDisable_Type()
)
wfAhbDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbDisable.setStatus("mandatory")


class _WfAhbAutoLearnMethod_Type(Integer32):
    """Custom type wfAhbAutoLearnMethod based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("none", 1),
          ("secure", 3),
          ("unsecure", 2))
    )


_WfAhbAutoLearnMethod_Type.__name__ = "Integer32"
_WfAhbAutoLearnMethod_Object = MibScalar
wfAhbAutoLearnMethod = _WfAhbAutoLearnMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 3),
    _WfAhbAutoLearnMethod_Type()
)
wfAhbAutoLearnMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbAutoLearnMethod.setStatus("mandatory")


class _WfAhbInitFile_Type(DisplayString):
    """Custom type wfAhbInitFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_WfAhbInitFile_Type.__name__ = "DisplayString"
_WfAhbInitFile_Object = MibScalar
wfAhbInitFile = _WfAhbInitFile_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 4),
    _WfAhbInitFile_Type()
)
wfAhbInitFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbInitFile.setStatus("mandatory")


class _WfAhbAltInitFile_Type(DisplayString):
    """Custom type wfAhbAltInitFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_WfAhbAltInitFile_Type.__name__ = "DisplayString"
_WfAhbAltInitFile_Object = MibScalar
wfAhbAltInitFile = _WfAhbAltInitFile_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 5),
    _WfAhbAltInitFile_Type()
)
wfAhbAltInitFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbAltInitFile.setStatus("mandatory")


class _WfAhbDebugLevel_Type(Integer32):
    """Custom type wfAhbDebugLevel based on Integer32"""
    defaultValue = 0


_WfAhbDebugLevel_Object = MibScalar
wfAhbDebugLevel = _WfAhbDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 6),
    _WfAhbDebugLevel_Type()
)
wfAhbDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbDebugLevel.setStatus("mandatory")


class _WfAhbInboundFiltDisable_Type(Integer32):
    """Custom type wfAhbInboundFiltDisable based on Integer32"""
    defaultValue = 2

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


_WfAhbInboundFiltDisable_Type.__name__ = "Integer32"
_WfAhbInboundFiltDisable_Object = MibScalar
wfAhbInboundFiltDisable = _WfAhbInboundFiltDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 7),
    _WfAhbInboundFiltDisable_Type()
)
wfAhbInboundFiltDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbInboundFiltDisable.setStatus("mandatory")


class _WfAhbReset_Type(Integer32):
    """Custom type wfAhbReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 1),
          ("reset", 2))
    )


_WfAhbReset_Type.__name__ = "Integer32"
_WfAhbReset_Object = MibScalar
wfAhbReset = _WfAhbReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 8),
    _WfAhbReset_Type()
)
wfAhbReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbReset.setStatus("mandatory")
_WfAhbStatNumNets_Type = Gauge32
_WfAhbStatNumNets_Object = MibScalar
wfAhbStatNumNets = _WfAhbStatNumNets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 9),
    _WfAhbStatNumNets_Type()
)
wfAhbStatNumNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatNumNets.setStatus("mandatory")
_WfAhbStatNumHosts_Type = Gauge32
_WfAhbStatNumHosts_Object = MibScalar
wfAhbStatNumHosts = _WfAhbStatNumHosts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 10),
    _WfAhbStatNumHosts_Type()
)
wfAhbStatNumHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatNumHosts.setStatus("mandatory")
_WfAhbStatTotOutPkts_Type = Counter32
_WfAhbStatTotOutPkts_Object = MibScalar
wfAhbStatTotOutPkts = _WfAhbStatTotOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 11),
    _WfAhbStatTotOutPkts_Type()
)
wfAhbStatTotOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatTotOutPkts.setStatus("mandatory")
_WfAhbStatFwdOutPkts_Type = Counter32
_WfAhbStatFwdOutPkts_Object = MibScalar
wfAhbStatFwdOutPkts = _WfAhbStatFwdOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 12),
    _WfAhbStatFwdOutPkts_Type()
)
wfAhbStatFwdOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatFwdOutPkts.setStatus("mandatory")
_WfAhbStatDropUnkPkts_Type = Counter32
_WfAhbStatDropUnkPkts_Object = MibScalar
wfAhbStatDropUnkPkts = _WfAhbStatDropUnkPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 13),
    _WfAhbStatDropUnkPkts_Type()
)
wfAhbStatDropUnkPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatDropUnkPkts.setStatus("mandatory")
_WfAhbStatTotInPkts_Type = Counter32
_WfAhbStatTotInPkts_Object = MibScalar
wfAhbStatTotInPkts = _WfAhbStatTotInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 14),
    _WfAhbStatTotInPkts_Type()
)
wfAhbStatTotInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatTotInPkts.setStatus("mandatory")
_WfAhbStatFwdInPkts_Type = Counter32
_WfAhbStatFwdInPkts_Object = MibScalar
wfAhbStatFwdInPkts = _WfAhbStatFwdInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 15),
    _WfAhbStatFwdInPkts_Type()
)
wfAhbStatFwdInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatFwdInPkts.setStatus("mandatory")
_WfAhbStatNumHostCopies_Type = Counter32
_WfAhbStatNumHostCopies_Object = MibScalar
wfAhbStatNumHostCopies = _WfAhbStatNumHostCopies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 16),
    _WfAhbStatNumHostCopies_Type()
)
wfAhbStatNumHostCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbStatNumHostCopies.setStatus("mandatory")


class _WfAhbPolicyDisable_Type(Integer32):
    """Custom type wfAhbPolicyDisable based on Integer32"""
    defaultValue = 2

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


_WfAhbPolicyDisable_Type.__name__ = "Integer32"
_WfAhbPolicyDisable_Object = MibScalar
wfAhbPolicyDisable = _WfAhbPolicyDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 17),
    _WfAhbPolicyDisable_Type()
)
wfAhbPolicyDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyDisable.setStatus("mandatory")


class _WfAhbBaseStatus_Type(Integer32):
    """Custom type wfAhbBaseStatus based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfAhbBaseStatus_Type.__name__ = "Integer32"
_WfAhbBaseStatus_Object = MibScalar
wfAhbBaseStatus = _WfAhbBaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 1, 18),
    _WfAhbBaseStatus_Type()
)
wfAhbBaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbBaseStatus.setStatus("mandatory")
_WfAhbCctTable_Object = MibTable
wfAhbCctTable = _WfAhbCctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2)
)
if mibBuilder.loadTexts:
    wfAhbCctTable.setStatus("mandatory")
_WfAhbCctEntry_Object = MibTableRow
wfAhbCctEntry = _WfAhbCctEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1)
)
wfAhbCctEntry.setIndexNames(
    (0, "BayNetworks-AHB-MIB", "wfAhbCctNum"),
)
if mibBuilder.loadTexts:
    wfAhbCctEntry.setStatus("mandatory")


class _WfAhbCctDelete_Type(Integer32):
    """Custom type wfAhbCctDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAhbCctDelete_Type.__name__ = "Integer32"
_WfAhbCctDelete_Object = MibTableColumn
wfAhbCctDelete = _WfAhbCctDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 1),
    _WfAhbCctDelete_Type()
)
wfAhbCctDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbCctDelete.setStatus("mandatory")


class _WfAhbCctDisable_Type(Integer32):
    """Custom type wfAhbCctDisable based on Integer32"""
    defaultValue = 1

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


_WfAhbCctDisable_Type.__name__ = "Integer32"
_WfAhbCctDisable_Object = MibTableColumn
wfAhbCctDisable = _WfAhbCctDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 2),
    _WfAhbCctDisable_Type()
)
wfAhbCctDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbCctDisable.setStatus("mandatory")
_WfAhbCctNum_Type = Integer32
_WfAhbCctNum_Object = MibTableColumn
wfAhbCctNum = _WfAhbCctNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 3),
    _WfAhbCctNum_Type()
)
wfAhbCctNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbCctNum.setStatus("mandatory")
_WfAhbCctDefSubNetMask_Type = IpAddress
_WfAhbCctDefSubNetMask_Object = MibTableColumn
wfAhbCctDefSubNetMask = _WfAhbCctDefSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 4),
    _WfAhbCctDefSubNetMask_Type()
)
wfAhbCctDefSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbCctDefSubNetMask.setStatus("mandatory")


class _WfAhbCctProxyArpDisable_Type(Integer32):
    """Custom type wfAhbCctProxyArpDisable based on Integer32"""
    defaultValue = 1

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


_WfAhbCctProxyArpDisable_Type.__name__ = "Integer32"
_WfAhbCctProxyArpDisable_Object = MibTableColumn
wfAhbCctProxyArpDisable = _WfAhbCctProxyArpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 5),
    _WfAhbCctProxyArpDisable_Type()
)
wfAhbCctProxyArpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbCctProxyArpDisable.setStatus("mandatory")


class _WfAhbCctMaxIdleTime_Type(Integer32):
    """Custom type wfAhbCctMaxIdleTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("default", 3600),
          ("minimum", 5))
    )


_WfAhbCctMaxIdleTime_Type.__name__ = "Integer32"
_WfAhbCctMaxIdleTime_Object = MibTableColumn
wfAhbCctMaxIdleTime = _WfAhbCctMaxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 6),
    _WfAhbCctMaxIdleTime_Type()
)
wfAhbCctMaxIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbCctMaxIdleTime.setStatus("mandatory")


class _WfAhbCctStatus_Type(Integer32):
    """Custom type wfAhbCctStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfAhbCctStatus_Type.__name__ = "Integer32"
_WfAhbCctStatus_Object = MibTableColumn
wfAhbCctStatus = _WfAhbCctStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 7),
    _WfAhbCctStatus_Type()
)
wfAhbCctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbCctStatus.setStatus("mandatory")
_WfAhbCctTxPkts_Type = Counter32
_WfAhbCctTxPkts_Object = MibTableColumn
wfAhbCctTxPkts = _WfAhbCctTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 8),
    _WfAhbCctTxPkts_Type()
)
wfAhbCctTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbCctTxPkts.setStatus("mandatory")
_WfAhbCctTxDrop_Type = Counter32
_WfAhbCctTxDrop_Object = MibTableColumn
wfAhbCctTxDrop = _WfAhbCctTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 9),
    _WfAhbCctTxDrop_Type()
)
wfAhbCctTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbCctTxDrop.setStatus("mandatory")
_WfAhbCctRxPkts_Type = Counter32
_WfAhbCctRxPkts_Object = MibTableColumn
wfAhbCctRxPkts = _WfAhbCctRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 10),
    _WfAhbCctRxPkts_Type()
)
wfAhbCctRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbCctRxPkts.setStatus("mandatory")
_WfAhbCctRxDrop_Type = Counter32
_WfAhbCctRxDrop_Object = MibTableColumn
wfAhbCctRxDrop = _WfAhbCctRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 2, 1, 11),
    _WfAhbCctRxDrop_Type()
)
wfAhbCctRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbCctRxDrop.setStatus("mandatory")
_WfAhbHostTable_Object = MibTable
wfAhbHostTable = _WfAhbHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3)
)
if mibBuilder.loadTexts:
    wfAhbHostTable.setStatus("mandatory")
_WfAhbHostEntry_Object = MibTableRow
wfAhbHostEntry = _WfAhbHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1)
)
wfAhbHostEntry.setIndexNames(
    (0, "BayNetworks-AHB-MIB", "wfAhbHostSlot"),
    (0, "BayNetworks-AHB-MIB", "wfAhbHostIpAddress"),
)
if mibBuilder.loadTexts:
    wfAhbHostEntry.setStatus("mandatory")


class _WfAhbHostDelete_Type(Integer32):
    """Custom type wfAhbHostDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAhbHostDelete_Type.__name__ = "Integer32"
_WfAhbHostDelete_Object = MibTableColumn
wfAhbHostDelete = _WfAhbHostDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 1),
    _WfAhbHostDelete_Type()
)
wfAhbHostDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostDelete.setStatus("mandatory")
_WfAhbHostSlot_Type = Integer32
_WfAhbHostSlot_Object = MibTableColumn
wfAhbHostSlot = _WfAhbHostSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 2),
    _WfAhbHostSlot_Type()
)
wfAhbHostSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbHostSlot.setStatus("mandatory")
_WfAhbHostSeqNum_Type = Integer32
_WfAhbHostSeqNum_Object = MibTableColumn
wfAhbHostSeqNum = _WfAhbHostSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 3),
    _WfAhbHostSeqNum_Type()
)
wfAhbHostSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostSeqNum.setStatus("mandatory")
_WfAhbHostIpAddress_Type = IpAddress
_WfAhbHostIpAddress_Object = MibTableColumn
wfAhbHostIpAddress = _WfAhbHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 4),
    _WfAhbHostIpAddress_Type()
)
wfAhbHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbHostIpAddress.setStatus("mandatory")


class _WfAhbHostSubNetMask_Type(IpAddress):
    """Custom type wfAhbHostSubNetMask based on IpAddress"""
    defaultValue = 0


_WfAhbHostSubNetMask_Object = MibTableColumn
wfAhbHostSubNetMask = _WfAhbHostSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 5),
    _WfAhbHostSubNetMask_Type()
)
wfAhbHostSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostSubNetMask.setStatus("mandatory")
_WfAhbHostCct_Type = Integer32
_WfAhbHostCct_Object = MibTableColumn
wfAhbHostCct = _WfAhbHostCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 6),
    _WfAhbHostCct_Type()
)
wfAhbHostCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostCct.setStatus("mandatory")


class _WfAhbHostVcid_Type(Integer32):
    """Custom type wfAhbHostVcid based on Integer32"""
    defaultValue = 0


_WfAhbHostVcid_Object = MibTableColumn
wfAhbHostVcid = _WfAhbHostVcid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 7),
    _WfAhbHostVcid_Type()
)
wfAhbHostVcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostVcid.setStatus("mandatory")


class _WfAhbHostBridgeHdr_Type(DisplayString):
    """Custom type wfAhbHostBridgeHdr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_WfAhbHostBridgeHdr_Type.__name__ = "DisplayString"
_WfAhbHostBridgeHdr_Object = MibTableColumn
wfAhbHostBridgeHdr = _WfAhbHostBridgeHdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 8),
    _WfAhbHostBridgeHdr_Type()
)
wfAhbHostBridgeHdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostBridgeHdr.setStatus("mandatory")


class _WfAhbHostFlags_Type(Integer32):
    """Custom type wfAhbHostFlags based on Integer32"""
    defaultValue = 0


_WfAhbHostFlags_Object = MibTableColumn
wfAhbHostFlags = _WfAhbHostFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 9),
    _WfAhbHostFlags_Type()
)
wfAhbHostFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostFlags.setStatus("mandatory")
_WfAhbHostTxPkts_Type = Counter32
_WfAhbHostTxPkts_Object = MibTableColumn
wfAhbHostTxPkts = _WfAhbHostTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 10),
    _WfAhbHostTxPkts_Type()
)
wfAhbHostTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbHostTxPkts.setStatus("mandatory")
_WfAhbHostRxPkts_Type = Counter32
_WfAhbHostRxPkts_Object = MibTableColumn
wfAhbHostRxPkts = _WfAhbHostRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 11),
    _WfAhbHostRxPkts_Type()
)
wfAhbHostRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbHostRxPkts.setStatus("mandatory")
_WfAhbHostMaxIdleTime_Type = Integer32
_WfAhbHostMaxIdleTime_Object = MibTableColumn
wfAhbHostMaxIdleTime = _WfAhbHostMaxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 12),
    _WfAhbHostMaxIdleTime_Type()
)
wfAhbHostMaxIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbHostMaxIdleTime.setStatus("mandatory")
_WfAhbHostCurIdleTime_Type = Integer32
_WfAhbHostCurIdleTime_Object = MibTableColumn
wfAhbHostCurIdleTime = _WfAhbHostCurIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 3, 1, 13),
    _WfAhbHostCurIdleTime_Type()
)
wfAhbHostCurIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbHostCurIdleTime.setStatus("mandatory")
_WfAhbPolicyTable_Object = MibTable
wfAhbPolicyTable = _WfAhbPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4)
)
if mibBuilder.loadTexts:
    wfAhbPolicyTable.setStatus("mandatory")
_WfAhbPolicyEntry_Object = MibTableRow
wfAhbPolicyEntry = _WfAhbPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1)
)
wfAhbPolicyEntry.setIndexNames(
    (0, "BayNetworks-AHB-MIB", "wfAhbPolicyIpAddress"),
    (0, "BayNetworks-AHB-MIB", "wfAhbPolicySubNetMask"),
)
if mibBuilder.loadTexts:
    wfAhbPolicyEntry.setStatus("mandatory")


class _WfAhbPolicyDelete_Type(Integer32):
    """Custom type wfAhbPolicyDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAhbPolicyDelete_Type.__name__ = "Integer32"
_WfAhbPolicyDelete_Object = MibTableColumn
wfAhbPolicyDelete = _WfAhbPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 1),
    _WfAhbPolicyDelete_Type()
)
wfAhbPolicyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyDelete.setStatus("mandatory")
_WfAhbPolicyIpAddress_Type = IpAddress
_WfAhbPolicyIpAddress_Object = MibTableColumn
wfAhbPolicyIpAddress = _WfAhbPolicyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 2),
    _WfAhbPolicyIpAddress_Type()
)
wfAhbPolicyIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbPolicyIpAddress.setStatus("mandatory")
_WfAhbPolicySubNetMask_Type = IpAddress
_WfAhbPolicySubNetMask_Object = MibTableColumn
wfAhbPolicySubNetMask = _WfAhbPolicySubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 3),
    _WfAhbPolicySubNetMask_Type()
)
wfAhbPolicySubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAhbPolicySubNetMask.setStatus("mandatory")


class _WfAhbPolicyCct_Type(Integer32):
    """Custom type wfAhbPolicyCct based on Integer32"""
    defaultValue = 0


_WfAhbPolicyCct_Object = MibTableColumn
wfAhbPolicyCct = _WfAhbPolicyCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 4),
    _WfAhbPolicyCct_Type()
)
wfAhbPolicyCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyCct.setStatus("mandatory")


class _WfAhbPolicyVPI_Type(Integer32):
    """Custom type wfAhbPolicyVPI based on Integer32"""
    defaultValue = 0


_WfAhbPolicyVPI_Object = MibTableColumn
wfAhbPolicyVPI = _WfAhbPolicyVPI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 5),
    _WfAhbPolicyVPI_Type()
)
wfAhbPolicyVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyVPI.setStatus("mandatory")


class _WfAhbPolicyVCI_Type(Integer32):
    """Custom type wfAhbPolicyVCI based on Integer32"""
    defaultValue = 0


_WfAhbPolicyVCI_Object = MibTableColumn
wfAhbPolicyVCI = _WfAhbPolicyVCI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 6),
    _WfAhbPolicyVCI_Type()
)
wfAhbPolicyVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyVCI.setStatus("mandatory")
_WfAhbPolicyMACAddr_Type = MacAddress
_WfAhbPolicyMACAddr_Object = MibTableColumn
wfAhbPolicyMACAddr = _WfAhbPolicyMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 7),
    _WfAhbPolicyMACAddr_Type()
)
wfAhbPolicyMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyMACAddr.setStatus("mandatory")


class _WfAhbPolicyFlags_Type(Integer32):
    """Custom type wfAhbPolicyFlags based on Integer32"""
    defaultValue = 0


_WfAhbPolicyFlags_Object = MibTableColumn
wfAhbPolicyFlags = _WfAhbPolicyFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 8),
    _WfAhbPolicyFlags_Type()
)
wfAhbPolicyFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyFlags.setStatus("mandatory")


class _WfAhbPolicyPermission_Type(Integer32):
    """Custom type wfAhbPolicyPermission based on Integer32"""
    defaultValue = 1

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
        *(("allow", 1),
          ("disallow", 2),
          ("notused", 4),
          ("static", 3))
    )


_WfAhbPolicyPermission_Type.__name__ = "Integer32"
_WfAhbPolicyPermission_Object = MibTableColumn
wfAhbPolicyPermission = _WfAhbPolicyPermission_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13, 4, 1, 9),
    _WfAhbPolicyPermission_Type()
)
wfAhbPolicyPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAhbPolicyPermission.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BayNetworks-AHB-MIB",
    **{"MacAddress": MacAddress,
       "wfAhb": wfAhb,
       "wfAhbDelete": wfAhbDelete,
       "wfAhbDisable": wfAhbDisable,
       "wfAhbAutoLearnMethod": wfAhbAutoLearnMethod,
       "wfAhbInitFile": wfAhbInitFile,
       "wfAhbAltInitFile": wfAhbAltInitFile,
       "wfAhbDebugLevel": wfAhbDebugLevel,
       "wfAhbInboundFiltDisable": wfAhbInboundFiltDisable,
       "wfAhbReset": wfAhbReset,
       "wfAhbStatNumNets": wfAhbStatNumNets,
       "wfAhbStatNumHosts": wfAhbStatNumHosts,
       "wfAhbStatTotOutPkts": wfAhbStatTotOutPkts,
       "wfAhbStatFwdOutPkts": wfAhbStatFwdOutPkts,
       "wfAhbStatDropUnkPkts": wfAhbStatDropUnkPkts,
       "wfAhbStatTotInPkts": wfAhbStatTotInPkts,
       "wfAhbStatFwdInPkts": wfAhbStatFwdInPkts,
       "wfAhbStatNumHostCopies": wfAhbStatNumHostCopies,
       "wfAhbPolicyDisable": wfAhbPolicyDisable,
       "wfAhbBaseStatus": wfAhbBaseStatus,
       "wfAhbCctTable": wfAhbCctTable,
       "wfAhbCctEntry": wfAhbCctEntry,
       "wfAhbCctDelete": wfAhbCctDelete,
       "wfAhbCctDisable": wfAhbCctDisable,
       "wfAhbCctNum": wfAhbCctNum,
       "wfAhbCctDefSubNetMask": wfAhbCctDefSubNetMask,
       "wfAhbCctProxyArpDisable": wfAhbCctProxyArpDisable,
       "wfAhbCctMaxIdleTime": wfAhbCctMaxIdleTime,
       "wfAhbCctStatus": wfAhbCctStatus,
       "wfAhbCctTxPkts": wfAhbCctTxPkts,
       "wfAhbCctTxDrop": wfAhbCctTxDrop,
       "wfAhbCctRxPkts": wfAhbCctRxPkts,
       "wfAhbCctRxDrop": wfAhbCctRxDrop,
       "wfAhbHostTable": wfAhbHostTable,
       "wfAhbHostEntry": wfAhbHostEntry,
       "wfAhbHostDelete": wfAhbHostDelete,
       "wfAhbHostSlot": wfAhbHostSlot,
       "wfAhbHostSeqNum": wfAhbHostSeqNum,
       "wfAhbHostIpAddress": wfAhbHostIpAddress,
       "wfAhbHostSubNetMask": wfAhbHostSubNetMask,
       "wfAhbHostCct": wfAhbHostCct,
       "wfAhbHostVcid": wfAhbHostVcid,
       "wfAhbHostBridgeHdr": wfAhbHostBridgeHdr,
       "wfAhbHostFlags": wfAhbHostFlags,
       "wfAhbHostTxPkts": wfAhbHostTxPkts,
       "wfAhbHostRxPkts": wfAhbHostRxPkts,
       "wfAhbHostMaxIdleTime": wfAhbHostMaxIdleTime,
       "wfAhbHostCurIdleTime": wfAhbHostCurIdleTime,
       "wfAhbPolicyTable": wfAhbPolicyTable,
       "wfAhbPolicyEntry": wfAhbPolicyEntry,
       "wfAhbPolicyDelete": wfAhbPolicyDelete,
       "wfAhbPolicyIpAddress": wfAhbPolicyIpAddress,
       "wfAhbPolicySubNetMask": wfAhbPolicySubNetMask,
       "wfAhbPolicyCct": wfAhbPolicyCct,
       "wfAhbPolicyVPI": wfAhbPolicyVPI,
       "wfAhbPolicyVCI": wfAhbPolicyVCI,
       "wfAhbPolicyMACAddr": wfAhbPolicyMACAddr,
       "wfAhbPolicyFlags": wfAhbPolicyFlags,
       "wfAhbPolicyPermission": wfAhbPolicyPermission}
)
