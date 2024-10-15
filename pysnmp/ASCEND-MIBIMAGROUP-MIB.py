# SNMP MIB module (ASCEND-MIBIMAGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIMAGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:41 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibimaGroupConfig_ObjectIdentity = ObjectIdentity
mibimaGroupConfig = _MibimaGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 23)
)
_MibimaGroupConfigTable_Object = MibTable
mibimaGroupConfigTable = _MibimaGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1)
)
if mibBuilder.loadTexts:
    mibimaGroupConfigTable.setStatus("mandatory")
_MibimaGroupConfigEntry_Object = MibTableRow
mibimaGroupConfigEntry = _MibimaGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1)
)
mibimaGroupConfigEntry.setIndexNames(
    (0, "ASCEND-MIBIMAGROUP-MIB", "imaGroupConfig-Name"),
)
if mibBuilder.loadTexts:
    mibimaGroupConfigEntry.setStatus("mandatory")
_ImaGroupConfig_Name_Type = DisplayString
_ImaGroupConfig_Name_Object = MibScalar
imaGroupConfig_Name = _ImaGroupConfig_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 1),
    _ImaGroupConfig_Name_Type()
)
imaGroupConfig_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupConfig_Name.setStatus("mandatory")


class _ImaGroupConfig_Active_Type(Integer32):
    """Custom type imaGroupConfig_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImaGroupConfig_Active_Type.__name__ = "Integer32"
_ImaGroupConfig_Active_Object = MibScalar
imaGroupConfig_Active = _ImaGroupConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 2),
    _ImaGroupConfig_Active_Type()
)
imaGroupConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_Active.setStatus("mandatory")
_ImaGroupConfig_NailedGroup_Type = Integer32
_ImaGroupConfig_NailedGroup_Object = MibScalar
imaGroupConfig_NailedGroup = _ImaGroupConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 3),
    _ImaGroupConfig_NailedGroup_Type()
)
imaGroupConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_NailedGroup.setStatus("mandatory")


class _ImaGroupConfig_GroupSymmetryMode_Type(Integer32):
    """Custom type imaGroupConfig_GroupSymmetryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asymmetricOperation", 3),
          ("configurationAsymmetric", 4),
          ("symmetricOperation", 2))
    )


_ImaGroupConfig_GroupSymmetryMode_Type.__name__ = "Integer32"
_ImaGroupConfig_GroupSymmetryMode_Object = MibScalar
imaGroupConfig_GroupSymmetryMode = _ImaGroupConfig_GroupSymmetryMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 4),
    _ImaGroupConfig_GroupSymmetryMode_Type()
)
imaGroupConfig_GroupSymmetryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_GroupSymmetryMode.setStatus("mandatory")


class _ImaGroupConfig_Version_Type(Integer32):
    """Custom type imaGroupConfig_Version based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("v10", 2),
          ("v11", 4))
    )


_ImaGroupConfig_Version_Type.__name__ = "Integer32"
_ImaGroupConfig_Version_Object = MibScalar
imaGroupConfig_Version = _ImaGroupConfig_Version_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 5),
    _ImaGroupConfig_Version_Type()
)
imaGroupConfig_Version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_Version.setStatus("mandatory")


class _ImaGroupConfig_DoVersionFallback_Type(Integer32):
    """Custom type imaGroupConfig_DoVersionFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImaGroupConfig_DoVersionFallback_Type.__name__ = "Integer32"
_ImaGroupConfig_DoVersionFallback_Object = MibScalar
imaGroupConfig_DoVersionFallback = _ImaGroupConfig_DoVersionFallback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 6),
    _ImaGroupConfig_DoVersionFallback_Type()
)
imaGroupConfig_DoVersionFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_DoVersionFallback.setStatus("mandatory")


class _ImaGroupConfig_Lasr_Type(Integer32):
    """Custom type imaGroupConfig_Lasr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImaGroupConfig_Lasr_Type.__name__ = "Integer32"
_ImaGroupConfig_Lasr_Object = MibScalar
imaGroupConfig_Lasr = _ImaGroupConfig_Lasr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 7),
    _ImaGroupConfig_Lasr_Type()
)
imaGroupConfig_Lasr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_Lasr.setStatus("mandatory")


class _ImaGroupConfig_NeTxClkMode_Type(Integer32):
    """Custom type imaGroupConfig_NeTxClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 2),
          ("itc", 3))
    )


