# SNMP MIB module (Vsm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Vsm-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:25 2024
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

(dv2,) = mibBuilder.importSymbols(
    "DV2-MIB",
    "dv2")

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



class VciInteger(Integer32):
    """Custom type VciInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class VpiInteger(Integer32):
    """Custom type VpiInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class VsmBundle(Integer32):
    """Custom type VsmBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dv2Vsm_ObjectIdentity = ObjectIdentity
dv2Vsm = _Dv2Vsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47)
)
_VsmCardCfgTable_Object = MibTable
vsmCardCfgTable = _VsmCardCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 1)
)
if mibBuilder.loadTexts:
    vsmCardCfgTable.setStatus("mandatory")
_VsmCardCfgTableEntry_Object = MibTableRow
vsmCardCfgTableEntry = _VsmCardCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 1, 1)
)
vsmCardCfgTableEntry.setIndexNames(
    (0, "Vsm-MIB", "vsmCardCfgIndex"),
)
if mibBuilder.loadTexts:
    vsmCardCfgTableEntry.setStatus("mandatory")


class _VsmCardCfgIndex_Type(Integer32):
    """Custom type vsmCardCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VsmCardCfgIndex_Type.__name__ = "Integer32"
_VsmCardCfgIndex_Object = MibTableColumn
vsmCardCfgIndex = _VsmCardCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 1, 1, 1),
    _VsmCardCfgIndex_Type()
)
vsmCardCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardCfgIndex.setStatus("mandatory")


class _VsmCardCfgBndlTslotStatus_Type(Integer32):
    """Custom type vsmCardCfgBndlTslotStatus based on Integer32"""
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


_VsmCardCfgBndlTslotStatus_Type.__name__ = "Integer32"
_VsmCardCfgBndlTslotStatus_Object = MibTableColumn
vsmCardCfgBndlTslotStatus = _VsmCardCfgBndlTslotStatus_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 1, 1, 2),
    _VsmCardCfgBndlTslotStatus_Type()
)
vsmCardCfgBndlTslotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardCfgBndlTslotStatus.setStatus("mandatory")
_VsmLinkTable_Object = MibTable
vsmLinkTable = _VsmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 2)
)
if mibBuilder.loadTexts:
    vsmLinkTable.setStatus("mandatory")
_VsmLinkEntry_Object = MibTableRow
vsmLinkEntry = _VsmLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 2, 1)
)
vsmLinkEntry.setIndexNames(
    (0, "Vsm-MIB", "vsmLinkLink"),
)
if mibBuilder.loadTexts:
    vsmLinkEntry.setStatus("mandatory")


class _VsmLinkLink_Type(Integer32):
    """Custom type vsmLinkLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VsmLinkLink_Type.__name__ = "Integer32"
_VsmLinkLink_Object = MibTableColumn
vsmLinkLink = _VsmLinkLink_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 2, 1, 1),
    _VsmLinkLink_Type()
)
vsmLinkLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmLinkLink.setStatus("mandatory")


class _VsmLinkEnable_Type(Integer32):
    """Custom type vsmLinkEnable based on Integer32"""
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


_VsmLinkEnable_Type.__name__ = "Integer32"
_VsmLinkEnable_Object = MibTableColumn
vsmLinkEnable = _VsmLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 2, 1, 2),
    _VsmLinkEnable_Type()
)
vsmLinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmLinkEnable.setStatus("mandatory")


class _VsmLinkEnableStat_Type(Integer32):
    """Custom type vsmLinkEnableStat based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 1),
          ("error", 5),
          ("link-not-used", 4),
          ("wait-for-valid-lim", 3),
          ("wait-frame-bit", 8),
          ("wait-lim-framing", 7),
          ("wait-signaling-lim", 6))
    )


_VsmLinkEnableStat_Type.__name__ = "Integer32"
_VsmLinkEnableStat_Object = MibTableColumn
vsmLinkEnableStat = _VsmLinkEnableStat_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 2, 1, 3),
    _VsmLinkEnableStat_Type()
)
vsmLinkEnableStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmLinkEnableStat.setStatus("mandatory")


class _VsmLinkSigType_Type(Integer32):
    """Custom type vsmLinkSigType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("none", 1))
    )


_VsmLinkSigType_Type.__name__ = "Integer32"
_VsmLinkSigType_Object = MibTableColumn
vsmLinkSigType = _VsmLinkSigType_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 2, 1, 4),
    _VsmLinkSigType_Type()
)
vsmLinkSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmLinkSigType.setStatus("mandatory")
_VsmTsCfgTable_Object = MibTable
vsmTsCfgTable = _VsmTsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3)
)
if mibBuilder.loadTexts:
    vsmTsCfgTable.setStatus("mandatory")
_VsmTsCfgTableEntry_Object = MibTableRow
vsmTsCfgTableEntry = _VsmTsCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1)
)
vsmTsCfgTableEntry.setIndexNames(
    (0, "Vsm-MIB", "vsmTsCfgLinkNo"),
    (0, "Vsm-MIB", "vsmTsCfgTsNo"),
)
if mibBuilder.loadTexts:
    vsmTsCfgTableEntry.setStatus("mandatory")


class _VsmTsCfgLinkNo_Type(Integer32):
    """Custom type vsmTsCfgLinkNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VsmTsCfgLinkNo_Type.__name__ = "Integer32"
_VsmTsCfgLinkNo_Object = MibTableColumn
vsmTsCfgLinkNo = _VsmTsCfgLinkNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 1),
    _VsmTsCfgLinkNo_Type()
)
vsmTsCfgLinkNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgLinkNo.setStatus("mandatory")


class _VsmTsCfgTsNo_Type(Integer32):
    """Custom type vsmTsCfgTsNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_VsmTsCfgTsNo_Type.__name__ = "Integer32"
_VsmTsCfgTsNo_Object = MibTableColumn
vsmTsCfgTsNo = _VsmTsCfgTsNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 2),
    _VsmTsCfgTsNo_Type()
)
vsmTsCfgTsNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgTsNo.setStatus("mandatory")


class _VsmTsCfgBundleNo_Type(VsmBundle):
    """Custom type vsmTsCfgBundleNo based on VsmBundle"""
    defaultValue = 1


_VsmTsCfgBundleNo_Object = MibTableColumn
vsmTsCfgBundleNo = _VsmTsCfgBundleNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 3),
    _VsmTsCfgBundleNo_Type()
)
vsmTsCfgBundleNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgBundleNo.setStatus("mandatory")


class _VsmTsCfgAALTyp_Type(Integer32):
    """Custom type vsmTsCfgAALTyp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal2", 2))
    )


_VsmTsCfgAALTyp_Type.__name__ = "Integer32"
_VsmTsCfgAALTyp_Object = MibTableColumn
vsmTsCfgAALTyp = _VsmTsCfgAALTyp_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 4),
    _VsmTsCfgAALTyp_Type()
)
vsmTsCfgAALTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgAALTyp.setStatus("mandatory")


