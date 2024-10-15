# SNMP MIB module (ASCEND-MIBTHRESHHDSL2SHDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBTHRESHHDSL2SHDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:27 2024
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

_MibthreshHdsl2ShdslProfile_ObjectIdentity = ObjectIdentity
mibthreshHdsl2ShdslProfile = _MibthreshHdsl2ShdslProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 160)
)
_MibthreshHdsl2ShdslProfileTable_Object = MibTable
mibthreshHdsl2ShdslProfileTable = _MibthreshHdsl2ShdslProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1)
)
if mibBuilder.loadTexts:
    mibthreshHdsl2ShdslProfileTable.setStatus("mandatory")
_MibthreshHdsl2ShdslProfileEntry_Object = MibTableRow
mibthreshHdsl2ShdslProfileEntry = _MibthreshHdsl2ShdslProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1)
)
mibthreshHdsl2ShdslProfileEntry.setIndexNames(
    (0, "ASCEND-MIBTHRESHHDSL2SHDSL-MIB", "threshHdsl2ShdslProfile-Name"),
)
if mibBuilder.loadTexts:
    mibthreshHdsl2ShdslProfileEntry.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_Name_Type = DisplayString
_ThreshHdsl2ShdslProfile_Name_Object = MibScalar
threshHdsl2ShdslProfile_Name = _ThreshHdsl2ShdslProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 1),
    _ThreshHdsl2ShdslProfile_Name_Type()
)
threshHdsl2ShdslProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_Name.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_LoopAttenuationThresh_Type = Integer32
_ThreshHdsl2ShdslProfile_LoopAttenuationThresh_Object = MibScalar
threshHdsl2ShdslProfile_LoopAttenuationThresh = _ThreshHdsl2ShdslProfile_LoopAttenuationThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 2),
    _ThreshHdsl2ShdslProfile_LoopAttenuationThresh_Type()
)
threshHdsl2ShdslProfile_LoopAttenuationThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_LoopAttenuationThresh.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_SnrMgnThresh_Type = Integer32
_ThreshHdsl2ShdslProfile_SnrMgnThresh_Object = MibScalar
threshHdsl2ShdslProfile_SnrMgnThresh = _ThreshHdsl2ShdslProfile_SnrMgnThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 3),
    _ThreshHdsl2ShdslProfile_SnrMgnThresh_Type()
)
threshHdsl2ShdslProfile_SnrMgnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_SnrMgnThresh.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_ErroredSecondsThresh_Type = Integer32
_ThreshHdsl2ShdslProfile_ErroredSecondsThresh_Object = MibScalar
threshHdsl2ShdslProfile_ErroredSecondsThresh = _ThreshHdsl2ShdslProfile_ErroredSecondsThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 4),
    _ThreshHdsl2ShdslProfile_ErroredSecondsThresh_Type()
)
threshHdsl2ShdslProfile_ErroredSecondsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_ErroredSecondsThresh.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_SeverelyErroredSecondsThresh_Type = Integer32
_ThreshHdsl2ShdslProfile_SeverelyErroredSecondsThresh_Object = MibScalar
threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh = _ThreshHdsl2ShdslProfile_SeverelyErroredSecondsThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 5),
    _ThreshHdsl2ShdslProfile_SeverelyErroredSecondsThresh_Type()
)
threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_CrcThresh_Type = Integer32
_ThreshHdsl2ShdslProfile_CrcThresh_Object = MibScalar
threshHdsl2ShdslProfile_CrcThresh = _ThreshHdsl2ShdslProfile_CrcThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 6),
    _ThreshHdsl2ShdslProfile_CrcThresh_Type()
)
threshHdsl2ShdslProfile_CrcThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_CrcThresh.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_LoswsThresh_Type = Integer32
_ThreshHdsl2ShdslProfile_LoswsThresh_Object = MibScalar
threshHdsl2ShdslProfile_LoswsThresh = _ThreshHdsl2ShdslProfile_LoswsThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 7),
    _ThreshHdsl2ShdslProfile_LoswsThresh_Type()
)
threshHdsl2ShdslProfile_LoswsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_LoswsThresh.setStatus("mandatory")
_ThreshHdsl2ShdslProfile_UasThresh_Type = Integer32
_ThreshHdsl2ShdslProfile_UasThresh_Object = MibScalar
threshHdsl2ShdslProfile_UasThresh = _ThreshHdsl2ShdslProfile_UasThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 8),
    _ThreshHdsl2ShdslProfile_UasThresh_Type()
)
threshHdsl2ShdslProfile_UasThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_UasThresh.setStatus("mandatory")


class _ThreshHdsl2ShdslProfile_Action_o_Type(Integer32):
    """Custom type threshHdsl2ShdslProfile_Action_o based on Integer32"""
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


_ThreshHdsl2ShdslProfile_Action_o_Type.__name__ = "Integer32"
_ThreshHdsl2ShdslProfile_Action_o_Object = MibScalar
threshHdsl2ShdslProfile_Action_o = _ThreshHdsl2ShdslProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 9),
    _ThreshHdsl2ShdslProfile_Action_o_Type()
)
threshHdsl2ShdslProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshHdsl2ShdslProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBTHRESHHDSL2SHDSL-MIB",
    **{"DisplayString": DisplayString,
       "mibthreshHdsl2ShdslProfile": mibthreshHdsl2ShdslProfile,
       "mibthreshHdsl2ShdslProfileTable": mibthreshHdsl2ShdslProfileTable,
       "mibthreshHdsl2ShdslProfileEntry": mibthreshHdsl2ShdslProfileEntry,
       "threshHdsl2ShdslProfile-Name": threshHdsl2ShdslProfile_Name,
       "threshHdsl2ShdslProfile-LoopAttenuationThresh": threshHdsl2ShdslProfile_LoopAttenuationThresh,
       "threshHdsl2ShdslProfile-SnrMgnThresh": threshHdsl2ShdslProfile_SnrMgnThresh,
       "threshHdsl2ShdslProfile-ErroredSecondsThresh": threshHdsl2ShdslProfile_ErroredSecondsThresh,
       "threshHdsl2ShdslProfile-SeverelyErroredSecondsThresh": threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh,
       "threshHdsl2ShdslProfile-CrcThresh": threshHdsl2ShdslProfile_CrcThresh,
       "threshHdsl2ShdslProfile-LoswsThresh": threshHdsl2ShdslProfile_LoswsThresh,
       "threshHdsl2ShdslProfile-UasThresh": threshHdsl2ShdslProfile_UasThresh,
       "threshHdsl2ShdslProfile-Action-o": threshHdsl2ShdslProfile_Action_o}
)