_ImaGroupConfig_NeTxClkMode_Type.__name__ = "Integer32"
_ImaGroupConfig_NeTxClkMode_Object = MibScalar
imaGroupConfig_NeTxClkMode = _ImaGroupConfig_NeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 8),
    _ImaGroupConfig_NeTxClkMode_Type()
)
imaGroupConfig_NeTxClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_NeTxClkMode.setStatus("mandatory")
_ImaGroupConfig_TxMinNumLinks_Type = Integer32
_ImaGroupConfig_TxMinNumLinks_Object = MibScalar
imaGroupConfig_TxMinNumLinks = _ImaGroupConfig_TxMinNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 9),
    _ImaGroupConfig_TxMinNumLinks_Type()
)
imaGroupConfig_TxMinNumLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_TxMinNumLinks.setStatus("mandatory")
_ImaGroupConfig_RxMinNumLinks_Type = Integer32
_ImaGroupConfig_RxMinNumLinks_Object = MibScalar
imaGroupConfig_RxMinNumLinks = _ImaGroupConfig_RxMinNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 10),
    _ImaGroupConfig_RxMinNumLinks_Type()
)
imaGroupConfig_RxMinNumLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_RxMinNumLinks.setStatus("mandatory")
_ImaGroupConfig_ImaId_Type = Integer32
_ImaGroupConfig_ImaId_Object = MibScalar
imaGroupConfig_ImaId = _ImaGroupConfig_ImaId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 11),
    _ImaGroupConfig_ImaId_Type()
)
imaGroupConfig_ImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_ImaId.setStatus("mandatory")


class _ImaGroupConfig_FrameLength_Type(Integer32):
    """Custom type imaGroupConfig_FrameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              65,
              129,
              257)
        )
    )
    namedValues = NamedValues(
        *(("n-128", 129),
          ("n-256", 257),
          ("n-32", 33),
          ("n-64", 65))
    )


_ImaGroupConfig_FrameLength_Type.__name__ = "Integer32"
_ImaGroupConfig_FrameLength_Object = MibScalar
imaGroupConfig_FrameLength = _ImaGroupConfig_FrameLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 12),
    _ImaGroupConfig_FrameLength_Type()
)
imaGroupConfig_FrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_FrameLength.setStatus("mandatory")
_ImaGroupConfig_DiffDelayMax_Type = Integer32
_ImaGroupConfig_DiffDelayMax_Object = MibScalar
imaGroupConfig_DiffDelayMax = _ImaGroupConfig_DiffDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 13),
    _ImaGroupConfig_DiffDelayMax_Type()
)
imaGroupConfig_DiffDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_DiffDelayMax.setStatus("mandatory")


class _ImaGroupConfig_CheckFarEndImaId_Type(Integer32):
    """Custom type imaGroupConfig_CheckFarEndImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImaGroupConfig_CheckFarEndImaId_Type.__name__ = "Integer32"
_ImaGroupConfig_CheckFarEndImaId_Object = MibScalar
imaGroupConfig_CheckFarEndImaId = _ImaGroupConfig_CheckFarEndImaId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 14),
    _ImaGroupConfig_CheckFarEndImaId_Type()
)
imaGroupConfig_CheckFarEndImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_CheckFarEndImaId.setStatus("mandatory")
_ImaGroupConfig_ExpectedFarEndImaId_Type = Integer32
_ImaGroupConfig_ExpectedFarEndImaId_Object = MibScalar
imaGroupConfig_ExpectedFarEndImaId = _ImaGroupConfig_ExpectedFarEndImaId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 15),
    _ImaGroupConfig_ExpectedFarEndImaId_Type()
)
imaGroupConfig_ExpectedFarEndImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_ExpectedFarEndImaId.setStatus("mandatory")


class _ImaGroupConfig_FarEndCheckFrameLength_Type(Integer32):
    """Custom type imaGroupConfig_FarEndCheckFrameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImaGroupConfig_FarEndCheckFrameLength_Type.__name__ = "Integer32"
_ImaGroupConfig_FarEndCheckFrameLength_Object = MibScalar
imaGroupConfig_FarEndCheckFrameLength = _ImaGroupConfig_FarEndCheckFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 16),
    _ImaGroupConfig_FarEndCheckFrameLength_Type()
)
imaGroupConfig_FarEndCheckFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_FarEndCheckFrameLength.setStatus("mandatory")


class _ImaGroupConfig_ExpectedFarEndFrameLength_Type(Integer32):
    """Custom type imaGroupConfig_ExpectedFarEndFrameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              65,
              129,
              257)
        )
    )
    namedValues = NamedValues(
        *(("n-128", 129),
          ("n-256", 257),
          ("n-32", 33),
          ("n-64", 65))
    )


_ImaGroupConfig_ExpectedFarEndFrameLength_Type.__name__ = "Integer32"
_ImaGroupConfig_ExpectedFarEndFrameLength_Object = MibScalar
imaGroupConfig_ExpectedFarEndFrameLength = _ImaGroupConfig_ExpectedFarEndFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 17),
    _ImaGroupConfig_ExpectedFarEndFrameLength_Type()
)
imaGroupConfig_ExpectedFarEndFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_ExpectedFarEndFrameLength.setStatus("mandatory")
_ImaGroupConfig_AtmIfDelay_Type = Integer32
_ImaGroupConfig_AtmIfDelay_Object = MibScalar
imaGroupConfig_AtmIfDelay = _ImaGroupConfig_AtmIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 18),
    _ImaGroupConfig_AtmIfDelay_Type()
)
imaGroupConfig_AtmIfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_AtmIfDelay.setStatus("mandatory")
_ImaGroupConfig_TppTestLink_Type = Integer32
_ImaGroupConfig_TppTestLink_Object = MibScalar
imaGroupConfig_TppTestLink = _ImaGroupConfig_TppTestLink_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 19),
    _ImaGroupConfig_TppTestLink_Type()
)
imaGroupConfig_TppTestLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_TppTestLink.setStatus("mandatory")
_ImaGroupConfig_TppTestPattern_Type = Integer32
_ImaGroupConfig_TppTestPattern_Object = MibScalar
imaGroupConfig_TppTestPattern = _ImaGroupConfig_TppTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 20),
    _ImaGroupConfig_TppTestPattern_Type()
)
imaGroupConfig_TppTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_TppTestPattern.setStatus("mandatory")