class _VsmTsCfgChanID_Type(Integer32):
    """Custom type vsmTsCfgChanID based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 255),
    )


_VsmTsCfgChanID_Type.__name__ = "Integer32"
_VsmTsCfgChanID_Object = MibTableColumn
vsmTsCfgChanID = _VsmTsCfgChanID_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 5),
    _VsmTsCfgChanID_Type()
)
vsmTsCfgChanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgChanID.setStatus("mandatory")


class _VsmTsCfgCmprssionTyp_Type(Integer32):
    """Custom type vsmTsCfgCmprssionTyp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adpcmG726-32k", 2),
          ("none", 1))
    )


_VsmTsCfgCmprssionTyp_Type.__name__ = "Integer32"
_VsmTsCfgCmprssionTyp_Object = MibTableColumn
vsmTsCfgCmprssionTyp = _VsmTsCfgCmprssionTyp_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 6),
    _VsmTsCfgCmprssionTyp_Type()
)
vsmTsCfgCmprssionTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgCmprssionTyp.setStatus("mandatory")


class _VsmTsCfgFaxMdmHndlng_Type(Integer32):
    """Custom type vsmTsCfgFaxMdmHndlng based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always-compress", 1),
          ("auto-disable", 2))
    )


_VsmTsCfgFaxMdmHndlng_Type.__name__ = "Integer32"
_VsmTsCfgFaxMdmHndlng_Object = MibTableColumn
vsmTsCfgFaxMdmHndlng = _VsmTsCfgFaxMdmHndlng_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 7),
    _VsmTsCfgFaxMdmHndlng_Type()
)
vsmTsCfgFaxMdmHndlng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgFaxMdmHndlng.setStatus("mandatory")


class _VsmTsCfgEchoCancel_Type(Integer32):
    """Custom type vsmTsCfgEchoCancel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-disable", 3),
          ("disable", 2),
          ("enable", 1))
    )


_VsmTsCfgEchoCancel_Type.__name__ = "Integer32"
_VsmTsCfgEchoCancel_Object = MibTableColumn
vsmTsCfgEchoCancel = _VsmTsCfgEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 8),
    _VsmTsCfgEchoCancel_Type()
)
vsmTsCfgEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgEchoCancel.setStatus("mandatory")


class _VsmTsCfgSilenceRmvl_Type(Integer32):
    """Custom type vsmTsCfgSilenceRmvl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-disable", 3),
          ("disable", 2),
          ("enable", 1))
    )


_VsmTsCfgSilenceRmvl_Type.__name__ = "Integer32"
_VsmTsCfgSilenceRmvl_Object = MibTableColumn
vsmTsCfgSilenceRmvl = _VsmTsCfgSilenceRmvl_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 9),
    _VsmTsCfgSilenceRmvl_Type()
)
vsmTsCfgSilenceRmvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgSilenceRmvl.setStatus("mandatory")


class _VsmTsCfgIdleDetect_Type(Integer32):
    """Custom type vsmTsCfgIdleDetect based on Integer32"""
    defaultValue = 1

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


_VsmTsCfgIdleDetect_Type.__name__ = "Integer32"
_VsmTsCfgIdleDetect_Object = MibTableColumn
vsmTsCfgIdleDetect = _VsmTsCfgIdleDetect_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 10),
    _VsmTsCfgIdleDetect_Type()
)
vsmTsCfgIdleDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgIdleDetect.setStatus("mandatory")


class _VsmTsCfgRmtLaw_Type(Integer32):
    """Custom type vsmTsCfgRmtLaw based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("a-law", 2),
          ("auto", 3),
          ("u-law", 1))
    )


_VsmTsCfgRmtLaw_Type.__name__ = "Integer32"
_VsmTsCfgRmtLaw_Object = MibTableColumn
vsmTsCfgRmtLaw = _VsmTsCfgRmtLaw_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 11),
    _VsmTsCfgRmtLaw_Type()
)
vsmTsCfgRmtLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgRmtLaw.setStatus("mandatory")


class _VsmTsCfgSignalTyp_Type(Integer32):
    """Custom type vsmTsCfgSignalTyp based on Integer32"""
    defaultValue = 6

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
        *(("e-and-m", 6),
          ("gs-fxo-fxs", 2),
          ("gs-fxs-fxo", 3),
          ("ls-fxo-fxs", 4),
          ("ls-fxs-fxo", 5),
          ("none", 1),
          ("plar", 8),
          ("ssr2", 7))
    )


_VsmTsCfgSignalTyp_Type.__name__ = "Integer32"
_VsmTsCfgSignalTyp_Object = MibTableColumn
vsmTsCfgSignalTyp = _VsmTsCfgSignalTyp_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 12),
    _VsmTsCfgSignalTyp_Type()
)
vsmTsCfgSignalTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgSignalTyp.setStatus("mandatory")


class _VsmTsCfgSigCndTypNB_Type(Integer32):
    """Custom type vsmTsCfgSigCndTypNB based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("failure-A10B1", 6),
          ("failure-A1B1", 5),
          ("failure-A1B1C1D1", 7),
          ("offhook-A01B01", 3),
          ("onhook-A0B0", 1),
          ("onhook-A0B1", 2))
    )


_VsmTsCfgSigCndTypNB_Type.__name__ = "Integer32"
_VsmTsCfgSigCndTypNB_Object = MibTableColumn
vsmTsCfgSigCndTypNB = _VsmTsCfgSigCndTypNB_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 13),
    _VsmTsCfgSigCndTypNB_Type()
)
vsmTsCfgSigCndTypNB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgSigCndTypNB.setStatus("mandatory")


class _VsmTsCfgSigCndTypATM_Type(Integer32):
    """Custom type vsmTsCfgSigCndTypATM based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("failure-A10B1", 6),
          ("failure-A1B1", 5),
          ("failure-A1B1C1D1", 7),
          ("offhook-A01B01", 3),
          ("onhook-A0B0", 1),
          ("onhook-A0B1", 2))
    )


_VsmTsCfgSigCndTypATM_Type.__name__ = "Integer32"
_VsmTsCfgSigCndTypATM_Object = MibTableColumn
vsmTsCfgSigCndTypATM = _VsmTsCfgSigCndTypATM_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 14),
    _VsmTsCfgSigCndTypATM_Type()
)
vsmTsCfgSigCndTypATM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgSigCndTypATM.setStatus("mandatory")


class _VsmTsCfgDataCndTypNB_Type(Integer32):
    """Custom type vsmTsCfgDataCndTypNB based on Integer32"""
    defaultValue = 2

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aLaw-0V-54", 5),
          ("aLaw-0V-D5", 4),
          ("cir-oos-36", 8),
          ("ctrl-mode-FE", 7),
          ("dacs-trbl-E4", 6),
          ("muLaw-0V-7F", 2),
          ("muLaw-0V-FF", 3),
          ("mux-oos-1A", 9),
          ("none", 1),
          ("user-data-FF", 10))
    )


_VsmTsCfgDataCndTypNB_Type.__name__ = "Integer32"
_VsmTsCfgDataCndTypNB_Object = MibTableColumn
vsmTsCfgDataCndTypNB = _VsmTsCfgDataCndTypNB_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 15),
    _VsmTsCfgDataCndTypNB_Type()
)
vsmTsCfgDataCndTypNB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgDataCndTypNB.setStatus("mandatory")