class _ImaGroupConfig_TppState_Type(Integer32):
    """Custom type imaGroupConfig_TppState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("operating", 3))
    )


_ImaGroupConfig_TppState_Type.__name__ = "Integer32"
_ImaGroupConfig_TppState_Object = MibScalar
imaGroupConfig_TppState = _ImaGroupConfig_TppState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 21),
    _ImaGroupConfig_TppState_Type()
)
imaGroupConfig_TppState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_TppState.setStatus("mandatory")
_ImaGroupConfig_VpSwitchingVpi_Type = Integer32
_ImaGroupConfig_VpSwitchingVpi_Object = MibScalar
imaGroupConfig_VpSwitchingVpi = _ImaGroupConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 22),
    _ImaGroupConfig_VpSwitchingVpi_Type()
)
imaGroupConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_VpSwitchingVpi.setStatus("mandatory")


class _ImaGroupConfig_Action_o_Type(Integer32):
    """Custom type imaGroupConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_ImaGroupConfig_Action_o_Type.__name__ = "Integer32"
_ImaGroupConfig_Action_o_Object = MibScalar
imaGroupConfig_Action_o = _ImaGroupConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 23),
    _ImaGroupConfig_Action_o_Type()
)
imaGroupConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_Action_o.setStatus("mandatory")


class _ImaGroupConfig_IgnoreLineup_Type(Integer32):
    """Custom type imaGroupConfig_IgnoreLineup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("systemDefined", 1),
          ("yes", 3))
    )


_ImaGroupConfig_IgnoreLineup_Type.__name__ = "Integer32"
_ImaGroupConfig_IgnoreLineup_Object = MibScalar
imaGroupConfig_IgnoreLineup = _ImaGroupConfig_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 23, 1, 1, 24),
    _ImaGroupConfig_IgnoreLineup_Type()
)
imaGroupConfig_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupConfig_IgnoreLineup.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIMAGROUP-MIB",
    **{"DisplayString": DisplayString,
       "mibimaGroupConfig": mibimaGroupConfig,
       "mibimaGroupConfigTable": mibimaGroupConfigTable,
       "mibimaGroupConfigEntry": mibimaGroupConfigEntry,
       "imaGroupConfig-Name": imaGroupConfig_Name,
       "imaGroupConfig-Active": imaGroupConfig_Active,
       "imaGroupConfig-NailedGroup": imaGroupConfig_NailedGroup,
       "imaGroupConfig-GroupSymmetryMode": imaGroupConfig_GroupSymmetryMode,
       "imaGroupConfig-Version": imaGroupConfig_Version,
       "imaGroupConfig-DoVersionFallback": imaGroupConfig_DoVersionFallback,
       "imaGroupConfig-Lasr": imaGroupConfig_Lasr,
       "imaGroupConfig-NeTxClkMode": imaGroupConfig_NeTxClkMode,
       "imaGroupConfig-TxMinNumLinks": imaGroupConfig_TxMinNumLinks,
       "imaGroupConfig-RxMinNumLinks": imaGroupConfig_RxMinNumLinks,
       "imaGroupConfig-ImaId": imaGroupConfig_ImaId,
       "imaGroupConfig-FrameLength": imaGroupConfig_FrameLength,
       "imaGroupConfig-DiffDelayMax": imaGroupConfig_DiffDelayMax,
       "imaGroupConfig-CheckFarEndImaId": imaGroupConfig_CheckFarEndImaId,
       "imaGroupConfig-ExpectedFarEndImaId": imaGroupConfig_ExpectedFarEndImaId,
       "imaGroupConfig-FarEndCheckFrameLength": imaGroupConfig_FarEndCheckFrameLength,
       "imaGroupConfig-ExpectedFarEndFrameLength": imaGroupConfig_ExpectedFarEndFrameLength,
       "imaGroupConfig-AtmIfDelay": imaGroupConfig_AtmIfDelay,
       "imaGroupConfig-TppTestLink": imaGroupConfig_TppTestLink,
       "imaGroupConfig-TppTestPattern": imaGroupConfig_TppTestPattern,
       "imaGroupConfig-TppState": imaGroupConfig_TppState,
       "imaGroupConfig-VpSwitchingVpi": imaGroupConfig_VpSwitchingVpi,
       "imaGroupConfig-Action-o": imaGroupConfig_Action_o,
       "imaGroupConfig-IgnoreLineup": imaGroupConfig_IgnoreLineup}
)