class _VsmTsCfgDataCndTypATM_Type(Integer32):
    """Custom type vsmTsCfgDataCndTypATM based on Integer32"""
    defaultValue = 2

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aLaw-0V-54", 5),
          ("aLaw-0V-D5", 4),
          ("cir-oos-36", 8),
          ("ctrl-mode-FE", 7),
          ("dacs-trbl-E4", 6),
          ("muLaw-0V-7F", 2),
          ("muLaw-0V-FF", 3),
          ("mux-oos-1A", 9),
          ("none", 1),
          ("user-data-FF", 10))
    )


_VsmTsCfgDataCndTypATM_Type.__name__ = "Integer32"
_VsmTsCfgDataCndTypATM_Object = MibTableColumn
vsmTsCfgDataCndTypATM = _VsmTsCfgDataCndTypATM_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 16),
    _VsmTsCfgDataCndTypATM_Type()
)
vsmTsCfgDataCndTypATM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgDataCndTypATM.setStatus("mandatory")


class _VsmTsCfgMulticast_Type(Integer32):
    """Custom type vsmTsCfgMulticast based on Integer32"""
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


_VsmTsCfgMulticast_Type.__name__ = "Integer32"
_VsmTsCfgMulticast_Object = MibTableColumn
vsmTsCfgMulticast = _VsmTsCfgMulticast_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 17),
    _VsmTsCfgMulticast_Type()
)
vsmTsCfgMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgMulticast.setStatus("mandatory")


class _VsmTsCfgOperStatus_Type(Integer32):
    """Custom type vsmTsCfgOperStatus based on Integer32"""
    defaultValue = 2

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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("aal-mismatch", 5),
          ("aal1-max-TS", 15),
          ("configured", 3),
          ("down", 2),
          ("inv-CID", 7),
          ("inv-CmpTyp", 11),
          ("inv-Lk-no", 9),
          ("inv-MCast", 13),
          ("inv-MCast-BN", 16),
          ("inv-Sil-Det", 10),
          ("inv-cfg", 4),
          ("inv-maxtslot", 14),
          ("no-more-DSPs", 6),
          ("non-CAS-link", 17),
          ("unknown-Lim", 12),
          ("up", 1))
    )


_VsmTsCfgOperStatus_Type.__name__ = "Integer32"
_VsmTsCfgOperStatus_Object = MibTableColumn
vsmTsCfgOperStatus = _VsmTsCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 18),
    _VsmTsCfgOperStatus_Type()
)
vsmTsCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsCfgOperStatus.setStatus("mandatory")


class _VsmTsCfgAdminStatus_Type(Integer32):
    """Custom type vsmTsCfgAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("reconfig", 3),
          ("up", 1))
    )


_VsmTsCfgAdminStatus_Type.__name__ = "Integer32"
_VsmTsCfgAdminStatus_Object = MibTableColumn
vsmTsCfgAdminStatus = _VsmTsCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 19),
    _VsmTsCfgAdminStatus_Type()
)
vsmTsCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgAdminStatus.setStatus("mandatory")


class _VsmTsCfgValidity_Type(Integer32):
    """Custom type vsmTsCfgValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_VsmTsCfgValidity_Type.__name__ = "Integer32"
_VsmTsCfgValidity_Object = MibTableColumn
vsmTsCfgValidity = _VsmTsCfgValidity_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 3, 1, 20),
    _VsmTsCfgValidity_Type()
)
vsmTsCfgValidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsCfgValidity.setStatus("mandatory")
_VsmBundleCfgTable_Object = MibTable
vsmBundleCfgTable = _VsmBundleCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4)
)
if mibBuilder.loadTexts:
    vsmBundleCfgTable.setStatus("mandatory")
_VsmBundleCfgTableEntry_Object = MibTableRow
vsmBundleCfgTableEntry = _VsmBundleCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1)
)
vsmBundleCfgTableEntry.setIndexNames(
    (0, "Vsm-MIB", "vsmBundleCfgNo"),
)
if mibBuilder.loadTexts:
    vsmBundleCfgTableEntry.setStatus("mandatory")
_VsmBundleCfgNo_Type = VsmBundle
_VsmBundleCfgNo_Object = MibTableColumn
vsmBundleCfgNo = _VsmBundleCfgNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 1),
    _VsmBundleCfgNo_Type()
)
vsmBundleCfgNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgNo.setStatus("mandatory")


class _VsmBundleCfgVcVpi_Type(VpiInteger):
    """Custom type vsmBundleCfgVcVpi based on VpiInteger"""
    defaultValue = 1


_VsmBundleCfgVcVpi_Object = MibTableColumn
vsmBundleCfgVcVpi = _VsmBundleCfgVcVpi_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 2),
    _VsmBundleCfgVcVpi_Type()
)
vsmBundleCfgVcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgVcVpi.setStatus("mandatory")


class _VsmBundleCfgVcVci_Type(VciInteger):
    """Custom type vsmBundleCfgVcVci based on VciInteger"""
    defaultValue = 1


_VsmBundleCfgVcVci_Object = MibTableColumn
vsmBundleCfgVcVci = _VsmBundleCfgVcVci_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 3),
    _VsmBundleCfgVcVci_Type()
)
vsmBundleCfgVcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleCfgVcVci.setStatus("mandatory")


class _VsmBundleCfgVcAALTyp_Type(Integer32):
    """Custom type vsmBundleCfgVcAALTyp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal2", 2))
    )


_VsmBundleCfgVcAALTyp_Type.__name__ = "Integer32"
_VsmBundleCfgVcAALTyp_Object = MibTableColumn
vsmBundleCfgVcAALTyp = _VsmBundleCfgVcAALTyp_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 4),
    _VsmBundleCfgVcAALTyp_Type()
)
vsmBundleCfgVcAALTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgVcAALTyp.setStatus("mandatory")


class _VsmBundleCfgMaxTslot_Type(Integer32):
    """Custom type vsmBundleCfgMaxTslot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_VsmBundleCfgMaxTslot_Type.__name__ = "Integer32"
_VsmBundleCfgMaxTslot_Object = MibTableColumn
vsmBundleCfgMaxTslot = _VsmBundleCfgMaxTslot_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 5),
    _VsmBundleCfgMaxTslot_Type()
)
vsmBundleCfgMaxTslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgMaxTslot.setStatus("mandatory")


class _VsmBundleCfgVcCDV_Type(Integer32):
    """Custom type vsmBundleCfgVcCDV based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VsmBundleCfgVcCDV_Type.__name__ = "Integer32"
_VsmBundleCfgVcCDV_Object = MibTableColumn
vsmBundleCfgVcCDV = _VsmBundleCfgVcCDV_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 6),
    _VsmBundleCfgVcCDV_Type()
)
vsmBundleCfgVcCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgVcCDV.setStatus("mandatory")


class _VsmBundleCfgTimerCU_Type(Integer32):
    """Custom type vsmBundleCfgTimerCU based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_VsmBundleCfgTimerCU_Type.__name__ = "Integer32"
_VsmBundleCfgTimerCU_Object = MibTableColumn
vsmBundleCfgTimerCU = _VsmBundleCfgTimerCU_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 7),
    _VsmBundleCfgTimerCU_Type()
)
vsmBundleCfgTimerCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgTimerCU.setStatus("mandatory")


class _VsmBundleCfgCESPartialFill_Type(Integer32):
    """Custom type vsmBundleCfgCESPartialFill based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 47),
    )


_VsmBundleCfgCESPartialFill_Type.__name__ = "Integer32"
_VsmBundleCfgCESPartialFill_Object = MibTableColumn
vsmBundleCfgCESPartialFill = _VsmBundleCfgCESPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 8),
    _VsmBundleCfgCESPartialFill_Type()
)
vsmBundleCfgCESPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgCESPartialFill.setStatus("mandatory")


class _VsmBundleCfgVcTyp_Type(Integer32):
    """Custom type vsmBundleCfgVcTyp based on Integer32"""
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
        *(("pvc", 1),
          ("spvc", 2),
          ("svc", 3))
    )


_VsmBundleCfgVcTyp_Type.__name__ = "Integer32"
_VsmBundleCfgVcTyp_Object = MibTableColumn
vsmBundleCfgVcTyp = _VsmBundleCfgVcTyp_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 9),
    _VsmBundleCfgVcTyp_Type()
)
vsmBundleCfgVcTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgVcTyp.setStatus("mandatory")


class _VsmBundleCfgTrapCfg_Type(Integer32):
    """Custom type vsmBundleCfgTrapCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-trap", 1),
          ("state-change", 2))
    )


_VsmBundleCfgTrapCfg_Type.__name__ = "Integer32"
_VsmBundleCfgTrapCfg_Object = MibTableColumn
vsmBundleCfgTrapCfg = _VsmBundleCfgTrapCfg_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 10),
    _VsmBundleCfgTrapCfg_Type()
)
vsmBundleCfgTrapCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgTrapCfg.setStatus("mandatory")


class _VsmBundleCfgOperStatus_Type(Integer32):
    """Custom type vsmBundleCfgOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("aal-mismatch", 5),
          ("bndl-novc", 9),
          ("configured", 3),
          ("down", 2),
          ("inv-VPI", 7),
          ("inv-VPI-15", 11),
          ("inv-cfg", 4),
          ("inv-maxtslot", 10),
          ("up", 1))
    )


_VsmBundleCfgOperStatus_Type.__name__ = "Integer32"
_VsmBundleCfgOperStatus_Object = MibTableColumn
vsmBundleCfgOperStatus = _VsmBundleCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 11),
    _VsmBundleCfgOperStatus_Type()
)
vsmBundleCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleCfgOperStatus.setStatus("mandatory")


class _VsmBundleCfgAdminStatus_Type(Integer32):
    """Custom type vsmBundleCfgAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("reconfig", 3),
          ("up", 1))
    )


_VsmBundleCfgAdminStatus_Type.__name__ = "Integer32"
_VsmBundleCfgAdminStatus_Object = MibTableColumn
vsmBundleCfgAdminStatus = _VsmBundleCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 12),
    _VsmBundleCfgAdminStatus_Type()
)
vsmBundleCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgAdminStatus.setStatus("mandatory")


class _VsmBundleCfgValidity_Type(Integer32):
    """Custom type vsmBundleCfgValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_VsmBundleCfgValidity_Type.__name__ = "Integer32"
_VsmBundleCfgValidity_Object = MibTableColumn
vsmBundleCfgValidity = _VsmBundleCfgValidity_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 4, 1, 13),
    _VsmBundleCfgValidity_Type()
)
vsmBundleCfgValidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleCfgValidity.setStatus("mandatory")
_VsmCardStatTable_Object = MibTable
vsmCardStatTable = _VsmCardStatTable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5)
)
if mibBuilder.loadTexts:
    vsmCardStatTable.setStatus("mandatory")
_VsmCardStatTableEntry_Object = MibTableRow
vsmCardStatTableEntry = _VsmCardStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1)
)
vsmCardStatTableEntry.setIndexNames(
    (0, "Vsm-MIB", "vsmCardStatIndex"),
)
if mibBuilder.loadTexts:
    vsmCardStatTableEntry.setStatus("mandatory")


class _VsmCardStatIndex_Type(Integer32):
    """Custom type vsmCardStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VsmCardStatIndex_Type.__name__ = "Integer32"
_VsmCardStatIndex_Object = MibTableColumn
vsmCardStatIndex = _VsmCardStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 1),
    _VsmCardStatIndex_Type()
)
vsmCardStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatIndex.setStatus("mandatory")


class _VsmCardStatBdType_Type(DisplayString):
    """Custom type vsmCardStatBdType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsmCardStatBdType_Type.__name__ = "DisplayString"
_VsmCardStatBdType_Object = MibTableColumn
vsmCardStatBdType = _VsmCardStatBdType_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 2),
    _VsmCardStatBdType_Type()
)
vsmCardStatBdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatBdType.setStatus("mandatory")


class _VsmCardStatHWSWCompatibility_Type(DisplayString):
    """Custom type vsmCardStatHWSWCompatibility based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsmCardStatHWSWCompatibility_Type.__name__ = "DisplayString"
_VsmCardStatHWSWCompatibility_Object = MibTableColumn
vsmCardStatHWSWCompatibility = _VsmCardStatHWSWCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 3),
    _VsmCardStatHWSWCompatibility_Type()
)
vsmCardStatHWSWCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatHWSWCompatibility.setStatus("mandatory")


class _VsmCardStatBinPres_Type(Integer32):
    """Custom type vsmCardStatBinPres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bin-not-present", 1),
          ("present", 2))
    )


_VsmCardStatBinPres_Type.__name__ = "Integer32"
_VsmCardStatBinPres_Object = MibTableColumn
vsmCardStatBinPres = _VsmCardStatBinPres_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 4),
    _VsmCardStatBinPres_Type()
)
vsmCardStatBinPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatBinPres.setStatus("mandatory")


class _VsmCardStatBinRev_Type(DisplayString):
    """Custom type vsmCardStatBinRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VsmCardStatBinRev_Type.__name__ = "DisplayString"
_VsmCardStatBinRev_Object = MibTableColumn
vsmCardStatBinRev = _VsmCardStatBinRev_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 5),
    _VsmCardStatBinRev_Type()
)
vsmCardStatBinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatBinRev.setStatus("mandatory")


class _VsmCardStatBdRev_Type(DisplayString):
    """Custom type vsmCardStatBdRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VsmCardStatBdRev_Type.__name__ = "DisplayString"
_VsmCardStatBdRev_Object = MibTableColumn
vsmCardStatBdRev = _VsmCardStatBdRev_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 6),
    _VsmCardStatBdRev_Type()
)
vsmCardStatBdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatBdRev.setStatus("mandatory")


class _VsmCardStatDoc1Type_Type(Integer32):
    """Custom type vsmCardStatDoc1Type based on Integer32"""
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
        *(("doc-not-present", 4),
          ("type-48-channel", 2),
          ("type-60-channel", 3),
          ("unknown-doc-type", 1))
    )


_VsmCardStatDoc1Type_Type.__name__ = "Integer32"
_VsmCardStatDoc1Type_Object = MibTableColumn
vsmCardStatDoc1Type = _VsmCardStatDoc1Type_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 7),
    _VsmCardStatDoc1Type_Type()
)
vsmCardStatDoc1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatDoc1Type.setStatus("mandatory")


class _VsmCardStatDoc1TypeRev_Type(DisplayString):
    """Custom type vsmCardStatDoc1TypeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VsmCardStatDoc1TypeRev_Type.__name__ = "DisplayString"
_VsmCardStatDoc1TypeRev_Object = MibTableColumn
vsmCardStatDoc1TypeRev = _VsmCardStatDoc1TypeRev_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 8),
    _VsmCardStatDoc1TypeRev_Type()
)
vsmCardStatDoc1TypeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatDoc1TypeRev.setStatus("mandatory")


class _VsmCardStatDoc2Type_Type(Integer32):
    """Custom type vsmCardStatDoc2Type based on Integer32"""
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
        *(("doc-not-present", 4),
          ("type-48-channel", 2),
          ("type-60-channel", 3),
          ("unknown-doc-type", 1))
    )


_VsmCardStatDoc2Type_Type.__name__ = "Integer32"
_VsmCardStatDoc2Type_Object = MibTableColumn
vsmCardStatDoc2Type = _VsmCardStatDoc2Type_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 9),
    _VsmCardStatDoc2Type_Type()
)
vsmCardStatDoc2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatDoc2Type.setStatus("mandatory")


class _VsmCardStatDoc2TypeRev_Type(DisplayString):
    """Custom type vsmCardStatDoc2TypeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VsmCardStatDoc2TypeRev_Type.__name__ = "DisplayString"
_VsmCardStatDoc2TypeRev_Object = MibTableColumn
vsmCardStatDoc2TypeRev = _VsmCardStatDoc2TypeRev_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 10),
    _VsmCardStatDoc2TypeRev_Type()
)
vsmCardStatDoc2TypeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatDoc2TypeRev.setStatus("mandatory")


class _VsmCardStatLimType_Type(Integer32):
    """Custom type vsmCardStatLimType based on Integer32"""
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
        *(("ds1-dual-signaling-lim", 2),
          ("ds1-quad-signaling-lim", 3),
          ("e1-dual-signaling-lim", 4),
          ("e1-quad-signaling-lim", 5),
          ("invalid-or-no-lim", 1))
    )


_VsmCardStatLimType_Type.__name__ = "Integer32"
_VsmCardStatLimType_Object = MibTableColumn
vsmCardStatLimType = _VsmCardStatLimType_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 5, 1, 11),
    _VsmCardStatLimType_Type()
)
vsmCardStatLimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardStatLimType.setStatus("mandatory")
_VsmTsStatTable_Object = MibTable
vsmTsStatTable = _VsmTsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6)
)
if mibBuilder.loadTexts:
    vsmTsStatTable.setStatus("mandatory")
_VsmTsStatTableEntry_Object = MibTableRow
vsmTsStatTableEntry = _VsmTsStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1)
)
vsmTsStatTableEntry.setIndexNames(
    (0, "Vsm-MIB", "vsmTsStatLinkNo"),
    (0, "Vsm-MIB", "vsmTsStatTSNo"),
)
if mibBuilder.loadTexts:
    vsmTsStatTableEntry.setStatus("mandatory")


class _VsmTsStatLinkNo_Type(Integer32):
    """Custom type vsmTsStatLinkNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VsmTsStatLinkNo_Type.__name__ = "Integer32"
_VsmTsStatLinkNo_Object = MibTableColumn
vsmTsStatLinkNo = _VsmTsStatLinkNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 1),
    _VsmTsStatLinkNo_Type()
)
vsmTsStatLinkNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatLinkNo.setStatus("mandatory")


class _VsmTsStatTSNo_Type(Integer32):
    """Custom type vsmTsStatTSNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_VsmTsStatTSNo_Type.__name__ = "Integer32"
_VsmTsStatTSNo_Object = MibTableColumn
vsmTsStatTSNo = _VsmTsStatTSNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 2),
    _VsmTsStatTSNo_Type()
)
vsmTsStatTSNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatTSNo.setStatus("mandatory")
_VsmTsStatBundleNo_Type = VsmBundle
_VsmTsStatBundleNo_Object = MibTableColumn
vsmTsStatBundleNo = _VsmTsStatBundleNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 3),
    _VsmTsStatBundleNo_Type()
)
vsmTsStatBundleNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatBundleNo.setStatus("mandatory")
_VsmTsStatXmitBytes_Type = Counter32
_VsmTsStatXmitBytes_Object = MibTableColumn
vsmTsStatXmitBytes = _VsmTsStatXmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 4),
    _VsmTsStatXmitBytes_Type()
)
vsmTsStatXmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatXmitBytes.setStatus("mandatory")
_VsmTsStatRecvBytes_Type = Counter32
_VsmTsStatRecvBytes_Object = MibTableColumn
vsmTsStatRecvBytes = _VsmTsStatRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 5),
    _VsmTsStatRecvBytes_Type()
)
vsmTsStatRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatRecvBytes.setStatus("mandatory")
_VsmTsStatUnderflows_Type = Counter32
_VsmTsStatUnderflows_Object = MibTableColumn
vsmTsStatUnderflows = _VsmTsStatUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 6),
    _VsmTsStatUnderflows_Type()
)
vsmTsStatUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatUnderflows.setStatus("mandatory")
_VsmTsStatLostPackets_Type = Counter32
_VsmTsStatLostPackets_Object = MibTableColumn
vsmTsStatLostPackets = _VsmTsStatLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 7),
    _VsmTsStatLostPackets_Type()
)
vsmTsStatLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatLostPackets.setStatus("mandatory")


class _VsmTsStatAALType_Type(Integer32):
    """Custom type vsmTsStatAALType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal2", 2))
    )


_VsmTsStatAALType_Type.__name__ = "Integer32"
_VsmTsStatAALType_Object = MibTableColumn
vsmTsStatAALType = _VsmTsStatAALType_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 8),
    _VsmTsStatAALType_Type()
)
vsmTsStatAALType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatAALType.setStatus("mandatory")
_VsmTsStatVCID_Type = Integer32
_VsmTsStatVCID_Object = MibTableColumn
vsmTsStatVCID = _VsmTsStatVCID_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 9),
    _VsmTsStatVCID_Type()
)
vsmTsStatVCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatVCID.setStatus("mandatory")
_VsmTsStatCID_Type = Integer32
_VsmTsStatCID_Object = MibTableColumn
vsmTsStatCID = _VsmTsStatCID_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 10),
    _VsmTsStatCID_Type()
)
vsmTsStatCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatCID.setStatus("mandatory")


class _VsmTsStatActive_Type(Integer32):
    """Custom type vsmTsStatActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatActive_Type.__name__ = "Integer32"
_VsmTsStatActive_Object = MibTableColumn
vsmTsStatActive = _VsmTsStatActive_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 11),
    _VsmTsStatActive_Type()
)
vsmTsStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatActive.setStatus("mandatory")


class _VsmTsStatDataLnk_Type(Integer32):
    """Custom type vsmTsStatDataLnk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("dsp", 1))
    )


_VsmTsStatDataLnk_Type.__name__ = "Integer32"
_VsmTsStatDataLnk_Object = MibTableColumn
vsmTsStatDataLnk = _VsmTsStatDataLnk_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 12),
    _VsmTsStatDataLnk_Type()
)
vsmTsStatDataLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatDataLnk.setStatus("mandatory")


class _VsmTsStatBlocked_Type(Integer32):
    """Custom type vsmTsStatBlocked based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatBlocked_Type.__name__ = "Integer32"
_VsmTsStatBlocked_Object = MibTableColumn
vsmTsStatBlocked = _VsmTsStatBlocked_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 13),
    _VsmTsStatBlocked_Type()
)
vsmTsStatBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatBlocked.setStatus("mandatory")


class _VsmTsStatIdleIdle_Type(Integer32):
    """Custom type vsmTsStatIdleIdle based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatIdleIdle_Type.__name__ = "Integer32"
_VsmTsStatIdleIdle_Object = MibTableColumn
vsmTsStatIdleIdle = _VsmTsStatIdleIdle_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 14),
    _VsmTsStatIdleIdle_Type()
)
vsmTsStatIdleIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatIdleIdle.setStatus("mandatory")


class _VsmTsStatHold_Type(Integer32):
    """Custom type vsmTsStatHold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatHold_Type.__name__ = "Integer32"
_VsmTsStatHold_Object = MibTableColumn
vsmTsStatHold = _VsmTsStatHold_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 15),
    _VsmTsStatHold_Type()
)
vsmTsStatHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatHold.setStatus("mandatory")


class _VsmTsStatRemoteCompressed_Type(Integer32):
    """Custom type vsmTsStatRemoteCompressed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatRemoteCompressed_Type.__name__ = "Integer32"
_VsmTsStatRemoteCompressed_Object = MibTableColumn
vsmTsStatRemoteCompressed = _VsmTsStatRemoteCompressed_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 16),
    _VsmTsStatRemoteCompressed_Type()
)
vsmTsStatRemoteCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatRemoteCompressed.setStatus("mandatory")


class _VsmTsStatRemoteSilent_Type(Integer32):
    """Custom type vsmTsStatRemoteSilent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatRemoteSilent_Type.__name__ = "Integer32"
_VsmTsStatRemoteSilent_Object = MibTableColumn
vsmTsStatRemoteSilent = _VsmTsStatRemoteSilent_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 17),
    _VsmTsStatRemoteSilent_Type()
)
vsmTsStatRemoteSilent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatRemoteSilent.setStatus("mandatory")


class _VsmTsStatCompressed_Type(Integer32):
    """Custom type vsmTsStatCompressed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatCompressed_Type.__name__ = "Integer32"
_VsmTsStatCompressed_Object = MibTableColumn
vsmTsStatCompressed = _VsmTsStatCompressed_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 18),
    _VsmTsStatCompressed_Type()
)
vsmTsStatCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatCompressed.setStatus("mandatory")


class _VsmTsStatSilent_Type(Integer32):
    """Custom type vsmTsStatSilent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatSilent_Type.__name__ = "Integer32"
_VsmTsStatSilent_Object = MibTableColumn
vsmTsStatSilent = _VsmTsStatSilent_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 19),
    _VsmTsStatSilent_Type()
)
vsmTsStatSilent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatSilent.setStatus("mandatory")


class _VsmTsStatConditioning_Type(Integer32):
    """Custom type vsmTsStatConditioning based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatConditioning_Type.__name__ = "Integer32"
_VsmTsStatConditioning_Object = MibTableColumn
vsmTsStatConditioning = _VsmTsStatConditioning_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 20),
    _VsmTsStatConditioning_Type()
)
vsmTsStatConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatConditioning.setStatus("mandatory")


class _VsmTsStatRemoteConditioning_Type(Integer32):
    """Custom type vsmTsStatRemoteConditioning based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatRemoteConditioning_Type.__name__ = "Integer32"
_VsmTsStatRemoteConditioning_Object = MibTableColumn
vsmTsStatRemoteConditioning = _VsmTsStatRemoteConditioning_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 21),
    _VsmTsStatRemoteConditioning_Type()
)
vsmTsStatRemoteConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatRemoteConditioning.setStatus("mandatory")


class _VsmTsStatRIWF_Type(Integer32):
    """Custom type vsmTsStatRIWF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatRIWF_Type.__name__ = "Integer32"
_VsmTsStatRIWF_Object = MibTableColumn
vsmTsStatRIWF = _VsmTsStatRIWF_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 22),
    _VsmTsStatRIWF_Type()
)
vsmTsStatRIWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatRIWF.setStatus("mandatory")


class _VsmTsStatLossofRefresh_Type(Integer32):
    """Custom type vsmTsStatLossofRefresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatLossofRefresh_Type.__name__ = "Integer32"
_VsmTsStatLossofRefresh_Object = MibTableColumn
vsmTsStatLossofRefresh = _VsmTsStatLossofRefresh_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 23),
    _VsmTsStatLossofRefresh_Type()
)
vsmTsStatLossofRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatLossofRefresh.setStatus("mandatory")


class _VsmTsStatCasValuesPDH_Type(Integer32):
    """Custom type vsmTsStatCasValuesPDH based on Integer32"""
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
        *(("a0-b0-c0-d0", 1),
          ("a0-b0-c0-d1", 2),
          ("a0-b0-c1-d0", 3),
          ("a0-b0-c1-d1", 4),
          ("a0-b1-c0-d0", 5),
          ("a0-b1-c0-d1", 6),
          ("a0-b1-c1-d0", 7),
          ("a0-b1-c1-d1", 8),
          ("a1-b0-c0-d0", 9),
          ("a1-b0-c0-d1", 10),
          ("a1-b0-c1-d0", 11),
          ("a1-b0-c1-d1", 12),
          ("a1-b1-c0-d0", 13),
          ("a1-b1-c0-d1", 14),
          ("a1-b1-c1-d0", 15),
          ("a1-b1-c1-d1", 16))
    )


_VsmTsStatCasValuesPDH_Type.__name__ = "Integer32"
_VsmTsStatCasValuesPDH_Object = MibTableColumn
vsmTsStatCasValuesPDH = _VsmTsStatCasValuesPDH_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 24),
    _VsmTsStatCasValuesPDH_Type()
)
vsmTsStatCasValuesPDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatCasValuesPDH.setStatus("mandatory")


class _VsmTsStatCasValuesATM_Type(Integer32):
    """Custom type vsmTsStatCasValuesATM based on Integer32"""
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
        *(("a0-b0-c0-d0", 1),
          ("a0-b0-c0-d1", 2),
          ("a0-b0-c1-d0", 3),
          ("a0-b0-c1-d1", 4),
          ("a0-b1-c0-d0", 5),
          ("a0-b1-c0-d1", 6),
          ("a0-b1-c1-d0", 7),
          ("a0-b1-c1-d1", 8),
          ("a1-b0-c0-d0", 9),
          ("a1-b0-c0-d1", 10),
          ("a1-b0-c1-d0", 11),
          ("a1-b0-c1-d1", 12),
          ("a1-b1-c0-d0", 13),
          ("a1-b1-c0-d1", 14),
          ("a1-b1-c1-d0", 15),
          ("a1-b1-c1-d1", 16))
    )


_VsmTsStatCasValuesATM_Type.__name__ = "Integer32"
_VsmTsStatCasValuesATM_Object = MibTableColumn
vsmTsStatCasValuesATM = _VsmTsStatCasValuesATM_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 25),
    _VsmTsStatCasValuesATM_Type()
)
vsmTsStatCasValuesATM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTsStatCasValuesATM.setStatus("mandatory")


class _VsmTsStatReset_Type(Integer32):
    """Custom type vsmTsStatReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmTsStatReset_Type.__name__ = "Integer32"
_VsmTsStatReset_Object = MibTableColumn
vsmTsStatReset = _VsmTsStatReset_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 6, 1, 26),
    _VsmTsStatReset_Type()
)
vsmTsStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmTsStatReset.setStatus("mandatory")
_VsmBundleStatTable_Object = MibTable
vsmBundleStatTable = _VsmBundleStatTable_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7)
)
if mibBuilder.loadTexts:
    vsmBundleStatTable.setStatus("mandatory")
_VsmBundleStatTableEntry_Object = MibTableRow
vsmBundleStatTableEntry = _VsmBundleStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1)
)
vsmBundleStatTableEntry.setIndexNames(
    (0, "Vsm-MIB", "vsmBundleStatBundleNo"),
)
if mibBuilder.loadTexts:
    vsmBundleStatTableEntry.setStatus("mandatory")
_VsmBundleStatBundleNo_Type = VsmBundle
_VsmBundleStatBundleNo_Object = MibTableColumn
vsmBundleStatBundleNo = _VsmBundleStatBundleNo_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 1),
    _VsmBundleStatBundleNo_Type()
)
vsmBundleStatBundleNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatBundleNo.setStatus("mandatory")
_VsmBundleStatXmitCells_Type = Counter32
_VsmBundleStatXmitCells_Object = MibTableColumn
vsmBundleStatXmitCells = _VsmBundleStatXmitCells_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 2),
    _VsmBundleStatXmitCells_Type()
)
vsmBundleStatXmitCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatXmitCells.setStatus("mandatory")
_VsmBundleStatRecvCells_Type = Counter32
_VsmBundleStatRecvCells_Object = MibTableColumn
vsmBundleStatRecvCells = _VsmBundleStatRecvCells_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 3),
    _VsmBundleStatRecvCells_Type()
)
vsmBundleStatRecvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatRecvCells.setStatus("mandatory")


class _VsmBundleStatPvcActive_Type(Integer32):
    """Custom type vsmBundleStatPvcActive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("not-active", 2))
    )


_VsmBundleStatPvcActive_Type.__name__ = "Integer32"
_VsmBundleStatPvcActive_Object = MibTableColumn
vsmBundleStatPvcActive = _VsmBundleStatPvcActive_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 4),
    _VsmBundleStatPvcActive_Type()
)
vsmBundleStatPvcActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatPvcActive.setStatus("mandatory")


class _VsmBundleStatAALType_Type(Integer32):
    """Custom type vsmBundleStatAALType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal2", 2))
    )


_VsmBundleStatAALType_Type.__name__ = "Integer32"
_VsmBundleStatAALType_Object = MibTableColumn
vsmBundleStatAALType = _VsmBundleStatAALType_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 5),
    _VsmBundleStatAALType_Type()
)
vsmBundleStatAALType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatAALType.setStatus("mandatory")
_VsmBundleStatBufUndrflws_Type = Counter32
_VsmBundleStatBufUndrflws_Object = MibTableColumn
vsmBundleStatBufUndrflws = _VsmBundleStatBufUndrflws_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 6),
    _VsmBundleStatBufUndrflws_Type()
)
vsmBundleStatBufUndrflws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatBufUndrflws.setStatus("mandatory")
_VsmBundleStatBufOverflows_Type = Counter32
_VsmBundleStatBufOverflows_Object = MibTableColumn
vsmBundleStatBufOverflows = _VsmBundleStatBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 7),
    _VsmBundleStatBufOverflows_Type()
)
vsmBundleStatBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatBufOverflows.setStatus("mandatory")
_VsmBundleStatPtrReframes_Type = Counter32
_VsmBundleStatPtrReframes_Object = MibTableColumn
vsmBundleStatPtrReframes = _VsmBundleStatPtrReframes_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 8),
    _VsmBundleStatPtrReframes_Type()
)
vsmBundleStatPtrReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatPtrReframes.setStatus("mandatory")
_VsmBundleStatLostCells_Type = Counter32
_VsmBundleStatLostCells_Object = MibTableColumn
vsmBundleStatLostCells = _VsmBundleStatLostCells_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 9),
    _VsmBundleStatLostCells_Type()
)
vsmBundleStatLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatLostCells.setStatus("mandatory")
_VsmBundleStatHdrErrors_Type = Counter32
_VsmBundleStatHdrErrors_Object = MibTableColumn
vsmBundleStatHdrErrors = _VsmBundleStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 10),
    _VsmBundleStatHdrErrors_Type()
)
vsmBundleStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatHdrErrors.setStatus("mandatory")
_VsmBundleStatBadCID_Type = Counter32
_VsmBundleStatBadCID_Object = MibTableColumn
vsmBundleStatBadCID = _VsmBundleStatBadCID_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 11),
    _VsmBundleStatBadCID_Type()
)
vsmBundleStatBadCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatBadCID.setStatus("mandatory")
_VsmBundleStatAAL2LostCells_Type = Counter32
_VsmBundleStatAAL2LostCells_Object = MibTableColumn
vsmBundleStatAAL2LostCells = _VsmBundleStatAAL2LostCells_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 12),
    _VsmBundleStatAAL2LostCells_Type()
)
vsmBundleStatAAL2LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatAAL2LostCells.setStatus("mandatory")


class _VsmBundleStatReset_Type(Integer32):
    """Custom type vsmBundleStatReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmBundleStatReset_Type.__name__ = "Integer32"
_VsmBundleStatReset_Object = MibTableColumn
vsmBundleStatReset = _VsmBundleStatReset_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 13),
    _VsmBundleStatReset_Type()
)
vsmBundleStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmBundleStatReset.setStatus("mandatory")


class _VsmBundleStatConditioning_Type(Integer32):
    """Custom type vsmBundleStatConditioning based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VsmBundleStatConditioning_Type.__name__ = "Integer32"
_VsmBundleStatConditioning_Object = MibTableColumn
vsmBundleStatConditioning = _VsmBundleStatConditioning_Object(
    (1, 3, 6, 1, 4, 1, 251, 1, 1, 47, 7, 1, 14),
    _VsmBundleStatConditioning_Type()
)
vsmBundleStatConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmBundleStatConditioning.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Vsm-MIB",
    **{"VciInteger": VciInteger,
       "VpiInteger": VpiInteger,
       "VsmBundle": VsmBundle,
       "dv2Vsm": dv2Vsm,
       "vsmCardCfgTable": vsmCardCfgTable,
       "vsmCardCfgTableEntry": vsmCardCfgTableEntry,
       "vsmCardCfgIndex": vsmCardCfgIndex,
       "vsmCardCfgBndlTslotStatus": vsmCardCfgBndlTslotStatus,
       "vsmLinkTable": vsmLinkTable,
       "vsmLinkEntry": vsmLinkEntry,
       "vsmLinkLink": vsmLinkLink,
       "vsmLinkEnable": vsmLinkEnable,
       "vsmLinkEnableStat": vsmLinkEnableStat,
       "vsmLinkSigType": vsmLinkSigType,
       "vsmTsCfgTable": vsmTsCfgTable,
       "vsmTsCfgTableEntry": vsmTsCfgTableEntry,
       "vsmTsCfgLinkNo": vsmTsCfgLinkNo,
       "vsmTsCfgTsNo": vsmTsCfgTsNo,
       "vsmTsCfgBundleNo": vsmTsCfgBundleNo,
       "vsmTsCfgAALTyp": vsmTsCfgAALTyp,
       "vsmTsCfgChanID": vsmTsCfgChanID,
       "vsmTsCfgCmprssionTyp": vsmTsCfgCmprssionTyp,
       "vsmTsCfgFaxMdmHndlng": vsmTsCfgFaxMdmHndlng,
       "vsmTsCfgEchoCancel": vsmTsCfgEchoCancel,
       "vsmTsCfgSilenceRmvl": vsmTsCfgSilenceRmvl,
       "vsmTsCfgIdleDetect": vsmTsCfgIdleDetect,
       "vsmTsCfgRmtLaw": vsmTsCfgRmtLaw,
       "vsmTsCfgSignalTyp": vsmTsCfgSignalTyp,
       "vsmTsCfgSigCndTypNB": vsmTsCfgSigCndTypNB,
       "vsmTsCfgSigCndTypATM": vsmTsCfgSigCndTypATM,
       "vsmTsCfgDataCndTypNB": vsmTsCfgDataCndTypNB,
       "vsmTsCfgDataCndTypATM": vsmTsCfgDataCndTypATM,
       "vsmTsCfgMulticast": vsmTsCfgMulticast,
       "vsmTsCfgOperStatus": vsmTsCfgOperStatus,
       "vsmTsCfgAdminStatus": vsmTsCfgAdminStatus,
       "vsmTsCfgValidity": vsmTsCfgValidity,
       "vsmBundleCfgTable": vsmBundleCfgTable,
       "vsmBundleCfgTableEntry": vsmBundleCfgTableEntry,
       "vsmBundleCfgNo": vsmBundleCfgNo,
       "vsmBundleCfgVcVpi": vsmBundleCfgVcVpi,
       "vsmBundleCfgVcVci": vsmBundleCfgVcVci,
       "vsmBundleCfgVcAALTyp": vsmBundleCfgVcAALTyp,
       "vsmBundleCfgMaxTslot": vsmBundleCfgMaxTslot,
       "vsmBundleCfgVcCDV": vsmBundleCfgVcCDV,
       "vsmBundleCfgTimerCU": vsmBundleCfgTimerCU,
       "vsmBundleCfgCESPartialFill": vsmBundleCfgCESPartialFill,
       "vsmBundleCfgVcTyp": vsmBundleCfgVcTyp,
       "vsmBundleCfgTrapCfg": vsmBundleCfgTrapCfg,
       "vsmBundleCfgOperStatus": vsmBundleCfgOperStatus,
       "vsmBundleCfgAdminStatus": vsmBundleCfgAdminStatus,
       "vsmBundleCfgValidity": vsmBundleCfgValidity,
       "vsmCardStatTable": vsmCardStatTable,
       "vsmCardStatTableEntry": vsmCardStatTableEntry,
       "vsmCardStatIndex": vsmCardStatIndex,
       "vsmCardStatBdType": vsmCardStatBdType,
       "vsmCardStatHWSWCompatibility": vsmCardStatHWSWCompatibility,
       "vsmCardStatBinPres": vsmCardStatBinPres,
       "vsmCardStatBinRev": vsmCardStatBinRev,
       "vsmCardStatBdRev": vsmCardStatBdRev,
       "vsmCardStatDoc1Type": vsmCardStatDoc1Type,
       "vsmCardStatDoc1TypeRev": vsmCardStatDoc1TypeRev,
       "vsmCardStatDoc2Type": vsmCardStatDoc2Type,
       "vsmCardStatDoc2TypeRev": vsmCardStatDoc2TypeRev,
       "vsmCardStatLimType": vsmCardStatLimType,
       "vsmTsStatTable": vsmTsStatTable,
       "vsmTsStatTableEntry": vsmTsStatTableEntry,
       "vsmTsStatLinkNo": vsmTsStatLinkNo,
       "vsmTsStatTSNo": vsmTsStatTSNo,
       "vsmTsStatBundleNo": vsmTsStatBundleNo,
       "vsmTsStatXmitBytes": vsmTsStatXmitBytes,
       "vsmTsStatRecvBytes": vsmTsStatRecvBytes,
       "vsmTsStatUnderflows": vsmTsStatUnderflows,
       "vsmTsStatLostPackets": vsmTsStatLostPackets,
       "vsmTsStatAALType": vsmTsStatAALType,
       "vsmTsStatVCID": vsmTsStatVCID,
       "vsmTsStatCID": vsmTsStatCID,
       "vsmTsStatActive": vsmTsStatActive,
       "vsmTsStatDataLnk": vsmTsStatDataLnk,
       "vsmTsStatBlocked": vsmTsStatBlocked,
       "vsmTsStatIdleIdle": vsmTsStatIdleIdle,
       "vsmTsStatHold": vsmTsStatHold,
       "vsmTsStatRemoteCompressed": vsmTsStatRemoteCompressed,
       "vsmTsStatRemoteSilent": vsmTsStatRemoteSilent,
       "vsmTsStatCompressed": vsmTsStatCompressed,
       "vsmTsStatSilent": vsmTsStatSilent,
       "vsmTsStatConditioning": vsmTsStatConditioning,
       "vsmTsStatRemoteConditioning": vsmTsStatRemoteConditioning,
       "vsmTsStatRIWF": vsmTsStatRIWF,
       "vsmTsStatLossofRefresh": vsmTsStatLossofRefresh,
       "vsmTsStatCasValuesPDH": vsmTsStatCasValuesPDH,
       "vsmTsStatCasValuesATM": vsmTsStatCasValuesATM,
       "vsmTsStatReset": vsmTsStatReset,
       "vsmBundleStatTable": vsmBundleStatTable,
       "vsmBundleStatTableEntry": vsmBundleStatTableEntry,
       "vsmBundleStatBundleNo": vsmBundleStatBundleNo,
       "vsmBundleStatXmitCells": vsmBundleStatXmitCells,
       "vsmBundleStatRecvCells": vsmBundleStatRecvCells,
       "vsmBundleStatPvcActive": vsmBundleStatPvcActive,
       "vsmBundleStatAALType": vsmBundleStatAALType,
       "vsmBundleStatBufUndrflws": vsmBundleStatBufUndrflws,
       "vsmBundleStatBufOverflows": vsmBundleStatBufOverflows,
       "vsmBundleStatPtrReframes": vsmBundleStatPtrReframes,
       "vsmBundleStatLostCells": vsmBundleStatLostCells,
       "vsmBundleStatHdrErrors": vsmBundleStatHdrErrors,
       "vsmBundleStatBadCID": vsmBundleStatBadCID,
       "vsmBundleStatAAL2LostCells": vsmBundleStatAAL2LostCells,
       "vsmBundleStatReset": vsmBundleStatReset,
       "vsmBundleStatConditioning": vsmBundleStatConditioning}
)
