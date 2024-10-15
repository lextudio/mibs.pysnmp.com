# SNMP MIB module (OLIVETTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLIVETTI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:10 2024
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
 NotificationType,
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
    "NotificationType",
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

_Olivetti_ObjectIdentity = ObjectIdentity
olivetti = _Olivetti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279)
)
_Lms_ObjectIdentity = ObjectIdentity
lms = _Lms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2)
)
_Pb_dos_ObjectIdentity = ObjectIdentity
pb_dos = _Pb_dos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 3)
)
_Pblms_systemrm_ObjectIdentity = ObjectIdentity
pblms_systemrm = _Pblms_systemrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 3, 7)
)
_Pblms_system_ObjectIdentity = ObjectIdentity
pblms_system = _Pblms_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 3, 7, 0)
)
_Pblms_systemrmTable_Object = MibTable
pblms_systemrmTable = _Pblms_systemrmTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 3, 7, 0, 1)
)
if mibBuilder.loadTexts:
    pblms_systemrmTable.setStatus("mandatory")
_Pblms_systemrmEntry_Object = MibTableRow
pblms_systemrmEntry = _Pblms_systemrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 3, 7, 0, 1, 1)
)
pblms_systemrmEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "pblms-systemrmSysName"),
    (0, "OLIVETTI-MIB", "pblms-systemrmInstName"),
    (0, "OLIVETTI-MIB", "pblms-systemrmSubAddr"),
)
if mibBuilder.loadTexts:
    pblms_systemrmEntry.setStatus("mandatory")


class _Pblms_systemrmSysName_Type(DisplayString):
    """Custom type pblms_systemrmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Pblms_systemrmSysName_Type.__name__ = "DisplayString"
_Pblms_systemrmSysName_Object = MibScalar
pblms_systemrmSysName = _Pblms_systemrmSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 3, 7, 0, 1, 1, 1),
    _Pblms_systemrmSysName_Type()
)
pblms_systemrmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pblms_systemrmSysName.setStatus("mandatory")


class _Pblms_systemrmInstName_Type(DisplayString):
    """Custom type pblms_systemrmInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Pblms_systemrmInstName_Type.__name__ = "DisplayString"
_Pblms_systemrmInstName_Object = MibScalar
pblms_systemrmInstName = _Pblms_systemrmInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 3, 7, 0, 1, 1, 2),
    _Pblms_systemrmInstName_Type()
)
pblms_systemrmInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pblms_systemrmInstName.setStatus("mandatory")


class _Pblms_systemrmSubAddr_Type(DisplayString):
    """Custom type pblms_systemrmSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Pblms_systemrmSubAddr_Type.__name__ = "DisplayString"
_Pblms_systemrmSubAddr_Object = MibScalar
pblms_systemrmSubAddr = _Pblms_systemrmSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 3, 7, 0, 1, 1, 3),
    _Pblms_systemrmSubAddr_Type()
)
pblms_systemrmSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pblms_systemrmSubAddr.setStatus("mandatory")
_Lsx_unix_ObjectIdentity = ObjectIdentity
lsx_unix = _Lsx_unix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6)
)
_Uxlms_systemrm_ObjectIdentity = ObjectIdentity
uxlms_systemrm = _Uxlms_systemrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 7)
)
_Uxlms_system_ObjectIdentity = ObjectIdentity
uxlms_system = _Uxlms_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 7, 0)
)
_Uxlms_systemrmTable_Object = MibTable
uxlms_systemrmTable = _Uxlms_systemrmTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 7, 0, 1)
)
if mibBuilder.loadTexts:
    uxlms_systemrmTable.setStatus("mandatory")
_Uxlms_systemrmEntry_Object = MibTableRow
uxlms_systemrmEntry = _Uxlms_systemrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 7, 0, 1, 1)
)
uxlms_systemrmEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxlms-systemrmSysName"),
    (0, "OLIVETTI-MIB", "uxlms-systemrmInstName"),
    (0, "OLIVETTI-MIB", "uxlms-systemrmSubAddr"),
)
if mibBuilder.loadTexts:
    uxlms_systemrmEntry.setStatus("mandatory")


class _Uxlms_systemrmSysName_Type(DisplayString):
    """Custom type uxlms_systemrmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxlms_systemrmSysName_Type.__name__ = "DisplayString"
_Uxlms_systemrmSysName_Object = MibScalar
uxlms_systemrmSysName = _Uxlms_systemrmSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 7, 0, 1, 1, 1),
    _Uxlms_systemrmSysName_Type()
)
uxlms_systemrmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlms_systemrmSysName.setStatus("mandatory")


class _Uxlms_systemrmInstName_Type(DisplayString):
    """Custom type uxlms_systemrmInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxlms_systemrmInstName_Type.__name__ = "DisplayString"
_Uxlms_systemrmInstName_Object = MibScalar
uxlms_systemrmInstName = _Uxlms_systemrmInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 7, 0, 1, 1, 2),
    _Uxlms_systemrmInstName_Type()
)
uxlms_systemrmInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlms_systemrmInstName.setStatus("mandatory")


class _Uxlms_systemrmSubAddr_Type(DisplayString):
    """Custom type uxlms_systemrmSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxlms_systemrmSubAddr_Type.__name__ = "DisplayString"
_Uxlms_systemrmSubAddr_Object = MibScalar
uxlms_systemrmSubAddr = _Uxlms_systemrmSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 7, 0, 1, 1, 3),
    _Uxlms_systemrmSubAddr_Type()
)
uxlms_systemrmSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlms_systemrmSubAddr.setStatus("mandatory")
_Uxlms_nms_ObjectIdentity = ObjectIdentity
uxlms_nms = _Uxlms_nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 12)
)
_Uxlms_sdrm_ObjectIdentity = ObjectIdentity
uxlms_sdrm = _Uxlms_sdrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 12, 2)
)
_Uxlms_sdrmTable_Object = MibTable
uxlms_sdrmTable = _Uxlms_sdrmTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 12, 2, 1)
)
if mibBuilder.loadTexts:
    uxlms_sdrmTable.setStatus("mandatory")
_Uxlms_sdrmEntry_Object = MibTableRow
uxlms_sdrmEntry = _Uxlms_sdrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 12, 2, 1, 1)
)
uxlms_sdrmEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxlms-sdrmSysName"),
    (0, "OLIVETTI-MIB", "uxlms-sdrmInstName"),
    (0, "OLIVETTI-MIB", "uxlms-sdrmSubAddr"),
)
if mibBuilder.loadTexts:
    uxlms_sdrmEntry.setStatus("mandatory")


class _Uxlms_sdrmSysName_Type(DisplayString):
    """Custom type uxlms_sdrmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxlms_sdrmSysName_Type.__name__ = "DisplayString"
_Uxlms_sdrmSysName_Object = MibScalar
uxlms_sdrmSysName = _Uxlms_sdrmSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 12, 2, 1, 1, 1),
    _Uxlms_sdrmSysName_Type()
)
uxlms_sdrmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlms_sdrmSysName.setStatus("mandatory")


class _Uxlms_sdrmInstName_Type(DisplayString):
    """Custom type uxlms_sdrmInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxlms_sdrmInstName_Type.__name__ = "DisplayString"
_Uxlms_sdrmInstName_Object = MibScalar
uxlms_sdrmInstName = _Uxlms_sdrmInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 12, 2, 1, 1, 2),
    _Uxlms_sdrmInstName_Type()
)
uxlms_sdrmInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlms_sdrmInstName.setStatus("mandatory")


class _Uxlms_sdrmSubAddr_Type(DisplayString):
    """Custom type uxlms_sdrmSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxlms_sdrmSubAddr_Type.__name__ = "DisplayString"
_Uxlms_sdrmSubAddr_Object = MibScalar
uxlms_sdrmSubAddr = _Uxlms_sdrmSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 12, 2, 1, 1, 3),
    _Uxlms_sdrmSubAddr_Type()
)
uxlms_sdrmSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlms_sdrmSubAddr.setStatus("mandatory")
_Uxlmx_LM_ObjectIdentity = ObjectIdentity
uxlmx_LM = _Uxlmx_LM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13)
)
_Uxlmx_SRVLM_ObjectIdentity = ObjectIdentity
uxlmx_SRVLM = _Uxlmx_SRVLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101)
)
_Uxlmx_SRVLMTable_Object = MibTable
uxlmx_SRVLMTable = _Uxlmx_SRVLMTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1)
)
if mibBuilder.loadTexts:
    uxlmx_SRVLMTable.setStatus("mandatory")
_Uxlmx_SRVLMEntry_Object = MibTableRow
uxlmx_SRVLMEntry = _Uxlmx_SRVLMEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1)
)
uxlmx_SRVLMEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxlmx-SRVLMSysName"),
    (0, "OLIVETTI-MIB", "uxlmx-SRVLMInstName"),
    (0, "OLIVETTI-MIB", "uxlmx-SRVLMSubAddr"),
)
if mibBuilder.loadTexts:
    uxlmx_SRVLMEntry.setStatus("mandatory")


class _Uxlmx_SRVLMSysName_Type(DisplayString):
    """Custom type uxlmx_SRVLMSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxlmx_SRVLMSysName_Type.__name__ = "DisplayString"
_Uxlmx_SRVLMSysName_Object = MibScalar
uxlmx_SRVLMSysName = _Uxlmx_SRVLMSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 1),
    _Uxlmx_SRVLMSysName_Type()
)
uxlmx_SRVLMSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_SRVLMSysName.setStatus("mandatory")


class _Uxlmx_SRVLMInstName_Type(DisplayString):
    """Custom type uxlmx_SRVLMInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxlmx_SRVLMInstName_Type.__name__ = "DisplayString"
_Uxlmx_SRVLMInstName_Object = MibScalar
uxlmx_SRVLMInstName = _Uxlmx_SRVLMInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 2),
    _Uxlmx_SRVLMInstName_Type()
)
uxlmx_SRVLMInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_SRVLMInstName.setStatus("mandatory")


class _Uxlmx_SRVLMSubAddr_Type(DisplayString):
    """Custom type uxlmx_SRVLMSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxlmx_SRVLMSubAddr_Type.__name__ = "DisplayString"
_Uxlmx_SRVLMSubAddr_Object = MibScalar
uxlmx_SRVLMSubAddr = _Uxlmx_SRVLMSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 3),
    _Uxlmx_SRVLMSubAddr_Type()
)
uxlmx_SRVLMSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_SRVLMSubAddr.setStatus("mandatory")
_Uxlmx_wknumNCBs_Type = Counter32
_Uxlmx_wknumNCBs_Object = MibScalar
uxlmx_wknumNCBs = _Uxlmx_wknumNCBs_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 4),
    _Uxlmx_wknumNCBs_Type()
)
uxlmx_wknumNCBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wknumNCBs.setStatus("mandatory")
_Uxlmx_wkfiNCBs_Type = Counter32
_Uxlmx_wkfiNCBs_Object = MibScalar
uxlmx_wkfiNCBs = _Uxlmx_wkfiNCBs_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 5),
    _Uxlmx_wkfiNCBs_Type()
)
uxlmx_wkfiNCBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wkfiNCBs.setStatus("mandatory")
_Uxlmx_wkfcNCBs_Type = Counter32
_Uxlmx_wkfcNCBs_Object = MibScalar
uxlmx_wkfcNCBs = _Uxlmx_wkfcNCBs_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 6),
    _Uxlmx_wkfcNCBs_Type()
)
uxlmx_wkfcNCBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wkfcNCBs.setStatus("mandatory")
_Uxlmx_wksesstart_Type = Counter32
_Uxlmx_wksesstart_Object = MibScalar
uxlmx_wksesstart = _Uxlmx_wksesstart_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 7),
    _Uxlmx_wksesstart_Type()
)
uxlmx_wksesstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wksesstart.setStatus("mandatory")
_Uxlmx_wksessfail_Type = Counter32
_Uxlmx_wksessfail_Object = MibScalar
uxlmx_wksessfail = _Uxlmx_wksessfail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 8),
    _Uxlmx_wksessfail_Type()
)
uxlmx_wksessfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wksessfail.setStatus("mandatory")
_Uxlmx_wkuses_Type = Counter32
_Uxlmx_wkuses_Object = MibScalar
uxlmx_wkuses = _Uxlmx_wkuses_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 9),
    _Uxlmx_wkuses_Type()
)
uxlmx_wkuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wkuses.setStatus("mandatory")
_Uxlmx_wkusefail_Type = Counter32
_Uxlmx_wkusefail_Object = MibScalar
uxlmx_wkusefail = _Uxlmx_wkusefail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 10),
    _Uxlmx_wkusefail_Type()
)
uxlmx_wkusefail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wkusefail.setStatus("mandatory")
_Uxlmx_wkautorec_Type = Counter32
_Uxlmx_wkautorec_Object = MibScalar
uxlmx_wkautorec = _Uxlmx_wkautorec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 11),
    _Uxlmx_wkautorec_Type()
)
uxlmx_wkautorec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_wkautorec.setStatus("mandatory")
_Uxlmx_svfopens_Type = Counter32
_Uxlmx_svfopens_Object = MibScalar
uxlmx_svfopens = _Uxlmx_svfopens_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 12),
    _Uxlmx_svfopens_Type()
)
uxlmx_svfopens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svfopens.setStatus("mandatory")
_Uxlmx_svdevopens_Type = Counter32
_Uxlmx_svdevopens_Object = MibScalar
uxlmx_svdevopens = _Uxlmx_svdevopens_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 13),
    _Uxlmx_svdevopens_Type()
)
uxlmx_svdevopens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svdevopens.setStatus("mandatory")
_Uxlmx_svjobsqueued_Type = Counter32
_Uxlmx_svjobsqueued_Object = MibScalar
uxlmx_svjobsqueued = _Uxlmx_svjobsqueued_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 14),
    _Uxlmx_svjobsqueued_Type()
)
uxlmx_svjobsqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svjobsqueued.setStatus("mandatory")
_Uxlmx_svsopens_Type = Counter32
_Uxlmx_svsopens_Object = MibScalar
uxlmx_svsopens = _Uxlmx_svsopens_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 15),
    _Uxlmx_svsopens_Type()
)
uxlmx_svsopens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svsopens.setStatus("mandatory")
_Uxlmx_svstimedout_Type = Counter32
_Uxlmx_svstimedout_Object = MibScalar
uxlmx_svstimedout = _Uxlmx_svstimedout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 16),
    _Uxlmx_svstimedout_Type()
)
uxlmx_svstimedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svstimedout.setStatus("mandatory")
_Uxlmx_svserrorout_Type = Counter32
_Uxlmx_svserrorout_Object = MibScalar
uxlmx_svserrorout = _Uxlmx_svserrorout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 17),
    _Uxlmx_svserrorout_Type()
)
uxlmx_svserrorout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svserrorout.setStatus("mandatory")
_Uxlmx_svpwerrors_Type = Counter32
_Uxlmx_svpwerrors_Object = MibScalar
uxlmx_svpwerrors = _Uxlmx_svpwerrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 18),
    _Uxlmx_svpwerrors_Type()
)
uxlmx_svpwerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svpwerrors.setStatus("mandatory")
_Uxlmx_svpermerrors_Type = Counter32
_Uxlmx_svpermerrors_Object = MibScalar
uxlmx_svpermerrors = _Uxlmx_svpermerrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 19),
    _Uxlmx_svpermerrors_Type()
)
uxlmx_svpermerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svpermerrors.setStatus("mandatory")
_Uxlmx_svsyserrors_Type = Counter32
_Uxlmx_svsyserrors_Object = MibScalar
uxlmx_svsyserrors = _Uxlmx_svsyserrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 20),
    _Uxlmx_svsyserrors_Type()
)
uxlmx_svsyserrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svsyserrors.setStatus("mandatory")
_Uxlmx_svbytessent_Type = Counter32
_Uxlmx_svbytessent_Object = MibScalar
uxlmx_svbytessent = _Uxlmx_svbytessent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 21),
    _Uxlmx_svbytessent_Type()
)
uxlmx_svbytessent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svbytessent.setStatus("mandatory")
_Uxlmx_svbytesrcvd_Type = Counter32
_Uxlmx_svbytesrcvd_Object = MibScalar
uxlmx_svbytesrcvd = _Uxlmx_svbytesrcvd_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 22),
    _Uxlmx_svbytesrcvd_Type()
)
uxlmx_svbytesrcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svbytesrcvd.setStatus("mandatory")
_Uxlmx_svavresponse_Type = Counter32
_Uxlmx_svavresponse_Object = MibScalar
uxlmx_svavresponse = _Uxlmx_svavresponse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 13, 101, 1, 1, 23),
    _Uxlmx_svavresponse_Type()
)
uxlmx_svavresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlmx_svavresponse.setStatus("mandatory")
_Wan_ObjectIdentity = ObjectIdentity
wan = _Wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15)
)
_Lapb_ObjectIdentity = ObjectIdentity
lapb = _Lapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2)
)
_LapbTable_Object = MibTable
lapbTable = _LapbTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1)
)
if mibBuilder.loadTexts:
    lapbTable.setStatus("mandatory")
_LapbEntry_Object = MibTableRow
lapbEntry = _LapbEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1)
)
lapbEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxlapb-lapbSysName"),
    (0, "OLIVETTI-MIB", "uxlapb-lapbInstName"),
    (0, "OLIVETTI-MIB", "uxlapb-lapbSubAddr"),
)
if mibBuilder.loadTexts:
    lapbEntry.setStatus("mandatory")


class _Uxlapb_lapbSysName_Type(DisplayString):
    """Custom type uxlapb_lapbSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxlapb_lapbSysName_Type.__name__ = "DisplayString"
_Uxlapb_lapbSysName_Object = MibScalar
uxlapb_lapbSysName = _Uxlapb_lapbSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 1),
    _Uxlapb_lapbSysName_Type()
)
uxlapb_lapbSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_lapbSysName.setStatus("mandatory")


class _Uxlapb_lapbInstName_Type(DisplayString):
    """Custom type uxlapb_lapbInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxlapb_lapbInstName_Type.__name__ = "DisplayString"
_Uxlapb_lapbInstName_Object = MibScalar
uxlapb_lapbInstName = _Uxlapb_lapbInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 2),
    _Uxlapb_lapbInstName_Type()
)
uxlapb_lapbInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_lapbInstName.setStatus("mandatory")


class _Uxlapb_lapbSubAddr_Type(DisplayString):
    """Custom type uxlapb_lapbSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxlapb_lapbSubAddr_Type.__name__ = "DisplayString"
_Uxlapb_lapbSubAddr_Object = MibScalar
uxlapb_lapbSubAddr = _Uxlapb_lapbSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 3),
    _Uxlapb_lapbSubAddr_Type()
)
uxlapb_lapbSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_lapbSubAddr.setStatus("mandatory")
_Uxlapb_numOfzerotime_Type = Counter32
_Uxlapb_numOfzerotime_Object = MibScalar
uxlapb_numOfzerotime = _Uxlapb_numOfzerotime_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 4),
    _Uxlapb_numOfzerotime_Type()
)
uxlapb_numOfzerotime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfzerotime.setStatus("mandatory")
_Uxlapb_numOfinfosent_Type = Counter32
_Uxlapb_numOfinfosent_Object = MibScalar
uxlapb_numOfinfosent = _Uxlapb_numOfinfosent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 5),
    _Uxlapb_numOfinfosent_Type()
)
uxlapb_numOfinfosent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfinfosent.setStatus("mandatory")
_Uxlapb_numOfinforece_Type = Counter32
_Uxlapb_numOfinforece_Object = MibScalar
uxlapb_numOfinforece = _Uxlapb_numOfinforece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 6),
    _Uxlapb_numOfinforece_Type()
)
uxlapb_numOfinforece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfinforece.setStatus("mandatory")
_Uxlapb_numOfrrsent_Type = Counter32
_Uxlapb_numOfrrsent_Object = MibScalar
uxlapb_numOfrrsent = _Uxlapb_numOfrrsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 7),
    _Uxlapb_numOfrrsent_Type()
)
uxlapb_numOfrrsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfrrsent.setStatus("mandatory")
_Uxlapb_numOfrrrece_Type = Counter32
_Uxlapb_numOfrrrece_Object = MibScalar
uxlapb_numOfrrrece = _Uxlapb_numOfrrrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 8),
    _Uxlapb_numOfrrrece_Type()
)
uxlapb_numOfrrrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfrrrece.setStatus("mandatory")
_Uxlapb_numOfrnrsent_Type = Counter32
_Uxlapb_numOfrnrsent_Object = MibScalar
uxlapb_numOfrnrsent = _Uxlapb_numOfrnrsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 9),
    _Uxlapb_numOfrnrsent_Type()
)
uxlapb_numOfrnrsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfrnrsent.setStatus("mandatory")
_Uxlapb_numOfrnrrece_Type = Counter32
_Uxlapb_numOfrnrrece_Object = MibScalar
uxlapb_numOfrnrrece = _Uxlapb_numOfrnrrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 10),
    _Uxlapb_numOfrnrrece_Type()
)
uxlapb_numOfrnrrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfrnrrece.setStatus("mandatory")
_Uxlapb_numOfSABMitsent_Type = Counter32
_Uxlapb_numOfSABMitsent_Object = MibScalar
uxlapb_numOfSABMitsent = _Uxlapb_numOfSABMitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 11),
    _Uxlapb_numOfSABMitsent_Type()
)
uxlapb_numOfSABMitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfSABMitsent.setStatus("mandatory")
_Uxlapb_numOfSABMnitsent_Type = Counter32
_Uxlapb_numOfSABMnitsent_Object = MibScalar
uxlapb_numOfSABMnitsent = _Uxlapb_numOfSABMnitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 12),
    _Uxlapb_numOfSABMnitsent_Type()
)
uxlapb_numOfSABMnitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfSABMnitsent.setStatus("mandatory")
_Uxlapb_numOfSABMitrece_Type = Counter32
_Uxlapb_numOfSABMitrece_Object = MibScalar
uxlapb_numOfSABMitrece = _Uxlapb_numOfSABMitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 13),
    _Uxlapb_numOfSABMitrece_Type()
)
uxlapb_numOfSABMitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfSABMitrece.setStatus("mandatory")
_Uxlapb_numOfSABMnitrece_Type = Counter32
_Uxlapb_numOfSABMnitrece_Object = MibScalar
uxlapb_numOfSABMnitrece = _Uxlapb_numOfSABMnitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 14),
    _Uxlapb_numOfSABMnitrece_Type()
)
uxlapb_numOfSABMnitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfSABMnitrece.setStatus("mandatory")
_Uxlapb_numOfDISCitsent_Type = Counter32
_Uxlapb_numOfDISCitsent_Object = MibScalar
uxlapb_numOfDISCitsent = _Uxlapb_numOfDISCitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 15),
    _Uxlapb_numOfDISCitsent_Type()
)
uxlapb_numOfDISCitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDISCitsent.setStatus("mandatory")
_Uxlapb_numOfDISCnitsent_Type = Counter32
_Uxlapb_numOfDISCnitsent_Object = MibScalar
uxlapb_numOfDISCnitsent = _Uxlapb_numOfDISCnitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 16),
    _Uxlapb_numOfDISCnitsent_Type()
)
uxlapb_numOfDISCnitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDISCnitsent.setStatus("mandatory")
_Uxlapb_numOfDISCitrece_Type = Counter32
_Uxlapb_numOfDISCitrece_Object = MibScalar
uxlapb_numOfDISCitrece = _Uxlapb_numOfDISCitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 17),
    _Uxlapb_numOfDISCitrece_Type()
)
uxlapb_numOfDISCitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDISCitrece.setStatus("mandatory")
_Uxlapb_numOfDISCnitrece_Type = Counter32
_Uxlapb_numOfDISCnitrece_Object = MibScalar
uxlapb_numOfDISCnitrece = _Uxlapb_numOfDISCnitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 18),
    _Uxlapb_numOfDISCnitrece_Type()
)
uxlapb_numOfDISCnitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDISCnitrece.setStatus("mandatory")
_Uxlapb_numOfUAitsent_Type = Counter32
_Uxlapb_numOfUAitsent_Object = MibScalar
uxlapb_numOfUAitsent = _Uxlapb_numOfUAitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 19),
    _Uxlapb_numOfUAitsent_Type()
)
uxlapb_numOfUAitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfUAitsent.setStatus("mandatory")
_Uxlapb_numOfUAnitsent_Type = Counter32
_Uxlapb_numOfUAnitsent_Object = MibScalar
uxlapb_numOfUAnitsent = _Uxlapb_numOfUAnitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 20),
    _Uxlapb_numOfUAnitsent_Type()
)
uxlapb_numOfUAnitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfUAnitsent.setStatus("mandatory")
_Uxlapb_numOfUAitrece_Type = Counter32
_Uxlapb_numOfUAitrece_Object = MibScalar
uxlapb_numOfUAitrece = _Uxlapb_numOfUAitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 21),
    _Uxlapb_numOfUAitrece_Type()
)
uxlapb_numOfUAitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfUAitrece.setStatus("mandatory")
_Uxlapb_numOfUAnitrece_Type = Counter32
_Uxlapb_numOfUAnitrece_Object = MibScalar
uxlapb_numOfUAnitrece = _Uxlapb_numOfUAnitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 22),
    _Uxlapb_numOfUAnitrece_Type()
)
uxlapb_numOfUAnitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfUAnitrece.setStatus("mandatory")
_Uxlapb_numOfDMitsent_Type = Counter32
_Uxlapb_numOfDMitsent_Object = MibScalar
uxlapb_numOfDMitsent = _Uxlapb_numOfDMitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 23),
    _Uxlapb_numOfDMitsent_Type()
)
uxlapb_numOfDMitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDMitsent.setStatus("mandatory")
_Uxlapb_numOfDMnitsent_Type = Counter32
_Uxlapb_numOfDMnitsent_Object = MibScalar
uxlapb_numOfDMnitsent = _Uxlapb_numOfDMnitsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 24),
    _Uxlapb_numOfDMnitsent_Type()
)
uxlapb_numOfDMnitsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDMnitsent.setStatus("mandatory")
_Uxlapb_numOfDMitrece_Type = Counter32
_Uxlapb_numOfDMitrece_Object = MibScalar
uxlapb_numOfDMitrece = _Uxlapb_numOfDMitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 25),
    _Uxlapb_numOfDMitrece_Type()
)
uxlapb_numOfDMitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDMitrece.setStatus("mandatory")
_Uxlapb_numOfDMnitrece_Type = Counter32
_Uxlapb_numOfDMnitrece_Object = MibScalar
uxlapb_numOfDMnitrece = _Uxlapb_numOfDMnitrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 26),
    _Uxlapb_numOfDMnitrece_Type()
)
uxlapb_numOfDMnitrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfDMnitrece.setStatus("mandatory")
_Uxlapb_numOffrmrsent_Type = Counter32
_Uxlapb_numOffrmrsent_Object = MibScalar
uxlapb_numOffrmrsent = _Uxlapb_numOffrmrsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 27),
    _Uxlapb_numOffrmrsent_Type()
)
uxlapb_numOffrmrsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOffrmrsent.setStatus("mandatory")
_Uxlapb_numOffrmrrece_Type = Counter32
_Uxlapb_numOffrmrrece_Object = MibScalar
uxlapb_numOffrmrrece = _Uxlapb_numOffrmrrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 28),
    _Uxlapb_numOffrmrrece_Type()
)
uxlapb_numOffrmrrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOffrmrrece.setStatus("mandatory")
_Uxlapb_numOfrejsent_Type = Counter32
_Uxlapb_numOfrejsent_Object = MibScalar
uxlapb_numOfrejsent = _Uxlapb_numOfrejsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 29),
    _Uxlapb_numOfrejsent_Type()
)
uxlapb_numOfrejsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfrejsent.setStatus("mandatory")
_Uxlapb_numOfrejrece_Type = Counter32
_Uxlapb_numOfrejrece_Object = MibScalar
uxlapb_numOfrejrece = _Uxlapb_numOfrejrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 30),
    _Uxlapb_numOfrejrece_Type()
)
uxlapb_numOfrejrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfrejrece.setStatus("mandatory")
_Uxlapb_numOfbusycondet_Type = Counter32
_Uxlapb_numOfbusycondet_Object = MibScalar
uxlapb_numOfbusycondet = _Uxlapb_numOfbusycondet_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 31),
    _Uxlapb_numOfbusycondet_Type()
)
uxlapb_numOfbusycondet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfbusycondet.setStatus("mandatory")
_Uxlapb_numOfbusyconent_Type = Counter32
_Uxlapb_numOfbusyconent_Object = MibScalar
uxlapb_numOfbusyconent = _Uxlapb_numOfbusyconent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 32),
    _Uxlapb_numOfbusyconent_Type()
)
uxlapb_numOfbusyconent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfbusyconent.setStatus("mandatory")
_Uxlapb_numOfdataoctsent_Type = Counter32
_Uxlapb_numOfdataoctsent_Object = MibScalar
uxlapb_numOfdataoctsent = _Uxlapb_numOfdataoctsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 33),
    _Uxlapb_numOfdataoctsent_Type()
)
uxlapb_numOfdataoctsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfdataoctsent.setStatus("mandatory")
_Uxlapb_numOfdataoctrece_Type = Counter32
_Uxlapb_numOfdataoctrece_Object = MibScalar
uxlapb_numOfdataoctrece = _Uxlapb_numOfdataoctrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 34),
    _Uxlapb_numOfdataoctrece_Type()
)
uxlapb_numOfdataoctrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfdataoctrece.setStatus("mandatory")
_Uxlapb_numOfoutsequence_Type = Counter32
_Uxlapb_numOfoutsequence_Object = MibScalar
uxlapb_numOfoutsequence = _Uxlapb_numOfoutsequence_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 35),
    _Uxlapb_numOfoutsequence_Type()
)
uxlapb_numOfoutsequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfoutsequence.setStatus("mandatory")
_Uxlapb_numOfretrframes_Type = Counter32
_Uxlapb_numOfretrframes_Object = MibScalar
uxlapb_numOfretrframes = _Uxlapb_numOfretrframes_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 36),
    _Uxlapb_numOfretrframes_Type()
)
uxlapb_numOfretrframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfretrframes.setStatus("mandatory")
_Uxlapb_numOfinvalidframes_Type = Counter32
_Uxlapb_numOfinvalidframes_Object = MibScalar
uxlapb_numOfinvalidframes = _Uxlapb_numOfinvalidframes_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 37),
    _Uxlapb_numOfinvalidframes_Type()
)
uxlapb_numOfinvalidframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfinvalidframes.setStatus("mandatory")
_Uxlapb_numOfphystxerrors_Type = Counter32
_Uxlapb_numOfphystxerrors_Object = MibScalar
uxlapb_numOfphystxerrors = _Uxlapb_numOfphystxerrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 38),
    _Uxlapb_numOfphystxerrors_Type()
)
uxlapb_numOfphystxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfphystxerrors.setStatus("mandatory")
_Uxlapb_numOfReserved1_Type = Counter32
_Uxlapb_numOfReserved1_Object = MibScalar
uxlapb_numOfReserved1 = _Uxlapb_numOfReserved1_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 39),
    _Uxlapb_numOfReserved1_Type()
)
uxlapb_numOfReserved1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfReserved1.setStatus("mandatory")
_Uxlapb_numOfReserved2_Type = Counter32
_Uxlapb_numOfReserved2_Object = MibScalar
uxlapb_numOfReserved2 = _Uxlapb_numOfReserved2_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 40),
    _Uxlapb_numOfReserved2_Type()
)
uxlapb_numOfReserved2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfReserved2.setStatus("mandatory")
_Uxlapb_numOfReserved3_Type = Counter32
_Uxlapb_numOfReserved3_Object = MibScalar
uxlapb_numOfReserved3 = _Uxlapb_numOfReserved3_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 41),
    _Uxlapb_numOfReserved3_Type()
)
uxlapb_numOfReserved3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfReserved3.setStatus("mandatory")
_Uxlapb_numOfReserved4_Type = Counter32
_Uxlapb_numOfReserved4_Object = MibScalar
uxlapb_numOfReserved4 = _Uxlapb_numOfReserved4_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 42),
    _Uxlapb_numOfReserved4_Type()
)
uxlapb_numOfReserved4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfReserved4.setStatus("mandatory")
_Uxlapb_numOfInformatype_Type = Counter32
_Uxlapb_numOfInformatype_Object = MibScalar
uxlapb_numOfInformatype = _Uxlapb_numOfInformatype_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 2, 1, 1, 43),
    _Uxlapb_numOfInformatype_Type()
)
uxlapb_numOfInformatype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxlapb_numOfInformatype.setStatus("mandatory")
_X25_ObjectIdentity = ObjectIdentity
x25 = _X25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3)
)
_X25Table_Object = MibTable
x25Table = _X25Table_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1)
)
if mibBuilder.loadTexts:
    x25Table.setStatus("mandatory")
_X25Entry_Object = MibTableRow
x25Entry = _X25Entry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1)
)
x25Entry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxx25-x25SysName"),
    (0, "OLIVETTI-MIB", "uxx25-x25InstName"),
    (0, "OLIVETTI-MIB", "uxx25-x25SubAddr"),
)
if mibBuilder.loadTexts:
    x25Entry.setStatus("mandatory")


class _Uxx25_x25SysName_Type(DisplayString):
    """Custom type uxx25_x25SysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxx25_x25SysName_Type.__name__ = "DisplayString"
_Uxx25_x25SysName_Object = MibScalar
uxx25_x25SysName = _Uxx25_x25SysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 1),
    _Uxx25_x25SysName_Type()
)
uxx25_x25SysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_x25SysName.setStatus("mandatory")


class _Uxx25_x25InstName_Type(DisplayString):
    """Custom type uxx25_x25InstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxx25_x25InstName_Type.__name__ = "DisplayString"
_Uxx25_x25InstName_Object = MibScalar
uxx25_x25InstName = _Uxx25_x25InstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 2),
    _Uxx25_x25InstName_Type()
)
uxx25_x25InstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_x25InstName.setStatus("mandatory")


class _Uxx25_x25SubAddr_Type(DisplayString):
    """Custom type uxx25_x25SubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxx25_x25SubAddr_Type.__name__ = "DisplayString"
_Uxx25_x25SubAddr_Object = MibScalar
uxx25_x25SubAddr = _Uxx25_x25SubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 3),
    _Uxx25_x25SubAddr_Type()
)
uxx25_x25SubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_x25SubAddr.setStatus("mandatory")
_Uxx25_numOfzerot_Type = Counter32
_Uxx25_numOfzerot_Object = MibScalar
uxx25_numOfzerot = _Uxx25_numOfzerot_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 4),
    _Uxx25_numOfzerot_Type()
)
uxx25_numOfzerot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfzerot.setStatus("mandatory")
_Uxx25_numOfrestsent_Type = Counter32
_Uxx25_numOfrestsent_Object = MibScalar
uxx25_numOfrestsent = _Uxx25_numOfrestsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 5),
    _Uxx25_numOfrestsent_Type()
)
uxx25_numOfrestsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrestsent.setStatus("mandatory")
_Uxx25_numOfrestrece_Type = Counter32
_Uxx25_numOfrestrece_Object = MibScalar
uxx25_numOfrestrece = _Uxx25_numOfrestrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 6),
    _Uxx25_numOfrestrece_Type()
)
uxx25_numOfrestrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrestrece.setStatus("mandatory")
_Uxx25_numOfcallsent_Type = Counter32
_Uxx25_numOfcallsent_Object = MibScalar
uxx25_numOfcallsent = _Uxx25_numOfcallsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 7),
    _Uxx25_numOfcallsent_Type()
)
uxx25_numOfcallsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfcallsent.setStatus("mandatory")
_Uxx25_numOfcallrece_Type = Counter32
_Uxx25_numOfcallrece_Object = MibScalar
uxx25_numOfcallrece = _Uxx25_numOfcallrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 8),
    _Uxx25_numOfcallrece_Type()
)
uxx25_numOfcallrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfcallrece.setStatus("mandatory")
_Uxx25_numOfclearsent_Type = Counter32
_Uxx25_numOfclearsent_Object = MibScalar
uxx25_numOfclearsent = _Uxx25_numOfclearsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 9),
    _Uxx25_numOfclearsent_Type()
)
uxx25_numOfclearsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfclearsent.setStatus("mandatory")
_Uxx25_numOfclearrece_Type = Counter32
_Uxx25_numOfclearrece_Object = MibScalar
uxx25_numOfclearrece = _Uxx25_numOfclearrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 10),
    _Uxx25_numOfclearrece_Type()
)
uxx25_numOfclearrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfclearrece.setStatus("mandatory")
_Uxx25_numOfdatasent_Type = Counter32
_Uxx25_numOfdatasent_Object = MibScalar
uxx25_numOfdatasent = _Uxx25_numOfdatasent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 11),
    _Uxx25_numOfdatasent_Type()
)
uxx25_numOfdatasent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfdatasent.setStatus("mandatory")
_Uxx25_numOfdatarece_Type = Counter32
_Uxx25_numOfdatarece_Object = MibScalar
uxx25_numOfdatarece = _Uxx25_numOfdatarece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 12),
    _Uxx25_numOfdatarece_Type()
)
uxx25_numOfdatarece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfdatarece.setStatus("mandatory")
_Uxx25_numOfoctsent_Type = Counter32
_Uxx25_numOfoctsent_Object = MibScalar
uxx25_numOfoctsent = _Uxx25_numOfoctsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 13),
    _Uxx25_numOfoctsent_Type()
)
uxx25_numOfoctsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfoctsent.setStatus("mandatory")
_Uxx25_numOfoctrece_Type = Counter32
_Uxx25_numOfoctrece_Object = MibScalar
uxx25_numOfoctrece = _Uxx25_numOfoctrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 14),
    _Uxx25_numOfoctrece_Type()
)
uxx25_numOfoctrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfoctrece.setStatus("mandatory")
_Uxx25_numOfintersent_Type = Counter32
_Uxx25_numOfintersent_Object = MibScalar
uxx25_numOfintersent = _Uxx25_numOfintersent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 15),
    _Uxx25_numOfintersent_Type()
)
uxx25_numOfintersent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfintersent.setStatus("mandatory")
_Uxx25_numOfinterrece_Type = Counter32
_Uxx25_numOfinterrece_Object = MibScalar
uxx25_numOfinterrece = _Uxx25_numOfinterrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 16),
    _Uxx25_numOfinterrece_Type()
)
uxx25_numOfinterrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfinterrece.setStatus("mandatory")
_Uxx25_numOfrrxsent_Type = Counter32
_Uxx25_numOfrrxsent_Object = MibScalar
uxx25_numOfrrxsent = _Uxx25_numOfrrxsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 17),
    _Uxx25_numOfrrxsent_Type()
)
uxx25_numOfrrxsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrrxsent.setStatus("mandatory")
_Uxx25_numOfrrxrece_Type = Counter32
_Uxx25_numOfrrxrece_Object = MibScalar
uxx25_numOfrrxrece = _Uxx25_numOfrrxrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 18),
    _Uxx25_numOfrrxrece_Type()
)
uxx25_numOfrrxrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrrxrece.setStatus("mandatory")
_Uxx25_numOfrnrxsent_Type = Counter32
_Uxx25_numOfrnrxsent_Object = MibScalar
uxx25_numOfrnrxsent = _Uxx25_numOfrnrxsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 19),
    _Uxx25_numOfrnrxsent_Type()
)
uxx25_numOfrnrxsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrnrxsent.setStatus("mandatory")
_Uxx25_numOfrnrxrece_Type = Counter32
_Uxx25_numOfrnrxrece_Object = MibScalar
uxx25_numOfrnrxrece = _Uxx25_numOfrnrxrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 20),
    _Uxx25_numOfrnrxrece_Type()
)
uxx25_numOfrnrxrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrnrxrece.setStatus("mandatory")
_Uxx25_numOfresetsent_Type = Counter32
_Uxx25_numOfresetsent_Object = MibScalar
uxx25_numOfresetsent = _Uxx25_numOfresetsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 21),
    _Uxx25_numOfresetsent_Type()
)
uxx25_numOfresetsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfresetsent.setStatus("mandatory")
_Uxx25_numOfresetrece_Type = Counter32
_Uxx25_numOfresetrece_Object = MibScalar
uxx25_numOfresetrece = _Uxx25_numOfresetrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 22),
    _Uxx25_numOfresetrece_Type()
)
uxx25_numOfresetrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfresetrece.setStatus("mandatory")
_Uxx25_numOfrejxsent_Type = Counter32
_Uxx25_numOfrejxsent_Object = MibScalar
uxx25_numOfrejxsent = _Uxx25_numOfrejxsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 23),
    _Uxx25_numOfrejxsent_Type()
)
uxx25_numOfrejxsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrejxsent.setStatus("mandatory")
_Uxx25_numOfrejxrece_Type = Counter32
_Uxx25_numOfrejxrece_Object = MibScalar
uxx25_numOfrejxrece = _Uxx25_numOfrejxrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 24),
    _Uxx25_numOfrejxrece_Type()
)
uxx25_numOfrejxrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrejxrece.setStatus("mandatory")
_Uxx25_numOfdiagnsent_Type = Counter32
_Uxx25_numOfdiagnsent_Object = MibScalar
uxx25_numOfdiagnsent = _Uxx25_numOfdiagnsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 25),
    _Uxx25_numOfdiagnsent_Type()
)
uxx25_numOfdiagnsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfdiagnsent.setStatus("mandatory")
_Uxx25_numOfdiagnrece_Type = Counter32
_Uxx25_numOfdiagnrece_Object = MibScalar
uxx25_numOfdiagnrece = _Uxx25_numOfdiagnrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 26),
    _Uxx25_numOfdiagnrece_Type()
)
uxx25_numOfdiagnrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfdiagnrece.setStatus("mandatory")
_Uxx25_numOfregistsent_Type = Counter32
_Uxx25_numOfregistsent_Object = MibScalar
uxx25_numOfregistsent = _Uxx25_numOfregistsent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 27),
    _Uxx25_numOfregistsent_Type()
)
uxx25_numOfregistsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfregistsent.setStatus("mandatory")
_Uxx25_numOfregistrece_Type = Counter32
_Uxx25_numOfregistrece_Object = MibScalar
uxx25_numOfregistrece = _Uxx25_numOfregistrece_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 28),
    _Uxx25_numOfregistrece_Type()
)
uxx25_numOfregistrece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfregistrece.setStatus("mandatory")
_Uxx25_numOfrestretries_Type = Counter32
_Uxx25_numOfrestretries_Object = MibScalar
uxx25_numOfrestretries = _Uxx25_numOfrestretries_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 29),
    _Uxx25_numOfrestretries_Type()
)
uxx25_numOfrestretries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrestretries.setStatus("mandatory")
_Uxx25_numOfrestunsucfull_Type = Counter32
_Uxx25_numOfrestunsucfull_Object = MibScalar
uxx25_numOfrestunsucfull = _Uxx25_numOfrestunsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 30),
    _Uxx25_numOfrestunsucfull_Type()
)
uxx25_numOfrestunsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrestunsucfull.setStatus("mandatory")
_Uxx25_numOfsyntaxerrors_Type = Counter32
_Uxx25_numOfsyntaxerrors_Object = MibScalar
uxx25_numOfsyntaxerrors = _Uxx25_numOfsyntaxerrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 31),
    _Uxx25_numOfsyntaxerrors_Type()
)
uxx25_numOfsyntaxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfsyntaxerrors.setStatus("mandatory")
_Uxx25_numOflogicalerrors_Type = Counter32
_Uxx25_numOflogicalerrors_Object = MibScalar
uxx25_numOflogicalerrors = _Uxx25_numOflogicalerrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 32),
    _Uxx25_numOflogicalerrors_Type()
)
uxx25_numOflogicalerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOflogicalerrors.setStatus("mandatory")
_Uxx25_numOfcallunsucfull_Type = Counter32
_Uxx25_numOfcallunsucfull_Object = MibScalar
uxx25_numOfcallunsucfull = _Uxx25_numOfcallunsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 33),
    _Uxx25_numOfcallunsucfull_Type()
)
uxx25_numOfcallunsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfcallunsucfull.setStatus("mandatory")
_Uxx25_numOfclearretries_Type = Counter32
_Uxx25_numOfclearretries_Object = MibScalar
uxx25_numOfclearretries = _Uxx25_numOfclearretries_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 34),
    _Uxx25_numOfclearretries_Type()
)
uxx25_numOfclearretries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfclearretries.setStatus("mandatory")
_Uxx25_numOfclearunsucfull_Type = Counter32
_Uxx25_numOfclearunsucfull_Object = MibScalar
uxx25_numOfclearunsucfull = _Uxx25_numOfclearunsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 35),
    _Uxx25_numOfclearunsucfull_Type()
)
uxx25_numOfclearunsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfclearunsucfull.setStatus("mandatory")
_Uxx25_numOfinterunsucfull_Type = Counter32
_Uxx25_numOfinterunsucfull_Object = MibScalar
uxx25_numOfinterunsucfull = _Uxx25_numOfinterunsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 36),
    _Uxx25_numOfinterunsucfull_Type()
)
uxx25_numOfinterunsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfinterunsucfull.setStatus("mandatory")
_Uxx25_numOfresetretries_Type = Counter32
_Uxx25_numOfresetretries_Object = MibScalar
uxx25_numOfresetretries = _Uxx25_numOfresetretries_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 37),
    _Uxx25_numOfresetretries_Type()
)
uxx25_numOfresetretries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfresetretries.setStatus("mandatory")
_Uxx25_numOfresetunsucfull_Type = Counter32
_Uxx25_numOfresetunsucfull_Object = MibScalar
uxx25_numOfresetunsucfull = _Uxx25_numOfresetunsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 38),
    _Uxx25_numOfresetunsucfull_Type()
)
uxx25_numOfresetunsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfresetunsucfull.setStatus("mandatory")
_Uxx25_numOfdataretrsucfull_Type = Counter32
_Uxx25_numOfdataretrsucfull_Object = MibScalar
uxx25_numOfdataretrsucfull = _Uxx25_numOfdataretrsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 39),
    _Uxx25_numOfdataretrsucfull_Type()
)
uxx25_numOfdataretrsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfdataretrsucfull.setStatus("mandatory")
_Uxx25_numOfdataretrunsucfull_Type = Counter32
_Uxx25_numOfdataretrunsucfull_Object = MibScalar
uxx25_numOfdataretrunsucfull = _Uxx25_numOfdataretrunsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 40),
    _Uxx25_numOfdataretrunsucfull_Type()
)
uxx25_numOfdataretrunsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfdataretrunsucfull.setStatus("mandatory")
_Uxx25_numOfrejretries_Type = Counter32
_Uxx25_numOfrejretries_Object = MibScalar
uxx25_numOfrejretries = _Uxx25_numOfrejretries_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 41),
    _Uxx25_numOfrejretries_Type()
)
uxx25_numOfrejretries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrejretries.setStatus("mandatory")
_Uxx25_numOfrejunsucfull_Type = Counter32
_Uxx25_numOfrejunsucfull_Object = MibScalar
uxx25_numOfrejunsucfull = _Uxx25_numOfrejunsucfull_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 42),
    _Uxx25_numOfrejunsucfull_Type()
)
uxx25_numOfrejunsucfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfrejunsucfull.setStatus("mandatory")
_Uxx25_numOfInformat_Type = Counter32
_Uxx25_numOfInformat_Object = MibScalar
uxx25_numOfInformat = _Uxx25_numOfInformat_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 3, 1, 1, 43),
    _Uxx25_numOfInformat_Type()
)
uxx25_numOfInformat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxx25_numOfInformat.setStatus("mandatory")
_Tp02_ObjectIdentity = ObjectIdentity
tp02 = _Tp02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4)
)
_Tp02Table_Object = MibTable
tp02Table = _Tp02Table_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1)
)
if mibBuilder.loadTexts:
    tp02Table.setStatus("mandatory")
_Tp02Entry_Object = MibTableRow
tp02Entry = _Tp02Entry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1)
)
tp02Entry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxtp02-tp02SysName"),
    (0, "OLIVETTI-MIB", "uxtp02-tp02InstName"),
    (0, "OLIVETTI-MIB", "uxtp02-tp02SubAddr"),
)
if mibBuilder.loadTexts:
    tp02Entry.setStatus("mandatory")


class _Uxtp02_tp02SysName_Type(DisplayString):
    """Custom type uxtp02_tp02SysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxtp02_tp02SysName_Type.__name__ = "DisplayString"
_Uxtp02_tp02SysName_Object = MibScalar
uxtp02_tp02SysName = _Uxtp02_tp02SysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 1),
    _Uxtp02_tp02SysName_Type()
)
uxtp02_tp02SysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_tp02SysName.setStatus("mandatory")


class _Uxtp02_tp02InstName_Type(DisplayString):
    """Custom type uxtp02_tp02InstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxtp02_tp02InstName_Type.__name__ = "DisplayString"
_Uxtp02_tp02InstName_Object = MibScalar
uxtp02_tp02InstName = _Uxtp02_tp02InstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 2),
    _Uxtp02_tp02InstName_Type()
)
uxtp02_tp02InstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_tp02InstName.setStatus("mandatory")


class _Uxtp02_tp02SubAddr_Type(DisplayString):
    """Custom type uxtp02_tp02SubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxtp02_tp02SubAddr_Type.__name__ = "DisplayString"
_Uxtp02_tp02SubAddr_Object = MibScalar
uxtp02_tp02SubAddr = _Uxtp02_tp02SubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 3),
    _Uxtp02_tp02SubAddr_Type()
)
uxtp02_tp02SubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_tp02SubAddr.setStatus("mandatory")
_Uxtp02_numOfzeroingtime_Type = Counter32
_Uxtp02_numOfzeroingtime_Object = MibScalar
uxtp02_numOfzeroingtime = _Uxtp02_numOfzeroingtime_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 4),
    _Uxtp02_numOfzeroingtime_Type()
)
uxtp02_numOfzeroingtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfzeroingtime.setStatus("mandatory")
_Uxtp02_numOfnumberTPDUSent_Type = Counter32
_Uxtp02_numOfnumberTPDUSent_Object = MibScalar
uxtp02_numOfnumberTPDUSent = _Uxtp02_numOfnumberTPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 5),
    _Uxtp02_numOfnumberTPDUSent_Type()
)
uxtp02_numOfnumberTPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfnumberTPDUSent.setStatus("mandatory")
_Uxtp02_numOfnumberTPDUReceived_Type = Counter32
_Uxtp02_numOfnumberTPDUReceived_Object = MibScalar
uxtp02_numOfnumberTPDUReceived = _Uxtp02_numOfnumberTPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 6),
    _Uxtp02_numOfnumberTPDUReceived_Type()
)
uxtp02_numOfnumberTPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfnumberTPDUReceived.setStatus("mandatory")
_Uxtp02_numOftDataSent_Type = Counter32
_Uxtp02_numOftDataSent_Object = MibScalar
uxtp02_numOftDataSent = _Uxtp02_numOftDataSent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 7),
    _Uxtp02_numOftDataSent_Type()
)
uxtp02_numOftDataSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOftDataSent.setStatus("mandatory")
_Uxtp02_numOftExpeditedDataSent_Type = Counter32
_Uxtp02_numOftExpeditedDataSent_Object = MibScalar
uxtp02_numOftExpeditedDataSent = _Uxtp02_numOftExpeditedDataSent_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 8),
    _Uxtp02_numOftExpeditedDataSent_Type()
)
uxtp02_numOftExpeditedDataSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOftExpeditedDataSent.setStatus("mandatory")
_Uxtp02_numOftDataReceived_Type = Counter32
_Uxtp02_numOftDataReceived_Object = MibScalar
uxtp02_numOftDataReceived = _Uxtp02_numOftDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 9),
    _Uxtp02_numOftDataReceived_Type()
)
uxtp02_numOftDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOftDataReceived.setStatus("mandatory")
_Uxtp02_numOftExpeditedDataReceived_Type = Counter32
_Uxtp02_numOftExpeditedDataReceived_Object = MibScalar
uxtp02_numOftExpeditedDataReceived = _Uxtp02_numOftExpeditedDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 10),
    _Uxtp02_numOftExpeditedDataReceived_Type()
)
uxtp02_numOftExpeditedDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOftExpeditedDataReceived.setStatus("mandatory")
_Uxtp02_numOfopenConnection_Type = Counter32
_Uxtp02_numOfopenConnection_Object = MibScalar
uxtp02_numOfopenConnection = _Uxtp02_numOfopenConnection_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 11),
    _Uxtp02_numOfopenConnection_Type()
)
uxtp02_numOfopenConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfopenConnection.setStatus("mandatory")
_Uxtp02_numOfctTPDUSuccessfullIncoming_Type = Counter32
_Uxtp02_numOfctTPDUSuccessfullIncoming_Object = MibScalar
uxtp02_numOfctTPDUSuccessfullIncoming = _Uxtp02_numOfctTPDUSuccessfullIncoming_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 12),
    _Uxtp02_numOfctTPDUSuccessfullIncoming_Type()
)
uxtp02_numOfctTPDUSuccessfullIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfctTPDUSuccessfullIncoming.setStatus("mandatory")
_Uxtp02_numOfctTPDUSuccessfullOutgoing_Type = Counter32
_Uxtp02_numOfctTPDUSuccessfullOutgoing_Object = MibScalar
uxtp02_numOfctTPDUSuccessfullOutgoing = _Uxtp02_numOfctTPDUSuccessfullOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 13),
    _Uxtp02_numOfctTPDUSuccessfullOutgoing_Type()
)
uxtp02_numOfctTPDUSuccessfullOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfctTPDUSuccessfullOutgoing.setStatus("mandatory")
_Uxtp02_numOfctTPDUUnSuccessfullIncoming_Type = Counter32
_Uxtp02_numOfctTPDUUnSuccessfullIncoming_Object = MibScalar
uxtp02_numOfctTPDUUnSuccessfullIncoming = _Uxtp02_numOfctTPDUUnSuccessfullIncoming_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 14),
    _Uxtp02_numOfctTPDUUnSuccessfullIncoming_Type()
)
uxtp02_numOfctTPDUUnSuccessfullIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfctTPDUUnSuccessfullIncoming.setStatus("mandatory")
_Uxtp02_numOfctTPDUUnSuccessfullOutgoing_Type = Counter32
_Uxtp02_numOfctTPDUUnSuccessfullOutgoing_Object = MibScalar
uxtp02_numOfctTPDUUnSuccessfullOutgoing = _Uxtp02_numOfctTPDUUnSuccessfullOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 15),
    _Uxtp02_numOfctTPDUUnSuccessfullOutgoing_Type()
)
uxtp02_numOfctTPDUUnSuccessfullOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfctTPDUUnSuccessfullOutgoing.setStatus("mandatory")
_Uxtp02_numOfctTPDUCongestion_Type = Counter32
_Uxtp02_numOfctTPDUCongestion_Object = MibScalar
uxtp02_numOfctTPDUCongestion = _Uxtp02_numOfctTPDUCongestion_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 16),
    _Uxtp02_numOfctTPDUCongestion_Type()
)
uxtp02_numOfctTPDUCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfctTPDUCongestion.setStatus("mandatory")
_Uxtp02_numOfctTPDUConfProtErrorDetected_Type = Counter32
_Uxtp02_numOfctTPDUConfProtErrorDetected_Object = MibScalar
uxtp02_numOfctTPDUConfProtErrorDetected = _Uxtp02_numOfctTPDUConfProtErrorDetected_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 17),
    _Uxtp02_numOfctTPDUConfProtErrorDetected_Type()
)
uxtp02_numOfctTPDUConfProtErrorDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfctTPDUConfProtErrorDetected.setStatus("mandatory")
_Uxtp02_numOfctTPDURefusedConfProtError_Type = Counter32
_Uxtp02_numOfctTPDURefusedConfProtError_Object = MibScalar
uxtp02_numOfctTPDURefusedConfProtError = _Uxtp02_numOfctTPDURefusedConfProtError_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 18),
    _Uxtp02_numOfctTPDURefusedConfProtError_Type()
)
uxtp02_numOfctTPDURefusedConfProtError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfctTPDURefusedConfProtError.setStatus("mandatory")
_Uxtp02_numOfdetectedTPDUProtocolError_Type = Counter32
_Uxtp02_numOfdetectedTPDUProtocolError_Object = MibScalar
uxtp02_numOfdetectedTPDUProtocolError = _Uxtp02_numOfdetectedTPDUProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 19),
    _Uxtp02_numOfdetectedTPDUProtocolError_Type()
)
uxtp02_numOfdetectedTPDUProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfdetectedTPDUProtocolError.setStatus("mandatory")
_Uxtp02_numOfrefusedTPDUProtocolError_Type = Counter32
_Uxtp02_numOfrefusedTPDUProtocolError_Object = MibScalar
uxtp02_numOfrefusedTPDUProtocolError = _Uxtp02_numOfrefusedTPDUProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 15, 4, 1, 1, 20),
    _Uxtp02_numOfrefusedTPDUProtocolError_Type()
)
uxtp02_numOfrefusedTPDUProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxtp02_numOfrefusedTPDUProtocolError.setStatus("mandatory")
_Tnetb_TNB_ObjectIdentity = ObjectIdentity
tnetb_TNB = _Tnetb_TNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16)
)
_Tnetb_NETB_ObjectIdentity = ObjectIdentity
tnetb_NETB = _Tnetb_NETB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0)
)
_Tnetb_NETBTable_Object = MibTable
tnetb_NETBTable = _Tnetb_NETBTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1)
)
if mibBuilder.loadTexts:
    tnetb_NETBTable.setStatus("mandatory")
_Tnetb_NETBEntry_Object = MibTableRow
tnetb_NETBEntry = _Tnetb_NETBEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1)
)
tnetb_NETBEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "tnetb-NETBSysName"),
    (0, "OLIVETTI-MIB", "tnetb-NETBInstName"),
    (0, "OLIVETTI-MIB", "tnetb-NETBSubAddr"),
)
if mibBuilder.loadTexts:
    tnetb_NETBEntry.setStatus("mandatory")


class _Tnetb_NETBSysName_Type(DisplayString):
    """Custom type tnetb_NETBSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_NETBSysName_Type.__name__ = "DisplayString"
_Tnetb_NETBSysName_Object = MibScalar
tnetb_NETBSysName = _Tnetb_NETBSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 1),
    _Tnetb_NETBSysName_Type()
)
tnetb_NETBSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBSysName.setStatus("mandatory")


class _Tnetb_NETBInstName_Type(DisplayString):
    """Custom type tnetb_NETBInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Tnetb_NETBInstName_Type.__name__ = "DisplayString"
_Tnetb_NETBInstName_Object = MibScalar
tnetb_NETBInstName = _Tnetb_NETBInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 2),
    _Tnetb_NETBInstName_Type()
)
tnetb_NETBInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBInstName.setStatus("mandatory")


class _Tnetb_NETBSubAddr_Type(DisplayString):
    """Custom type tnetb_NETBSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_NETBSubAddr_Type.__name__ = "DisplayString"
_Tnetb_NETBSubAddr_Object = MibScalar
tnetb_NETBSubAddr = _Tnetb_NETBSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 3),
    _Tnetb_NETBSubAddr_Type()
)
tnetb_NETBSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBSubAddr.setStatus("mandatory")
_Tnetb_NETBtxPDU_Type = Counter32
_Tnetb_NETBtxPDU_Object = MibScalar
tnetb_NETBtxPDU = _Tnetb_NETBtxPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 4),
    _Tnetb_NETBtxPDU_Type()
)
tnetb_NETBtxPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBtxPDU.setStatus("mandatory")
_Tnetb_NETBrxPDU_Type = Counter32
_Tnetb_NETBrxPDU_Object = MibScalar
tnetb_NETBrxPDU = _Tnetb_NETBrxPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 5),
    _Tnetb_NETBrxPDU_Type()
)
tnetb_NETBrxPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBrxPDU.setStatus("mandatory")
_Tnetb_NETBsuccessregistr_Type = Counter32
_Tnetb_NETBsuccessregistr_Object = MibScalar
tnetb_NETBsuccessregistr = _Tnetb_NETBsuccessregistr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 6),
    _Tnetb_NETBsuccessregistr_Type()
)
tnetb_NETBsuccessregistr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBsuccessregistr.setStatus("mandatory")
_Tnetb_NETBunsuccessregistr_Type = Counter32
_Tnetb_NETBunsuccessregistr_Object = MibScalar
tnetb_NETBunsuccessregistr = _Tnetb_NETBunsuccessregistr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 7),
    _Tnetb_NETBunsuccessregistr_Type()
)
tnetb_NETBunsuccessregistr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBunsuccessregistr.setStatus("mandatory")
_Tnetb_NETBsuccessderegistr_Type = Counter32
_Tnetb_NETBsuccessderegistr_Object = MibScalar
tnetb_NETBsuccessderegistr = _Tnetb_NETBsuccessderegistr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 8),
    _Tnetb_NETBsuccessderegistr_Type()
)
tnetb_NETBsuccessderegistr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBsuccessderegistr.setStatus("mandatory")
_Tnetb_NETBunsuccessderegistr_Type = Counter32
_Tnetb_NETBunsuccessderegistr_Object = MibScalar
tnetb_NETBunsuccessderegistr = _Tnetb_NETBunsuccessderegistr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 9),
    _Tnetb_NETBunsuccessderegistr_Type()
)
tnetb_NETBunsuccessderegistr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBunsuccessderegistr.setStatus("mandatory")
_Tnetb_NETBresolutednames_Type = Counter32
_Tnetb_NETBresolutednames_Object = MibScalar
tnetb_NETBresolutednames = _Tnetb_NETBresolutednames_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 10),
    _Tnetb_NETBresolutednames_Type()
)
tnetb_NETBresolutednames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBresolutednames.setStatus("mandatory")
_Tnetb_NETBunresolutednames_Type = Counter32
_Tnetb_NETBunresolutednames_Object = MibScalar
tnetb_NETBunresolutednames = _Tnetb_NETBunresolutednames_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 11),
    _Tnetb_NETBunresolutednames_Type()
)
tnetb_NETBunresolutednames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBunresolutednames.setStatus("mandatory")
_Tnetb_NETBreserved_Type = Counter32
_Tnetb_NETBreserved_Object = MibScalar
tnetb_NETBreserved = _Tnetb_NETBreserved_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 12),
    _Tnetb_NETBreserved_Type()
)
tnetb_NETBreserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnetb_NETBreserved.setStatus("mandatory")
_Tnetb_NETBrxinvalidPDU_Type = Counter32
_Tnetb_NETBrxinvalidPDU_Object = MibScalar
tnetb_NETBrxinvalidPDU = _Tnetb_NETBrxinvalidPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 0, 1, 1, 13),
    _Tnetb_NETBrxinvalidPDU_Type()
)
tnetb_NETBrxinvalidPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NETBrxinvalidPDU.setStatus("mandatory")
_Tnetb_TRSP_ObjectIdentity = ObjectIdentity
tnetb_TRSP = _Tnetb_TRSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1)
)
_Tnetb_TRSPTable_Object = MibTable
tnetb_TRSPTable = _Tnetb_TRSPTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1)
)
if mibBuilder.loadTexts:
    tnetb_TRSPTable.setStatus("mandatory")
_Tnetb_TRSPEntry_Object = MibTableRow
tnetb_TRSPEntry = _Tnetb_TRSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1)
)
tnetb_TRSPEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "tnetb-TRSPSysName"),
    (0, "OLIVETTI-MIB", "tnetb-TRSPInstName"),
    (0, "OLIVETTI-MIB", "tnetb-TRSPSubAddr"),
)
if mibBuilder.loadTexts:
    tnetb_TRSPEntry.setStatus("mandatory")


class _Tnetb_TRSPSysName_Type(DisplayString):
    """Custom type tnetb_TRSPSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_TRSPSysName_Type.__name__ = "DisplayString"
_Tnetb_TRSPSysName_Object = MibScalar
tnetb_TRSPSysName = _Tnetb_TRSPSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 1),
    _Tnetb_TRSPSysName_Type()
)
tnetb_TRSPSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPSysName.setStatus("mandatory")


class _Tnetb_TRSPInstName_Type(DisplayString):
    """Custom type tnetb_TRSPInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Tnetb_TRSPInstName_Type.__name__ = "DisplayString"
_Tnetb_TRSPInstName_Object = MibScalar
tnetb_TRSPInstName = _Tnetb_TRSPInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 2),
    _Tnetb_TRSPInstName_Type()
)
tnetb_TRSPInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPInstName.setStatus("mandatory")


class _Tnetb_TRSPSubAddr_Type(DisplayString):
    """Custom type tnetb_TRSPSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_TRSPSubAddr_Type.__name__ = "DisplayString"
_Tnetb_TRSPSubAddr_Object = MibScalar
tnetb_TRSPSubAddr = _Tnetb_TRSPSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 3),
    _Tnetb_TRSPSubAddr_Type()
)
tnetb_TRSPSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPSubAddr.setStatus("mandatory")
_Tnetb_TRSPreserved1_Type = Counter32
_Tnetb_TRSPreserved1_Object = MibScalar
tnetb_TRSPreserved1 = _Tnetb_TRSPreserved1_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 4),
    _Tnetb_TRSPreserved1_Type()
)
tnetb_TRSPreserved1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPreserved1.setStatus("mandatory")
_Tnetb_TRSPsuppconnection_Type = Integer32
_Tnetb_TRSPsuppconnection_Object = MibScalar
tnetb_TRSPsuppconnection = _Tnetb_TRSPsuppconnection_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 5),
    _Tnetb_TRSPsuppconnection_Type()
)
tnetb_TRSPsuppconnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPsuppconnection.setStatus("mandatory")
_Tnetb_TRSPreserved2_Type = Counter32
_Tnetb_TRSPreserved2_Object = MibScalar
tnetb_TRSPreserved2 = _Tnetb_TRSPreserved2_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 6),
    _Tnetb_TRSPreserved2_Type()
)
tnetb_TRSPreserved2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPreserved2.setStatus("mandatory")
_Tnetb_TRSPreserved3_Type = Counter32
_Tnetb_TRSPreserved3_Object = MibScalar
tnetb_TRSPreserved3 = _Tnetb_TRSPreserved3_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 7),
    _Tnetb_TRSPreserved3_Type()
)
tnetb_TRSPreserved3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPreserved3.setStatus("mandatory")
_Tnetb_TRSPreserved4_Type = Counter32
_Tnetb_TRSPreserved4_Object = MibScalar
tnetb_TRSPreserved4 = _Tnetb_TRSPreserved4_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 8),
    _Tnetb_TRSPreserved4_Type()
)
tnetb_TRSPreserved4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPreserved4.setStatus("mandatory")
_Tnetb_TRSPreserved5_Type = Counter32
_Tnetb_TRSPreserved5_Object = MibScalar
tnetb_TRSPreserved5 = _Tnetb_TRSPreserved5_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 9),
    _Tnetb_TRSPreserved5_Type()
)
tnetb_TRSPreserved5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPreserved5.setStatus("mandatory")
_Tnetb_TRSPtxTPDU_Type = Counter32
_Tnetb_TRSPtxTPDU_Object = MibScalar
tnetb_TRSPtxTPDU = _Tnetb_TRSPtxTPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 10),
    _Tnetb_TRSPtxTPDU_Type()
)
tnetb_TRSPtxTPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPtxTPDU.setStatus("mandatory")
_Tnetb_TRSPrxTPDU_Type = Counter32
_Tnetb_TRSPrxTPDU_Object = MibScalar
tnetb_TRSPrxTPDU = _Tnetb_TRSPrxTPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 11),
    _Tnetb_TRSPrxTPDU_Type()
)
tnetb_TRSPrxTPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPrxTPDU.setStatus("mandatory")
_Tnetb_TRSPtxretranTPDU_Type = Counter32
_Tnetb_TRSPtxretranTPDU_Object = MibScalar
tnetb_TRSPtxretranTPDU = _Tnetb_TRSPtxretranTPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 12),
    _Tnetb_TRSPtxretranTPDU_Type()
)
tnetb_TRSPtxretranTPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPtxretranTPDU.setStatus("mandatory")
_Tnetb_TRSPtxretranDATATPDU_Type = Counter32
_Tnetb_TRSPtxretranDATATPDU_Object = MibScalar
tnetb_TRSPtxretranDATATPDU = _Tnetb_TRSPtxretranDATATPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 13),
    _Tnetb_TRSPtxretranDATATPDU_Type()
)
tnetb_TRSPtxretranDATATPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPtxretranDATATPDU.setStatus("mandatory")
_Tnetb_TRSPactiveconnection_Type = Integer32
_Tnetb_TRSPactiveconnection_Object = MibScalar
tnetb_TRSPactiveconnection = _Tnetb_TRSPactiveconnection_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 14),
    _Tnetb_TRSPactiveconnection_Type()
)
tnetb_TRSPactiveconnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPactiveconnection.setStatus("mandatory")
_Tnetb_TRSPreserved6_Type = Counter32
_Tnetb_TRSPreserved6_Object = MibScalar
tnetb_TRSPreserved6 = _Tnetb_TRSPreserved6_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 15),
    _Tnetb_TRSPreserved6_Type()
)
tnetb_TRSPreserved6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPreserved6.setStatus("mandatory")
_Tnetb_TRSPsuccessinconnect_Type = Counter32
_Tnetb_TRSPsuccessinconnect_Object = MibScalar
tnetb_TRSPsuccessinconnect = _Tnetb_TRSPsuccessinconnect_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 16),
    _Tnetb_TRSPsuccessinconnect_Type()
)
tnetb_TRSPsuccessinconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPsuccessinconnect.setStatus("mandatory")
_Tnetb_TRSPsuccessoutconnect_Type = Counter32
_Tnetb_TRSPsuccessoutconnect_Object = MibScalar
tnetb_TRSPsuccessoutconnect = _Tnetb_TRSPsuccessoutconnect_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 17),
    _Tnetb_TRSPsuccessoutconnect_Type()
)
tnetb_TRSPsuccessoutconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPsuccessoutconnect.setStatus("mandatory")
_Tnetb_TRSPunsuccessinconnect_Type = Counter32
_Tnetb_TRSPunsuccessinconnect_Object = MibScalar
tnetb_TRSPunsuccessinconnect = _Tnetb_TRSPunsuccessinconnect_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 18),
    _Tnetb_TRSPunsuccessinconnect_Type()
)
tnetb_TRSPunsuccessinconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPunsuccessinconnect.setStatus("mandatory")
_Tnetb_TRSPunsuccessoutconnect_Type = Counter32
_Tnetb_TRSPunsuccessoutconnect_Object = MibScalar
tnetb_TRSPunsuccessoutconnect = _Tnetb_TRSPunsuccessoutconnect_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 19),
    _Tnetb_TRSPunsuccessoutconnect_Type()
)
tnetb_TRSPunsuccessoutconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPunsuccessoutconnect.setStatus("mandatory")
_Tnetb_TRSPconnectinactivity_Type = Counter32
_Tnetb_TRSPconnectinactivity_Object = MibScalar
tnetb_TRSPconnectinactivity = _Tnetb_TRSPconnectinactivity_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 20),
    _Tnetb_TRSPconnectinactivity_Type()
)
tnetb_TRSPconnectinactivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPconnectinactivity.setStatus("mandatory")
_Tnetb_TRSPprotocolerror_Type = Counter32
_Tnetb_TRSPprotocolerror_Object = MibScalar
tnetb_TRSPprotocolerror = _Tnetb_TRSPprotocolerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 21),
    _Tnetb_TRSPprotocolerror_Type()
)
tnetb_TRSPprotocolerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPprotocolerror.setStatus("mandatory")
_Tnetb_TRSPrxinvalidTPDU_Type = Counter32
_Tnetb_TRSPrxinvalidTPDU_Object = MibScalar
tnetb_TRSPrxinvalidTPDU = _Tnetb_TRSPrxinvalidTPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 22),
    _Tnetb_TRSPrxinvalidTPDU_Type()
)
tnetb_TRSPrxinvalidTPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPrxinvalidTPDU.setStatus("mandatory")
_Tnetb_TRSPrxTSDU_Type = Counter32
_Tnetb_TRSPrxTSDU_Object = MibScalar
tnetb_TRSPrxTSDU = _Tnetb_TRSPrxTSDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 23),
    _Tnetb_TRSPrxTSDU_Type()
)
tnetb_TRSPrxTSDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPrxTSDU.setStatus("mandatory")
_Tnetb_TRSPtxTSDU_Type = Counter32
_Tnetb_TRSPtxTSDU_Object = MibScalar
tnetb_TRSPtxTSDU = _Tnetb_TRSPtxTSDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 24),
    _Tnetb_TRSPtxTSDU_Type()
)
tnetb_TRSPtxTSDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPtxTSDU.setStatus("mandatory")
_Tnetb_TRSPtxdatabyte_Type = Counter32
_Tnetb_TRSPtxdatabyte_Object = MibScalar
tnetb_TRSPtxdatabyte = _Tnetb_TRSPtxdatabyte_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 25),
    _Tnetb_TRSPtxdatabyte_Type()
)
tnetb_TRSPtxdatabyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPtxdatabyte.setStatus("mandatory")
_Tnetb_TRSPrxdatabyte_Type = Counter32
_Tnetb_TRSPrxdatabyte_Object = MibScalar
tnetb_TRSPrxdatabyte = _Tnetb_TRSPrxdatabyte_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 26),
    _Tnetb_TRSPrxdatabyte_Type()
)
tnetb_TRSPrxdatabyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPrxdatabyte.setStatus("mandatory")
_Tnetb_TRSPallocerror_Type = Counter32
_Tnetb_TRSPallocerror_Object = MibScalar
tnetb_TRSPallocerror = _Tnetb_TRSPallocerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 27),
    _Tnetb_TRSPallocerror_Type()
)
tnetb_TRSPallocerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPallocerror.setStatus("mandatory")
_Tnetb_TRSPtxdatagramTPDU_Type = Counter32
_Tnetb_TRSPtxdatagramTPDU_Object = MibScalar
tnetb_TRSPtxdatagramTPDU = _Tnetb_TRSPtxdatagramTPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 28),
    _Tnetb_TRSPtxdatagramTPDU_Type()
)
tnetb_TRSPtxdatagramTPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPtxdatagramTPDU.setStatus("mandatory")
_Tnetb_TRSPrxdatagrmTPDU_Type = Counter32
_Tnetb_TRSPrxdatagrmTPDU_Object = MibScalar
tnetb_TRSPrxdatagrmTPDU = _Tnetb_TRSPrxdatagrmTPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 29),
    _Tnetb_TRSPrxdatagrmTPDU_Type()
)
tnetb_TRSPrxdatagrmTPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPrxdatagrmTPDU.setStatus("mandatory")
_Tnetb_TRSPoverrunTPDU_Type = Counter32
_Tnetb_TRSPoverrunTPDU_Object = MibScalar
tnetb_TRSPoverrunTPDU = _Tnetb_TRSPoverrunTPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 30),
    _Tnetb_TRSPoverrunTPDU_Type()
)
tnetb_TRSPoverrunTPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPoverrunTPDU.setStatus("mandatory")
_Tnetb_TRSPopenerror_Type = Counter32
_Tnetb_TRSPopenerror_Object = MibScalar
tnetb_TRSPopenerror = _Tnetb_TRSPopenerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 31),
    _Tnetb_TRSPopenerror_Type()
)
tnetb_TRSPopenerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPopenerror.setStatus("mandatory")
_Tnetb_TRSPnoendpoint_Type = Counter32
_Tnetb_TRSPnoendpoint_Object = MibScalar
tnetb_TRSPnoendpoint = _Tnetb_TRSPnoendpoint_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 1, 1, 1, 32),
    _Tnetb_TRSPnoendpoint_Type()
)
tnetb_TRSPnoendpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_TRSPnoendpoint.setStatus("mandatory")
_Tnetb_NTWK_ObjectIdentity = ObjectIdentity
tnetb_NTWK = _Tnetb_NTWK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2)
)
_Tnetb_NTWKTable_Object = MibTable
tnetb_NTWKTable = _Tnetb_NTWKTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1)
)
if mibBuilder.loadTexts:
    tnetb_NTWKTable.setStatus("mandatory")
_Tnetb_NTWKEntry_Object = MibTableRow
tnetb_NTWKEntry = _Tnetb_NTWKEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1)
)
tnetb_NTWKEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "tnetb-NTWKSysName"),
    (0, "OLIVETTI-MIB", "tnetb-NTWKInstName"),
    (0, "OLIVETTI-MIB", "tnetb-NTWKSubAddr"),
)
if mibBuilder.loadTexts:
    tnetb_NTWKEntry.setStatus("mandatory")


class _Tnetb_NTWKSysName_Type(DisplayString):
    """Custom type tnetb_NTWKSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_NTWKSysName_Type.__name__ = "DisplayString"
_Tnetb_NTWKSysName_Object = MibScalar
tnetb_NTWKSysName = _Tnetb_NTWKSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 1),
    _Tnetb_NTWKSysName_Type()
)
tnetb_NTWKSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKSysName.setStatus("mandatory")


class _Tnetb_NTWKInstName_Type(DisplayString):
    """Custom type tnetb_NTWKInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Tnetb_NTWKInstName_Type.__name__ = "DisplayString"
_Tnetb_NTWKInstName_Object = MibScalar
tnetb_NTWKInstName = _Tnetb_NTWKInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 2),
    _Tnetb_NTWKInstName_Type()
)
tnetb_NTWKInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKInstName.setStatus("mandatory")


class _Tnetb_NTWKSubAddr_Type(DisplayString):
    """Custom type tnetb_NTWKSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_NTWKSubAddr_Type.__name__ = "DisplayString"
_Tnetb_NTWKSubAddr_Object = MibScalar
tnetb_NTWKSubAddr = _Tnetb_NTWKSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 3),
    _Tnetb_NTWKSubAddr_Type()
)
tnetb_NTWKSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKSubAddr.setStatus("mandatory")
_Tnetb_NTWKresourceerror_Type = Counter32
_Tnetb_NTWKresourceerror_Object = MibScalar
tnetb_NTWKresourceerror = _Tnetb_NTWKresourceerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 4),
    _Tnetb_NTWKresourceerror_Type()
)
tnetb_NTWKresourceerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKresourceerror.setStatus("mandatory")
_Tnetb_NTWKrxPDU_Type = Counter32
_Tnetb_NTWKrxPDU_Object = MibScalar
tnetb_NTWKrxPDU = _Tnetb_NTWKrxPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 5),
    _Tnetb_NTWKrxPDU_Type()
)
tnetb_NTWKrxPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKrxPDU.setStatus("mandatory")
_Tnetb_NTWKtxPDU_Type = Counter32
_Tnetb_NTWKtxPDU_Object = MibScalar
tnetb_NTWKtxPDU = _Tnetb_NTWKtxPDU_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 6),
    _Tnetb_NTWKtxPDU_Type()
)
tnetb_NTWKtxPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKtxPDU.setStatus("mandatory")
_Tnetb_NTWKrxbyte_Type = Counter32
_Tnetb_NTWKrxbyte_Object = MibScalar
tnetb_NTWKrxbyte = _Tnetb_NTWKrxbyte_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 7),
    _Tnetb_NTWKrxbyte_Type()
)
tnetb_NTWKrxbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKrxbyte.setStatus("mandatory")
_Tnetb_NTWKtxbyte_Type = Counter32
_Tnetb_NTWKtxbyte_Object = MibScalar
tnetb_NTWKtxbyte = _Tnetb_NTWKtxbyte_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 8),
    _Tnetb_NTWKtxbyte_Type()
)
tnetb_NTWKtxbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKtxbyte.setStatus("mandatory")
_Tnetb_NTWKtxsegmented_Type = Counter32
_Tnetb_NTWKtxsegmented_Object = MibScalar
tnetb_NTWKtxsegmented = _Tnetb_NTWKtxsegmented_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 9),
    _Tnetb_NTWKtxsegmented_Type()
)
tnetb_NTWKtxsegmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKtxsegmented.setStatus("mandatory")
_Tnetb_NTWKtxnetworkerror_Type = Counter32
_Tnetb_NTWKtxnetworkerror_Object = MibScalar
tnetb_NTWKtxnetworkerror = _Tnetb_NTWKtxnetworkerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 10),
    _Tnetb_NTWKtxnetworkerror_Type()
)
tnetb_NTWKtxnetworkerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKtxnetworkerror.setStatus("mandatory")
_Tnetb_NTWKrxnetworkerror_Type = Counter32
_Tnetb_NTWKrxnetworkerror_Object = MibScalar
tnetb_NTWKrxnetworkerror = _Tnetb_NTWKrxnetworkerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 11),
    _Tnetb_NTWKrxnetworkerror_Type()
)
tnetb_NTWKrxnetworkerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKrxnetworkerror.setStatus("mandatory")
_Tnetb_NTWKtxcongested_Type = Counter32
_Tnetb_NTWKtxcongested_Object = MibScalar
tnetb_NTWKtxcongested = _Tnetb_NTWKtxcongested_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 12),
    _Tnetb_NTWKtxcongested_Type()
)
tnetb_NTWKtxcongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKtxcongested.setStatus("mandatory")
_Tnetb_NTWKrxreassembled_Type = Counter32
_Tnetb_NTWKrxreassembled_Object = MibScalar
tnetb_NTWKrxreassembled = _Tnetb_NTWKrxreassembled_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 13),
    _Tnetb_NTWKrxreassembled_Type()
)
tnetb_NTWKrxreassembled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKrxreassembled.setStatus("mandatory")
_Tnetb_NTWKreassemblytimeout_Type = Counter32
_Tnetb_NTWKreassemblytimeout_Object = MibScalar
tnetb_NTWKreassemblytimeout = _Tnetb_NTWKreassemblytimeout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 14),
    _Tnetb_NTWKreassemblytimeout_Type()
)
tnetb_NTWKreassemblytimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKreassemblytimeout.setStatus("mandatory")
_Tnetb_NTWKtxforwarded_Type = Counter32
_Tnetb_NTWKtxforwarded_Object = MibScalar
tnetb_NTWKtxforwarded = _Tnetb_NTWKtxforwarded_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 15),
    _Tnetb_NTWKtxforwarded_Type()
)
tnetb_NTWKtxforwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKtxforwarded.setStatus("mandatory")
_Tnetb_NTWKPDUbadformat_Type = Counter32
_Tnetb_NTWKPDUbadformat_Object = MibScalar
tnetb_NTWKPDUbadformat = _Tnetb_NTWKPDUbadformat_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 16),
    _Tnetb_NTWKPDUbadformat_Type()
)
tnetb_NTWKPDUbadformat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKPDUbadformat.setStatus("mandatory")
_Tnetb_NTWKPDUdestinunreach_Type = Counter32
_Tnetb_NTWKPDUdestinunreach_Object = MibScalar
tnetb_NTWKPDUdestinunreach = _Tnetb_NTWKPDUdestinunreach_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 17),
    _Tnetb_NTWKPDUdestinunreach_Type()
)
tnetb_NTWKPDUdestinunreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKPDUdestinunreach.setStatus("mandatory")
_Tnetb_NTWKPDUunsupportedoption_Type = Counter32
_Tnetb_NTWKPDUunsupportedoption_Object = MibScalar
tnetb_NTWKPDUunsupportedoption = _Tnetb_NTWKPDUunsupportedoption_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 18),
    _Tnetb_NTWKPDUunsupportedoption_Type()
)
tnetb_NTWKPDUunsupportedoption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKPDUunsupportedoption.setStatus("mandatory")
_Tnetb_NTWKlifetime_Type = Counter32
_Tnetb_NTWKlifetime_Object = MibScalar
tnetb_NTWKlifetime = _Tnetb_NTWKlifetime_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 2, 1, 1, 19),
    _Tnetb_NTWKlifetime_Type()
)
tnetb_NTWKlifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_NTWKlifetime.setStatus("mandatory")
_Tnetb_LLCN_ObjectIdentity = ObjectIdentity
tnetb_LLCN = _Tnetb_LLCN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3)
)
_Tnetb_LLCNTable_Object = MibTable
tnetb_LLCNTable = _Tnetb_LLCNTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1)
)
if mibBuilder.loadTexts:
    tnetb_LLCNTable.setStatus("mandatory")
_Tnetb_LLCNEntry_Object = MibTableRow
tnetb_LLCNEntry = _Tnetb_LLCNEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1)
)
tnetb_LLCNEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "tnetb-LLCNSysName"),
    (0, "OLIVETTI-MIB", "tnetb-LLCNInstName"),
    (0, "OLIVETTI-MIB", "tnetb-LLCNSubAddr"),
)
if mibBuilder.loadTexts:
    tnetb_LLCNEntry.setStatus("mandatory")


class _Tnetb_LLCNSysName_Type(DisplayString):
    """Custom type tnetb_LLCNSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_LLCNSysName_Type.__name__ = "DisplayString"
_Tnetb_LLCNSysName_Object = MibScalar
tnetb_LLCNSysName = _Tnetb_LLCNSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 1),
    _Tnetb_LLCNSysName_Type()
)
tnetb_LLCNSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNSysName.setStatus("mandatory")


class _Tnetb_LLCNInstName_Type(DisplayString):
    """Custom type tnetb_LLCNInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Tnetb_LLCNInstName_Type.__name__ = "DisplayString"
_Tnetb_LLCNInstName_Object = MibScalar
tnetb_LLCNInstName = _Tnetb_LLCNInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 2),
    _Tnetb_LLCNInstName_Type()
)
tnetb_LLCNInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNInstName.setStatus("mandatory")


class _Tnetb_LLCNSubAddr_Type(DisplayString):
    """Custom type tnetb_LLCNSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tnetb_LLCNSubAddr_Type.__name__ = "DisplayString"
_Tnetb_LLCNSubAddr_Object = MibScalar
tnetb_LLCNSubAddr = _Tnetb_LLCNSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 3),
    _Tnetb_LLCNSubAddr_Type()
)
tnetb_LLCNSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNSubAddr.setStatus("mandatory")
_Tnetb_LLCNtxUI5rame_Type = Counter32
_Tnetb_LLCNtxUI5rame_Object = MibScalar
tnetb_LLCNtxUI5rame = _Tnetb_LLCNtxUI5rame_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 4),
    _Tnetb_LLCNtxUI5rame_Type()
)
tnetb_LLCNtxUI5rame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNtxUI5rame.setStatus("mandatory")
_Tnetb_LLCNrxUIframe_Type = Counter32
_Tnetb_LLCNrxUIframe_Object = MibScalar
tnetb_LLCNrxUIframe = _Tnetb_LLCNrxUIframe_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 5),
    _Tnetb_LLCNrxUIframe_Type()
)
tnetb_LLCNrxUIframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNrxUIframe.setStatus("mandatory")
_Tnetb_LLCNtxMACerror_Type = Counter32
_Tnetb_LLCNtxMACerror_Object = MibScalar
tnetb_LLCNtxMACerror = _Tnetb_LLCNtxMACerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 6),
    _Tnetb_LLCNtxMACerror_Type()
)
tnetb_LLCNtxMACerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNtxMACerror.setStatus("mandatory")
_Tnetb_LLCNrxMACerror_Type = Counter32
_Tnetb_LLCNrxMACerror_Object = MibScalar
tnetb_LLCNrxMACerror = _Tnetb_LLCNrxMACerror_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 7),
    _Tnetb_LLCNrxMACerror_Type()
)
tnetb_LLCNrxMACerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNrxMACerror.setStatus("mandatory")
_Tnetb_LLCNtxTESTframe_Type = Counter32
_Tnetb_LLCNtxTESTframe_Object = MibScalar
tnetb_LLCNtxTESTframe = _Tnetb_LLCNtxTESTframe_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 8),
    _Tnetb_LLCNtxTESTframe_Type()
)
tnetb_LLCNtxTESTframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNtxTESTframe.setStatus("mandatory")
_Tnetb_LLCNrxTESTframe_Type = Counter32
_Tnetb_LLCNrxTESTframe_Object = MibScalar
tnetb_LLCNrxTESTframe = _Tnetb_LLCNrxTESTframe_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 9),
    _Tnetb_LLCNrxTESTframe_Type()
)
tnetb_LLCNrxTESTframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNrxTESTframe.setStatus("mandatory")
_Tnetb_LLCNtxXIDframe_Type = Counter32
_Tnetb_LLCNtxXIDframe_Object = MibScalar
tnetb_LLCNtxXIDframe = _Tnetb_LLCNtxXIDframe_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 10),
    _Tnetb_LLCNtxXIDframe_Type()
)
tnetb_LLCNtxXIDframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNtxXIDframe.setStatus("mandatory")
_Tnetb_LLCNrxXIDframe_Type = Counter32
_Tnetb_LLCNrxXIDframe_Object = MibScalar
tnetb_LLCNrxXIDframe = _Tnetb_LLCNrxXIDframe_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 11),
    _Tnetb_LLCNrxXIDframe_Type()
)
tnetb_LLCNrxXIDframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNrxXIDframe.setStatus("mandatory")
_Tnetb_LLCNtxTESTresponse_Type = Counter32
_Tnetb_LLCNtxTESTresponse_Object = MibScalar
tnetb_LLCNtxTESTresponse = _Tnetb_LLCNtxTESTresponse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 12),
    _Tnetb_LLCNtxTESTresponse_Type()
)
tnetb_LLCNtxTESTresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNtxTESTresponse.setStatus("mandatory")
_Tnetb_LLCNrxTESTresponse_Type = Counter32
_Tnetb_LLCNrxTESTresponse_Object = MibScalar
tnetb_LLCNrxTESTresponse = _Tnetb_LLCNrxTESTresponse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 13),
    _Tnetb_LLCNrxTESTresponse_Type()
)
tnetb_LLCNrxTESTresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNrxTESTresponse.setStatus("mandatory")
_Tnetb_LLCNtxXIDresponse_Type = Counter32
_Tnetb_LLCNtxXIDresponse_Object = MibScalar
tnetb_LLCNtxXIDresponse = _Tnetb_LLCNtxXIDresponse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 14),
    _Tnetb_LLCNtxXIDresponse_Type()
)
tnetb_LLCNtxXIDresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNtxXIDresponse.setStatus("mandatory")
_Tnetb_LLCNrxXIDresponse_Type = Counter32
_Tnetb_LLCNrxXIDresponse_Object = MibScalar
tnetb_LLCNrxXIDresponse = _Tnetb_LLCNrxXIDresponse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 16, 3, 1, 1, 15),
    _Tnetb_LLCNrxXIDresponse_Type()
)
tnetb_LLCNrxXIDresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnetb_LLCNrxXIDresponse.setStatus("mandatory")
_Netb_NB_ObjectIdentity = ObjectIdentity
netb_NB = _Netb_NB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17)
)
_Netb_NBEUI_ObjectIdentity = ObjectIdentity
netb_NBEUI = _Netb_NBEUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0)
)
_Netb_NBEUITable_Object = MibTable
netb_NBEUITable = _Netb_NBEUITable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1)
)
if mibBuilder.loadTexts:
    netb_NBEUITable.setStatus("mandatory")
_Netb_NBEUIEntry_Object = MibTableRow
netb_NBEUIEntry = _Netb_NBEUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1)
)
netb_NBEUIEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "netbSysName"),
    (0, "OLIVETTI-MIB", "netbInstName"),
    (0, "OLIVETTI-MIB", "netbSubAddr"),
)
if mibBuilder.loadTexts:
    netb_NBEUIEntry.setStatus("mandatory")


class _NetbSysName_Type(DisplayString):
    """Custom type netbSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NetbSysName_Type.__name__ = "DisplayString"
_NetbSysName_Object = MibTableColumn
netbSysName = _NetbSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 1),
    _NetbSysName_Type()
)
netbSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbSysName.setStatus("mandatory")


class _NetbInstName_Type(DisplayString):
    """Custom type netbInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_NetbInstName_Type.__name__ = "DisplayString"
_NetbInstName_Object = MibTableColumn
netbInstName = _NetbInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 2),
    _NetbInstName_Type()
)
netbInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbInstName.setStatus("mandatory")


class _NetbSubAddr_Type(DisplayString):
    """Custom type netbSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NetbSubAddr_Type.__name__ = "DisplayString"
_NetbSubAddr_Object = MibTableColumn
netbSubAddr = _NetbSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 3),
    _NetbSubAddr_Type()
)
netbSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbSubAddr.setStatus("mandatory")
_Netbreserved_Type = Integer32
_Netbreserved_Object = MibTableColumn
netbreserved = _Netbreserved_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 4),
    _Netbreserved_Type()
)
netbreserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbreserved.setStatus("mandatory")
_Netbreleaselevel_Type = Integer32
_Netbreleaselevel_Object = MibTableColumn
netbreleaselevel = _Netbreleaselevel_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 5),
    _Netbreleaselevel_Type()
)
netbreleaselevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbreleaselevel.setStatus("mandatory")
_Netbsoftwarelevel_Type = Integer32
_Netbsoftwarelevel_Object = MibTableColumn
netbsoftwarelevel = _Netbsoftwarelevel_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 6),
    _Netbsoftwarelevel_Type()
)
netbsoftwarelevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbsoftwarelevel.setStatus("mandatory")
_Netbadaptertype_Type = Integer32
_Netbadaptertype_Object = MibTableColumn
netbadaptertype = _Netbadaptertype_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 7),
    _Netbadaptertype_Type()
)
netbadaptertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbadaptertype.setStatus("mandatory")
_Netbparamstype_Type = Integer32
_Netbparamstype_Object = MibTableColumn
netbparamstype = _Netbparamstype_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 8),
    _Netbparamstype_Type()
)
netbparamstype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbparamstype.setStatus("mandatory")
_Netbreportingperiod_Type = Integer32
_Netbreportingperiod_Object = MibTableColumn
netbreportingperiod = _Netbreportingperiod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 9),
    _Netbreportingperiod_Type()
)
netbreportingperiod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbreportingperiod.setStatus("mandatory")
_NetbrxFRMR_Type = Counter32
_NetbrxFRMR_Object = MibTableColumn
netbrxFRMR = _NetbrxFRMR_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 10),
    _NetbrxFRMR_Type()
)
netbrxFRMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbrxFRMR.setStatus("mandatory")
_NetbtxFRMR_Type = Counter32
_NetbtxFRMR_Object = MibTableColumn
netbtxFRMR = _NetbtxFRMR_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 11),
    _NetbtxFRMR_Type()
)
netbtxFRMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbtxFRMR.setStatus("mandatory")
_NetbrxIframeserr_Type = Counter32
_NetbrxIframeserr_Object = MibTableColumn
netbrxIframeserr = _NetbrxIframeserr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 12),
    _NetbrxIframeserr_Type()
)
netbrxIframeserr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbrxIframeserr.setStatus("mandatory")
_Netbtxaborted_Type = Counter32
_Netbtxaborted_Object = MibTableColumn
netbtxaborted = _Netbtxaborted_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 13),
    _Netbtxaborted_Type()
)
netbtxaborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbtxaborted.setStatus("mandatory")
_Netbtxsuccesspack_Type = Counter32
_Netbtxsuccesspack_Object = MibTableColumn
netbtxsuccesspack = _Netbtxsuccesspack_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 14),
    _Netbtxsuccesspack_Type()
)
netbtxsuccesspack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbtxsuccesspack.setStatus("mandatory")
_Netbrxsuccesspack_Type = Counter32
_Netbrxsuccesspack_Object = MibTableColumn
netbrxsuccesspack = _Netbrxsuccesspack_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 15),
    _Netbrxsuccesspack_Type()
)
netbrxsuccesspack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbrxsuccesspack.setStatus("mandatory")
_NetbtxIframeserr_Type = Counter32
_NetbtxIframeserr_Object = MibTableColumn
netbtxIframeserr = _NetbtxIframeserr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 16),
    _NetbtxIframeserr_Type()
)
netbtxIframeserr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbtxIframeserr.setStatus("mandatory")
_Netbrxnobuffer_Type = Counter32
_Netbrxnobuffer_Object = MibTableColumn
netbrxnobuffer = _Netbrxnobuffer_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 17),
    _Netbrxnobuffer_Type()
)
netbrxnobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbrxnobuffer.setStatus("mandatory")
_NetbT1expired_Type = Counter32
_NetbT1expired_Object = MibTableColumn
netbT1expired = _NetbT1expired_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 18),
    _NetbT1expired_Type()
)
netbT1expired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbT1expired.setStatus("mandatory")
_NetbTiexpired_Type = Counter32
_NetbTiexpired_Object = MibTableColumn
netbTiexpired = _NetbTiexpired_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 19),
    _NetbTiexpired_Type()
)
netbTiexpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbTiexpired.setStatus("mandatory")
_NetbfreeNCB_Type = Integer32
_NetbfreeNCB_Object = MibTableColumn
netbfreeNCB = _NetbfreeNCB_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 20),
    _NetbfreeNCB_Type()
)
netbfreeNCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbfreeNCB.setStatus("mandatory")
_NetbconfiguredNCB_Type = Integer32
_NetbconfiguredNCB_Object = MibTableColumn
netbconfiguredNCB = _NetbconfiguredNCB_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 21),
    _NetbconfiguredNCB_Type()
)
netbconfiguredNCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbconfiguredNCB.setStatus("mandatory")
_NetbmaxNCB_Type = Integer32
_NetbmaxNCB_Object = MibTableColumn
netbmaxNCB = _NetbmaxNCB_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 22),
    _NetbmaxNCB_Type()
)
netbmaxNCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbmaxNCB.setStatus("mandatory")
_Netbtxnobuffer_Type = Integer32
_Netbtxnobuffer_Object = MibTableColumn
netbtxnobuffer = _Netbtxnobuffer_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 23),
    _Netbtxnobuffer_Type()
)
netbtxnobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbtxnobuffer.setStatus("mandatory")
_Netbmaxdatagram_Type = Integer32
_Netbmaxdatagram_Object = MibTableColumn
netbmaxdatagram = _Netbmaxdatagram_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 24),
    _Netbmaxdatagram_Type()
)
netbmaxdatagram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbmaxdatagram.setStatus("mandatory")
_Netbpendingsession_Type = Integer32
_Netbpendingsession_Object = MibTableColumn
netbpendingsession = _Netbpendingsession_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 25),
    _Netbpendingsession_Type()
)
netbpendingsession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbpendingsession.setStatus("mandatory")
_Netbconfiguredpending_Type = Integer32
_Netbconfiguredpending_Object = MibTableColumn
netbconfiguredpending = _Netbconfiguredpending_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 26),
    _Netbconfiguredpending_Type()
)
netbconfiguredpending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbconfiguredpending.setStatus("mandatory")
_Netbmaxpending_Type = Integer32
_Netbmaxpending_Object = MibTableColumn
netbmaxpending = _Netbmaxpending_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 27),
    _Netbmaxpending_Type()
)
netbmaxpending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbmaxpending.setStatus("mandatory")
_Netbmaxdatapacket_Type = Integer32
_Netbmaxdatapacket_Object = MibTableColumn
netbmaxdatapacket = _Netbmaxdatapacket_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 28),
    _Netbmaxdatapacket_Type()
)
netbmaxdatapacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbmaxdatapacket.setStatus("mandatory")
_Netbnumbernames_Type = Integer32
_Netbnumbernames_Object = MibTableColumn
netbnumbernames = _Netbnumbernames_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 29),
    _Netbnumbernames_Type()
)
netbnumbernames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbnumbernames.setStatus("mandatory")
_Netbnumbersessions_Type = Integer32
_Netbnumbersessions_Object = MibTableColumn
netbnumbersessions = _Netbnumbersessions_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 30),
    _Netbnumbersessions_Type()
)
netbnumbersessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbnumbersessions.setStatus("mandatory")
_NetbDATAGRAMoutstanding_Type = Integer32
_NetbDATAGRAMoutstanding_Object = MibTableColumn
netbDATAGRAMoutstanding = _NetbDATAGRAMoutstanding_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 31),
    _NetbDATAGRAMoutstanding_Type()
)
netbDATAGRAMoutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbDATAGRAMoutstanding.setStatus("mandatory")
_NetbANYoustanding_Type = Integer32
_NetbANYoustanding_Object = MibTableColumn
netbANYoustanding = _NetbANYoustanding_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 17, 0, 1, 1, 32),
    _NetbANYoustanding_Type()
)
netbANYoustanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbANYoustanding.setStatus("mandatory")
_Elc_MAC_ObjectIdentity = ObjectIdentity
elc_MAC = _Elc_MAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18)
)
_Elc_ELC_ObjectIdentity = ObjectIdentity
elc_ELC = _Elc_ELC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0)
)
_Elc_ELCTable_Object = MibTable
elc_ELCTable = _Elc_ELCTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1)
)
if mibBuilder.loadTexts:
    elc_ELCTable.setStatus("mandatory")
_Elc_ELCEntry_Object = MibTableRow
elc_ELCEntry = _Elc_ELCEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1)
)
elc_ELCEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "elcSysName"),
    (0, "OLIVETTI-MIB", "elcInstName"),
    (0, "OLIVETTI-MIB", "elcSubAddr"),
)
if mibBuilder.loadTexts:
    elc_ELCEntry.setStatus("mandatory")


class _ElcSysName_Type(DisplayString):
    """Custom type elcSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ElcSysName_Type.__name__ = "DisplayString"
_ElcSysName_Object = MibTableColumn
elcSysName = _ElcSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 1),
    _ElcSysName_Type()
)
elcSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcSysName.setStatus("mandatory")


class _ElcInstName_Type(DisplayString):
    """Custom type elcInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ElcInstName_Type.__name__ = "DisplayString"
_ElcInstName_Object = MibTableColumn
elcInstName = _ElcInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 2),
    _ElcInstName_Type()
)
elcInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcInstName.setStatus("mandatory")


class _ElcSubAddr_Type(DisplayString):
    """Custom type elcSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ElcSubAddr_Type.__name__ = "DisplayString"
_ElcSubAddr_Object = MibTableColumn
elcSubAddr = _ElcSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 3),
    _ElcSubAddr_Type()
)
elcSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcSubAddr.setStatus("mandatory")
_Elctxsuccess_Type = Counter32
_Elctxsuccess_Object = MibTableColumn
elctxsuccess = _Elctxsuccess_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 4),
    _Elctxsuccess_Type()
)
elctxsuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxsuccess.setStatus("mandatory")
_Elctxcollision_Type = Counter32
_Elctxcollision_Object = MibTableColumn
elctxcollision = _Elctxcollision_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 5),
    _Elctxcollision_Type()
)
elctxcollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxcollision.setStatus("mandatory")
_ElcSQEtsterrors_Type = Counter32
_ElcSQEtsterrors_Object = MibTableColumn
elcSQEtsterrors = _ElcSQEtsterrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 6),
    _ElcSQEtsterrors_Type()
)
elcSQEtsterrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcSQEtsterrors.setStatus("mandatory")
_Elcrxsuccess_Type = Counter32
_Elcrxsuccess_Object = MibTableColumn
elcrxsuccess = _Elcrxsuccess_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 7),
    _Elcrxsuccess_Type()
)
elcrxsuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcrxsuccess.setStatus("mandatory")
_ElcrxCRC_Type = Counter32
_ElcrxCRC_Object = MibTableColumn
elcrxCRC = _ElcrxCRC_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 8),
    _ElcrxCRC_Type()
)
elcrxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcrxCRC.setStatus("mandatory")
_Elcrxalignment_Type = Counter32
_Elcrxalignment_Object = MibTableColumn
elcrxalignment = _Elcrxalignment_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 9),
    _Elcrxalignment_Type()
)
elcrxalignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcrxalignment.setStatus("mandatory")
_Elcrxnobuffer_Type = Counter32
_Elcrxnobuffer_Object = MibTableColumn
elcrxnobuffer = _Elcrxnobuffer_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 10),
    _Elcrxnobuffer_Type()
)
elcrxnobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcrxnobuffer.setStatus("mandatory")
_Elcrxoverrun_Type = Counter32
_Elcrxoverrun_Object = MibTableColumn
elcrxoverrun = _Elcrxoverrun_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 11),
    _Elcrxoverrun_Type()
)
elcrxoverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcrxoverrun.setStatus("mandatory")
_Elcrxshframe_Type = Counter32
_Elcrxshframe_Object = MibTableColumn
elcrxshframe = _Elcrxshframe_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 12),
    _Elcrxshframe_Type()
)
elcrxshframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcrxshframe.setStatus("mandatory")
_Elcrxcollision_Type = Counter32
_Elcrxcollision_Object = MibTableColumn
elcrxcollision = _Elcrxcollision_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 13),
    _Elcrxcollision_Type()
)
elcrxcollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elcrxcollision.setStatus("mandatory")
_Elctxattempted_Type = Counter32
_Elctxattempted_Object = MibTableColumn
elctxattempted = _Elctxattempted_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 14),
    _Elctxattempted_Type()
)
elctxattempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxattempted.setStatus("mandatory")
_ElctxlostCS_Type = Counter32
_ElctxlostCS_Object = MibTableColumn
elctxlostCS = _ElctxlostCS_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 15),
    _ElctxlostCS_Type()
)
elctxlostCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxlostCS.setStatus("mandatory")
_ElctxlostCTS_Type = Counter32
_ElctxlostCTS_Object = MibTableColumn
elctxlostCTS = _ElctxlostCTS_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 16),
    _ElctxlostCTS_Type()
)
elctxlostCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxlostCTS.setStatus("mandatory")
_Elctxunderrun_Type = Counter32
_Elctxunderrun_Object = MibTableColumn
elctxunderrun = _Elctxunderrun_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 17),
    _Elctxunderrun_Type()
)
elctxunderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxunderrun.setStatus("mandatory")
_Elctxmaxcollision_Type = Counter32
_Elctxmaxcollision_Object = MibTableColumn
elctxmaxcollision = _Elctxmaxcollision_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 18),
    _Elctxmaxcollision_Type()
)
elctxmaxcollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxmaxcollision.setStatus("mandatory")
_Elctxdeferred_Type = Counter32
_Elctxdeferred_Object = MibTableColumn
elctxdeferred = _Elctxdeferred_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 19),
    _Elctxdeferred_Type()
)
elctxdeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxdeferred.setStatus("mandatory")
_Elctxframexceeding_Type = Counter32
_Elctxframexceeding_Object = MibTableColumn
elctxframexceeding = _Elctxframexceeding_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 20),
    _Elctxframexceeding_Type()
)
elctxframexceeding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxframexceeding.setStatus("mandatory")
_Elctxbytesuccess_Type = Counter32
_Elctxbytesuccess_Object = MibTableColumn
elctxbytesuccess = _Elctxbytesuccess_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 18, 0, 1, 1, 21),
    _Elctxbytesuccess_Type()
)
elctxbytesuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elctxbytesuccess.setStatus("mandatory")
_Ethe_MAC1_ObjectIdentity = ObjectIdentity
ethe_MAC1 = _Ethe_MAC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19)
)
_Ethe_ETH_ObjectIdentity = ObjectIdentity
ethe_ETH = _Ethe_ETH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0)
)
_Ethe_ETHTable_Object = MibTable
ethe_ETHTable = _Ethe_ETHTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1)
)
if mibBuilder.loadTexts:
    ethe_ETHTable.setStatus("mandatory")
_Ethe_ETHEntry_Object = MibTableRow
ethe_ETHEntry = _Ethe_ETHEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1)
)
ethe_ETHEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "etheSysName"),
    (0, "OLIVETTI-MIB", "etheInstName"),
    (0, "OLIVETTI-MIB", "etheSubAddr"),
)
if mibBuilder.loadTexts:
    ethe_ETHEntry.setStatus("mandatory")


class _EtheSysName_Type(DisplayString):
    """Custom type etheSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EtheSysName_Type.__name__ = "DisplayString"
_EtheSysName_Object = MibTableColumn
etheSysName = _EtheSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 1),
    _EtheSysName_Type()
)
etheSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etheSysName.setStatus("mandatory")


class _EtheInstName_Type(DisplayString):
    """Custom type etheInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_EtheInstName_Type.__name__ = "DisplayString"
_EtheInstName_Object = MibTableColumn
etheInstName = _EtheInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 2),
    _EtheInstName_Type()
)
etheInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etheInstName.setStatus("mandatory")


class _EtheSubAddr_Type(DisplayString):
    """Custom type etheSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EtheSubAddr_Type.__name__ = "DisplayString"
_EtheSubAddr_Object = MibTableColumn
etheSubAddr = _EtheSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 3),
    _EtheSubAddr_Type()
)
etheSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etheSubAddr.setStatus("mandatory")
_Ethetxsuccess_Type = Counter32
_Ethetxsuccess_Object = MibTableColumn
ethetxsuccess = _Ethetxsuccess_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 4),
    _Ethetxsuccess_Type()
)
ethetxsuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxsuccess.setStatus("mandatory")
_Ethetxcollision_Type = Counter32
_Ethetxcollision_Object = MibTableColumn
ethetxcollision = _Ethetxcollision_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 5),
    _Ethetxcollision_Type()
)
ethetxcollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxcollision.setStatus("mandatory")
_EtheSQEtsterrors_Type = Counter32
_EtheSQEtsterrors_Object = MibTableColumn
etheSQEtsterrors = _EtheSQEtsterrors_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 6),
    _EtheSQEtsterrors_Type()
)
etheSQEtsterrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etheSQEtsterrors.setStatus("mandatory")
_Etherxsuccess_Type = Counter32
_Etherxsuccess_Object = MibTableColumn
etherxsuccess = _Etherxsuccess_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 7),
    _Etherxsuccess_Type()
)
etherxsuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherxsuccess.setStatus("mandatory")
_EtherxCRC_Type = Counter32
_EtherxCRC_Object = MibTableColumn
etherxCRC = _EtherxCRC_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 8),
    _EtherxCRC_Type()
)
etherxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherxCRC.setStatus("mandatory")
_Etherxalignment_Type = Counter32
_Etherxalignment_Object = MibTableColumn
etherxalignment = _Etherxalignment_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 9),
    _Etherxalignment_Type()
)
etherxalignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherxalignment.setStatus("mandatory")
_Etherxnobuffer_Type = Counter32
_Etherxnobuffer_Object = MibTableColumn
etherxnobuffer = _Etherxnobuffer_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 10),
    _Etherxnobuffer_Type()
)
etherxnobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherxnobuffer.setStatus("mandatory")
_Etherxoverrun_Type = Counter32
_Etherxoverrun_Object = MibTableColumn
etherxoverrun = _Etherxoverrun_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 11),
    _Etherxoverrun_Type()
)
etherxoverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherxoverrun.setStatus("mandatory")
_Etherxshframe_Type = Counter32
_Etherxshframe_Object = MibTableColumn
etherxshframe = _Etherxshframe_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 12),
    _Etherxshframe_Type()
)
etherxshframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherxshframe.setStatus("mandatory")
_Etherxcollision_Type = Counter32
_Etherxcollision_Object = MibTableColumn
etherxcollision = _Etherxcollision_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 13),
    _Etherxcollision_Type()
)
etherxcollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherxcollision.setStatus("mandatory")
_Ethetxattempted_Type = Counter32
_Ethetxattempted_Object = MibTableColumn
ethetxattempted = _Ethetxattempted_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 14),
    _Ethetxattempted_Type()
)
ethetxattempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxattempted.setStatus("mandatory")
_EthetxlostCS_Type = Counter32
_EthetxlostCS_Object = MibTableColumn
ethetxlostCS = _EthetxlostCS_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 15),
    _EthetxlostCS_Type()
)
ethetxlostCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxlostCS.setStatus("mandatory")
_EthetxlostCTS_Type = Counter32
_EthetxlostCTS_Object = MibTableColumn
ethetxlostCTS = _EthetxlostCTS_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 16),
    _EthetxlostCTS_Type()
)
ethetxlostCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxlostCTS.setStatus("mandatory")
_Ethetxunderrun_Type = Counter32
_Ethetxunderrun_Object = MibTableColumn
ethetxunderrun = _Ethetxunderrun_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 17),
    _Ethetxunderrun_Type()
)
ethetxunderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxunderrun.setStatus("mandatory")
_Ethetxmaxcollision_Type = Counter32
_Ethetxmaxcollision_Object = MibTableColumn
ethetxmaxcollision = _Ethetxmaxcollision_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 18),
    _Ethetxmaxcollision_Type()
)
ethetxmaxcollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxmaxcollision.setStatus("mandatory")
_Ethetxdeferred_Type = Counter32
_Ethetxdeferred_Object = MibTableColumn
ethetxdeferred = _Ethetxdeferred_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 19),
    _Ethetxdeferred_Type()
)
ethetxdeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxdeferred.setStatus("mandatory")
_Ethetxframexceeding_Type = Counter32
_Ethetxframexceeding_Object = MibTableColumn
ethetxframexceeding = _Ethetxframexceeding_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 20),
    _Ethetxframexceeding_Type()
)
ethetxframexceeding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxframexceeding.setStatus("mandatory")
_Ethetxbytesuccess_Type = Counter32
_Ethetxbytesuccess_Object = MibTableColumn
ethetxbytesuccess = _Ethetxbytesuccess_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 19, 0, 1, 1, 21),
    _Ethetxbytesuccess_Type()
)
ethetxbytesuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethetxbytesuccess.setStatus("mandatory")
_Onetware_NW_ObjectIdentity = ObjectIdentity
onetware_NW = _Onetware_NW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53)
)
_Onetware_SRVNW_ObjectIdentity = ObjectIdentity
onetware_SRVNW = _Onetware_SRVNW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1)
)
_Onetware_SRVNWTable_Object = MibTable
onetware_SRVNWTable = _Onetware_SRVNWTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1)
)
if mibBuilder.loadTexts:
    onetware_SRVNWTable.setStatus("mandatory")
_Onetware_SRVNWEntry_Object = MibTableRow
onetware_SRVNWEntry = _Onetware_SRVNWEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1)
)
onetware_SRVNWEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "onetwareSysName"),
    (0, "OLIVETTI-MIB", "onetwareInstName"),
    (0, "OLIVETTI-MIB", "onetwareSubAddr"),
)
if mibBuilder.loadTexts:
    onetware_SRVNWEntry.setStatus("mandatory")


class _OnetwareSysName_Type(DisplayString):
    """Custom type onetwareSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OnetwareSysName_Type.__name__ = "DisplayString"
_OnetwareSysName_Object = MibTableColumn
onetwareSysName = _OnetwareSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 1),
    _OnetwareSysName_Type()
)
onetwareSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareSysName.setStatus("mandatory")


class _OnetwareInstName_Type(DisplayString):
    """Custom type onetwareInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_OnetwareInstName_Type.__name__ = "DisplayString"
_OnetwareInstName_Object = MibTableColumn
onetwareInstName = _OnetwareInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 2),
    _OnetwareInstName_Type()
)
onetwareInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareInstName.setStatus("mandatory")


class _OnetwareSubAddr_Type(DisplayString):
    """Custom type onetwareSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OnetwareSubAddr_Type.__name__ = "DisplayString"
_OnetwareSubAddr_Object = MibTableColumn
onetwareSubAddr = _OnetwareSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 3),
    _OnetwareSubAddr_Type()
)
onetwareSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareSubAddr.setStatus("mandatory")
_OnetwareMaxClientConnSupported_Type = Counter32
_OnetwareMaxClientConnSupported_Object = MibTableColumn
onetwareMaxClientConnSupported = _OnetwareMaxClientConnSupported_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 4),
    _OnetwareMaxClientConnSupported_Type()
)
onetwareMaxClientConnSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxClientConnSupported.setStatus("mandatory")
_OnetwareClientConnInUse_Type = Counter32
_OnetwareClientConnInUse_Object = MibTableColumn
onetwareClientConnInUse = _OnetwareClientConnInUse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 5),
    _OnetwareClientConnInUse_Type()
)
onetwareClientConnInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareClientConnInUse.setStatus("mandatory")
_OnetwarePeakClientConnUsed_Type = Counter32
_OnetwarePeakClientConnUsed_Object = MibTableColumn
onetwarePeakClientConnUsed = _OnetwarePeakClientConnUsed_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 6),
    _OnetwarePeakClientConnUsed_Type()
)
onetwarePeakClientConnUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwarePeakClientConnUsed.setStatus("mandatory")
_OnetwareMaxVolumes_Type = Counter32
_OnetwareMaxVolumes_Object = MibTableColumn
onetwareMaxVolumes = _OnetwareMaxVolumes_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 7),
    _OnetwareMaxVolumes_Type()
)
onetwareMaxVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxVolumes.setStatus("mandatory")
_OnetwareNWProcs_Type = Counter32
_OnetwareNWProcs_Object = MibTableColumn
onetwareNWProcs = _OnetwareNWProcs_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 8),
    _OnetwareNWProcs_Type()
)
onetwareNWProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareNWProcs.setStatus("mandatory")
_OnetwareTotalPackets_Type = Integer32
_OnetwareTotalPackets_Object = MibTableColumn
onetwareTotalPackets = _OnetwareTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 9),
    _OnetwareTotalPackets_Type()
)
onetwareTotalPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareTotalPackets.setStatus("mandatory")
_OnetwareCreateConnectionRequests_Type = Integer32
_OnetwareCreateConnectionRequests_Object = MibTableColumn
onetwareCreateConnectionRequests = _OnetwareCreateConnectionRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 10),
    _OnetwareCreateConnectionRequests_Type()
)
onetwareCreateConnectionRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareCreateConnectionRequests.setStatus("mandatory")
_OnetwareCreateFileRequests_Type = Integer32
_OnetwareCreateFileRequests_Object = MibTableColumn
onetwareCreateFileRequests = _OnetwareCreateFileRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 11),
    _OnetwareCreateFileRequests_Type()
)
onetwareCreateFileRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareCreateFileRequests.setStatus("mandatory")
_OnetwareOpenRequests_Type = Integer32
_OnetwareOpenRequests_Object = MibTableColumn
onetwareOpenRequests = _OnetwareOpenRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 12),
    _OnetwareOpenRequests_Type()
)
onetwareOpenRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareOpenRequests.setStatus("mandatory")
_OnetwareReadRequests_Type = Integer32
_OnetwareReadRequests_Object = MibTableColumn
onetwareReadRequests = _OnetwareReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 13),
    _OnetwareReadRequests_Type()
)
onetwareReadRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareReadRequests.setStatus("mandatory")
_OnetwareWriteRequests_Type = Integer32
_OnetwareWriteRequests_Object = MibTableColumn
onetwareWriteRequests = _OnetwareWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 14),
    _OnetwareWriteRequests_Type()
)
onetwareWriteRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareWriteRequests.setStatus("mandatory")
_OnetwareNumOpenFiles_Type = Counter32
_OnetwareNumOpenFiles_Object = MibTableColumn
onetwareNumOpenFiles = _OnetwareNumOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 15),
    _OnetwareNumOpenFiles_Type()
)
onetwareNumOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareNumOpenFiles.setStatus("mandatory")
_OnetwareMaxSimultaneousOpens_Type = Counter32
_OnetwareMaxSimultaneousOpens_Object = MibTableColumn
onetwareMaxSimultaneousOpens = _OnetwareMaxSimultaneousOpens_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 16),
    _OnetwareMaxSimultaneousOpens_Type()
)
onetwareMaxSimultaneousOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxSimultaneousOpens.setStatus("mandatory")
_OnetwareLostPacketResends_Type = Integer32
_OnetwareLostPacketResends_Object = MibTableColumn
onetwareLostPacketResends = _OnetwareLostPacketResends_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 17),
    _OnetwareLostPacketResends_Type()
)
onetwareLostPacketResends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareLostPacketResends.setStatus("mandatory")
_OnetwareCacheHits_Type = Integer32
_OnetwareCacheHits_Object = MibTableColumn
onetwareCacheHits = _OnetwareCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 18),
    _OnetwareCacheHits_Type()
)
onetwareCacheHits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareCacheHits.setStatus("mandatory")
_OnetwareCacheMisses_Type = Integer32
_OnetwareCacheMisses_Object = MibTableColumn
onetwareCacheMisses = _OnetwareCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 19),
    _OnetwareCacheMisses_Type()
)
onetwareCacheMisses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareCacheMisses.setStatus("mandatory")
_OnetwarePrintRequests_Type = Integer32
_OnetwarePrintRequests_Object = MibTableColumn
onetwarePrintRequests = _OnetwarePrintRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 20),
    _OnetwarePrintRequests_Type()
)
onetwarePrintRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwarePrintRequests.setStatus("mandatory")
_OnetwareMessageRequests_Type = Integer32
_OnetwareMessageRequests_Object = MibTableColumn
onetwareMessageRequests = _OnetwareMessageRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 21),
    _OnetwareMessageRequests_Type()
)
onetwareMessageRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareMessageRequests.setStatus("mandatory")
_OnetwareDirectoryRequests_Type = Integer32
_OnetwareDirectoryRequests_Object = MibTableColumn
onetwareDirectoryRequests = _OnetwareDirectoryRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 22),
    _OnetwareDirectoryRequests_Type()
)
onetwareDirectoryRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareDirectoryRequests.setStatus("mandatory")
_OnetwareBinderyAndMiscRequests_Type = Integer32
_OnetwareBinderyAndMiscRequests_Object = MibTableColumn
onetwareBinderyAndMiscRequests = _OnetwareBinderyAndMiscRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 23),
    _OnetwareBinderyAndMiscRequests_Type()
)
onetwareBinderyAndMiscRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareBinderyAndMiscRequests.setStatus("mandatory")
_OnetwareUnknownRequests_Type = Integer32
_OnetwareUnknownRequests_Object = MibTableColumn
onetwareUnknownRequests = _OnetwareUnknownRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 24),
    _OnetwareUnknownRequests_Type()
)
onetwareUnknownRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareUnknownRequests.setStatus("mandatory")
_OnetwareSharedMemorySize_Type = Counter32
_OnetwareSharedMemorySize_Object = MibTableColumn
onetwareSharedMemorySize = _OnetwareSharedMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 25),
    _OnetwareSharedMemorySize_Type()
)
onetwareSharedMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareSharedMemorySize.setStatus("mandatory")
_OnetwareCurrentSharedMemoryUsage_Type = Counter32
_OnetwareCurrentSharedMemoryUsage_Object = MibTableColumn
onetwareCurrentSharedMemoryUsage = _OnetwareCurrentSharedMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 26),
    _OnetwareCurrentSharedMemoryUsage_Type()
)
onetwareCurrentSharedMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareCurrentSharedMemoryUsage.setStatus("mandatory")
_OnetwareMaxSharedMemoryUsed_Type = Counter32
_OnetwareMaxSharedMemoryUsed_Object = MibTableColumn
onetwareMaxSharedMemoryUsed = _OnetwareMaxSharedMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 27),
    _OnetwareMaxSharedMemoryUsed_Type()
)
onetwareMaxSharedMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxSharedMemoryUsed.setStatus("mandatory")
_OnetwareLogicalLockRequests_Type = Integer32
_OnetwareLogicalLockRequests_Object = MibTableColumn
onetwareLogicalLockRequests = _OnetwareLogicalLockRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 28),
    _OnetwareLogicalLockRequests_Type()
)
onetwareLogicalLockRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareLogicalLockRequests.setStatus("mandatory")
_OnetwareNumLogicalLocks_Type = Counter32
_OnetwareNumLogicalLocks_Object = MibTableColumn
onetwareNumLogicalLocks = _OnetwareNumLogicalLocks_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 29),
    _OnetwareNumLogicalLocks_Type()
)
onetwareNumLogicalLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareNumLogicalLocks.setStatus("mandatory")
_OnetwareMaxSimultaneousLogLocks_Type = Counter32
_OnetwareMaxSimultaneousLogLocks_Object = MibTableColumn
onetwareMaxSimultaneousLogLocks = _OnetwareMaxSimultaneousLogLocks_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 30),
    _OnetwareMaxSimultaneousLogLocks_Type()
)
onetwareMaxSimultaneousLogLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxSimultaneousLogLocks.setStatus("mandatory")
_OnetwareFileLockRequests_Type = Integer32
_OnetwareFileLockRequests_Object = MibTableColumn
onetwareFileLockRequests = _OnetwareFileLockRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 31),
    _OnetwareFileLockRequests_Type()
)
onetwareFileLockRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareFileLockRequests.setStatus("mandatory")
_OnetwareNumFileLocks_Type = Counter32
_OnetwareNumFileLocks_Object = MibTableColumn
onetwareNumFileLocks = _OnetwareNumFileLocks_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 32),
    _OnetwareNumFileLocks_Type()
)
onetwareNumFileLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareNumFileLocks.setStatus("mandatory")
_OnetwareMaxSimultaneousFileLocks_Type = Counter32
_OnetwareMaxSimultaneousFileLocks_Object = MibTableColumn
onetwareMaxSimultaneousFileLocks = _OnetwareMaxSimultaneousFileLocks_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 33),
    _OnetwareMaxSimultaneousFileLocks_Type()
)
onetwareMaxSimultaneousFileLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxSimultaneousFileLocks.setStatus("mandatory")
_OnetwarePhysLockRequests_Type = Integer32
_OnetwarePhysLockRequests_Object = MibTableColumn
onetwarePhysLockRequests = _OnetwarePhysLockRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 34),
    _OnetwarePhysLockRequests_Type()
)
onetwarePhysLockRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwarePhysLockRequests.setStatus("mandatory")
_OnetwareNumPhysLocks_Type = Counter32
_OnetwareNumPhysLocks_Object = MibTableColumn
onetwareNumPhysLocks = _OnetwareNumPhysLocks_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 35),
    _OnetwareNumPhysLocks_Type()
)
onetwareNumPhysLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareNumPhysLocks.setStatus("mandatory")
_OnetwareMaxSimultaneousPhysLocks_Type = Counter32
_OnetwareMaxSimultaneousPhysLocks_Object = MibTableColumn
onetwareMaxSimultaneousPhysLocks = _OnetwareMaxSimultaneousPhysLocks_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 36),
    _OnetwareMaxSimultaneousPhysLocks_Type()
)
onetwareMaxSimultaneousPhysLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxSimultaneousPhysLocks.setStatus("mandatory")
_OnetwareSemaphoreRequests_Type = Integer32
_OnetwareSemaphoreRequests_Object = MibTableColumn
onetwareSemaphoreRequests = _OnetwareSemaphoreRequests_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 37),
    _OnetwareSemaphoreRequests_Type()
)
onetwareSemaphoreRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onetwareSemaphoreRequests.setStatus("mandatory")
_OnetwareNumSemaphores_Type = Counter32
_OnetwareNumSemaphores_Object = MibTableColumn
onetwareNumSemaphores = _OnetwareNumSemaphores_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 38),
    _OnetwareNumSemaphores_Type()
)
onetwareNumSemaphores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareNumSemaphores.setStatus("mandatory")
_OnetwareMaxSimultaneousSemaphores_Type = Counter32
_OnetwareMaxSimultaneousSemaphores_Object = MibTableColumn
onetwareMaxSimultaneousSemaphores = _OnetwareMaxSimultaneousSemaphores_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 53, 1, 1, 1, 39),
    _OnetwareMaxSimultaneousSemaphores_Type()
)
onetwareMaxSimultaneousSemaphores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onetwareMaxSimultaneousSemaphores.setStatus("mandatory")
_Uxos_disc_ObjectIdentity = ObjectIdentity
uxos_disc = _Uxos_disc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65)
)
_Uxos_scsi_ObjectIdentity = ObjectIdentity
uxos_scsi = _Uxos_scsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0)
)
_Uxos_diskTable_Object = MibTable
uxos_diskTable = _Uxos_diskTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1)
)
if mibBuilder.loadTexts:
    uxos_diskTable.setStatus("mandatory")
_Uxos_diskEntry_Object = MibTableRow
uxos_diskEntry = _Uxos_diskEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1)
)
uxos_diskEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-diskSysName"),
    (0, "OLIVETTI-MIB", "uxos-diskInstName"),
    (0, "OLIVETTI-MIB", "uxos-diskSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_diskEntry.setStatus("mandatory")


class _Uxos_diskSysName_Type(DisplayString):
    """Custom type uxos_diskSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_diskSysName_Type.__name__ = "DisplayString"
_Uxos_diskSysName_Object = MibScalar
uxos_diskSysName = _Uxos_diskSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 1),
    _Uxos_diskSysName_Type()
)
uxos_diskSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_diskSysName.setStatus("mandatory")


class _Uxos_diskInstName_Type(DisplayString):
    """Custom type uxos_diskInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_diskInstName_Type.__name__ = "DisplayString"
_Uxos_diskInstName_Object = MibScalar
uxos_diskInstName = _Uxos_diskInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 2),
    _Uxos_diskInstName_Type()
)
uxos_diskInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_diskInstName.setStatus("mandatory")


class _Uxos_diskSubAddr_Type(DisplayString):
    """Custom type uxos_diskSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_diskSubAddr_Type.__name__ = "DisplayString"
_Uxos_diskSubAddr_Object = MibScalar
uxos_diskSubAddr = _Uxos_diskSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 3),
    _Uxos_diskSubAddr_Type()
)
uxos_diskSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_diskSubAddr.setStatus("mandatory")
_Uxos_numRW_Type = Counter32
_Uxos_numRW_Object = MibScalar
uxos_numRW = _Uxos_numRW_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 4),
    _Uxos_numRW_Type()
)
uxos_numRW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numRW.setStatus("mandatory")
_Uxos_numOtherOp_Type = Counter32
_Uxos_numOtherOp_Object = MibScalar
uxos_numOtherOp = _Uxos_numOtherOp_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 5),
    _Uxos_numOtherOp_Type()
)
uxos_numOtherOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numOtherOp.setStatus("mandatory")
_Uxos_numJobsToDr_Type = Counter32
_Uxos_numJobsToDr_Object = MibScalar
uxos_numJobsToDr = _Uxos_numJobsToDr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 6),
    _Uxos_numJobsToDr_Type()
)
uxos_numJobsToDr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numJobsToDr.setStatus("mandatory")
_Uxos_numUnlogErr_Type = Counter32
_Uxos_numUnlogErr_Object = MibScalar
uxos_numUnlogErr = _Uxos_numUnlogErr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 7),
    _Uxos_numUnlogErr_Type()
)
uxos_numUnlogErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numUnlogErr.setStatus("mandatory")
_Uxos_totBlkTrans_Type = Counter32
_Uxos_totBlkTrans_Object = MibScalar
uxos_totBlkTrans = _Uxos_totBlkTrans_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 8),
    _Uxos_totBlkTrans_Type()
)
uxos_totBlkTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_totBlkTrans.setStatus("mandatory")
_Uxos_totBlkResp_Type = Counter32
_Uxos_totBlkResp_Object = MibScalar
uxos_totBlkResp = _Uxos_totBlkResp_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 9),
    _Uxos_totBlkResp_Type()
)
uxos_totBlkResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_totBlkResp.setStatus("mandatory")
_Uxos_cumulUse_Type = Counter32
_Uxos_cumulUse_Object = MibScalar
uxos_cumulUse = _Uxos_cumulUse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 10),
    _Uxos_cumulUse_Type()
)
uxos_cumulUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cumulUse.setStatus("mandatory")
_Uxos_major_Type = Counter32
_Uxos_major_Object = MibScalar
uxos_major = _Uxos_major_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 11),
    _Uxos_major_Type()
)
uxos_major.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_major.setStatus("mandatory")
_Uxos_minor_Type = Counter32
_Uxos_minor_Object = MibScalar
uxos_minor = _Uxos_minor_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 12),
    _Uxos_minor_Type()
)
uxos_minor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_minor.setStatus("mandatory")
_Uxos_totNumRead_Type = Counter32
_Uxos_totNumRead_Object = MibScalar
uxos_totNumRead = _Uxos_totNumRead_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 13),
    _Uxos_totNumRead_Type()
)
uxos_totNumRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_totNumRead.setStatus("mandatory")
_Uxos_totNumWrite_Type = Counter32
_Uxos_totNumWrite_Object = MibScalar
uxos_totNumWrite = _Uxos_totNumWrite_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 14),
    _Uxos_totNumWrite_Type()
)
uxos_totNumWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_totNumWrite.setStatus("mandatory")
_Uxos_cumulQueLen_Type = Counter32
_Uxos_cumulQueLen_Object = MibScalar
uxos_cumulQueLen = _Uxos_cumulQueLen_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 15),
    _Uxos_cumulQueLen_Type()
)
uxos_cumulQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cumulQueLen.setStatus("mandatory")
_Uxos_maxQueLen_Type = Counter32
_Uxos_maxQueLen_Object = MibScalar
uxos_maxQueLen = _Uxos_maxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 16),
    _Uxos_maxQueLen_Type()
)
uxos_maxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_maxQueLen.setStatus("mandatory")
_Uxos_minQueLen_Type = Counter32
_Uxos_minQueLen_Object = MibScalar
uxos_minQueLen = _Uxos_minQueLen_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 17),
    _Uxos_minQueLen_Type()
)
uxos_minQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_minQueLen.setStatus("mandatory")
_Uxos_cumulSeekDist_Type = Counter32
_Uxos_cumulSeekDist_Object = MibScalar
uxos_cumulSeekDist = _Uxos_cumulSeekDist_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 18),
    _Uxos_cumulSeekDist_Type()
)
uxos_cumulSeekDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cumulSeekDist.setStatus("mandatory")
_Uxos_driveActive_Type = Counter32
_Uxos_driveActive_Object = MibScalar
uxos_driveActive = _Uxos_driveActive_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 19),
    _Uxos_driveActive_Type()
)
uxos_driveActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_driveActive.setStatus("mandatory")
_Uxos_drivePerf_Type = Counter32
_Uxos_drivePerf_Object = MibScalar
uxos_drivePerf = _Uxos_drivePerf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 20),
    _Uxos_drivePerf_Type()
)
uxos_drivePerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_drivePerf.setStatus("mandatory")
_Uxos_startOfQueue_Type = Integer32
_Uxos_startOfQueue_Object = MibScalar
uxos_startOfQueue = _Uxos_startOfQueue_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 21),
    _Uxos_startOfQueue_Type()
)
uxos_startOfQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_startOfQueue.setStatus("mandatory")
_Uxos_lastInQueue_Type = Integer32
_Uxos_lastInQueue_Object = MibScalar
uxos_lastInQueue = _Uxos_lastInQueue_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 22),
    _Uxos_lastInQueue_Type()
)
uxos_lastInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lastInQueue.setStatus("mandatory")
_Uxos_queue01_Type = Integer32
_Uxos_queue01_Object = MibScalar
uxos_queue01 = _Uxos_queue01_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 23),
    _Uxos_queue01_Type()
)
uxos_queue01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue01.setStatus("mandatory")
_Uxos_queue02_Type = Integer32
_Uxos_queue02_Object = MibScalar
uxos_queue02 = _Uxos_queue02_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 24),
    _Uxos_queue02_Type()
)
uxos_queue02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue02.setStatus("mandatory")
_Uxos_queue11_Type = Integer32
_Uxos_queue11_Object = MibScalar
uxos_queue11 = _Uxos_queue11_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 25),
    _Uxos_queue11_Type()
)
uxos_queue11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue11.setStatus("mandatory")
_Uxos_queue12_Type = Integer32
_Uxos_queue12_Object = MibScalar
uxos_queue12 = _Uxos_queue12_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 26),
    _Uxos_queue12_Type()
)
uxos_queue12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue12.setStatus("mandatory")
_Uxos_queue21_Type = Integer32
_Uxos_queue21_Object = MibScalar
uxos_queue21 = _Uxos_queue21_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 27),
    _Uxos_queue21_Type()
)
uxos_queue21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue21.setStatus("mandatory")
_Uxos_queue22_Type = Integer32
_Uxos_queue22_Object = MibScalar
uxos_queue22 = _Uxos_queue22_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 28),
    _Uxos_queue22_Type()
)
uxos_queue22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue22.setStatus("mandatory")
_Uxos_queue31_Type = Integer32
_Uxos_queue31_Object = MibScalar
uxos_queue31 = _Uxos_queue31_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 29),
    _Uxos_queue31_Type()
)
uxos_queue31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue31.setStatus("mandatory")
_Uxos_queue32_Type = Integer32
_Uxos_queue32_Object = MibScalar
uxos_queue32 = _Uxos_queue32_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 30),
    _Uxos_queue32_Type()
)
uxos_queue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue32.setStatus("mandatory")
_Uxos_queue41_Type = Integer32
_Uxos_queue41_Object = MibScalar
uxos_queue41 = _Uxos_queue41_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 31),
    _Uxos_queue41_Type()
)
uxos_queue41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue41.setStatus("mandatory")
_Uxos_queue42_Type = Integer32
_Uxos_queue42_Object = MibScalar
uxos_queue42 = _Uxos_queue42_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 32),
    _Uxos_queue42_Type()
)
uxos_queue42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue42.setStatus("mandatory")
_Uxos_queue51_Type = Integer32
_Uxos_queue51_Object = MibScalar
uxos_queue51 = _Uxos_queue51_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 33),
    _Uxos_queue51_Type()
)
uxos_queue51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue51.setStatus("mandatory")
_Uxos_queue52_Type = Integer32
_Uxos_queue52_Object = MibScalar
uxos_queue52 = _Uxos_queue52_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 34),
    _Uxos_queue52_Type()
)
uxos_queue52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue52.setStatus("mandatory")
_Uxos_queue61_Type = Integer32
_Uxos_queue61_Object = MibScalar
uxos_queue61 = _Uxos_queue61_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 35),
    _Uxos_queue61_Type()
)
uxos_queue61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue61.setStatus("mandatory")
_Uxos_queue62_Type = Integer32
_Uxos_queue62_Object = MibScalar
uxos_queue62 = _Uxos_queue62_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 36),
    _Uxos_queue62_Type()
)
uxos_queue62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue62.setStatus("mandatory")
_Uxos_queue71_Type = Integer32
_Uxos_queue71_Object = MibScalar
uxos_queue71 = _Uxos_queue71_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 37),
    _Uxos_queue71_Type()
)
uxos_queue71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue71.setStatus("mandatory")
_Uxos_queue72_Type = Integer32
_Uxos_queue72_Object = MibScalar
uxos_queue72 = _Uxos_queue72_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 38),
    _Uxos_queue72_Type()
)
uxos_queue72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue72.setStatus("mandatory")
_Uxos_queue81_Type = Integer32
_Uxos_queue81_Object = MibScalar
uxos_queue81 = _Uxos_queue81_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 39),
    _Uxos_queue81_Type()
)
uxos_queue81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue81.setStatus("mandatory")
_Uxos_queue82_Type = Integer32
_Uxos_queue82_Object = MibScalar
uxos_queue82 = _Uxos_queue82_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 40),
    _Uxos_queue82_Type()
)
uxos_queue82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue82.setStatus("mandatory")
_Uxos_queue91_Type = Integer32
_Uxos_queue91_Object = MibScalar
uxos_queue91 = _Uxos_queue91_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 41),
    _Uxos_queue91_Type()
)
uxos_queue91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue91.setStatus("mandatory")
_Uxos_queue92_Type = Integer32
_Uxos_queue92_Object = MibScalar
uxos_queue92 = _Uxos_queue92_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 65, 0, 1, 1, 42),
    _Uxos_queue92_Type()
)
uxos_queue92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_queue92.setStatus("mandatory")
_Uxos_core_ObjectIdentity = ObjectIdentity
uxos_core = _Uxos_core_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77)
)
_Uxos_cpu_ObjectIdentity = ObjectIdentity
uxos_cpu = _Uxos_cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 1)
)
_Uxos_cpuTable_Object = MibTable
uxos_cpuTable = _Uxos_cpuTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 1, 1)
)
if mibBuilder.loadTexts:
    uxos_cpuTable.setStatus("mandatory")
_Uxos_cpuEntry_Object = MibTableRow
uxos_cpuEntry = _Uxos_cpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 1, 1, 1)
)
uxos_cpuEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-cpuSysName"),
    (0, "OLIVETTI-MIB", "uxos-cpuInstName"),
    (0, "OLIVETTI-MIB", "uxos-cpuSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_cpuEntry.setStatus("mandatory")


class _Uxos_cpuSysName_Type(DisplayString):
    """Custom type uxos_cpuSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_cpuSysName_Type.__name__ = "DisplayString"
_Uxos_cpuSysName_Object = MibScalar
uxos_cpuSysName = _Uxos_cpuSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 1, 1, 1, 1),
    _Uxos_cpuSysName_Type()
)
uxos_cpuSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuSysName.setStatus("mandatory")


class _Uxos_cpuInstName_Type(DisplayString):
    """Custom type uxos_cpuInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_cpuInstName_Type.__name__ = "DisplayString"
_Uxos_cpuInstName_Object = MibScalar
uxos_cpuInstName = _Uxos_cpuInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 1, 1, 1, 2),
    _Uxos_cpuInstName_Type()
)
uxos_cpuInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuInstName.setStatus("mandatory")


class _Uxos_cpuSubAddr_Type(DisplayString):
    """Custom type uxos_cpuSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_cpuSubAddr_Type.__name__ = "DisplayString"
_Uxos_cpuSubAddr_Object = MibScalar
uxos_cpuSubAddr = _Uxos_cpuSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 1, 1, 1, 3),
    _Uxos_cpuSubAddr_Type()
)
uxos_cpuSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuSubAddr.setStatus("mandatory")
_Uxos_numOfCpu_Type = Counter32
_Uxos_numOfCpu_Object = MibScalar
uxos_numOfCpu = _Uxos_numOfCpu_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 1, 1, 1, 4),
    _Uxos_numOfCpu_Type()
)
uxos_numOfCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numOfCpu.setStatus("mandatory")
_Uxos_nproc_ObjectIdentity = ObjectIdentity
uxos_nproc = _Uxos_nproc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 2)
)
_Uxos_nprocTable_Object = MibTable
uxos_nprocTable = _Uxos_nprocTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 2, 1)
)
if mibBuilder.loadTexts:
    uxos_nprocTable.setStatus("mandatory")
_Uxos_nprocEntry_Object = MibTableRow
uxos_nprocEntry = _Uxos_nprocEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 2, 1, 1)
)
uxos_nprocEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-nprocSysName"),
    (0, "OLIVETTI-MIB", "uxos-nprocInstName"),
    (0, "OLIVETTI-MIB", "uxos-nprocSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_nprocEntry.setStatus("mandatory")


class _Uxos_nprocSysName_Type(DisplayString):
    """Custom type uxos_nprocSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_nprocSysName_Type.__name__ = "DisplayString"
_Uxos_nprocSysName_Object = MibScalar
uxos_nprocSysName = _Uxos_nprocSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 2, 1, 1, 1),
    _Uxos_nprocSysName_Type()
)
uxos_nprocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_nprocSysName.setStatus("mandatory")


class _Uxos_nprocInstName_Type(DisplayString):
    """Custom type uxos_nprocInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_nprocInstName_Type.__name__ = "DisplayString"
_Uxos_nprocInstName_Object = MibScalar
uxos_nprocInstName = _Uxos_nprocInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 2, 1, 1, 2),
    _Uxos_nprocInstName_Type()
)
uxos_nprocInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_nprocInstName.setStatus("mandatory")


class _Uxos_nprocSubAddr_Type(DisplayString):
    """Custom type uxos_nprocSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_nprocSubAddr_Type.__name__ = "DisplayString"
_Uxos_nprocSubAddr_Object = MibScalar
uxos_nprocSubAddr = _Uxos_nprocSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 2, 1, 1, 3),
    _Uxos_nprocSubAddr_Type()
)
uxos_nprocSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_nprocSubAddr.setStatus("mandatory")
_Uxos_numOfProc_Type = Counter32
_Uxos_numOfProc_Object = MibScalar
uxos_numOfProc = _Uxos_numOfProc_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 2, 1, 1, 4),
    _Uxos_numOfProc_Type()
)
uxos_numOfProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numOfProc.setStatus("mandatory")
_Uxos_ufsfreeinode_ObjectIdentity = ObjectIdentity
uxos_ufsfreeinode = _Uxos_ufsfreeinode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 3)
)
_Uxos_ufsfreeinodeTable_Object = MibTable
uxos_ufsfreeinodeTable = _Uxos_ufsfreeinodeTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 3, 1)
)
if mibBuilder.loadTexts:
    uxos_ufsfreeinodeTable.setStatus("mandatory")
_Uxos_ufsfreeinodeEntry_Object = MibTableRow
uxos_ufsfreeinodeEntry = _Uxos_ufsfreeinodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 3, 1, 1)
)
uxos_ufsfreeinodeEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-ufsfreeinodeSysName"),
    (0, "OLIVETTI-MIB", "uxos-ufsfreeinodeInstName"),
    (0, "OLIVETTI-MIB", "uxos-ufsfreeinodeSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_ufsfreeinodeEntry.setStatus("mandatory")


class _Uxos_ufsfreeinodeSysName_Type(DisplayString):
    """Custom type uxos_ufsfreeinodeSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_ufsfreeinodeSysName_Type.__name__ = "DisplayString"
_Uxos_ufsfreeinodeSysName_Object = MibScalar
uxos_ufsfreeinodeSysName = _Uxos_ufsfreeinodeSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 3, 1, 1, 1),
    _Uxos_ufsfreeinodeSysName_Type()
)
uxos_ufsfreeinodeSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ufsfreeinodeSysName.setStatus("mandatory")


class _Uxos_ufsfreeinodeInstName_Type(DisplayString):
    """Custom type uxos_ufsfreeinodeInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_ufsfreeinodeInstName_Type.__name__ = "DisplayString"
_Uxos_ufsfreeinodeInstName_Object = MibScalar
uxos_ufsfreeinodeInstName = _Uxos_ufsfreeinodeInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 3, 1, 1, 2),
    _Uxos_ufsfreeinodeInstName_Type()
)
uxos_ufsfreeinodeInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ufsfreeinodeInstName.setStatus("mandatory")


class _Uxos_ufsfreeinodeSubAddr_Type(DisplayString):
    """Custom type uxos_ufsfreeinodeSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_ufsfreeinodeSubAddr_Type.__name__ = "DisplayString"
_Uxos_ufsfreeinodeSubAddr_Object = MibScalar
uxos_ufsfreeinodeSubAddr = _Uxos_ufsfreeinodeSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 3, 1, 1, 3),
    _Uxos_ufsfreeinodeSubAddr_Type()
)
uxos_ufsfreeinodeSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ufsfreeinodeSubAddr.setStatus("mandatory")
_Uxos_numOfUfsfreeinode_Type = Counter32
_Uxos_numOfUfsfreeinode_Object = MibScalar
uxos_numOfUfsfreeinode = _Uxos_numOfUfsfreeinode_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 3, 1, 1, 4),
    _Uxos_numOfUfsfreeinode_Type()
)
uxos_numOfUfsfreeinode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numOfUfsfreeinode.setStatus("mandatory")
_Uxos_physmem_ObjectIdentity = ObjectIdentity
uxos_physmem = _Uxos_physmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 4)
)
_Uxos_memTable_Object = MibTable
uxos_memTable = _Uxos_memTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 4, 1)
)
if mibBuilder.loadTexts:
    uxos_memTable.setStatus("mandatory")
_Uxos_memEntry_Object = MibTableRow
uxos_memEntry = _Uxos_memEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 4, 1, 1)
)
uxos_memEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-memSysName"),
    (0, "OLIVETTI-MIB", "uxos-memInstName"),
    (0, "OLIVETTI-MIB", "uxos-memSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_memEntry.setStatus("mandatory")


class _Uxos_memSysName_Type(DisplayString):
    """Custom type uxos_memSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_memSysName_Type.__name__ = "DisplayString"
_Uxos_memSysName_Object = MibScalar
uxos_memSysName = _Uxos_memSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 4, 1, 1, 1),
    _Uxos_memSysName_Type()
)
uxos_memSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_memSysName.setStatus("mandatory")


class _Uxos_memInstName_Type(DisplayString):
    """Custom type uxos_memInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_memInstName_Type.__name__ = "DisplayString"
_Uxos_memInstName_Object = MibScalar
uxos_memInstName = _Uxos_memInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 4, 1, 1, 2),
    _Uxos_memInstName_Type()
)
uxos_memInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_memInstName.setStatus("mandatory")


class _Uxos_memSubAddr_Type(DisplayString):
    """Custom type uxos_memSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_memSubAddr_Type.__name__ = "DisplayString"
_Uxos_memSubAddr_Object = MibScalar
uxos_memSubAddr = _Uxos_memSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 4, 1, 1, 3),
    _Uxos_memSubAddr_Type()
)
uxos_memSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_memSubAddr.setStatus("mandatory")
_Uxos_memSize_Type = Counter32
_Uxos_memSize_Object = MibScalar
uxos_memSize = _Uxos_memSize_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 4, 1, 1, 4),
    _Uxos_memSize_Type()
)
uxos_memSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_memSize.setStatus("mandatory")
_Uxos_filecnt_ObjectIdentity = ObjectIdentity
uxos_filecnt = _Uxos_filecnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 5)
)
_Uxos_fileTable_Object = MibTable
uxos_fileTable = _Uxos_fileTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 5, 1)
)
if mibBuilder.loadTexts:
    uxos_fileTable.setStatus("mandatory")
_Uxos_fileEntry_Object = MibTableRow
uxos_fileEntry = _Uxos_fileEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 5, 1, 1)
)
uxos_fileEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-fileSysName"),
    (0, "OLIVETTI-MIB", "uxos-fileInstName"),
    (0, "OLIVETTI-MIB", "uxos-fileSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_fileEntry.setStatus("mandatory")


class _Uxos_fileSysName_Type(DisplayString):
    """Custom type uxos_fileSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_fileSysName_Type.__name__ = "DisplayString"
_Uxos_fileSysName_Object = MibScalar
uxos_fileSysName = _Uxos_fileSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 5, 1, 1, 1),
    _Uxos_fileSysName_Type()
)
uxos_fileSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_fileSysName.setStatus("mandatory")


class _Uxos_fileInstName_Type(DisplayString):
    """Custom type uxos_fileInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_fileInstName_Type.__name__ = "DisplayString"
_Uxos_fileInstName_Object = MibScalar
uxos_fileInstName = _Uxos_fileInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 5, 1, 1, 2),
    _Uxos_fileInstName_Type()
)
uxos_fileInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_fileInstName.setStatus("mandatory")


class _Uxos_fileSubAddr_Type(DisplayString):
    """Custom type uxos_fileSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_fileSubAddr_Type.__name__ = "DisplayString"
_Uxos_fileSubAddr_Object = MibScalar
uxos_fileSubAddr = _Uxos_fileSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 5, 1, 1, 3),
    _Uxos_fileSubAddr_Type()
)
uxos_fileSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_fileSubAddr.setStatus("mandatory")
_Uxos_numOfFile_Type = Counter32
_Uxos_numOfFile_Object = MibScalar
uxos_numOfFile = _Uxos_numOfFile_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 5, 1, 1, 4),
    _Uxos_numOfFile_Type()
)
uxos_numOfFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numOfFile.setStatus("mandatory")
_Uxos_boottime_ObjectIdentity = ObjectIdentity
uxos_boottime = _Uxos_boottime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 6)
)
_Uxos_bootTable_Object = MibTable
uxos_bootTable = _Uxos_bootTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 6, 1)
)
if mibBuilder.loadTexts:
    uxos_bootTable.setStatus("mandatory")
_Uxos_bootEntry_Object = MibTableRow
uxos_bootEntry = _Uxos_bootEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 6, 1, 1)
)
uxos_bootEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-bootSysName"),
    (0, "OLIVETTI-MIB", "uxos-bootInstName"),
    (0, "OLIVETTI-MIB", "uxos-bootSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_bootEntry.setStatus("mandatory")


class _Uxos_bootSysName_Type(DisplayString):
    """Custom type uxos_bootSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_bootSysName_Type.__name__ = "DisplayString"
_Uxos_bootSysName_Object = MibScalar
uxos_bootSysName = _Uxos_bootSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 6, 1, 1, 1),
    _Uxos_bootSysName_Type()
)
uxos_bootSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_bootSysName.setStatus("mandatory")


class _Uxos_bootInstName_Type(DisplayString):
    """Custom type uxos_bootInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_bootInstName_Type.__name__ = "DisplayString"
_Uxos_bootInstName_Object = MibScalar
uxos_bootInstName = _Uxos_bootInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 6, 1, 1, 2),
    _Uxos_bootInstName_Type()
)
uxos_bootInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_bootInstName.setStatus("mandatory")


class _Uxos_bootSubAddr_Type(DisplayString):
    """Custom type uxos_bootSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_bootSubAddr_Type.__name__ = "DisplayString"
_Uxos_bootSubAddr_Object = MibScalar
uxos_bootSubAddr = _Uxos_bootSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 6, 1, 1, 3),
    _Uxos_bootSubAddr_Type()
)
uxos_bootSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_bootSubAddr.setStatus("mandatory")
_Uxos_bootTime_Type = Counter32
_Uxos_bootTime_Object = MibScalar
uxos_bootTime = _Uxos_bootTime_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 6, 1, 1, 4),
    _Uxos_bootTime_Type()
)
uxos_bootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_bootTime.setStatus("mandatory")
_Uxos_sysinfo_ObjectIdentity = ObjectIdentity
uxos_sysinfo = _Uxos_sysinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7)
)
_Uxos_sysTable_Object = MibTable
uxos_sysTable = _Uxos_sysTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1)
)
if mibBuilder.loadTexts:
    uxos_sysTable.setStatus("mandatory")
_Uxos_sysEntry_Object = MibTableRow
uxos_sysEntry = _Uxos_sysEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1)
)
uxos_sysEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-sysSysName"),
    (0, "OLIVETTI-MIB", "uxos-sysInstName"),
    (0, "OLIVETTI-MIB", "uxos-sysSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_sysEntry.setStatus("mandatory")


class _Uxos_sysSysName_Type(DisplayString):
    """Custom type uxos_sysSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_sysSysName_Type.__name__ = "DisplayString"
_Uxos_sysSysName_Object = MibScalar
uxos_sysSysName = _Uxos_sysSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 1),
    _Uxos_sysSysName_Type()
)
uxos_sysSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sysSysName.setStatus("mandatory")


class _Uxos_sysInstName_Type(DisplayString):
    """Custom type uxos_sysInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_sysInstName_Type.__name__ = "DisplayString"
_Uxos_sysInstName_Object = MibScalar
uxos_sysInstName = _Uxos_sysInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 2),
    _Uxos_sysInstName_Type()
)
uxos_sysInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sysInstName.setStatus("mandatory")


class _Uxos_sysSubAddr_Type(DisplayString):
    """Custom type uxos_sysSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_sysSubAddr_Type.__name__ = "DisplayString"
_Uxos_sysSubAddr_Object = MibScalar
uxos_sysSubAddr = _Uxos_sysSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 3),
    _Uxos_sysSubAddr_Type()
)
uxos_sysSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sysSubAddr.setStatus("mandatory")
_Uxos_cpuIdle_Type = Counter32
_Uxos_cpuIdle_Object = MibScalar
uxos_cpuIdle = _Uxos_cpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 4),
    _Uxos_cpuIdle_Type()
)
uxos_cpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuIdle.setStatus("mandatory")
_Uxos_cpuUser_Type = Counter32
_Uxos_cpuUser_Object = MibScalar
uxos_cpuUser = _Uxos_cpuUser_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 5),
    _Uxos_cpuUser_Type()
)
uxos_cpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuUser.setStatus("mandatory")
_Uxos_cpuKernel_Type = Counter32
_Uxos_cpuKernel_Object = MibScalar
uxos_cpuKernel = _Uxos_cpuKernel_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 6),
    _Uxos_cpuKernel_Type()
)
uxos_cpuKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuKernel.setStatus("mandatory")
_Uxos_cpuWait_Type = Counter32
_Uxos_cpuWait_Object = MibScalar
uxos_cpuWait = _Uxos_cpuWait_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 7),
    _Uxos_cpuWait_Type()
)
uxos_cpuWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuWait.setStatus("mandatory")
_Uxos_cpuSxbrk_Type = Counter32
_Uxos_cpuSxbrk_Object = MibScalar
uxos_cpuSxbrk = _Uxos_cpuSxbrk_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 8),
    _Uxos_cpuSxbrk_Type()
)
uxos_cpuSxbrk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cpuSxbrk.setStatus("mandatory")
_Uxos_wIo_Type = Counter32
_Uxos_wIo_Object = MibScalar
uxos_wIo = _Uxos_wIo_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 9),
    _Uxos_wIo_Type()
)
uxos_wIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_wIo.setStatus("mandatory")
_Uxos_wSwap_Type = Counter32
_Uxos_wSwap_Object = MibScalar
uxos_wSwap = _Uxos_wSwap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 10),
    _Uxos_wSwap_Type()
)
uxos_wSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_wSwap.setStatus("mandatory")
_Uxos_wPio_Type = Counter32
_Uxos_wPio_Object = MibScalar
uxos_wPio = _Uxos_wPio_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 11),
    _Uxos_wPio_Type()
)
uxos_wPio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_wPio.setStatus("mandatory")
_Uxos_bread_Type = Counter32
_Uxos_bread_Object = MibScalar
uxos_bread = _Uxos_bread_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 12),
    _Uxos_bread_Type()
)
uxos_bread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_bread.setStatus("mandatory")
_Uxos_bwrite_Type = Counter32
_Uxos_bwrite_Object = MibScalar
uxos_bwrite = _Uxos_bwrite_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 13),
    _Uxos_bwrite_Type()
)
uxos_bwrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_bwrite.setStatus("mandatory")
_Uxos_lread_Type = Counter32
_Uxos_lread_Object = MibScalar
uxos_lread = _Uxos_lread_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 14),
    _Uxos_lread_Type()
)
uxos_lread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lread.setStatus("mandatory")
_Uxos_lwrite_Type = Counter32
_Uxos_lwrite_Object = MibScalar
uxos_lwrite = _Uxos_lwrite_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 15),
    _Uxos_lwrite_Type()
)
uxos_lwrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lwrite.setStatus("mandatory")
_Uxos_phread_Type = Counter32
_Uxos_phread_Object = MibScalar
uxos_phread = _Uxos_phread_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 16),
    _Uxos_phread_Type()
)
uxos_phread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_phread.setStatus("mandatory")
_Uxos_phwrite_Type = Counter32
_Uxos_phwrite_Object = MibScalar
uxos_phwrite = _Uxos_phwrite_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 17),
    _Uxos_phwrite_Type()
)
uxos_phwrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_phwrite.setStatus("mandatory")
_Uxos_swapin_Type = Counter32
_Uxos_swapin_Object = MibScalar
uxos_swapin = _Uxos_swapin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 18),
    _Uxos_swapin_Type()
)
uxos_swapin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_swapin.setStatus("mandatory")
_Uxos_swapout_Type = Counter32
_Uxos_swapout_Object = MibScalar
uxos_swapout = _Uxos_swapout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 19),
    _Uxos_swapout_Type()
)
uxos_swapout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_swapout.setStatus("mandatory")
_Uxos_pswapin_Type = Counter32
_Uxos_pswapin_Object = MibScalar
uxos_pswapin = _Uxos_pswapin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 20),
    _Uxos_pswapin_Type()
)
uxos_pswapin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pswapin.setStatus("mandatory")
_Uxos_pswapout_Type = Counter32
_Uxos_pswapout_Object = MibScalar
uxos_pswapout = _Uxos_pswapout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 21),
    _Uxos_pswapout_Type()
)
uxos_pswapout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pswapout.setStatus("mandatory")
_Uxos_pswitch_Type = Counter32
_Uxos_pswitch_Object = MibScalar
uxos_pswitch = _Uxos_pswitch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 22),
    _Uxos_pswitch_Type()
)
uxos_pswitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pswitch.setStatus("mandatory")
_Uxos_syscall_Type = Counter32
_Uxos_syscall_Object = MibScalar
uxos_syscall = _Uxos_syscall_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 23),
    _Uxos_syscall_Type()
)
uxos_syscall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_syscall.setStatus("mandatory")
_Uxos_sysread_Type = Counter32
_Uxos_sysread_Object = MibScalar
uxos_sysread = _Uxos_sysread_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 24),
    _Uxos_sysread_Type()
)
uxos_sysread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sysread.setStatus("mandatory")
_Uxos_syswrite_Type = Counter32
_Uxos_syswrite_Object = MibScalar
uxos_syswrite = _Uxos_syswrite_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 25),
    _Uxos_syswrite_Type()
)
uxos_syswrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_syswrite.setStatus("mandatory")
_Uxos_sysfork_Type = Counter32
_Uxos_sysfork_Object = MibScalar
uxos_sysfork = _Uxos_sysfork_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 26),
    _Uxos_sysfork_Type()
)
uxos_sysfork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sysfork.setStatus("mandatory")
_Uxos_sysexec_Type = Counter32
_Uxos_sysexec_Object = MibScalar
uxos_sysexec = _Uxos_sysexec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 27),
    _Uxos_sysexec_Type()
)
uxos_sysexec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sysexec.setStatus("mandatory")
_Uxos_runque_Type = Counter32
_Uxos_runque_Object = MibScalar
uxos_runque = _Uxos_runque_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 28),
    _Uxos_runque_Type()
)
uxos_runque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_runque.setStatus("mandatory")
_Uxos_runocc_Type = Counter32
_Uxos_runocc_Object = MibScalar
uxos_runocc = _Uxos_runocc_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 29),
    _Uxos_runocc_Type()
)
uxos_runocc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_runocc.setStatus("mandatory")
_Uxos_swpque_Type = Counter32
_Uxos_swpque_Object = MibScalar
uxos_swpque = _Uxos_swpque_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 30),
    _Uxos_swpque_Type()
)
uxos_swpque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_swpque.setStatus("mandatory")
_Uxos_swpocc_Type = Counter32
_Uxos_swpocc_Object = MibScalar
uxos_swpocc = _Uxos_swpocc_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 31),
    _Uxos_swpocc_Type()
)
uxos_swpocc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_swpocc.setStatus("mandatory")
_Uxos_iget_Type = Counter32
_Uxos_iget_Object = MibScalar
uxos_iget = _Uxos_iget_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 32),
    _Uxos_iget_Type()
)
uxos_iget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_iget.setStatus("mandatory")
_Uxos_namei_Type = Counter32
_Uxos_namei_Object = MibScalar
uxos_namei = _Uxos_namei_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 33),
    _Uxos_namei_Type()
)
uxos_namei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_namei.setStatus("mandatory")
_Uxos_dirblk_Type = Counter32
_Uxos_dirblk_Object = MibScalar
uxos_dirblk = _Uxos_dirblk_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 34),
    _Uxos_dirblk_Type()
)
uxos_dirblk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_dirblk.setStatus("mandatory")
_Uxos_readch_Type = Counter32
_Uxos_readch_Object = MibScalar
uxos_readch = _Uxos_readch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 35),
    _Uxos_readch_Type()
)
uxos_readch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_readch.setStatus("mandatory")
_Uxos_writech_Type = Counter32
_Uxos_writech_Object = MibScalar
uxos_writech = _Uxos_writech_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 36),
    _Uxos_writech_Type()
)
uxos_writech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_writech.setStatus("mandatory")
_Uxos_rcvint_Type = Counter32
_Uxos_rcvint_Object = MibScalar
uxos_rcvint = _Uxos_rcvint_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 37),
    _Uxos_rcvint_Type()
)
uxos_rcvint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rcvint.setStatus("mandatory")
_Uxos_xmtint_Type = Counter32
_Uxos_xmtint_Object = MibScalar
uxos_xmtint = _Uxos_xmtint_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 38),
    _Uxos_xmtint_Type()
)
uxos_xmtint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_xmtint.setStatus("mandatory")
_Uxos_mdmint_Type = Counter32
_Uxos_mdmint_Object = MibScalar
uxos_mdmint = _Uxos_mdmint_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 39),
    _Uxos_mdmint_Type()
)
uxos_mdmint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_mdmint.setStatus("mandatory")
_Uxos_rawch_Type = Counter32
_Uxos_rawch_Object = MibScalar
uxos_rawch = _Uxos_rawch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 40),
    _Uxos_rawch_Type()
)
uxos_rawch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rawch.setStatus("mandatory")
_Uxos_canch_Type = Counter32
_Uxos_canch_Object = MibScalar
uxos_canch = _Uxos_canch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 41),
    _Uxos_canch_Type()
)
uxos_canch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_canch.setStatus("mandatory")
_Uxos_outch_Type = Counter32
_Uxos_outch_Object = MibScalar
uxos_outch = _Uxos_outch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 42),
    _Uxos_outch_Type()
)
uxos_outch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_outch.setStatus("mandatory")
_Uxos_msg_Type = Counter32
_Uxos_msg_Object = MibScalar
uxos_msg = _Uxos_msg_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 43),
    _Uxos_msg_Type()
)
uxos_msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg.setStatus("mandatory")
_Uxos_sema_Type = Counter32
_Uxos_sema_Object = MibScalar
uxos_sema = _Uxos_sema_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 7, 1, 1, 44),
    _Uxos_sema_Type()
)
uxos_sema.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sema.setStatus("mandatory")
_Uxos_minfo_ObjectIdentity = ObjectIdentity
uxos_minfo = _Uxos_minfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8)
)
_Uxos_minfoTable_Object = MibTable
uxos_minfoTable = _Uxos_minfoTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1)
)
if mibBuilder.loadTexts:
    uxos_minfoTable.setStatus("mandatory")
_Uxos_minfoEntry_Object = MibTableRow
uxos_minfoEntry = _Uxos_minfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1)
)
uxos_minfoEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-minfoSysName"),
    (0, "OLIVETTI-MIB", "uxos-minfoInstName"),
    (0, "OLIVETTI-MIB", "uxos-minfoSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_minfoEntry.setStatus("mandatory")


class _Uxos_minfoSysName_Type(DisplayString):
    """Custom type uxos_minfoSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_minfoSysName_Type.__name__ = "DisplayString"
_Uxos_minfoSysName_Object = MibScalar
uxos_minfoSysName = _Uxos_minfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 1),
    _Uxos_minfoSysName_Type()
)
uxos_minfoSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_minfoSysName.setStatus("mandatory")


class _Uxos_minfoInstName_Type(DisplayString):
    """Custom type uxos_minfoInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_minfoInstName_Type.__name__ = "DisplayString"
_Uxos_minfoInstName_Object = MibScalar
uxos_minfoInstName = _Uxos_minfoInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 2),
    _Uxos_minfoInstName_Type()
)
uxos_minfoInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_minfoInstName.setStatus("mandatory")


class _Uxos_minfoSubAddr_Type(DisplayString):
    """Custom type uxos_minfoSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_minfoSubAddr_Type.__name__ = "DisplayString"
_Uxos_minfoSubAddr_Object = MibScalar
uxos_minfoSubAddr = _Uxos_minfoSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 3),
    _Uxos_minfoSubAddr_Type()
)
uxos_minfoSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_minfoSubAddr.setStatus("mandatory")
_Uxos_freememLeast_Type = Counter32
_Uxos_freememLeast_Object = MibScalar
uxos_freememLeast = _Uxos_freememLeast_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 4),
    _Uxos_freememLeast_Type()
)
uxos_freememLeast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_freememLeast.setStatus("mandatory")
_Uxos_freememMost_Type = Counter32
_Uxos_freememMost_Object = MibScalar
uxos_freememMost = _Uxos_freememMost_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 5),
    _Uxos_freememMost_Type()
)
uxos_freememMost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_freememMost.setStatus("mandatory")
_Uxos_freeswap_Type = Counter32
_Uxos_freeswap_Object = MibScalar
uxos_freeswap = _Uxos_freeswap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 6),
    _Uxos_freeswap_Type()
)
uxos_freeswap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_freeswap.setStatus("mandatory")
_Uxos_sumvfault_Type = Counter32
_Uxos_sumvfault_Object = MibScalar
uxos_sumvfault = _Uxos_sumvfault_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 7),
    _Uxos_sumvfault_Type()
)
uxos_sumvfault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvfault.setStatus("mandatory")
_Uxos_demand_Type = Counter32
_Uxos_demand_Object = MibScalar
uxos_demand = _Uxos_demand_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 8),
    _Uxos_demand_Type()
)
uxos_demand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_demand.setStatus("mandatory")
_Uxos_swap_Type = Counter32
_Uxos_swap_Object = MibScalar
uxos_swap = _Uxos_swap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 9),
    _Uxos_swap_Type()
)
uxos_swap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_swap.setStatus("mandatory")
_Uxos_cache_Type = Counter32
_Uxos_cache_Object = MibScalar
uxos_cache = _Uxos_cache_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 10),
    _Uxos_cache_Type()
)
uxos_cache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cache.setStatus("mandatory")
_Uxos_file_Type = Counter32
_Uxos_file_Object = MibScalar
uxos_file = _Uxos_file_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 11),
    _Uxos_file_Type()
)
uxos_file.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_file.setStatus("mandatory")
_Uxos_pfault_Type = Counter32
_Uxos_pfault_Object = MibScalar
uxos_pfault = _Uxos_pfault_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 12),
    _Uxos_pfault_Type()
)
uxos_pfault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pfault.setStatus("mandatory")
_Uxos_cw_Type = Counter32
_Uxos_cw_Object = MibScalar
uxos_cw = _Uxos_cw_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 13),
    _Uxos_cw_Type()
)
uxos_cw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cw.setStatus("mandatory")
_Uxos_steal_Type = Counter32
_Uxos_steal_Object = MibScalar
uxos_steal = _Uxos_steal_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 14),
    _Uxos_steal_Type()
)
uxos_steal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_steal.setStatus("mandatory")
_Uxos_freedpgs_Type = Counter32
_Uxos_freedpgs_Object = MibScalar
uxos_freedpgs = _Uxos_freedpgs_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 15),
    _Uxos_freedpgs_Type()
)
uxos_freedpgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_freedpgs.setStatus("mandatory")
_Uxos_vfpg_Type = Counter32
_Uxos_vfpg_Object = MibScalar
uxos_vfpg = _Uxos_vfpg_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 16),
    _Uxos_vfpg_Type()
)
uxos_vfpg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_vfpg.setStatus("mandatory")
_Uxos_sfpg_Type = Counter32
_Uxos_sfpg_Object = MibScalar
uxos_sfpg = _Uxos_sfpg_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 17),
    _Uxos_sfpg_Type()
)
uxos_sfpg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sfpg.setStatus("mandatory")
_Uxos_vspg_Type = Counter32
_Uxos_vspg_Object = MibScalar
uxos_vspg = _Uxos_vspg_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 18),
    _Uxos_vspg_Type()
)
uxos_vspg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_vspg.setStatus("mandatory")
_Uxos_sspg_Type = Counter32
_Uxos_sspg_Object = MibScalar
uxos_sspg = _Uxos_sspg_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 19),
    _Uxos_sspg_Type()
)
uxos_sspg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sspg.setStatus("mandatory")
_Uxos_unmodsw_Type = Counter32
_Uxos_unmodsw_Object = MibScalar
uxos_unmodsw = _Uxos_unmodsw_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 20),
    _Uxos_unmodsw_Type()
)
uxos_unmodsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_unmodsw.setStatus("mandatory")
_Uxos_unmodfl_Type = Counter32
_Uxos_unmodfl_Object = MibScalar
uxos_unmodfl = _Uxos_unmodfl_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 21),
    _Uxos_unmodfl_Type()
)
uxos_unmodfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_unmodfl.setStatus("mandatory")
_Uxos_psoutok_Type = Counter32
_Uxos_psoutok_Object = MibScalar
uxos_psoutok = _Uxos_psoutok_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 22),
    _Uxos_psoutok_Type()
)
uxos_psoutok.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_psoutok.setStatus("mandatory")
_Uxos_psinfail_Type = Counter32
_Uxos_psinfail_Object = MibScalar
uxos_psinfail = _Uxos_psinfail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 23),
    _Uxos_psinfail_Type()
)
uxos_psinfail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_psinfail.setStatus("mandatory")
_Uxos_psinok_Type = Counter32
_Uxos_psinok_Object = MibScalar
uxos_psinok = _Uxos_psinok_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 24),
    _Uxos_psinok_Type()
)
uxos_psinok.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_psinok.setStatus("mandatory")
_Uxos_rsout_Type = Counter32
_Uxos_rsout_Object = MibScalar
uxos_rsout = _Uxos_rsout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 25),
    _Uxos_rsout_Type()
)
uxos_rsout.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_rsout.setStatus("mandatory")
_Uxos_rsin_Type = Counter32
_Uxos_rsin_Object = MibScalar
uxos_rsin = _Uxos_rsin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 26),
    _Uxos_rsin_Type()
)
uxos_rsin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_rsin.setStatus("mandatory")
_Uxos_shmem_Type = Counter32
_Uxos_shmem_Object = MibScalar
uxos_shmem = _Uxos_shmem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 8, 1, 1, 27),
    _Uxos_shmem_Type()
)
uxos_shmem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_shmem.setStatus("mandatory")
_Uxos_vminfo_ObjectIdentity = ObjectIdentity
uxos_vminfo = _Uxos_vminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9)
)
_Uxos_vminfoTable_Object = MibTable
uxos_vminfoTable = _Uxos_vminfoTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1)
)
if mibBuilder.loadTexts:
    uxos_vminfoTable.setStatus("mandatory")
_Uxos_vminfoEntry_Object = MibTableRow
uxos_vminfoEntry = _Uxos_vminfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1)
)
uxos_vminfoEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-vminfoSysName"),
    (0, "OLIVETTI-MIB", "uxos-vminfoInstName"),
    (0, "OLIVETTI-MIB", "uxos-vminfoSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_vminfoEntry.setStatus("mandatory")


class _Uxos_vminfoSysName_Type(DisplayString):
    """Custom type uxos_vminfoSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vminfoSysName_Type.__name__ = "DisplayString"
_Uxos_vminfoSysName_Object = MibScalar
uxos_vminfoSysName = _Uxos_vminfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 1),
    _Uxos_vminfoSysName_Type()
)
uxos_vminfoSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vminfoSysName.setStatus("mandatory")


class _Uxos_vminfoInstName_Type(DisplayString):
    """Custom type uxos_vminfoInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vminfoInstName_Type.__name__ = "DisplayString"
_Uxos_vminfoInstName_Object = MibScalar
uxos_vminfoInstName = _Uxos_vminfoInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 2),
    _Uxos_vminfoInstName_Type()
)
uxos_vminfoInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vminfoInstName.setStatus("mandatory")


class _Uxos_vminfoSubAddr_Type(DisplayString):
    """Custom type uxos_vminfoSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vminfoSubAddr_Type.__name__ = "DisplayString"
_Uxos_vminfoSubAddr_Object = MibScalar
uxos_vminfoSubAddr = _Uxos_vminfoSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 3),
    _Uxos_vminfoSubAddr_Type()
)
uxos_vminfoSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vminfoSubAddr.setStatus("mandatory")
_Uxos_vPgrec_Type = Counter32
_Uxos_vPgrec_Object = MibScalar
uxos_vPgrec = _Uxos_vPgrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 4),
    _Uxos_vPgrec_Type()
)
uxos_vPgrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPgrec.setStatus("mandatory")
_Uxos_vXsfrec_Type = Counter32
_Uxos_vXsfrec_Object = MibScalar
uxos_vXsfrec = _Uxos_vXsfrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 5),
    _Uxos_vXsfrec_Type()
)
uxos_vXsfrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vXsfrec.setStatus("mandatory")
_Uxos_vXifrec_Type = Counter32
_Uxos_vXifrec_Object = MibScalar
uxos_vXifrec = _Uxos_vXifrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 6),
    _Uxos_vXifrec_Type()
)
uxos_vXifrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vXifrec.setStatus("mandatory")
_Uxos_vPgin_Type = Counter32
_Uxos_vPgin_Object = MibScalar
uxos_vPgin = _Uxos_vPgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 7),
    _Uxos_vPgin_Type()
)
uxos_vPgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPgin.setStatus("mandatory")
_Uxos_vPgpgin_Type = Counter32
_Uxos_vPgpgin_Object = MibScalar
uxos_vPgpgin = _Uxos_vPgpgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 8),
    _Uxos_vPgpgin_Type()
)
uxos_vPgpgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPgpgin.setStatus("mandatory")
_Uxos_vPgout_Type = Counter32
_Uxos_vPgout_Object = MibScalar
uxos_vPgout = _Uxos_vPgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 9),
    _Uxos_vPgout_Type()
)
uxos_vPgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPgout.setStatus("mandatory")
_Uxos_vPgpgout_Type = Counter32
_Uxos_vPgpgout_Object = MibScalar
uxos_vPgpgout = _Uxos_vPgpgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 10),
    _Uxos_vPgpgout_Type()
)
uxos_vPgpgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPgpgout.setStatus("mandatory")
_Uxos_vSwpout_Type = Counter32
_Uxos_vSwpout_Object = MibScalar
uxos_vSwpout = _Uxos_vSwpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 11),
    _Uxos_vSwpout_Type()
)
uxos_vSwpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vSwpout.setStatus("mandatory")
_Uxos_vPswpout_Type = Counter32
_Uxos_vPswpout_Object = MibScalar
uxos_vPswpout = _Uxos_vPswpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 12),
    _Uxos_vPswpout_Type()
)
uxos_vPswpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPswpout.setStatus("mandatory")
_Uxos_vSwpin_Type = Counter32
_Uxos_vSwpin_Object = MibScalar
uxos_vSwpin = _Uxos_vSwpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 13),
    _Uxos_vSwpin_Type()
)
uxos_vSwpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vSwpin.setStatus("mandatory")
_Uxos_vPswpin_Type = Counter32
_Uxos_vPswpin_Object = MibScalar
uxos_vPswpin = _Uxos_vPswpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 14),
    _Uxos_vPswpin_Type()
)
uxos_vPswpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPswpin.setStatus("mandatory")
_Uxos_vDfree_Type = Counter32
_Uxos_vDfree_Object = MibScalar
uxos_vDfree = _Uxos_vDfree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 15),
    _Uxos_vDfree_Type()
)
uxos_vDfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vDfree.setStatus("mandatory")
_Uxos_vScan_Type = Counter32
_Uxos_vScan_Object = MibScalar
uxos_vScan = _Uxos_vScan_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 16),
    _Uxos_vScan_Type()
)
uxos_vScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vScan.setStatus("mandatory")
_Uxos_vPfault_Type = Counter32
_Uxos_vPfault_Object = MibScalar
uxos_vPfault = _Uxos_vPfault_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 17),
    _Uxos_vPfault_Type()
)
uxos_vPfault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPfault.setStatus("mandatory")
_Uxos_vVfault_Type = Counter32
_Uxos_vVfault_Object = MibScalar
uxos_vVfault = _Uxos_vVfault_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 18),
    _Uxos_vVfault_Type()
)
uxos_vVfault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vVfault.setStatus("mandatory")
_Uxos_vSftlock_Type = Counter32
_Uxos_vSftlock_Object = MibScalar
uxos_vSftlock = _Uxos_vSftlock_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 9, 1, 1, 19),
    _Uxos_vSftlock_Type()
)
uxos_vSftlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vSftlock.setStatus("mandatory")
_Uxos_syserr_ObjectIdentity = ObjectIdentity
uxos_syserr = _Uxos_syserr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10)
)
_Uxos_syserrTable_Object = MibTable
uxos_syserrTable = _Uxos_syserrTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1)
)
if mibBuilder.loadTexts:
    uxos_syserrTable.setStatus("mandatory")
_Uxos_syserrEntry_Object = MibTableRow
uxos_syserrEntry = _Uxos_syserrEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1)
)
uxos_syserrEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-syserrSysName"),
    (0, "OLIVETTI-MIB", "uxos-syserrInstName"),
    (0, "OLIVETTI-MIB", "uxos-syserrSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_syserrEntry.setStatus("mandatory")


class _Uxos_syserrSysName_Type(DisplayString):
    """Custom type uxos_syserrSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_syserrSysName_Type.__name__ = "DisplayString"
_Uxos_syserrSysName_Object = MibScalar
uxos_syserrSysName = _Uxos_syserrSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 1),
    _Uxos_syserrSysName_Type()
)
uxos_syserrSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_syserrSysName.setStatus("mandatory")


class _Uxos_syserrInstName_Type(DisplayString):
    """Custom type uxos_syserrInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_syserrInstName_Type.__name__ = "DisplayString"
_Uxos_syserrInstName_Object = MibScalar
uxos_syserrInstName = _Uxos_syserrInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 2),
    _Uxos_syserrInstName_Type()
)
uxos_syserrInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_syserrInstName.setStatus("mandatory")


class _Uxos_syserrSubAddr_Type(DisplayString):
    """Custom type uxos_syserrSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_syserrSubAddr_Type.__name__ = "DisplayString"
_Uxos_syserrSubAddr_Object = MibScalar
uxos_syserrSubAddr = _Uxos_syserrSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 3),
    _Uxos_syserrSubAddr_Type()
)
uxos_syserrSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_syserrSubAddr.setStatus("mandatory")
_Uxos_inodeovf_Type = Counter32
_Uxos_inodeovf_Object = MibScalar
uxos_inodeovf = _Uxos_inodeovf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 4),
    _Uxos_inodeovf_Type()
)
uxos_inodeovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_inodeovf.setStatus("mandatory")
_Uxos_ufsinodeovf_Type = Counter32
_Uxos_ufsinodeovf_Object = MibScalar
uxos_ufsinodeovf = _Uxos_ufsinodeovf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 5),
    _Uxos_ufsinodeovf_Type()
)
uxos_ufsinodeovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ufsinodeovf.setStatus("mandatory")
_Uxos_fileovf_Type = Counter32
_Uxos_fileovf_Object = MibScalar
uxos_fileovf = _Uxos_fileovf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 6),
    _Uxos_fileovf_Type()
)
uxos_fileovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_fileovf.setStatus("mandatory")
_Uxos_textovf_Type = Counter32
_Uxos_textovf_Object = MibScalar
uxos_textovf = _Uxos_textovf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 7),
    _Uxos_textovf_Type()
)
uxos_textovf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_textovf.setStatus("mandatory")
_Uxos_procovf_Type = Counter32
_Uxos_procovf_Object = MibScalar
uxos_procovf = _Uxos_procovf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 10, 1, 1, 8),
    _Uxos_procovf_Type()
)
uxos_procovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_procovf.setStatus("mandatory")
_Uxos_kmeminfo_ObjectIdentity = ObjectIdentity
uxos_kmeminfo = _Uxos_kmeminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11)
)
_Uxos_kmeminfoTable_Object = MibTable
uxos_kmeminfoTable = _Uxos_kmeminfoTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1)
)
if mibBuilder.loadTexts:
    uxos_kmeminfoTable.setStatus("mandatory")
_Uxos_kmeminfoEntry_Object = MibTableRow
uxos_kmeminfoEntry = _Uxos_kmeminfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1)
)
uxos_kmeminfoEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-kmeminfoSysName"),
    (0, "OLIVETTI-MIB", "uxos-kmeminfoInstName"),
    (0, "OLIVETTI-MIB", "uxos-kmeminfoSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_kmeminfoEntry.setStatus("mandatory")


class _Uxos_kmeminfoSysName_Type(DisplayString):
    """Custom type uxos_kmeminfoSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_kmeminfoSysName_Type.__name__ = "DisplayString"
_Uxos_kmeminfoSysName_Object = MibScalar
uxos_kmeminfoSysName = _Uxos_kmeminfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 1),
    _Uxos_kmeminfoSysName_Type()
)
uxos_kmeminfoSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_kmeminfoSysName.setStatus("mandatory")


class _Uxos_kmeminfoInstName_Type(DisplayString):
    """Custom type uxos_kmeminfoInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_kmeminfoInstName_Type.__name__ = "DisplayString"
_Uxos_kmeminfoInstName_Object = MibScalar
uxos_kmeminfoInstName = _Uxos_kmeminfoInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 2),
    _Uxos_kmeminfoInstName_Type()
)
uxos_kmeminfoInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_kmeminfoInstName.setStatus("mandatory")


class _Uxos_kmeminfoSubAddr_Type(DisplayString):
    """Custom type uxos_kmeminfoSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_kmeminfoSubAddr_Type.__name__ = "DisplayString"
_Uxos_kmeminfoSubAddr_Object = MibScalar
uxos_kmeminfoSubAddr = _Uxos_kmeminfoSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 3),
    _Uxos_kmeminfoSubAddr_Type()
)
uxos_kmeminfoSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_kmeminfoSubAddr.setStatus("mandatory")
_Uxos_smlMem_Type = Counter32
_Uxos_smlMem_Object = MibScalar
uxos_smlMem = _Uxos_smlMem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 4),
    _Uxos_smlMem_Type()
)
uxos_smlMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smlMem.setStatus("mandatory")
_Uxos_smlAlloc_Type = Counter32
_Uxos_smlAlloc_Object = MibScalar
uxos_smlAlloc = _Uxos_smlAlloc_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 5),
    _Uxos_smlAlloc_Type()
)
uxos_smlAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smlAlloc.setStatus("mandatory")
_Uxos_smlFail_Type = Counter32
_Uxos_smlFail_Object = MibScalar
uxos_smlFail = _Uxos_smlFail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 6),
    _Uxos_smlFail_Type()
)
uxos_smlFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smlFail.setStatus("mandatory")
_Uxos_lgMem_Type = Counter32
_Uxos_lgMem_Object = MibScalar
uxos_lgMem = _Uxos_lgMem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 7),
    _Uxos_lgMem_Type()
)
uxos_lgMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lgMem.setStatus("mandatory")
_Uxos_lgAlloc_Type = Counter32
_Uxos_lgAlloc_Object = MibScalar
uxos_lgAlloc = _Uxos_lgAlloc_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 8),
    _Uxos_lgAlloc_Type()
)
uxos_lgAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lgAlloc.setStatus("mandatory")
_Uxos_lgFail_Type = Counter32
_Uxos_lgFail_Object = MibScalar
uxos_lgFail = _Uxos_lgFail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 9),
    _Uxos_lgFail_Type()
)
uxos_lgFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lgFail.setStatus("mandatory")
_Uxos_ovszMem_Type = Counter32
_Uxos_ovszMem_Object = MibScalar
uxos_ovszMem = _Uxos_ovszMem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 10),
    _Uxos_ovszMem_Type()
)
uxos_ovszMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ovszMem.setStatus("mandatory")
_Uxos_ovszAlloc_Type = Counter32
_Uxos_ovszAlloc_Object = MibScalar
uxos_ovszAlloc = _Uxos_ovszAlloc_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 11),
    _Uxos_ovszAlloc_Type()
)
uxos_ovszAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ovszAlloc.setStatus("mandatory")
_Uxos_ovszFail_Type = Counter32
_Uxos_ovszFail_Object = MibScalar
uxos_ovszFail = _Uxos_ovszFail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 11, 1, 1, 12),
    _Uxos_ovszFail_Type()
)
uxos_ovszFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ovszFail.setStatus("mandatory")
_Uxos_rtminfo_ObjectIdentity = ObjectIdentity
uxos_rtminfo = _Uxos_rtminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12)
)
_Uxos_rtminfoTable_Object = MibTable
uxos_rtminfoTable = _Uxos_rtminfoTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1)
)
if mibBuilder.loadTexts:
    uxos_rtminfoTable.setStatus("mandatory")
_Uxos_rtminfoEntry_Object = MibTableRow
uxos_rtminfoEntry = _Uxos_rtminfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1, 1)
)
uxos_rtminfoEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-rtminfoSysName"),
    (0, "OLIVETTI-MIB", "uxos-rtminfoInstName"),
    (0, "OLIVETTI-MIB", "uxos-rtminfoSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_rtminfoEntry.setStatus("mandatory")


class _Uxos_rtminfoSysName_Type(DisplayString):
    """Custom type uxos_rtminfoSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_rtminfoSysName_Type.__name__ = "DisplayString"
_Uxos_rtminfoSysName_Object = MibScalar
uxos_rtminfoSysName = _Uxos_rtminfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1, 1, 1),
    _Uxos_rtminfoSysName_Type()
)
uxos_rtminfoSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rtminfoSysName.setStatus("mandatory")


class _Uxos_rtminfoInstName_Type(DisplayString):
    """Custom type uxos_rtminfoInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_rtminfoInstName_Type.__name__ = "DisplayString"
_Uxos_rtminfoInstName_Object = MibScalar
uxos_rtminfoInstName = _Uxos_rtminfoInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1, 1, 2),
    _Uxos_rtminfoInstName_Type()
)
uxos_rtminfoInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rtminfoInstName.setStatus("mandatory")


class _Uxos_rtminfoSubAddr_Type(DisplayString):
    """Custom type uxos_rtminfoSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_rtminfoSubAddr_Type.__name__ = "DisplayString"
_Uxos_rtminfoSubAddr_Object = MibScalar
uxos_rtminfoSubAddr = _Uxos_rtminfoSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1, 1, 3),
    _Uxos_rtminfoSubAddr_Type()
)
uxos_rtminfoSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rtminfoSubAddr.setStatus("mandatory")
_Uxos_evPost_Type = Counter32
_Uxos_evPost_Object = MibScalar
uxos_evPost = _Uxos_evPost_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1, 1, 4),
    _Uxos_evPost_Type()
)
uxos_evPost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_evPost.setStatus("mandatory")
_Uxos_evPoll_Type = Counter32
_Uxos_evPoll_Object = MibScalar
uxos_evPoll = _Uxos_evPoll_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1, 1, 5),
    _Uxos_evPoll_Type()
)
uxos_evPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_evPoll.setStatus("mandatory")
_Uxos_evTrap_Type = Counter32
_Uxos_evTrap_Object = MibScalar
uxos_evTrap = _Uxos_evTrap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 12, 1, 1, 6),
    _Uxos_evTrap_Type()
)
uxos_evTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_evTrap.setStatus("mandatory")
_Uxos_var_ObjectIdentity = ObjectIdentity
uxos_var = _Uxos_var_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13)
)
_Uxos_varTable_Object = MibTable
uxos_varTable = _Uxos_varTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1)
)
if mibBuilder.loadTexts:
    uxos_varTable.setStatus("mandatory")
_Uxos_varEntry_Object = MibTableRow
uxos_varEntry = _Uxos_varEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1)
)
uxos_varEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-varSysName"),
    (0, "OLIVETTI-MIB", "uxos-varInstName"),
    (0, "OLIVETTI-MIB", "uxos-varSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_varEntry.setStatus("mandatory")


class _Uxos_varSysName_Type(DisplayString):
    """Custom type uxos_varSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_varSysName_Type.__name__ = "DisplayString"
_Uxos_varSysName_Object = MibScalar
uxos_varSysName = _Uxos_varSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 1),
    _Uxos_varSysName_Type()
)
uxos_varSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_varSysName.setStatus("mandatory")


class _Uxos_varInstName_Type(DisplayString):
    """Custom type uxos_varInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_varInstName_Type.__name__ = "DisplayString"
_Uxos_varInstName_Object = MibScalar
uxos_varInstName = _Uxos_varInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 2),
    _Uxos_varInstName_Type()
)
uxos_varInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_varInstName.setStatus("mandatory")


class _Uxos_varSubAddr_Type(DisplayString):
    """Custom type uxos_varSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_varSubAddr_Type.__name__ = "DisplayString"
_Uxos_varSubAddr_Object = MibScalar
uxos_varSubAddr = _Uxos_varSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 3),
    _Uxos_varSubAddr_Type()
)
uxos_varSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_varSubAddr.setStatus("mandatory")
_Uxos_vBuf_Type = Counter32
_Uxos_vBuf_Object = MibScalar
uxos_vBuf = _Uxos_vBuf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 4),
    _Uxos_vBuf_Type()
)
uxos_vBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vBuf.setStatus("mandatory")
_Uxos_vCall_Type = Counter32
_Uxos_vCall_Object = MibScalar
uxos_vCall = _Uxos_vCall_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 5),
    _Uxos_vCall_Type()
)
uxos_vCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vCall.setStatus("mandatory")
_Uxos_vProc_Type = Counter32
_Uxos_vProc_Object = MibScalar
uxos_vProc = _Uxos_vProc_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 6),
    _Uxos_vProc_Type()
)
uxos_vProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vProc.setStatus("mandatory")
_Uxos_vFiller_Type = Counter32
_Uxos_vFiller_Object = MibScalar
uxos_vFiller = _Uxos_vFiller_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 7),
    _Uxos_vFiller_Type()
)
uxos_vFiller.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_vFiller.setStatus("mandatory")
_Uxos_vNglobpris_Type = Counter32
_Uxos_vNglobpris_Object = MibScalar
uxos_vNglobpris = _Uxos_vNglobpris_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 8),
    _Uxos_vNglobpris_Type()
)
uxos_vNglobpris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vNglobpris.setStatus("mandatory")
_Uxos_vMaxsyspri_Type = Counter32
_Uxos_vMaxsyspri_Object = MibScalar
uxos_vMaxsyspri = _Uxos_vMaxsyspri_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 9),
    _Uxos_vMaxsyspri_Type()
)
uxos_vMaxsyspri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vMaxsyspri.setStatus("mandatory")
_Uxos_vClist_Type = Counter32
_Uxos_vClist_Object = MibScalar
uxos_vClist = _Uxos_vClist_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 10),
    _Uxos_vClist_Type()
)
uxos_vClist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vClist.setStatus("mandatory")
_Uxos_vMaxup_Type = Counter32
_Uxos_vMaxup_Object = MibScalar
uxos_vMaxup = _Uxos_vMaxup_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 11),
    _Uxos_vMaxup_Type()
)
uxos_vMaxup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vMaxup.setStatus("mandatory")
_Uxos_vHbuf_Type = Counter32
_Uxos_vHbuf_Object = MibScalar
uxos_vHbuf = _Uxos_vHbuf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 12),
    _Uxos_vHbuf_Type()
)
uxos_vHbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vHbuf.setStatus("mandatory")
_Uxos_vHmask_Type = Counter32
_Uxos_vHmask_Object = MibScalar
uxos_vHmask = _Uxos_vHmask_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 13),
    _Uxos_vHmask_Type()
)
uxos_vHmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vHmask.setStatus("mandatory")
_Uxos_vPbuf_Type = Counter32
_Uxos_vPbuf_Object = MibScalar
uxos_vPbuf = _Uxos_vPbuf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 14),
    _Uxos_vPbuf_Type()
)
uxos_vPbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPbuf.setStatus("mandatory")
_Uxos_vSptmap_Type = Counter32
_Uxos_vSptmap_Object = MibScalar
uxos_vSptmap = _Uxos_vSptmap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 15),
    _Uxos_vSptmap_Type()
)
uxos_vSptmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vSptmap.setStatus("mandatory")
_Uxos_vMaxpmem_Type = Counter32
_Uxos_vMaxpmem_Object = MibScalar
uxos_vMaxpmem = _Uxos_vMaxpmem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 16),
    _Uxos_vMaxpmem_Type()
)
uxos_vMaxpmem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vMaxpmem.setStatus("mandatory")
_Uxos_vAutoup_Type = Counter32
_Uxos_vAutoup_Object = MibScalar
uxos_vAutoup = _Uxos_vAutoup_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 17),
    _Uxos_vAutoup_Type()
)
uxos_vAutoup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vAutoup.setStatus("mandatory")
_Uxos_vBufhwm_Type = Counter32
_Uxos_vBufhwm_Object = MibScalar
uxos_vBufhwm = _Uxos_vBufhwm_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 18),
    _Uxos_vBufhwm_Type()
)
uxos_vBufhwm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vBufhwm.setStatus("mandatory")
_Uxos_vScrn_Type = Counter32
_Uxos_vScrn_Object = MibScalar
uxos_vScrn = _Uxos_vScrn_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 19),
    _Uxos_vScrn_Type()
)
uxos_vScrn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vScrn.setStatus("mandatory")
_Uxos_vEmap_Type = Counter32
_Uxos_vEmap_Object = MibScalar
uxos_vEmap = _Uxos_vEmap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 20),
    _Uxos_vEmap_Type()
)
uxos_vEmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vEmap.setStatus("mandatory")
_Uxos_vSxt_Type = Counter32
_Uxos_vSxt_Object = MibScalar
uxos_vSxt = _Uxos_vSxt_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 21),
    _Uxos_vSxt_Type()
)
uxos_vSxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vSxt.setStatus("mandatory")
_Uxos_vXsdsegs_Type = Counter32
_Uxos_vXsdsegs_Object = MibScalar
uxos_vXsdsegs = _Uxos_vXsdsegs_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 22),
    _Uxos_vXsdsegs_Type()
)
uxos_vXsdsegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vXsdsegs.setStatus("mandatory")
_Uxos_vXsdslots_Type = Counter32
_Uxos_vXsdslots_Object = MibScalar
uxos_vXsdslots = _Uxos_vXsdslots_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 23),
    _Uxos_vXsdslots_Type()
)
uxos_vXsdslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vXsdslots.setStatus("mandatory")
_Uxos_vPhash_Type = Counter32
_Uxos_vPhash_Object = MibScalar
uxos_vPhash = _Uxos_vPhash_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 13, 1, 1, 24),
    _Uxos_vPhash_Type()
)
uxos_vPhash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vPhash.setStatus("mandatory")
_Uxos_shlbinfo_ObjectIdentity = ObjectIdentity
uxos_shlbinfo = _Uxos_shlbinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14)
)
_Uxos_shlbinfoTable_Object = MibTable
uxos_shlbinfoTable = _Uxos_shlbinfoTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1)
)
if mibBuilder.loadTexts:
    uxos_shlbinfoTable.setStatus("mandatory")
_Uxos_shlbinfoEntry_Object = MibTableRow
uxos_shlbinfoEntry = _Uxos_shlbinfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1)
)
uxos_shlbinfoEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-shlbinfoSysName"),
    (0, "OLIVETTI-MIB", "uxos-shlbinfoInstName"),
    (0, "OLIVETTI-MIB", "uxos-shlbinfoSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_shlbinfoEntry.setStatus("mandatory")


class _Uxos_shlbinfoSysName_Type(DisplayString):
    """Custom type uxos_shlbinfoSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_shlbinfoSysName_Type.__name__ = "DisplayString"
_Uxos_shlbinfoSysName_Object = MibScalar
uxos_shlbinfoSysName = _Uxos_shlbinfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1, 1),
    _Uxos_shlbinfoSysName_Type()
)
uxos_shlbinfoSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shlbinfoSysName.setStatus("mandatory")


class _Uxos_shlbinfoInstName_Type(DisplayString):
    """Custom type uxos_shlbinfoInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_shlbinfoInstName_Type.__name__ = "DisplayString"
_Uxos_shlbinfoInstName_Object = MibScalar
uxos_shlbinfoInstName = _Uxos_shlbinfoInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1, 2),
    _Uxos_shlbinfoInstName_Type()
)
uxos_shlbinfoInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shlbinfoInstName.setStatus("mandatory")


class _Uxos_shlbinfoSubAddr_Type(DisplayString):
    """Custom type uxos_shlbinfoSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_shlbinfoSubAddr_Type.__name__ = "DisplayString"
_Uxos_shlbinfoSubAddr_Object = MibScalar
uxos_shlbinfoSubAddr = _Uxos_shlbinfoSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1, 3),
    _Uxos_shlbinfoSubAddr_Type()
)
uxos_shlbinfoSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shlbinfoSubAddr.setStatus("mandatory")
_Uxos_shlbs_Type = Counter32
_Uxos_shlbs_Object = MibScalar
uxos_shlbs = _Uxos_shlbs_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1, 4),
    _Uxos_shlbs_Type()
)
uxos_shlbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shlbs.setStatus("mandatory")
_Uxos_shlblnks_Type = Counter32
_Uxos_shlblnks_Object = MibScalar
uxos_shlblnks = _Uxos_shlblnks_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1, 5),
    _Uxos_shlblnks_Type()
)
uxos_shlblnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shlblnks.setStatus("mandatory")
_Uxos_shlbovf_Type = Counter32
_Uxos_shlbovf_Object = MibScalar
uxos_shlbovf = _Uxos_shlbovf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1, 6),
    _Uxos_shlbovf_Type()
)
uxos_shlbovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shlbovf.setStatus("mandatory")
_Uxos_shlbatts_Type = Counter32
_Uxos_shlbatts_Object = MibScalar
uxos_shlbatts = _Uxos_shlbatts_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 14, 1, 1, 7),
    _Uxos_shlbatts_Type()
)
uxos_shlbatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shlbatts.setStatus("mandatory")
_Uxos_flckinfo_ObjectIdentity = ObjectIdentity
uxos_flckinfo = _Uxos_flckinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15)
)
_Uxos_flckinfoTable_Object = MibTable
uxos_flckinfoTable = _Uxos_flckinfoTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15, 1)
)
if mibBuilder.loadTexts:
    uxos_flckinfoTable.setStatus("mandatory")
_Uxos_flckinfoEntry_Object = MibTableRow
uxos_flckinfoEntry = _Uxos_flckinfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15, 1, 1)
)
uxos_flckinfoEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-flckinfoSysName"),
    (0, "OLIVETTI-MIB", "uxos-flckinfoInstName"),
    (0, "OLIVETTI-MIB", "uxos-flckinfoSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_flckinfoEntry.setStatus("mandatory")


class _Uxos_flckinfoSysName_Type(DisplayString):
    """Custom type uxos_flckinfoSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_flckinfoSysName_Type.__name__ = "DisplayString"
_Uxos_flckinfoSysName_Object = MibScalar
uxos_flckinfoSysName = _Uxos_flckinfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15, 1, 1, 1),
    _Uxos_flckinfoSysName_Type()
)
uxos_flckinfoSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_flckinfoSysName.setStatus("mandatory")


class _Uxos_flckinfoInstName_Type(DisplayString):
    """Custom type uxos_flckinfoInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_flckinfoInstName_Type.__name__ = "DisplayString"
_Uxos_flckinfoInstName_Object = MibScalar
uxos_flckinfoInstName = _Uxos_flckinfoInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15, 1, 1, 2),
    _Uxos_flckinfoInstName_Type()
)
uxos_flckinfoInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_flckinfoInstName.setStatus("mandatory")


class _Uxos_flckinfoSubAddr_Type(DisplayString):
    """Custom type uxos_flckinfoSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_flckinfoSubAddr_Type.__name__ = "DisplayString"
_Uxos_flckinfoSubAddr_Object = MibScalar
uxos_flckinfoSubAddr = _Uxos_flckinfoSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15, 1, 1, 3),
    _Uxos_flckinfoSubAddr_Type()
)
uxos_flckinfoSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_flckinfoSubAddr.setStatus("mandatory")
_Uxos_reccnt_Type = Counter32
_Uxos_reccnt_Object = MibScalar
uxos_reccnt = _Uxos_reccnt_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15, 1, 1, 4),
    _Uxos_reccnt_Type()
)
uxos_reccnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_reccnt.setStatus("mandatory")
_Uxos_rectot_Type = Counter32
_Uxos_rectot_Object = MibScalar
uxos_rectot = _Uxos_rectot_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 15, 1, 1, 5),
    _Uxos_rectot_Type()
)
uxos_rectot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rectot.setStatus("mandatory")
_Uxos_tune_ObjectIdentity = ObjectIdentity
uxos_tune = _Uxos_tune_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16)
)
_Uxos_tuneTable_Object = MibTable
uxos_tuneTable = _Uxos_tuneTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1)
)
if mibBuilder.loadTexts:
    uxos_tuneTable.setStatus("mandatory")
_Uxos_tuneEntry_Object = MibTableRow
uxos_tuneEntry = _Uxos_tuneEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1)
)
uxos_tuneEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-tuneSysName"),
    (0, "OLIVETTI-MIB", "uxos-tuneInstName"),
    (0, "OLIVETTI-MIB", "uxos-tuneSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_tuneEntry.setStatus("mandatory")


class _Uxos_tuneSysName_Type(DisplayString):
    """Custom type uxos_tuneSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_tuneSysName_Type.__name__ = "DisplayString"
_Uxos_tuneSysName_Object = MibScalar
uxos_tuneSysName = _Uxos_tuneSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 1),
    _Uxos_tuneSysName_Type()
)
uxos_tuneSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tuneSysName.setStatus("mandatory")


class _Uxos_tuneInstName_Type(DisplayString):
    """Custom type uxos_tuneInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_tuneInstName_Type.__name__ = "DisplayString"
_Uxos_tuneInstName_Object = MibScalar
uxos_tuneInstName = _Uxos_tuneInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 2),
    _Uxos_tuneInstName_Type()
)
uxos_tuneInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tuneInstName.setStatus("mandatory")


class _Uxos_tuneSubAddr_Type(DisplayString):
    """Custom type uxos_tuneSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_tuneSubAddr_Type.__name__ = "DisplayString"
_Uxos_tuneSubAddr_Object = MibScalar
uxos_tuneSubAddr = _Uxos_tuneSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 3),
    _Uxos_tuneSubAddr_Type()
)
uxos_tuneSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tuneSubAddr.setStatus("mandatory")
_Uxos_tGpgslo_Type = Counter32
_Uxos_tGpgslo_Object = MibScalar
uxos_tGpgslo = _Uxos_tGpgslo_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 4),
    _Uxos_tGpgslo_Type()
)
uxos_tGpgslo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tGpgslo.setStatus("mandatory")
_Uxos_tGpgshi_Type = Counter32
_Uxos_tGpgshi_Object = MibScalar
uxos_tGpgshi = _Uxos_tGpgshi_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 5),
    _Uxos_tGpgshi_Type()
)
uxos_tGpgshi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tGpgshi.setStatus("mandatory")
_Uxos_tPadd_Type = Counter32
_Uxos_tPadd_Object = MibScalar
uxos_tPadd = _Uxos_tPadd_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 6),
    _Uxos_tPadd_Type()
)
uxos_tPadd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tPadd.setStatus("mandatory")
_Uxos_tNotused_Type = Counter32
_Uxos_tNotused_Object = MibScalar
uxos_tNotused = _Uxos_tNotused_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 7),
    _Uxos_tNotused_Type()
)
uxos_tNotused.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_tNotused.setStatus("mandatory")
_Uxos_tAgeinterval_Type = Counter32
_Uxos_tAgeinterval_Object = MibScalar
uxos_tAgeinterval = _Uxos_tAgeinterval_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 8),
    _Uxos_tAgeinterval_Type()
)
uxos_tAgeinterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tAgeinterval.setStatus("mandatory")
_Uxos_tPadd11_Type = Counter32
_Uxos_tPadd11_Object = MibScalar
uxos_tPadd11 = _Uxos_tPadd11_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 9),
    _Uxos_tPadd11_Type()
)
uxos_tPadd11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tPadd11.setStatus("mandatory")
_Uxos_tPadd12_Type = Counter32
_Uxos_tPadd12_Object = MibScalar
uxos_tPadd12 = _Uxos_tPadd12_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 10),
    _Uxos_tPadd12_Type()
)
uxos_tPadd12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tPadd12.setStatus("mandatory")
_Uxos_tPadd13_Type = Counter32
_Uxos_tPadd13_Object = MibScalar
uxos_tPadd13 = _Uxos_tPadd13_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 11),
    _Uxos_tPadd13_Type()
)
uxos_tPadd13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tPadd13.setStatus("mandatory")
_Uxos_tFsflushr_Type = Counter32
_Uxos_tFsflushr_Object = MibScalar
uxos_tFsflushr = _Uxos_tFsflushr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 12),
    _Uxos_tFsflushr_Type()
)
uxos_tFsflushr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tFsflushr.setStatus("mandatory")
_Uxos_tMinarmem_Type = Counter32
_Uxos_tMinarmem_Object = MibScalar
uxos_tMinarmem = _Uxos_tMinarmem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 13),
    _Uxos_tMinarmem_Type()
)
uxos_tMinarmem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tMinarmem.setStatus("mandatory")
_Uxos_tMinasmem_Type = Counter32
_Uxos_tMinasmem_Object = MibScalar
uxos_tMinasmem = _Uxos_tMinasmem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 14),
    _Uxos_tMinasmem_Type()
)
uxos_tMinasmem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tMinasmem.setStatus("mandatory")
_Uxos_tDmalimit_Type = Counter32
_Uxos_tDmalimit_Object = MibScalar
uxos_tDmalimit = _Uxos_tDmalimit_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 15),
    _Uxos_tDmalimit_Type()
)
uxos_tDmalimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tDmalimit.setStatus("mandatory")
_Uxos_tFlckrec_Type = Counter32
_Uxos_tFlckrec_Object = MibScalar
uxos_tFlckrec = _Uxos_tFlckrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 16),
    _Uxos_tFlckrec_Type()
)
uxos_tFlckrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tFlckrec.setStatus("mandatory")
_Uxos_tMinakmem_Type = Counter32
_Uxos_tMinakmem_Object = MibScalar
uxos_tMinakmem = _Uxos_tMinakmem_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 16, 1, 1, 17),
    _Uxos_tMinakmem_Type()
)
uxos_tMinakmem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tMinakmem.setStatus("mandatory")
_Uxos_avenrun_ObjectIdentity = ObjectIdentity
uxos_avenrun = _Uxos_avenrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17)
)
_Uxos_avenrunTable_Object = MibTable
uxos_avenrunTable = _Uxos_avenrunTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1)
)
if mibBuilder.loadTexts:
    uxos_avenrunTable.setStatus("mandatory")
_Uxos_avenrunEntry_Object = MibTableRow
uxos_avenrunEntry = _Uxos_avenrunEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1, 1)
)
uxos_avenrunEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-avenrunSysName"),
    (0, "OLIVETTI-MIB", "uxos-avenrunInstName"),
    (0, "OLIVETTI-MIB", "uxos-avenrunSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_avenrunEntry.setStatus("mandatory")


class _Uxos_avenrunSysName_Type(DisplayString):
    """Custom type uxos_avenrunSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_avenrunSysName_Type.__name__ = "DisplayString"
_Uxos_avenrunSysName_Object = MibScalar
uxos_avenrunSysName = _Uxos_avenrunSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1, 1, 1),
    _Uxos_avenrunSysName_Type()
)
uxos_avenrunSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_avenrunSysName.setStatus("mandatory")


class _Uxos_avenrunInstName_Type(DisplayString):
    """Custom type uxos_avenrunInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_avenrunInstName_Type.__name__ = "DisplayString"
_Uxos_avenrunInstName_Object = MibScalar
uxos_avenrunInstName = _Uxos_avenrunInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1, 1, 2),
    _Uxos_avenrunInstName_Type()
)
uxos_avenrunInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_avenrunInstName.setStatus("mandatory")


class _Uxos_avenrunSubAddr_Type(DisplayString):
    """Custom type uxos_avenrunSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_avenrunSubAddr_Type.__name__ = "DisplayString"
_Uxos_avenrunSubAddr_Object = MibScalar
uxos_avenrunSubAddr = _Uxos_avenrunSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1, 1, 3),
    _Uxos_avenrunSubAddr_Type()
)
uxos_avenrunSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_avenrunSubAddr.setStatus("mandatory")
_Uxos_avenrun1_Type = Counter32
_Uxos_avenrun1_Object = MibScalar
uxos_avenrun1 = _Uxos_avenrun1_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1, 1, 4),
    _Uxos_avenrun1_Type()
)
uxos_avenrun1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_avenrun1.setStatus("mandatory")
_Uxos_avenrun2_Type = Counter32
_Uxos_avenrun2_Object = MibScalar
uxos_avenrun2 = _Uxos_avenrun2_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1, 1, 5),
    _Uxos_avenrun2_Type()
)
uxos_avenrun2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_avenrun2.setStatus("mandatory")
_Uxos_avenrun3_Type = Counter32
_Uxos_avenrun3_Object = MibScalar
uxos_avenrun3 = _Uxos_avenrun3_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 17, 1, 1, 6),
    _Uxos_avenrun3_Type()
)
uxos_avenrun3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_avenrun3.setStatus("mandatory")
_Uxos_vmcnt_ObjectIdentity = ObjectIdentity
uxos_vmcnt = _Uxos_vmcnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18)
)
_Uxos_vmcntTable_Object = MibTable
uxos_vmcntTable = _Uxos_vmcntTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1)
)
if mibBuilder.loadTexts:
    uxos_vmcntTable.setStatus("mandatory")
_Uxos_vmcntEntry_Object = MibTableRow
uxos_vmcntEntry = _Uxos_vmcntEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1)
)
uxos_vmcntEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-vmcntSysName"),
    (0, "OLIVETTI-MIB", "uxos-vmcntInstName"),
    (0, "OLIVETTI-MIB", "uxos-vmcntSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_vmcntEntry.setStatus("mandatory")


class _Uxos_vmcntSysName_Type(DisplayString):
    """Custom type uxos_vmcntSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmcntSysName_Type.__name__ = "DisplayString"
_Uxos_vmcntSysName_Object = MibScalar
uxos_vmcntSysName = _Uxos_vmcntSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 1),
    _Uxos_vmcntSysName_Type()
)
uxos_vmcntSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmcntSysName.setStatus("mandatory")


class _Uxos_vmcntInstName_Type(DisplayString):
    """Custom type uxos_vmcntInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmcntInstName_Type.__name__ = "DisplayString"
_Uxos_vmcntInstName_Object = MibScalar
uxos_vmcntInstName = _Uxos_vmcntInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 2),
    _Uxos_vmcntInstName_Type()
)
uxos_vmcntInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmcntInstName.setStatus("mandatory")


class _Uxos_vmcntSubAddr_Type(DisplayString):
    """Custom type uxos_vmcntSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmcntSubAddr_Type.__name__ = "DisplayString"
_Uxos_vmcntSubAddr_Object = MibScalar
uxos_vmcntSubAddr = _Uxos_vmcntSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 3),
    _Uxos_vmcntSubAddr_Type()
)
uxos_vmcntSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmcntSubAddr.setStatus("mandatory")
_Uxos_cntvSwtch_Type = Counter32
_Uxos_cntvSwtch_Object = MibScalar
uxos_cntvSwtch = _Uxos_cntvSwtch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 4),
    _Uxos_cntvSwtch_Type()
)
uxos_cntvSwtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvSwtch.setStatus("mandatory")
_Uxos_cntvTrap_Type = Counter32
_Uxos_cntvTrap_Object = MibScalar
uxos_cntvTrap = _Uxos_cntvTrap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 5),
    _Uxos_cntvTrap_Type()
)
uxos_cntvTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvTrap.setStatus("mandatory")
_Uxos_cntvSyscall_Type = Counter32
_Uxos_cntvSyscall_Object = MibScalar
uxos_cntvSyscall = _Uxos_cntvSyscall_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 6),
    _Uxos_cntvSyscall_Type()
)
uxos_cntvSyscall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvSyscall.setStatus("mandatory")
_Uxos_cntvIntr_Type = Counter32
_Uxos_cntvIntr_Object = MibScalar
uxos_cntvIntr = _Uxos_cntvIntr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 7),
    _Uxos_cntvIntr_Type()
)
uxos_cntvIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvIntr.setStatus("mandatory")
_Uxos_cntvPdma_Type = Counter32
_Uxos_cntvPdma_Object = MibScalar
uxos_cntvPdma = _Uxos_cntvPdma_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 8),
    _Uxos_cntvPdma_Type()
)
uxos_cntvPdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPdma.setStatus("mandatory")
_Uxos_cntvPswpin_Type = Counter32
_Uxos_cntvPswpin_Object = MibScalar
uxos_cntvPswpin = _Uxos_cntvPswpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 9),
    _Uxos_cntvPswpin_Type()
)
uxos_cntvPswpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPswpin.setStatus("mandatory")
_Uxos_cntvPswpout_Type = Counter32
_Uxos_cntvPswpout_Object = MibScalar
uxos_cntvPswpout = _Uxos_cntvPswpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 10),
    _Uxos_cntvPswpout_Type()
)
uxos_cntvPswpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPswpout.setStatus("mandatory")
_Uxos_cntvPgin_Type = Counter32
_Uxos_cntvPgin_Object = MibScalar
uxos_cntvPgin = _Uxos_cntvPgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 11),
    _Uxos_cntvPgin_Type()
)
uxos_cntvPgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPgin.setStatus("mandatory")
_Uxos_cntvPgout_Type = Counter32
_Uxos_cntvPgout_Object = MibScalar
uxos_cntvPgout = _Uxos_cntvPgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 12),
    _Uxos_cntvPgout_Type()
)
uxos_cntvPgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPgout.setStatus("mandatory")
_Uxos_cntvPgpgin_Type = Counter32
_Uxos_cntvPgpgin_Object = MibScalar
uxos_cntvPgpgin = _Uxos_cntvPgpgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 13),
    _Uxos_cntvPgpgin_Type()
)
uxos_cntvPgpgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPgpgin.setStatus("mandatory")
_Uxos_cntvPgpgout_Type = Counter32
_Uxos_cntvPgpgout_Object = MibScalar
uxos_cntvPgpgout = _Uxos_cntvPgpgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 14),
    _Uxos_cntvPgpgout_Type()
)
uxos_cntvPgpgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPgpgout.setStatus("mandatory")
_Uxos_cntvIntrans_Type = Counter32
_Uxos_cntvIntrans_Object = MibScalar
uxos_cntvIntrans = _Uxos_cntvIntrans_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 15),
    _Uxos_cntvIntrans_Type()
)
uxos_cntvIntrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvIntrans.setStatus("mandatory")
_Uxos_cntvPgrec_Type = Counter32
_Uxos_cntvPgrec_Object = MibScalar
uxos_cntvPgrec = _Uxos_cntvPgrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 16),
    _Uxos_cntvPgrec_Type()
)
uxos_cntvPgrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPgrec.setStatus("mandatory")
_Uxos_cntvXsfrec_Type = Counter32
_Uxos_cntvXsfrec_Object = MibScalar
uxos_cntvXsfrec = _Uxos_cntvXsfrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 17),
    _Uxos_cntvXsfrec_Type()
)
uxos_cntvXsfrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvXsfrec.setStatus("mandatory")
_Uxos_cntvXifrec_Type = Counter32
_Uxos_cntvXifrec_Object = MibScalar
uxos_cntvXifrec = _Uxos_cntvXifrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 18),
    _Uxos_cntvXifrec_Type()
)
uxos_cntvXifrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvXifrec.setStatus("mandatory")
_Uxos_cntvExfod_Type = Counter32
_Uxos_cntvExfod_Object = MibScalar
uxos_cntvExfod = _Uxos_cntvExfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 19),
    _Uxos_cntvExfod_Type()
)
uxos_cntvExfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_cntvExfod.setStatus("mandatory")
_Uxos_cntvZfod_Type = Counter32
_Uxos_cntvZfod_Object = MibScalar
uxos_cntvZfod = _Uxos_cntvZfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 20),
    _Uxos_cntvZfod_Type()
)
uxos_cntvZfod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvZfod.setStatus("mandatory")
_Uxos_cntvVrfod_Type = Counter32
_Uxos_cntvVrfod_Object = MibScalar
uxos_cntvVrfod = _Uxos_cntvVrfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 21),
    _Uxos_cntvVrfod_Type()
)
uxos_cntvVrfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_cntvVrfod.setStatus("mandatory")
_Uxos_cntvNexfod_Type = Counter32
_Uxos_cntvNexfod_Object = MibScalar
uxos_cntvNexfod = _Uxos_cntvNexfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 22),
    _Uxos_cntvNexfod_Type()
)
uxos_cntvNexfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_cntvNexfod.setStatus("mandatory")
_Uxos_cntvNzfod_Type = Counter32
_Uxos_cntvNzfod_Object = MibScalar
uxos_cntvNzfod = _Uxos_cntvNzfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 23),
    _Uxos_cntvNzfod_Type()
)
uxos_cntvNzfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_cntvNzfod.setStatus("mandatory")
_Uxos_cntvNvrfod_Type = Counter32
_Uxos_cntvNvrfod_Object = MibScalar
uxos_cntvNvrfod = _Uxos_cntvNvrfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 24),
    _Uxos_cntvNvrfod_Type()
)
uxos_cntvNvrfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_cntvNvrfod.setStatus("mandatory")
_Uxos_cntvPgfrec_Type = Counter32
_Uxos_cntvPgfrec_Object = MibScalar
uxos_cntvPgfrec = _Uxos_cntvPgfrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 25),
    _Uxos_cntvPgfrec_Type()
)
uxos_cntvPgfrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvPgfrec.setStatus("mandatory")
_Uxos_cntvFaults_Type = Counter32
_Uxos_cntvFaults_Object = MibScalar
uxos_cntvFaults = _Uxos_cntvFaults_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 26),
    _Uxos_cntvFaults_Type()
)
uxos_cntvFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvFaults.setStatus("mandatory")
_Uxos_cntvScan_Type = Counter32
_Uxos_cntvScan_Object = MibScalar
uxos_cntvScan = _Uxos_cntvScan_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 27),
    _Uxos_cntvScan_Type()
)
uxos_cntvScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvScan.setStatus("mandatory")
_Uxos_cntvRev_Type = Counter32
_Uxos_cntvRev_Object = MibScalar
uxos_cntvRev = _Uxos_cntvRev_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 28),
    _Uxos_cntvRev_Type()
)
uxos_cntvRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvRev.setStatus("mandatory")
_Uxos_cntvSeqfree_Type = Counter32
_Uxos_cntvSeqfree_Object = MibScalar
uxos_cntvSeqfree = _Uxos_cntvSeqfree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 29),
    _Uxos_cntvSeqfree_Type()
)
uxos_cntvSeqfree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_cntvSeqfree.setStatus("mandatory")
_Uxos_cntvDfree_Type = Counter32
_Uxos_cntvDfree_Object = MibScalar
uxos_cntvDfree = _Uxos_cntvDfree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 30),
    _Uxos_cntvDfree_Type()
)
uxos_cntvDfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvDfree.setStatus("mandatory")
_Uxos_cntvFastpgrec_Type = Counter32
_Uxos_cntvFastpgrec_Object = MibScalar
uxos_cntvFastpgrec = _Uxos_cntvFastpgrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 31),
    _Uxos_cntvFastpgrec_Type()
)
uxos_cntvFastpgrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_cntvFastpgrec.setStatus("mandatory")
_Uxos_cntvSwpin_Type = Counter32
_Uxos_cntvSwpin_Object = MibScalar
uxos_cntvSwpin = _Uxos_cntvSwpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 32),
    _Uxos_cntvSwpin_Type()
)
uxos_cntvSwpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvSwpin.setStatus("mandatory")
_Uxos_cntvSwpout_Type = Counter32
_Uxos_cntvSwpout_Object = MibScalar
uxos_cntvSwpout = _Uxos_cntvSwpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 18, 1, 1, 33),
    _Uxos_cntvSwpout_Type()
)
uxos_cntvSwpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cntvSwpout.setStatus("mandatory")
_Uxos_vmrate_ObjectIdentity = ObjectIdentity
uxos_vmrate = _Uxos_vmrate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19)
)
_Uxos_vmrateTable_Object = MibTable
uxos_vmrateTable = _Uxos_vmrateTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1)
)
if mibBuilder.loadTexts:
    uxos_vmrateTable.setStatus("mandatory")
_Uxos_vmrateEntry_Object = MibTableRow
uxos_vmrateEntry = _Uxos_vmrateEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1)
)
uxos_vmrateEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-vmrateSysName"),
    (0, "OLIVETTI-MIB", "uxos-vmrateInstName"),
    (0, "OLIVETTI-MIB", "uxos-vmrateSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_vmrateEntry.setStatus("mandatory")


class _Uxos_vmrateSysName_Type(DisplayString):
    """Custom type uxos_vmrateSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmrateSysName_Type.__name__ = "DisplayString"
_Uxos_vmrateSysName_Object = MibScalar
uxos_vmrateSysName = _Uxos_vmrateSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 1),
    _Uxos_vmrateSysName_Type()
)
uxos_vmrateSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmrateSysName.setStatus("mandatory")


class _Uxos_vmrateInstName_Type(DisplayString):
    """Custom type uxos_vmrateInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmrateInstName_Type.__name__ = "DisplayString"
_Uxos_vmrateInstName_Object = MibScalar
uxos_vmrateInstName = _Uxos_vmrateInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 2),
    _Uxos_vmrateInstName_Type()
)
uxos_vmrateInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmrateInstName.setStatus("mandatory")


class _Uxos_vmrateSubAddr_Type(DisplayString):
    """Custom type uxos_vmrateSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmrateSubAddr_Type.__name__ = "DisplayString"
_Uxos_vmrateSubAddr_Object = MibScalar
uxos_vmrateSubAddr = _Uxos_vmrateSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 3),
    _Uxos_vmrateSubAddr_Type()
)
uxos_vmrateSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmrateSubAddr.setStatus("mandatory")
_Uxos_ratevSwtch_Type = Counter32
_Uxos_ratevSwtch_Object = MibScalar
uxos_ratevSwtch = _Uxos_ratevSwtch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 4),
    _Uxos_ratevSwtch_Type()
)
uxos_ratevSwtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevSwtch.setStatus("mandatory")
_Uxos_ratevTrap_Type = Counter32
_Uxos_ratevTrap_Object = MibScalar
uxos_ratevTrap = _Uxos_ratevTrap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 5),
    _Uxos_ratevTrap_Type()
)
uxos_ratevTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevTrap.setStatus("mandatory")
_Uxos_ratevSyscall_Type = Counter32
_Uxos_ratevSyscall_Object = MibScalar
uxos_ratevSyscall = _Uxos_ratevSyscall_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 6),
    _Uxos_ratevSyscall_Type()
)
uxos_ratevSyscall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevSyscall.setStatus("mandatory")
_Uxos_ratevIntr_Type = Counter32
_Uxos_ratevIntr_Object = MibScalar
uxos_ratevIntr = _Uxos_ratevIntr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 7),
    _Uxos_ratevIntr_Type()
)
uxos_ratevIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevIntr.setStatus("mandatory")
_Uxos_ratevPdma_Type = Counter32
_Uxos_ratevPdma_Object = MibScalar
uxos_ratevPdma = _Uxos_ratevPdma_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 8),
    _Uxos_ratevPdma_Type()
)
uxos_ratevPdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPdma.setStatus("mandatory")
_Uxos_ratevPswpin_Type = Counter32
_Uxos_ratevPswpin_Object = MibScalar
uxos_ratevPswpin = _Uxos_ratevPswpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 9),
    _Uxos_ratevPswpin_Type()
)
uxos_ratevPswpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPswpin.setStatus("mandatory")
_Uxos_ratevPswpout_Type = Counter32
_Uxos_ratevPswpout_Object = MibScalar
uxos_ratevPswpout = _Uxos_ratevPswpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 10),
    _Uxos_ratevPswpout_Type()
)
uxos_ratevPswpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPswpout.setStatus("mandatory")
_Uxos_ratevPgin_Type = Counter32
_Uxos_ratevPgin_Object = MibScalar
uxos_ratevPgin = _Uxos_ratevPgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 11),
    _Uxos_ratevPgin_Type()
)
uxos_ratevPgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPgin.setStatus("mandatory")
_Uxos_ratevPgout_Type = Counter32
_Uxos_ratevPgout_Object = MibScalar
uxos_ratevPgout = _Uxos_ratevPgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 12),
    _Uxos_ratevPgout_Type()
)
uxos_ratevPgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPgout.setStatus("mandatory")
_Uxos_ratevPgpgin_Type = Counter32
_Uxos_ratevPgpgin_Object = MibScalar
uxos_ratevPgpgin = _Uxos_ratevPgpgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 13),
    _Uxos_ratevPgpgin_Type()
)
uxos_ratevPgpgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPgpgin.setStatus("mandatory")
_Uxos_ratevPgpgout_Type = Counter32
_Uxos_ratevPgpgout_Object = MibScalar
uxos_ratevPgpgout = _Uxos_ratevPgpgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 14),
    _Uxos_ratevPgpgout_Type()
)
uxos_ratevPgpgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPgpgout.setStatus("mandatory")
_Uxos_ratevIntrans_Type = Counter32
_Uxos_ratevIntrans_Object = MibScalar
uxos_ratevIntrans = _Uxos_ratevIntrans_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 15),
    _Uxos_ratevIntrans_Type()
)
uxos_ratevIntrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevIntrans.setStatus("mandatory")
_Uxos_ratevPgrec_Type = Counter32
_Uxos_ratevPgrec_Object = MibScalar
uxos_ratevPgrec = _Uxos_ratevPgrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 16),
    _Uxos_ratevPgrec_Type()
)
uxos_ratevPgrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPgrec.setStatus("mandatory")
_Uxos_ratevXsfrec_Type = Counter32
_Uxos_ratevXsfrec_Object = MibScalar
uxos_ratevXsfrec = _Uxos_ratevXsfrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 17),
    _Uxos_ratevXsfrec_Type()
)
uxos_ratevXsfrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevXsfrec.setStatus("mandatory")
_Uxos_ratevXifrec_Type = Counter32
_Uxos_ratevXifrec_Object = MibScalar
uxos_ratevXifrec = _Uxos_ratevXifrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 18),
    _Uxos_ratevXifrec_Type()
)
uxos_ratevXifrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevXifrec.setStatus("mandatory")
_Uxos_ratevExfod_Type = Counter32
_Uxos_ratevExfod_Object = MibScalar
uxos_ratevExfod = _Uxos_ratevExfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 19),
    _Uxos_ratevExfod_Type()
)
uxos_ratevExfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_ratevExfod.setStatus("mandatory")
_Uxos_ratevZfod_Type = Counter32
_Uxos_ratevZfod_Object = MibScalar
uxos_ratevZfod = _Uxos_ratevZfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 20),
    _Uxos_ratevZfod_Type()
)
uxos_ratevZfod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevZfod.setStatus("mandatory")
_Uxos_ratevVrfod_Type = Counter32
_Uxos_ratevVrfod_Object = MibScalar
uxos_ratevVrfod = _Uxos_ratevVrfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 21),
    _Uxos_ratevVrfod_Type()
)
uxos_ratevVrfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_ratevVrfod.setStatus("mandatory")
_Uxos_ratevNexfod_Type = Counter32
_Uxos_ratevNexfod_Object = MibScalar
uxos_ratevNexfod = _Uxos_ratevNexfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 22),
    _Uxos_ratevNexfod_Type()
)
uxos_ratevNexfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_ratevNexfod.setStatus("mandatory")
_Uxos_ratevNzfod_Type = Counter32
_Uxos_ratevNzfod_Object = MibScalar
uxos_ratevNzfod = _Uxos_ratevNzfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 23),
    _Uxos_ratevNzfod_Type()
)
uxos_ratevNzfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_ratevNzfod.setStatus("mandatory")
_Uxos_ratevNvrfod_Type = Counter32
_Uxos_ratevNvrfod_Object = MibScalar
uxos_ratevNvrfod = _Uxos_ratevNvrfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 24),
    _Uxos_ratevNvrfod_Type()
)
uxos_ratevNvrfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_ratevNvrfod.setStatus("mandatory")
_Uxos_ratevPgfrec_Type = Counter32
_Uxos_ratevPgfrec_Object = MibScalar
uxos_ratevPgfrec = _Uxos_ratevPgfrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 25),
    _Uxos_ratevPgfrec_Type()
)
uxos_ratevPgfrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevPgfrec.setStatus("mandatory")
_Uxos_ratevFaults_Type = Counter32
_Uxos_ratevFaults_Object = MibScalar
uxos_ratevFaults = _Uxos_ratevFaults_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 26),
    _Uxos_ratevFaults_Type()
)
uxos_ratevFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevFaults.setStatus("mandatory")
_Uxos_ratevScan_Type = Counter32
_Uxos_ratevScan_Object = MibScalar
uxos_ratevScan = _Uxos_ratevScan_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 27),
    _Uxos_ratevScan_Type()
)
uxos_ratevScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevScan.setStatus("mandatory")
_Uxos_ratevRev_Type = Counter32
_Uxos_ratevRev_Object = MibScalar
uxos_ratevRev = _Uxos_ratevRev_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 28),
    _Uxos_ratevRev_Type()
)
uxos_ratevRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevRev.setStatus("mandatory")
_Uxos_ratevSeqfree_Type = Counter32
_Uxos_ratevSeqfree_Object = MibScalar
uxos_ratevSeqfree = _Uxos_ratevSeqfree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 29),
    _Uxos_ratevSeqfree_Type()
)
uxos_ratevSeqfree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_ratevSeqfree.setStatus("mandatory")
_Uxos_ratevDfree_Type = Counter32
_Uxos_ratevDfree_Object = MibScalar
uxos_ratevDfree = _Uxos_ratevDfree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 30),
    _Uxos_ratevDfree_Type()
)
uxos_ratevDfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevDfree.setStatus("mandatory")
_Uxos_ratevFastpgrec_Type = Counter32
_Uxos_ratevFastpgrec_Object = MibScalar
uxos_ratevFastpgrec = _Uxos_ratevFastpgrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 31),
    _Uxos_ratevFastpgrec_Type()
)
uxos_ratevFastpgrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_ratevFastpgrec.setStatus("mandatory")
_Uxos_ratevSwpin_Type = Counter32
_Uxos_ratevSwpin_Object = MibScalar
uxos_ratevSwpin = _Uxos_ratevSwpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 32),
    _Uxos_ratevSwpin_Type()
)
uxos_ratevSwpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevSwpin.setStatus("mandatory")
_Uxos_ratevSwpout_Type = Counter32
_Uxos_ratevSwpout_Object = MibScalar
uxos_ratevSwpout = _Uxos_ratevSwpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 19, 1, 1, 33),
    _Uxos_ratevSwpout_Type()
)
uxos_ratevSwpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ratevSwpout.setStatus("mandatory")
_Uxos_vmsum_ObjectIdentity = ObjectIdentity
uxos_vmsum = _Uxos_vmsum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20)
)
_Uxos_vmsumTable_Object = MibTable
uxos_vmsumTable = _Uxos_vmsumTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1)
)
if mibBuilder.loadTexts:
    uxos_vmsumTable.setStatus("mandatory")
_Uxos_vmsumEntry_Object = MibTableRow
uxos_vmsumEntry = _Uxos_vmsumEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1)
)
uxos_vmsumEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-vmsumSysName"),
    (0, "OLIVETTI-MIB", "uxos-vmsumInstName"),
    (0, "OLIVETTI-MIB", "uxos-vmsumSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_vmsumEntry.setStatus("mandatory")


class _Uxos_vmsumSysName_Type(DisplayString):
    """Custom type uxos_vmsumSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmsumSysName_Type.__name__ = "DisplayString"
_Uxos_vmsumSysName_Object = MibScalar
uxos_vmsumSysName = _Uxos_vmsumSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 1),
    _Uxos_vmsumSysName_Type()
)
uxos_vmsumSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmsumSysName.setStatus("mandatory")


class _Uxos_vmsumInstName_Type(DisplayString):
    """Custom type uxos_vmsumInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmsumInstName_Type.__name__ = "DisplayString"
_Uxos_vmsumInstName_Object = MibScalar
uxos_vmsumInstName = _Uxos_vmsumInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 2),
    _Uxos_vmsumInstName_Type()
)
uxos_vmsumInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmsumInstName.setStatus("mandatory")


class _Uxos_vmsumSubAddr_Type(DisplayString):
    """Custom type uxos_vmsumSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmsumSubAddr_Type.__name__ = "DisplayString"
_Uxos_vmsumSubAddr_Object = MibScalar
uxos_vmsumSubAddr = _Uxos_vmsumSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 3),
    _Uxos_vmsumSubAddr_Type()
)
uxos_vmsumSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmsumSubAddr.setStatus("mandatory")
_Uxos_sumvSwtch_Type = Counter32
_Uxos_sumvSwtch_Object = MibScalar
uxos_sumvSwtch = _Uxos_sumvSwtch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 4),
    _Uxos_sumvSwtch_Type()
)
uxos_sumvSwtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvSwtch.setStatus("mandatory")
_Uxos_sumvTrap_Type = Counter32
_Uxos_sumvTrap_Object = MibScalar
uxos_sumvTrap = _Uxos_sumvTrap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 5),
    _Uxos_sumvTrap_Type()
)
uxos_sumvTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvTrap.setStatus("mandatory")
_Uxos_sumvSyscall_Type = Counter32
_Uxos_sumvSyscall_Object = MibScalar
uxos_sumvSyscall = _Uxos_sumvSyscall_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 6),
    _Uxos_sumvSyscall_Type()
)
uxos_sumvSyscall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvSyscall.setStatus("mandatory")
_Uxos_sumvIntr_Type = Counter32
_Uxos_sumvIntr_Object = MibScalar
uxos_sumvIntr = _Uxos_sumvIntr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 7),
    _Uxos_sumvIntr_Type()
)
uxos_sumvIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvIntr.setStatus("mandatory")
_Uxos_sumvPdma_Type = Counter32
_Uxos_sumvPdma_Object = MibScalar
uxos_sumvPdma = _Uxos_sumvPdma_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 8),
    _Uxos_sumvPdma_Type()
)
uxos_sumvPdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPdma.setStatus("mandatory")
_Uxos_sumvPswpin_Type = Counter32
_Uxos_sumvPswpin_Object = MibScalar
uxos_sumvPswpin = _Uxos_sumvPswpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 9),
    _Uxos_sumvPswpin_Type()
)
uxos_sumvPswpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPswpin.setStatus("mandatory")
_Uxos_sumvPswpout_Type = Counter32
_Uxos_sumvPswpout_Object = MibScalar
uxos_sumvPswpout = _Uxos_sumvPswpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 10),
    _Uxos_sumvPswpout_Type()
)
uxos_sumvPswpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPswpout.setStatus("mandatory")
_Uxos_sumvPgin_Type = Counter32
_Uxos_sumvPgin_Object = MibScalar
uxos_sumvPgin = _Uxos_sumvPgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 11),
    _Uxos_sumvPgin_Type()
)
uxos_sumvPgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPgin.setStatus("mandatory")
_Uxos_sumvPgout_Type = Counter32
_Uxos_sumvPgout_Object = MibScalar
uxos_sumvPgout = _Uxos_sumvPgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 12),
    _Uxos_sumvPgout_Type()
)
uxos_sumvPgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPgout.setStatus("mandatory")
_Uxos_sumvPgpgin_Type = Counter32
_Uxos_sumvPgpgin_Object = MibScalar
uxos_sumvPgpgin = _Uxos_sumvPgpgin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 13),
    _Uxos_sumvPgpgin_Type()
)
uxos_sumvPgpgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPgpgin.setStatus("mandatory")
_Uxos_sumvPgpgout_Type = Counter32
_Uxos_sumvPgpgout_Object = MibScalar
uxos_sumvPgpgout = _Uxos_sumvPgpgout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 14),
    _Uxos_sumvPgpgout_Type()
)
uxos_sumvPgpgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPgpgout.setStatus("mandatory")
_Uxos_sumvIntrans_Type = Counter32
_Uxos_sumvIntrans_Object = MibScalar
uxos_sumvIntrans = _Uxos_sumvIntrans_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 15),
    _Uxos_sumvIntrans_Type()
)
uxos_sumvIntrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvIntrans.setStatus("mandatory")
_Uxos_sumvPgrec_Type = Counter32
_Uxos_sumvPgrec_Object = MibScalar
uxos_sumvPgrec = _Uxos_sumvPgrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 16),
    _Uxos_sumvPgrec_Type()
)
uxos_sumvPgrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPgrec.setStatus("mandatory")
_Uxos_sumvXsfrec_Type = Counter32
_Uxos_sumvXsfrec_Object = MibScalar
uxos_sumvXsfrec = _Uxos_sumvXsfrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 17),
    _Uxos_sumvXsfrec_Type()
)
uxos_sumvXsfrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvXsfrec.setStatus("mandatory")
_Uxos_sumvXifrec_Type = Counter32
_Uxos_sumvXifrec_Object = MibScalar
uxos_sumvXifrec = _Uxos_sumvXifrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 18),
    _Uxos_sumvXifrec_Type()
)
uxos_sumvXifrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvXifrec.setStatus("mandatory")
_Uxos_sumvExfod_Type = Counter32
_Uxos_sumvExfod_Object = MibScalar
uxos_sumvExfod = _Uxos_sumvExfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 19),
    _Uxos_sumvExfod_Type()
)
uxos_sumvExfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sumvExfod.setStatus("mandatory")
_Uxos_sumvZfod_Type = Counter32
_Uxos_sumvZfod_Object = MibScalar
uxos_sumvZfod = _Uxos_sumvZfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 20),
    _Uxos_sumvZfod_Type()
)
uxos_sumvZfod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvZfod.setStatus("mandatory")
_Uxos_sumvVrfod_Type = Counter32
_Uxos_sumvVrfod_Object = MibScalar
uxos_sumvVrfod = _Uxos_sumvVrfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 21),
    _Uxos_sumvVrfod_Type()
)
uxos_sumvVrfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sumvVrfod.setStatus("mandatory")
_Uxos_sumvNexfod_Type = Counter32
_Uxos_sumvNexfod_Object = MibScalar
uxos_sumvNexfod = _Uxos_sumvNexfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 22),
    _Uxos_sumvNexfod_Type()
)
uxos_sumvNexfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sumvNexfod.setStatus("mandatory")
_Uxos_sumvNzfod_Type = Counter32
_Uxos_sumvNzfod_Object = MibScalar
uxos_sumvNzfod = _Uxos_sumvNzfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 23),
    _Uxos_sumvNzfod_Type()
)
uxos_sumvNzfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sumvNzfod.setStatus("mandatory")
_Uxos_sumvNvrfod_Type = Counter32
_Uxos_sumvNvrfod_Object = MibScalar
uxos_sumvNvrfod = _Uxos_sumvNvrfod_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 24),
    _Uxos_sumvNvrfod_Type()
)
uxos_sumvNvrfod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sumvNvrfod.setStatus("mandatory")
_Uxos_sumvPgfrec_Type = Counter32
_Uxos_sumvPgfrec_Object = MibScalar
uxos_sumvPgfrec = _Uxos_sumvPgfrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 25),
    _Uxos_sumvPgfrec_Type()
)
uxos_sumvPgfrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvPgfrec.setStatus("mandatory")
_Uxos_sumvFaults_Type = Counter32
_Uxos_sumvFaults_Object = MibScalar
uxos_sumvFaults = _Uxos_sumvFaults_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 26),
    _Uxos_sumvFaults_Type()
)
uxos_sumvFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvFaults.setStatus("mandatory")
_Uxos_sumvScan_Type = Counter32
_Uxos_sumvScan_Object = MibScalar
uxos_sumvScan = _Uxos_sumvScan_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 27),
    _Uxos_sumvScan_Type()
)
uxos_sumvScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvScan.setStatus("mandatory")
_Uxos_sumvRev_Type = Counter32
_Uxos_sumvRev_Object = MibScalar
uxos_sumvRev = _Uxos_sumvRev_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 28),
    _Uxos_sumvRev_Type()
)
uxos_sumvRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvRev.setStatus("mandatory")
_Uxos_sumvSeqfree_Type = Counter32
_Uxos_sumvSeqfree_Object = MibScalar
uxos_sumvSeqfree = _Uxos_sumvSeqfree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 29),
    _Uxos_sumvSeqfree_Type()
)
uxos_sumvSeqfree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sumvSeqfree.setStatus("mandatory")
_Uxos_sumvDfree_Type = Counter32
_Uxos_sumvDfree_Object = MibScalar
uxos_sumvDfree = _Uxos_sumvDfree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 30),
    _Uxos_sumvDfree_Type()
)
uxos_sumvDfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvDfree.setStatus("mandatory")
_Uxos_sumvFastpgrec_Type = Counter32
_Uxos_sumvFastpgrec_Object = MibScalar
uxos_sumvFastpgrec = _Uxos_sumvFastpgrec_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 31),
    _Uxos_sumvFastpgrec_Type()
)
uxos_sumvFastpgrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_sumvFastpgrec.setStatus("mandatory")
_Uxos_sumvSwpin_Type = Counter32
_Uxos_sumvSwpin_Object = MibScalar
uxos_sumvSwpin = _Uxos_sumvSwpin_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 32),
    _Uxos_sumvSwpin_Type()
)
uxos_sumvSwpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvSwpin.setStatus("mandatory")
_Uxos_sumvSwpout_Type = Counter32
_Uxos_sumvSwpout_Object = MibScalar
uxos_sumvSwpout = _Uxos_sumvSwpout_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 20, 1, 1, 33),
    _Uxos_sumvSwpout_Type()
)
uxos_sumvSwpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sumvSwpout.setStatus("mandatory")
_Uxos_vmtotal_ObjectIdentity = ObjectIdentity
uxos_vmtotal = _Uxos_vmtotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21)
)
_Uxos_vmtotalTable_Object = MibTable
uxos_vmtotalTable = _Uxos_vmtotalTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1)
)
if mibBuilder.loadTexts:
    uxos_vmtotalTable.setStatus("mandatory")
_Uxos_vmtotalEntry_Object = MibTableRow
uxos_vmtotalEntry = _Uxos_vmtotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1)
)
uxos_vmtotalEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-vmtotalSysName"),
    (0, "OLIVETTI-MIB", "uxos-vmtotalInstName"),
    (0, "OLIVETTI-MIB", "uxos-vmtotalSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_vmtotalEntry.setStatus("mandatory")


class _Uxos_vmtotalSysName_Type(DisplayString):
    """Custom type uxos_vmtotalSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmtotalSysName_Type.__name__ = "DisplayString"
_Uxos_vmtotalSysName_Object = MibScalar
uxos_vmtotalSysName = _Uxos_vmtotalSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 1),
    _Uxos_vmtotalSysName_Type()
)
uxos_vmtotalSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmtotalSysName.setStatus("mandatory")


class _Uxos_vmtotalInstName_Type(DisplayString):
    """Custom type uxos_vmtotalInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmtotalInstName_Type.__name__ = "DisplayString"
_Uxos_vmtotalInstName_Object = MibScalar
uxos_vmtotalInstName = _Uxos_vmtotalInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 2),
    _Uxos_vmtotalInstName_Type()
)
uxos_vmtotalInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmtotalInstName.setStatus("mandatory")


class _Uxos_vmtotalSubAddr_Type(DisplayString):
    """Custom type uxos_vmtotalSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vmtotalSubAddr_Type.__name__ = "DisplayString"
_Uxos_vmtotalSubAddr_Object = MibScalar
uxos_vmtotalSubAddr = _Uxos_vmtotalSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 3),
    _Uxos_vmtotalSubAddr_Type()
)
uxos_vmtotalSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vmtotalSubAddr.setStatus("mandatory")
_Uxos_tRq_Type = Counter32
_Uxos_tRq_Object = MibScalar
uxos_tRq = _Uxos_tRq_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 4),
    _Uxos_tRq_Type()
)
uxos_tRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tRq.setStatus("mandatory")
_Uxos_tDw_Type = Counter32
_Uxos_tDw_Object = MibScalar
uxos_tDw = _Uxos_tDw_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 5),
    _Uxos_tDw_Type()
)
uxos_tDw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tDw.setStatus("mandatory")
_Uxos_tPw_Type = Counter32
_Uxos_tPw_Object = MibScalar
uxos_tPw = _Uxos_tPw_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 6),
    _Uxos_tPw_Type()
)
uxos_tPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tPw.setStatus("mandatory")
_Uxos_tSl_Type = Counter32
_Uxos_tSl_Object = MibScalar
uxos_tSl = _Uxos_tSl_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 7),
    _Uxos_tSl_Type()
)
uxos_tSl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tSl.setStatus("mandatory")
_Uxos_tSw_Type = Counter32
_Uxos_tSw_Object = MibScalar
uxos_tSw = _Uxos_tSw_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 8),
    _Uxos_tSw_Type()
)
uxos_tSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tSw.setStatus("mandatory")
_Uxos_tVm_Type = Counter32
_Uxos_tVm_Object = MibScalar
uxos_tVm = _Uxos_tVm_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 9),
    _Uxos_tVm_Type()
)
uxos_tVm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_tVm.setStatus("mandatory")
_Uxos_tAvm_Type = Counter32
_Uxos_tAvm_Object = MibScalar
uxos_tAvm = _Uxos_tAvm_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 10),
    _Uxos_tAvm_Type()
)
uxos_tAvm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_tAvm.setStatus("mandatory")
_Uxos_tRm_Type = Counter32
_Uxos_tRm_Object = MibScalar
uxos_tRm = _Uxos_tRm_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 11),
    _Uxos_tRm_Type()
)
uxos_tRm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tRm.setStatus("mandatory")
_Uxos_tArm_Type = Counter32
_Uxos_tArm_Object = MibScalar
uxos_tArm = _Uxos_tArm_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 12),
    _Uxos_tArm_Type()
)
uxos_tArm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tArm.setStatus("mandatory")
_Uxos_tVmtxt_Type = Counter32
_Uxos_tVmtxt_Object = MibScalar
uxos_tVmtxt = _Uxos_tVmtxt_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 13),
    _Uxos_tVmtxt_Type()
)
uxos_tVmtxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tVmtxt.setStatus("mandatory")
_Uxos_tAvmtxt_Type = Counter32
_Uxos_tAvmtxt_Object = MibScalar
uxos_tAvmtxt = _Uxos_tAvmtxt_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 14),
    _Uxos_tAvmtxt_Type()
)
uxos_tAvmtxt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_tAvmtxt.setStatus("mandatory")
_Uxos_tRmtxt_Type = Counter32
_Uxos_tRmtxt_Object = MibScalar
uxos_tRmtxt = _Uxos_tRmtxt_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 15),
    _Uxos_tRmtxt_Type()
)
uxos_tRmtxt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_tRmtxt.setStatus("mandatory")
_Uxos_tArmtxt_Type = Counter32
_Uxos_tArmtxt_Object = MibScalar
uxos_tArmtxt = _Uxos_tArmtxt_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 16),
    _Uxos_tArmtxt_Type()
)
uxos_tArmtxt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_tArmtxt.setStatus("mandatory")
_Uxos_tFree_Type = Counter32
_Uxos_tFree_Object = MibScalar
uxos_tFree = _Uxos_tFree_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 21, 1, 1, 17),
    _Uxos_tFree_Type()
)
uxos_tFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_tFree.setStatus("mandatory")
_Uxos_lbolt_ObjectIdentity = ObjectIdentity
uxos_lbolt = _Uxos_lbolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 22)
)
_Uxos_lboltTable_Object = MibTable
uxos_lboltTable = _Uxos_lboltTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 22, 1)
)
if mibBuilder.loadTexts:
    uxos_lboltTable.setStatus("mandatory")
_Uxos_lboltEntry_Object = MibTableRow
uxos_lboltEntry = _Uxos_lboltEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 22, 1, 1)
)
uxos_lboltEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-lboltSysName"),
    (0, "OLIVETTI-MIB", "uxos-lboltInstName"),
    (0, "OLIVETTI-MIB", "uxos-lboltSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_lboltEntry.setStatus("mandatory")


class _Uxos_lboltSysName_Type(DisplayString):
    """Custom type uxos_lboltSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_lboltSysName_Type.__name__ = "DisplayString"
_Uxos_lboltSysName_Object = MibScalar
uxos_lboltSysName = _Uxos_lboltSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 22, 1, 1, 1),
    _Uxos_lboltSysName_Type()
)
uxos_lboltSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lboltSysName.setStatus("mandatory")


class _Uxos_lboltInstName_Type(DisplayString):
    """Custom type uxos_lboltInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_lboltInstName_Type.__name__ = "DisplayString"
_Uxos_lboltInstName_Object = MibScalar
uxos_lboltInstName = _Uxos_lboltInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 22, 1, 1, 2),
    _Uxos_lboltInstName_Type()
)
uxos_lboltInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lboltInstName.setStatus("mandatory")


class _Uxos_lboltSubAddr_Type(DisplayString):
    """Custom type uxos_lboltSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_lboltSubAddr_Type.__name__ = "DisplayString"
_Uxos_lboltSubAddr_Object = MibScalar
uxos_lboltSubAddr = _Uxos_lboltSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 22, 1, 1, 3),
    _Uxos_lboltSubAddr_Type()
)
uxos_lboltSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lboltSubAddr.setStatus("mandatory")
_Uxos_numOfTick_Type = Counter32
_Uxos_numOfTick_Object = MibScalar
uxos_numOfTick = _Uxos_numOfTick_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 22, 1, 1, 4),
    _Uxos_numOfTick_Type()
)
uxos_numOfTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_numOfTick.setStatus("mandatory")
_Uxos_availsmem_ObjectIdentity = ObjectIdentity
uxos_availsmem = _Uxos_availsmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 23)
)
_Uxos_smemTable_Object = MibTable
uxos_smemTable = _Uxos_smemTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 23, 1)
)
if mibBuilder.loadTexts:
    uxos_smemTable.setStatus("mandatory")
_Uxos_smemEntry_Object = MibTableRow
uxos_smemEntry = _Uxos_smemEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 23, 1, 1)
)
uxos_smemEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-smemSysName"),
    (0, "OLIVETTI-MIB", "uxos-smemInstName"),
    (0, "OLIVETTI-MIB", "uxos-smemSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_smemEntry.setStatus("mandatory")


class _Uxos_smemSysName_Type(DisplayString):
    """Custom type uxos_smemSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_smemSysName_Type.__name__ = "DisplayString"
_Uxos_smemSysName_Object = MibScalar
uxos_smemSysName = _Uxos_smemSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 23, 1, 1, 1),
    _Uxos_smemSysName_Type()
)
uxos_smemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smemSysName.setStatus("mandatory")


class _Uxos_smemInstName_Type(DisplayString):
    """Custom type uxos_smemInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_smemInstName_Type.__name__ = "DisplayString"
_Uxos_smemInstName_Object = MibScalar
uxos_smemInstName = _Uxos_smemInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 23, 1, 1, 2),
    _Uxos_smemInstName_Type()
)
uxos_smemInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smemInstName.setStatus("mandatory")


class _Uxos_smemSubAddr_Type(DisplayString):
    """Custom type uxos_smemSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_smemSubAddr_Type.__name__ = "DisplayString"
_Uxos_smemSubAddr_Object = MibScalar
uxos_smemSubAddr = _Uxos_smemSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 23, 1, 1, 3),
    _Uxos_smemSubAddr_Type()
)
uxos_smemSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smemSubAddr.setStatus("mandatory")
_Uxos_smemNumOfPages_Type = Counter32
_Uxos_smemNumOfPages_Object = MibScalar
uxos_smemNumOfPages = _Uxos_smemNumOfPages_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 23, 1, 1, 4),
    _Uxos_smemNumOfPages_Type()
)
uxos_smemNumOfPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smemNumOfPages.setStatus("mandatory")
_Uxos_availrmem_ObjectIdentity = ObjectIdentity
uxos_availrmem = _Uxos_availrmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 24)
)
_Uxos_rmemTable_Object = MibTable
uxos_rmemTable = _Uxos_rmemTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 24, 1)
)
if mibBuilder.loadTexts:
    uxos_rmemTable.setStatus("mandatory")
_Uxos_rmemEntry_Object = MibTableRow
uxos_rmemEntry = _Uxos_rmemEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 24, 1, 1)
)
uxos_rmemEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-rmemSysName"),
    (0, "OLIVETTI-MIB", "uxos-rmemInstName"),
    (0, "OLIVETTI-MIB", "uxos-rmemSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_rmemEntry.setStatus("mandatory")


class _Uxos_rmemSysName_Type(DisplayString):
    """Custom type uxos_rmemSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_rmemSysName_Type.__name__ = "DisplayString"
_Uxos_rmemSysName_Object = MibScalar
uxos_rmemSysName = _Uxos_rmemSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 24, 1, 1, 1),
    _Uxos_rmemSysName_Type()
)
uxos_rmemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rmemSysName.setStatus("mandatory")


class _Uxos_rmemInstName_Type(DisplayString):
    """Custom type uxos_rmemInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_rmemInstName_Type.__name__ = "DisplayString"
_Uxos_rmemInstName_Object = MibScalar
uxos_rmemInstName = _Uxos_rmemInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 24, 1, 1, 2),
    _Uxos_rmemInstName_Type()
)
uxos_rmemInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rmemInstName.setStatus("mandatory")


class _Uxos_rmemSubAddr_Type(DisplayString):
    """Custom type uxos_rmemSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_rmemSubAddr_Type.__name__ = "DisplayString"
_Uxos_rmemSubAddr_Object = MibScalar
uxos_rmemSubAddr = _Uxos_rmemSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 24, 1, 1, 3),
    _Uxos_rmemSubAddr_Type()
)
uxos_rmemSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rmemSubAddr.setStatus("mandatory")
_Uxos_rmemNumOfPages_Type = Counter32
_Uxos_rmemNumOfPages_Object = MibScalar
uxos_rmemNumOfPages = _Uxos_rmemNumOfPages_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 24, 1, 1, 4),
    _Uxos_rmemNumOfPages_Type()
)
uxos_rmemNumOfPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rmemNumOfPages.setStatus("mandatory")
_Uxos_availkmem_ObjectIdentity = ObjectIdentity
uxos_availkmem = _Uxos_availkmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 25)
)
_Uxos_kmemTable_Object = MibTable
uxos_kmemTable = _Uxos_kmemTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 25, 1)
)
if mibBuilder.loadTexts:
    uxos_kmemTable.setStatus("mandatory")
_Uxos_kmemEntry_Object = MibTableRow
uxos_kmemEntry = _Uxos_kmemEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 25, 1, 1)
)
uxos_kmemEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-kmemSysName"),
    (0, "OLIVETTI-MIB", "uxos-kmemInstName"),
    (0, "OLIVETTI-MIB", "uxos-kmemSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_kmemEntry.setStatus("mandatory")


class _Uxos_kmemSysName_Type(DisplayString):
    """Custom type uxos_kmemSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_kmemSysName_Type.__name__ = "DisplayString"
_Uxos_kmemSysName_Object = MibScalar
uxos_kmemSysName = _Uxos_kmemSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 25, 1, 1, 1),
    _Uxos_kmemSysName_Type()
)
uxos_kmemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_kmemSysName.setStatus("mandatory")


class _Uxos_kmemInstName_Type(DisplayString):
    """Custom type uxos_kmemInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_kmemInstName_Type.__name__ = "DisplayString"
_Uxos_kmemInstName_Object = MibScalar
uxos_kmemInstName = _Uxos_kmemInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 25, 1, 1, 2),
    _Uxos_kmemInstName_Type()
)
uxos_kmemInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_kmemInstName.setStatus("mandatory")


class _Uxos_kmemSubAddr_Type(DisplayString):
    """Custom type uxos_kmemSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uxos_kmemSubAddr_Type.__name__ = "DisplayString"
_Uxos_kmemSubAddr_Object = MibScalar
uxos_kmemSubAddr = _Uxos_kmemSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 25, 1, 1, 3),
    _Uxos_kmemSubAddr_Type()
)
uxos_kmemSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_kmemSubAddr.setStatus("mandatory")
_Uxos_kmemNumOfPages_Type = Counter32
_Uxos_kmemNumOfPages_Object = MibScalar
uxos_kmemNumOfPages = _Uxos_kmemNumOfPages_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 25, 1, 1, 4),
    _Uxos_kmemNumOfPages_Type()
)
uxos_kmemNumOfPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_kmemNumOfPages.setStatus("mandatory")
_Uxos_namecache_ObjectIdentity = ObjectIdentity
uxos_namecache = _Uxos_namecache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26)
)
_Uxos_namecacheTable_Object = MibTable
uxos_namecacheTable = _Uxos_namecacheTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1)
)
if mibBuilder.loadTexts:
    uxos_namecacheTable.setStatus("mandatory")
_Uxos_namecacheEntry_Object = MibTableRow
uxos_namecacheEntry = _Uxos_namecacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1)
)
uxos_namecacheEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-namecacheSysName"),
    (0, "OLIVETTI-MIB", "uxos-namecacheInstName"),
    (0, "OLIVETTI-MIB", "uxos-namecacheSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_namecacheEntry.setStatus("mandatory")


class _Uxos_namecacheSysName_Type(DisplayString):
    """Custom type uxos_namecacheSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_namecacheSysName_Type.__name__ = "DisplayString"
_Uxos_namecacheSysName_Object = MibScalar
uxos_namecacheSysName = _Uxos_namecacheSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 1),
    _Uxos_namecacheSysName_Type()
)
uxos_namecacheSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_namecacheSysName.setStatus("mandatory")


class _Uxos_namecacheInstName_Type(DisplayString):
    """Custom type uxos_namecacheInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_namecacheInstName_Type.__name__ = "DisplayString"
_Uxos_namecacheInstName_Object = MibScalar
uxos_namecacheInstName = _Uxos_namecacheInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 2),
    _Uxos_namecacheInstName_Type()
)
uxos_namecacheInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_namecacheInstName.setStatus("mandatory")


class _Uxos_namecacheSubAddr_Type(DisplayString):
    """Custom type uxos_namecacheSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_namecacheSubAddr_Type.__name__ = "DisplayString"
_Uxos_namecacheSubAddr_Object = MibScalar
uxos_namecacheSubAddr = _Uxos_namecacheSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 3),
    _Uxos_namecacheSubAddr_Type()
)
uxos_namecacheSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_namecacheSubAddr.setStatus("mandatory")
_Uxos_hits_Type = Counter32
_Uxos_hits_Object = MibScalar
uxos_hits = _Uxos_hits_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 4),
    _Uxos_hits_Type()
)
uxos_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_hits.setStatus("mandatory")
_Uxos_misses_Type = Counter32
_Uxos_misses_Object = MibScalar
uxos_misses = _Uxos_misses_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 5),
    _Uxos_misses_Type()
)
uxos_misses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_misses.setStatus("mandatory")
_Uxos_enters_Type = Counter32
_Uxos_enters_Object = MibScalar
uxos_enters = _Uxos_enters_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 6),
    _Uxos_enters_Type()
)
uxos_enters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_enters.setStatus("mandatory")
_Uxos_dblEnters_Type = Counter32
_Uxos_dblEnters_Object = MibScalar
uxos_dblEnters = _Uxos_dblEnters_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 7),
    _Uxos_dblEnters_Type()
)
uxos_dblEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_dblEnters.setStatus("mandatory")
_Uxos_longEnter_Type = Counter32
_Uxos_longEnter_Object = MibScalar
uxos_longEnter = _Uxos_longEnter_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 8),
    _Uxos_longEnter_Type()
)
uxos_longEnter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_longEnter.setStatus("mandatory")
_Uxos_longLook_Type = Counter32
_Uxos_longLook_Object = MibScalar
uxos_longLook = _Uxos_longLook_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 9),
    _Uxos_longLook_Type()
)
uxos_longLook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_longLook.setStatus("mandatory")
_Uxos_lruEmpty_Type = Counter32
_Uxos_lruEmpty_Object = MibScalar
uxos_lruEmpty = _Uxos_lruEmpty_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 10),
    _Uxos_lruEmpty_Type()
)
uxos_lruEmpty.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_lruEmpty.setStatus("mandatory")
_Uxos_purges_Type = Counter32
_Uxos_purges_Object = MibScalar
uxos_purges = _Uxos_purges_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 26, 1, 1, 11),
    _Uxos_purges_Type()
)
uxos_purges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_purges.setStatus("mandatory")
_Uxos_buffercache_ObjectIdentity = ObjectIdentity
uxos_buffercache = _Uxos_buffercache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27)
)
_Uxos_buffercacheTable_Object = MibTable
uxos_buffercacheTable = _Uxos_buffercacheTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1)
)
if mibBuilder.loadTexts:
    uxos_buffercacheTable.setStatus("mandatory")
_Uxos_buffercacheEntry_Object = MibTableRow
uxos_buffercacheEntry = _Uxos_buffercacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1)
)
uxos_buffercacheEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-buffercacheSysName"),
    (0, "OLIVETTI-MIB", "uxos-buffercacheInstName"),
    (0, "OLIVETTI-MIB", "uxos-buffercacheSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_buffercacheEntry.setStatus("mandatory")


class _Uxos_buffercacheSysName_Type(DisplayString):
    """Custom type uxos_buffercacheSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_buffercacheSysName_Type.__name__ = "DisplayString"
_Uxos_buffercacheSysName_Object = MibScalar
uxos_buffercacheSysName = _Uxos_buffercacheSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 1),
    _Uxos_buffercacheSysName_Type()
)
uxos_buffercacheSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_buffercacheSysName.setStatus("mandatory")


class _Uxos_buffercacheInstName_Type(DisplayString):
    """Custom type uxos_buffercacheInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_buffercacheInstName_Type.__name__ = "DisplayString"
_Uxos_buffercacheInstName_Object = MibScalar
uxos_buffercacheInstName = _Uxos_buffercacheInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 2),
    _Uxos_buffercacheInstName_Type()
)
uxos_buffercacheInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_buffercacheInstName.setStatus("mandatory")


class _Uxos_buffercacheSubAddr_Type(DisplayString):
    """Custom type uxos_buffercacheSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_buffercacheSubAddr_Type.__name__ = "DisplayString"
_Uxos_buffercacheSubAddr_Object = MibScalar
uxos_buffercacheSubAddr = _Uxos_buffercacheSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 3),
    _Uxos_buffercacheSubAddr_Type()
)
uxos_buffercacheSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_buffercacheSubAddr.setStatus("mandatory")
_Uxos_cachehit_Type = Counter32
_Uxos_cachehit_Object = MibScalar
uxos_cachehit = _Uxos_cachehit_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 4),
    _Uxos_cachehit_Type()
)
uxos_cachehit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cachehit.setStatus("mandatory")
_Uxos_cachemiss_Type = Counter32
_Uxos_cachemiss_Object = MibScalar
uxos_cachemiss = _Uxos_cachemiss_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 5),
    _Uxos_cachemiss_Type()
)
uxos_cachemiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_cachemiss.setStatus("mandatory")
_Uxos_freehit_Type = Counter32
_Uxos_freehit_Object = MibScalar
uxos_freehit = _Uxos_freehit_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 6),
    _Uxos_freehit_Type()
)
uxos_freehit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_freehit.setStatus("mandatory")
_Uxos_freemiss_Type = Counter32
_Uxos_freemiss_Object = MibScalar
uxos_freemiss = _Uxos_freemiss_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 7),
    _Uxos_freemiss_Type()
)
uxos_freemiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_freemiss.setStatus("mandatory")
_Uxos_bbusy_Type = Counter32
_Uxos_bbusy_Object = MibScalar
uxos_bbusy = _Uxos_bbusy_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 8),
    _Uxos_bbusy_Type()
)
uxos_bbusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_bbusy.setStatus("mandatory")
_Uxos_pfreemiss_Type = Counter32
_Uxos_pfreemiss_Object = MibScalar
uxos_pfreemiss = _Uxos_pfreemiss_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 9),
    _Uxos_pfreemiss_Type()
)
uxos_pfreemiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pfreemiss.setStatus("mandatory")
_Uxos_prepfreemiss_Type = Counter32
_Uxos_prepfreemiss_Object = MibScalar
uxos_prepfreemiss = _Uxos_prepfreemiss_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 10),
    _Uxos_prepfreemiss_Type()
)
uxos_prepfreemiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_prepfreemiss.setStatus("mandatory")
_Uxos_spare_Type = Counter32
_Uxos_spare_Object = MibScalar
uxos_spare = _Uxos_spare_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 27, 1, 1, 11),
    _Uxos_spare_Type()
)
uxos_spare.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxos_spare.setStatus("mandatory")
_Uxos_aioinfo_ObjectIdentity = ObjectIdentity
uxos_aioinfo = _Uxos_aioinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28)
)
_Uxos_aioTable_Object = MibTable
uxos_aioTable = _Uxos_aioTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1)
)
if mibBuilder.loadTexts:
    uxos_aioTable.setStatus("mandatory")
_Uxos_aioEntry_Object = MibTableRow
uxos_aioEntry = _Uxos_aioEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1)
)
uxos_aioEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-aioSysName"),
    (0, "OLIVETTI-MIB", "uxos-aioInstName"),
    (0, "OLIVETTI-MIB", "uxos-aioSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_aioEntry.setStatus("mandatory")


class _Uxos_aioSysName_Type(DisplayString):
    """Custom type uxos_aioSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_aioSysName_Type.__name__ = "DisplayString"
_Uxos_aioSysName_Object = MibScalar
uxos_aioSysName = _Uxos_aioSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 1),
    _Uxos_aioSysName_Type()
)
uxos_aioSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aioSysName.setStatus("mandatory")


class _Uxos_aioInstName_Type(DisplayString):
    """Custom type uxos_aioInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_aioInstName_Type.__name__ = "DisplayString"
_Uxos_aioInstName_Object = MibScalar
uxos_aioInstName = _Uxos_aioInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 2),
    _Uxos_aioInstName_Type()
)
uxos_aioInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aioInstName.setStatus("mandatory")


class _Uxos_aioSubAddr_Type(DisplayString):
    """Custom type uxos_aioSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_aioSubAddr_Type.__name__ = "DisplayString"
_Uxos_aioSubAddr_Object = MibScalar
uxos_aioSubAddr = _Uxos_aioSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 3),
    _Uxos_aioSubAddr_Type()
)
uxos_aioSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aioSubAddr.setStatus("mandatory")
_Uxos_aioread_Type = Counter32
_Uxos_aioread_Object = MibScalar
uxos_aioread = _Uxos_aioread_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 4),
    _Uxos_aioread_Type()
)
uxos_aioread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aioread.setStatus("mandatory")
_Uxos_aiowrite_Type = Counter32
_Uxos_aiowrite_Object = MibScalar
uxos_aiowrite = _Uxos_aiowrite_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 5),
    _Uxos_aiowrite_Type()
)
uxos_aiowrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aiowrite.setStatus("mandatory")
_Uxos_aiolock_Type = Counter32
_Uxos_aiolock_Object = MibScalar
uxos_aiolock = _Uxos_aiolock_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 6),
    _Uxos_aiolock_Type()
)
uxos_aiolock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aiolock.setStatus("mandatory")
_Uxos_aiopoll_Type = Counter32
_Uxos_aiopoll_Object = MibScalar
uxos_aiopoll = _Uxos_aiopoll_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 7),
    _Uxos_aiopoll_Type()
)
uxos_aiopoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aiopoll.setStatus("mandatory")
_Uxos_aiohfbuf_Type = Counter32
_Uxos_aiohfbuf_Object = MibScalar
uxos_aiohfbuf = _Uxos_aiohfbuf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 8),
    _Uxos_aiohfbuf_Type()
)
uxos_aiohfbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aiohfbuf.setStatus("mandatory")
_Uxos_aiohab_Type = Counter32
_Uxos_aiohab_Object = MibScalar
uxos_aiohab = _Uxos_aiohab_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 9),
    _Uxos_aiohab_Type()
)
uxos_aiohab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aiohab.setStatus("mandatory")
_Uxos_aiomsb_Type = Counter32
_Uxos_aiomsb_Object = MibScalar
uxos_aiomsb = _Uxos_aiomsb_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 28, 1, 1, 10),
    _Uxos_aiomsb_Type()
)
uxos_aiomsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_aiomsb.setStatus("mandatory")
_Uxos_lioinfo_ObjectIdentity = ObjectIdentity
uxos_lioinfo = _Uxos_lioinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29)
)
_Uxos_lioTable_Object = MibTable
uxos_lioTable = _Uxos_lioTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1)
)
if mibBuilder.loadTexts:
    uxos_lioTable.setStatus("mandatory")
_Uxos_lioEntry_Object = MibTableRow
uxos_lioEntry = _Uxos_lioEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1)
)
uxos_lioEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-lioSysName"),
    (0, "OLIVETTI-MIB", "uxos-lioInstName"),
    (0, "OLIVETTI-MIB", "uxos-lioSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_lioEntry.setStatus("mandatory")


class _Uxos_lioSysName_Type(DisplayString):
    """Custom type uxos_lioSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_lioSysName_Type.__name__ = "DisplayString"
_Uxos_lioSysName_Object = MibScalar
uxos_lioSysName = _Uxos_lioSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 1),
    _Uxos_lioSysName_Type()
)
uxos_lioSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lioSysName.setStatus("mandatory")


class _Uxos_lioInstName_Type(DisplayString):
    """Custom type uxos_lioInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_lioInstName_Type.__name__ = "DisplayString"
_Uxos_lioInstName_Object = MibScalar
uxos_lioInstName = _Uxos_lioInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 2),
    _Uxos_lioInstName_Type()
)
uxos_lioInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lioInstName.setStatus("mandatory")


class _Uxos_lioSubAddr_Type(DisplayString):
    """Custom type uxos_lioSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_lioSubAddr_Type.__name__ = "DisplayString"
_Uxos_lioSubAddr_Object = MibScalar
uxos_lioSubAddr = _Uxos_lioSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 3),
    _Uxos_lioSubAddr_Type()
)
uxos_lioSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lioSubAddr.setStatus("mandatory")
_Uxos_liocall_Type = Counter32
_Uxos_liocall_Object = MibScalar
uxos_liocall = _Uxos_liocall_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 4),
    _Uxos_liocall_Type()
)
uxos_liocall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_liocall.setStatus("mandatory")
_Uxos_lioread_Type = Counter32
_Uxos_lioread_Object = MibScalar
uxos_lioread = _Uxos_lioread_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 5),
    _Uxos_lioread_Type()
)
uxos_lioread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lioread.setStatus("mandatory")
_Uxos_liowrite_Type = Counter32
_Uxos_liowrite_Object = MibScalar
uxos_liowrite = _Uxos_liowrite_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 6),
    _Uxos_liowrite_Type()
)
uxos_liowrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_liowrite.setStatus("mandatory")
_Uxos_liolock_Type = Counter32
_Uxos_liolock_Object = MibScalar
uxos_liolock = _Uxos_liolock_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 7),
    _Uxos_liolock_Type()
)
uxos_liolock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_liolock.setStatus("mandatory")
_Uxos_liopoll_Type = Counter32
_Uxos_liopoll_Object = MibScalar
uxos_liopoll = _Uxos_liopoll_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 8),
    _Uxos_liopoll_Type()
)
uxos_liopoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_liopoll.setStatus("mandatory")
_Uxos_liowait_Type = Counter32
_Uxos_liowait_Object = MibScalar
uxos_liowait = _Uxos_liowait_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 29, 1, 1, 9),
    _Uxos_liowait_Type()
)
uxos_liowait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_liowait.setStatus("mandatory")
_Uxos_ipcinfo_ObjectIdentity = ObjectIdentity
uxos_ipcinfo = _Uxos_ipcinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30)
)
_Uxos_ipcTable_Object = MibTable
uxos_ipcTable = _Uxos_ipcTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1)
)
if mibBuilder.loadTexts:
    uxos_ipcTable.setStatus("mandatory")
_Uxos_ipcEntry_Object = MibTableRow
uxos_ipcEntry = _Uxos_ipcEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1)
)
uxos_ipcEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-ipcSysName"),
    (0, "OLIVETTI-MIB", "uxos-ipcInstName"),
    (0, "OLIVETTI-MIB", "uxos-ipcSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_ipcEntry.setStatus("mandatory")


class _Uxos_ipcSysName_Type(DisplayString):
    """Custom type uxos_ipcSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_ipcSysName_Type.__name__ = "DisplayString"
_Uxos_ipcSysName_Object = MibScalar
uxos_ipcSysName = _Uxos_ipcSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 1),
    _Uxos_ipcSysName_Type()
)
uxos_ipcSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ipcSysName.setStatus("mandatory")


class _Uxos_ipcInstName_Type(DisplayString):
    """Custom type uxos_ipcInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_ipcInstName_Type.__name__ = "DisplayString"
_Uxos_ipcInstName_Object = MibScalar
uxos_ipcInstName = _Uxos_ipcInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 2),
    _Uxos_ipcInstName_Type()
)
uxos_ipcInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ipcInstName.setStatus("mandatory")


class _Uxos_ipcSubAddr_Type(DisplayString):
    """Custom type uxos_ipcSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_ipcSubAddr_Type.__name__ = "DisplayString"
_Uxos_ipcSubAddr_Object = MibScalar
uxos_ipcSubAddr = _Uxos_ipcSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 3),
    _Uxos_ipcSubAddr_Type()
)
uxos_ipcSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_ipcSubAddr.setStatus("mandatory")
_Uxos_shm_get_Type = Counter32
_Uxos_shm_get_Object = MibScalar
uxos_shm_get = _Uxos_shm_get_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 4),
    _Uxos_shm_get_Type()
)
uxos_shm_get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shm_get.setStatus("mandatory")
_Uxos_shm_get_fail_Type = Counter32
_Uxos_shm_get_fail_Object = MibScalar
uxos_shm_get_fail = _Uxos_shm_get_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 5),
    _Uxos_shm_get_fail_Type()
)
uxos_shm_get_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shm_get_fail.setStatus("mandatory")
_Uxos_shm_atch_Type = Counter32
_Uxos_shm_atch_Object = MibScalar
uxos_shm_atch = _Uxos_shm_atch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 6),
    _Uxos_shm_atch_Type()
)
uxos_shm_atch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shm_atch.setStatus("mandatory")
_Uxos_shm_atch_fail_Type = Counter32
_Uxos_shm_atch_fail_Object = MibScalar
uxos_shm_atch_fail = _Uxos_shm_atch_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 7),
    _Uxos_shm_atch_fail_Type()
)
uxos_shm_atch_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shm_atch_fail.setStatus("mandatory")
_Uxos_shm_dtch_Type = Counter32
_Uxos_shm_dtch_Object = MibScalar
uxos_shm_dtch = _Uxos_shm_dtch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 8),
    _Uxos_shm_dtch_Type()
)
uxos_shm_dtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shm_dtch.setStatus("mandatory")
_Uxos_shm_cntl_Type = Counter32
_Uxos_shm_cntl_Object = MibScalar
uxos_shm_cntl = _Uxos_shm_cntl_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 9),
    _Uxos_shm_cntl_Type()
)
uxos_shm_cntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_shm_cntl.setStatus("mandatory")
_Uxos_msg_get_Type = Counter32
_Uxos_msg_get_Object = MibScalar
uxos_msg_get = _Uxos_msg_get_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 10),
    _Uxos_msg_get_Type()
)
uxos_msg_get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_get.setStatus("mandatory")
_Uxos_msg_get_fail_Type = Counter32
_Uxos_msg_get_fail_Object = MibScalar
uxos_msg_get_fail = _Uxos_msg_get_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 11),
    _Uxos_msg_get_fail_Type()
)
uxos_msg_get_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_get_fail.setStatus("mandatory")
_Uxos_msg_snd_Type = Counter32
_Uxos_msg_snd_Object = MibScalar
uxos_msg_snd = _Uxos_msg_snd_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 12),
    _Uxos_msg_snd_Type()
)
uxos_msg_snd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_snd.setStatus("mandatory")
_Uxos_msg_snd_fail_Type = Counter32
_Uxos_msg_snd_fail_Object = MibScalar
uxos_msg_snd_fail = _Uxos_msg_snd_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 13),
    _Uxos_msg_snd_fail_Type()
)
uxos_msg_snd_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_snd_fail.setStatus("mandatory")
_Uxos_msg_snd_sleep_Type = Counter32
_Uxos_msg_snd_sleep_Object = MibScalar
uxos_msg_snd_sleep = _Uxos_msg_snd_sleep_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 14),
    _Uxos_msg_snd_sleep_Type()
)
uxos_msg_snd_sleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_snd_sleep.setStatus("mandatory")
_Uxos_msg_snd_intr_Type = Counter32
_Uxos_msg_snd_intr_Object = MibScalar
uxos_msg_snd_intr = _Uxos_msg_snd_intr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 15),
    _Uxos_msg_snd_intr_Type()
)
uxos_msg_snd_intr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_snd_intr.setStatus("mandatory")
_Uxos_msg_snd_again_Type = Counter32
_Uxos_msg_snd_again_Object = MibScalar
uxos_msg_snd_again = _Uxos_msg_snd_again_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 16),
    _Uxos_msg_snd_again_Type()
)
uxos_msg_snd_again.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_snd_again.setStatus("mandatory")
_Uxos_msg_rcv_Type = Counter32
_Uxos_msg_rcv_Object = MibScalar
uxos_msg_rcv = _Uxos_msg_rcv_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 17),
    _Uxos_msg_rcv_Type()
)
uxos_msg_rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_rcv.setStatus("mandatory")
_Uxos_msg_rcv_fail_Type = Counter32
_Uxos_msg_rcv_fail_Object = MibScalar
uxos_msg_rcv_fail = _Uxos_msg_rcv_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 18),
    _Uxos_msg_rcv_fail_Type()
)
uxos_msg_rcv_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_rcv_fail.setStatus("mandatory")
_Uxos_msg_rcv_sleep_Type = Counter32
_Uxos_msg_rcv_sleep_Object = MibScalar
uxos_msg_rcv_sleep = _Uxos_msg_rcv_sleep_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 19),
    _Uxos_msg_rcv_sleep_Type()
)
uxos_msg_rcv_sleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_rcv_sleep.setStatus("mandatory")
_Uxos_msg_rcv_intr_Type = Counter32
_Uxos_msg_rcv_intr_Object = MibScalar
uxos_msg_rcv_intr = _Uxos_msg_rcv_intr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 20),
    _Uxos_msg_rcv_intr_Type()
)
uxos_msg_rcv_intr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_rcv_intr.setStatus("mandatory")
_Uxos_msg_rcv_again_Type = Counter32
_Uxos_msg_rcv_again_Object = MibScalar
uxos_msg_rcv_again = _Uxos_msg_rcv_again_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 21),
    _Uxos_msg_rcv_again_Type()
)
uxos_msg_rcv_again.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_rcv_again.setStatus("mandatory")
_Uxos_msg_cntl_Type = Counter32
_Uxos_msg_cntl_Object = MibScalar
uxos_msg_cntl = _Uxos_msg_cntl_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 22),
    _Uxos_msg_cntl_Type()
)
uxos_msg_cntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_cntl.setStatus("mandatory")
_Uxos_msg_lock_sleep_Type = Counter32
_Uxos_msg_lock_sleep_Object = MibScalar
uxos_msg_lock_sleep = _Uxos_msg_lock_sleep_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 23),
    _Uxos_msg_lock_sleep_Type()
)
uxos_msg_lock_sleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_msg_lock_sleep.setStatus("mandatory")
_Uxos_sem_get_Type = Counter32
_Uxos_sem_get_Object = MibScalar
uxos_sem_get = _Uxos_sem_get_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 24),
    _Uxos_sem_get_Type()
)
uxos_sem_get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_get.setStatus("mandatory")
_Uxos_sem_get_fail_Type = Counter32
_Uxos_sem_get_fail_Object = MibScalar
uxos_sem_get_fail = _Uxos_sem_get_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 25),
    _Uxos_sem_get_fail_Type()
)
uxos_sem_get_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_get_fail.setStatus("mandatory")
_Uxos_sem_op_Type = Counter32
_Uxos_sem_op_Object = MibScalar
uxos_sem_op = _Uxos_sem_op_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 26),
    _Uxos_sem_op_Type()
)
uxos_sem_op.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_op.setStatus("mandatory")
_Uxos_sem_op_fail_Type = Counter32
_Uxos_sem_op_fail_Object = MibScalar
uxos_sem_op_fail = _Uxos_sem_op_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 27),
    _Uxos_sem_op_fail_Type()
)
uxos_sem_op_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_op_fail.setStatus("mandatory")
_Uxos_sem_op_sleep_Type = Counter32
_Uxos_sem_op_sleep_Object = MibScalar
uxos_sem_op_sleep = _Uxos_sem_op_sleep_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 28),
    _Uxos_sem_op_sleep_Type()
)
uxos_sem_op_sleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_op_sleep.setStatus("mandatory")
_Uxos_sem_op_intr_Type = Counter32
_Uxos_sem_op_intr_Object = MibScalar
uxos_sem_op_intr = _Uxos_sem_op_intr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 29),
    _Uxos_sem_op_intr_Type()
)
uxos_sem_op_intr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_op_intr.setStatus("mandatory")
_Uxos_sem_op_again_Type = Counter32
_Uxos_sem_op_again_Object = MibScalar
uxos_sem_op_again = _Uxos_sem_op_again_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 30),
    _Uxos_sem_op_again_Type()
)
uxos_sem_op_again.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_op_again.setStatus("mandatory")
_Uxos_sem_cntl_Type = Counter32
_Uxos_sem_cntl_Object = MibScalar
uxos_sem_cntl = _Uxos_sem_cntl_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 30, 1, 1, 31),
    _Uxos_sem_cntl_Type()
)
uxos_sem_cntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_sem_cntl.setStatus("mandatory")
_Uxos_flockinfo_ObjectIdentity = ObjectIdentity
uxos_flockinfo = _Uxos_flockinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31)
)
_Uxos_flockTable_Object = MibTable
uxos_flockTable = _Uxos_flockTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1)
)
if mibBuilder.loadTexts:
    uxos_flockTable.setStatus("mandatory")
_Uxos_flockEntry_Object = MibTableRow
uxos_flockEntry = _Uxos_flockEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1)
)
uxos_flockEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-flockSysName"),
    (0, "OLIVETTI-MIB", "uxos-flockInstName"),
    (0, "OLIVETTI-MIB", "uxos-flockSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_flockEntry.setStatus("mandatory")


class _Uxos_flockSysName_Type(DisplayString):
    """Custom type uxos_flockSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_flockSysName_Type.__name__ = "DisplayString"
_Uxos_flockSysName_Object = MibScalar
uxos_flockSysName = _Uxos_flockSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 1),
    _Uxos_flockSysName_Type()
)
uxos_flockSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_flockSysName.setStatus("mandatory")


class _Uxos_flockInstName_Type(DisplayString):
    """Custom type uxos_flockInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_flockInstName_Type.__name__ = "DisplayString"
_Uxos_flockInstName_Object = MibScalar
uxos_flockInstName = _Uxos_flockInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 2),
    _Uxos_flockInstName_Type()
)
uxos_flockInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_flockInstName.setStatus("mandatory")


class _Uxos_flockSubAddr_Type(DisplayString):
    """Custom type uxos_flockSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_flockSubAddr_Type.__name__ = "DisplayString"
_Uxos_flockSubAddr_Object = MibScalar
uxos_flockSubAddr = _Uxos_flockSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 3),
    _Uxos_flockSubAddr_Type()
)
uxos_flockSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_flockSubAddr.setStatus("mandatory")
_Uxos_lock_read_Type = Counter32
_Uxos_lock_read_Object = MibScalar
uxos_lock_read = _Uxos_lock_read_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 4),
    _Uxos_lock_read_Type()
)
uxos_lock_read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_read.setStatus("mandatory")
_Uxos_lock_rd_fail_Type = Counter32
_Uxos_lock_rd_fail_Object = MibScalar
uxos_lock_rd_fail = _Uxos_lock_rd_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 5),
    _Uxos_lock_rd_fail_Type()
)
uxos_lock_rd_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_rd_fail.setStatus("mandatory")
_Uxos_lock_rd_sleep_Type = Counter32
_Uxos_lock_rd_sleep_Object = MibScalar
uxos_lock_rd_sleep = _Uxos_lock_rd_sleep_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 6),
    _Uxos_lock_rd_sleep_Type()
)
uxos_lock_rd_sleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_rd_sleep.setStatus("mandatory")
_Uxos_lock_rd_intr_Type = Counter32
_Uxos_lock_rd_intr_Object = MibScalar
uxos_lock_rd_intr = _Uxos_lock_rd_intr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 7),
    _Uxos_lock_rd_intr_Type()
)
uxos_lock_rd_intr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_rd_intr.setStatus("mandatory")
_Uxos_lock_rd_again_Type = Counter32
_Uxos_lock_rd_again_Object = MibScalar
uxos_lock_rd_again = _Uxos_lock_rd_again_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 8),
    _Uxos_lock_rd_again_Type()
)
uxos_lock_rd_again.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_rd_again.setStatus("mandatory")
_Uxos_lock_write_Type = Counter32
_Uxos_lock_write_Object = MibScalar
uxos_lock_write = _Uxos_lock_write_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 9),
    _Uxos_lock_write_Type()
)
uxos_lock_write.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_write.setStatus("mandatory")
_Uxos_lock_wr_fail_Type = Counter32
_Uxos_lock_wr_fail_Object = MibScalar
uxos_lock_wr_fail = _Uxos_lock_wr_fail_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 10),
    _Uxos_lock_wr_fail_Type()
)
uxos_lock_wr_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_wr_fail.setStatus("mandatory")
_Uxos_lock_wr_sleep_Type = Counter32
_Uxos_lock_wr_sleep_Object = MibScalar
uxos_lock_wr_sleep = _Uxos_lock_wr_sleep_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 11),
    _Uxos_lock_wr_sleep_Type()
)
uxos_lock_wr_sleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_wr_sleep.setStatus("mandatory")
_Uxos_lock_wr_intr_Type = Counter32
_Uxos_lock_wr_intr_Object = MibScalar
uxos_lock_wr_intr = _Uxos_lock_wr_intr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 12),
    _Uxos_lock_wr_intr_Type()
)
uxos_lock_wr_intr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_wr_intr.setStatus("mandatory")
_Uxos_lock_wr_again_Type = Counter32
_Uxos_lock_wr_again_Object = MibScalar
uxos_lock_wr_again = _Uxos_lock_wr_again_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 13),
    _Uxos_lock_wr_again_Type()
)
uxos_lock_wr_again.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_lock_wr_again.setStatus("mandatory")
_Uxos_unlock_Type = Counter32
_Uxos_unlock_Object = MibScalar
uxos_unlock = _Uxos_unlock_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 31, 1, 1, 14),
    _Uxos_unlock_Type()
)
uxos_unlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_unlock.setStatus("mandatory")
_Uxos_segminfo_ObjectIdentity = ObjectIdentity
uxos_segminfo = _Uxos_segminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32)
)
_Uxos_smTable_Object = MibTable
uxos_smTable = _Uxos_smTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1)
)
if mibBuilder.loadTexts:
    uxos_smTable.setStatus("mandatory")
_Uxos_smEntry_Object = MibTableRow
uxos_smEntry = _Uxos_smEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1)
)
uxos_smEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-smSysName"),
    (0, "OLIVETTI-MIB", "uxos-smInstName"),
    (0, "OLIVETTI-MIB", "uxos-smSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_smEntry.setStatus("mandatory")


class _Uxos_smSysName_Type(DisplayString):
    """Custom type uxos_smSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_smSysName_Type.__name__ = "DisplayString"
_Uxos_smSysName_Object = MibScalar
uxos_smSysName = _Uxos_smSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 1),
    _Uxos_smSysName_Type()
)
uxos_smSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smSysName.setStatus("mandatory")


class _Uxos_smInstName_Type(DisplayString):
    """Custom type uxos_smInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_smInstName_Type.__name__ = "DisplayString"
_Uxos_smInstName_Object = MibScalar
uxos_smInstName = _Uxos_smInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 2),
    _Uxos_smInstName_Type()
)
uxos_smInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smInstName.setStatus("mandatory")


class _Uxos_smSubAddr_Type(DisplayString):
    """Custom type uxos_smSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_smSubAddr_Type.__name__ = "DisplayString"
_Uxos_smSubAddr_Object = MibScalar
uxos_smSubAddr = _Uxos_smSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 3),
    _Uxos_smSubAddr_Type()
)
uxos_smSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_smSubAddr.setStatus("mandatory")
_Uxos_fault_Type = Counter32
_Uxos_fault_Object = MibScalar
uxos_fault = _Uxos_fault_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 4),
    _Uxos_fault_Type()
)
uxos_fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_fault.setStatus("mandatory")
_Uxos_faulta_Type = Counter32
_Uxos_faulta_Object = MibScalar
uxos_faulta = _Uxos_faulta_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 5),
    _Uxos_faulta_Type()
)
uxos_faulta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_faulta.setStatus("mandatory")
_Uxos_getmap_Type = Counter32
_Uxos_getmap_Object = MibScalar
uxos_getmap = _Uxos_getmap_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 6),
    _Uxos_getmap_Type()
)
uxos_getmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_getmap.setStatus("mandatory")
_Uxos_get_use_Type = Counter32
_Uxos_get_use_Object = MibScalar
uxos_get_use = _Uxos_get_use_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 7),
    _Uxos_get_use_Type()
)
uxos_get_use.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_get_use.setStatus("mandatory")
_Uxos_get_reclaim_Type = Counter32
_Uxos_get_reclaim_Object = MibScalar
uxos_get_reclaim = _Uxos_get_reclaim_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 8),
    _Uxos_get_reclaim_Type()
)
uxos_get_reclaim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_get_reclaim.setStatus("mandatory")
_Uxos_get_reuse_Type = Counter32
_Uxos_get_reuse_Object = MibScalar
uxos_get_reuse = _Uxos_get_reuse_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 9),
    _Uxos_get_reuse_Type()
)
uxos_get_reuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_get_reuse.setStatus("mandatory")
_Uxos_rel_async_Type = Counter32
_Uxos_rel_async_Object = MibScalar
uxos_rel_async = _Uxos_rel_async_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 10),
    _Uxos_rel_async_Type()
)
uxos_rel_async.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rel_async.setStatus("mandatory")
_Uxos_rel_write_Type = Counter32
_Uxos_rel_write_Object = MibScalar
uxos_rel_write = _Uxos_rel_write_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 11),
    _Uxos_rel_write_Type()
)
uxos_rel_write.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rel_write.setStatus("mandatory")
_Uxos_rel_free_Type = Counter32
_Uxos_rel_free_Object = MibScalar
uxos_rel_free = _Uxos_rel_free_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 12),
    _Uxos_rel_free_Type()
)
uxos_rel_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rel_free.setStatus("mandatory")
_Uxos_rel_abort_Type = Counter32
_Uxos_rel_abort_Object = MibScalar
uxos_rel_abort = _Uxos_rel_abort_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 13),
    _Uxos_rel_abort_Type()
)
uxos_rel_abort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rel_abort.setStatus("mandatory")
_Uxos_rel_dontneed_Type = Counter32
_Uxos_rel_dontneed_Object = MibScalar
uxos_rel_dontneed = _Uxos_rel_dontneed_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 14),
    _Uxos_rel_dontneed_Type()
)
uxos_rel_dontneed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_rel_dontneed.setStatus("mandatory")
_Uxos_release_Type = Counter32
_Uxos_release_Object = MibScalar
uxos_release = _Uxos_release_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 15),
    _Uxos_release_Type()
)
uxos_release.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_release.setStatus("mandatory")
_Uxos_pagecreate_Type = Counter32
_Uxos_pagecreate_Object = MibScalar
uxos_pagecreate = _Uxos_pagecreate_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 16),
    _Uxos_pagecreate_Type()
)
uxos_pagecreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pagecreate.setStatus("mandatory")
_Uxos_pagemiss_Type = Counter32
_Uxos_pagemiss_Object = MibScalar
uxos_pagemiss = _Uxos_pagemiss_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 17),
    _Uxos_pagemiss_Type()
)
uxos_pagemiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pagemiss.setStatus("mandatory")
_Uxos_pagemissatch_Type = Counter32
_Uxos_pagemissatch_Object = MibScalar
uxos_pagemissatch = _Uxos_pagemissatch_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 32, 1, 1, 18),
    _Uxos_pagemissatch_Type()
)
uxos_pagemissatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_pagemissatch.setStatus("mandatory")
_Uxos_vxinfo_ObjectIdentity = ObjectIdentity
uxos_vxinfo = _Uxos_vxinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33)
)
_Uxos_vxTable_Object = MibTable
uxos_vxTable = _Uxos_vxTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1)
)
if mibBuilder.loadTexts:
    uxos_vxTable.setStatus("mandatory")
_Uxos_vxEntry_Object = MibTableRow
uxos_vxEntry = _Uxos_vxEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1, 1)
)
uxos_vxEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "uxos-vxSysName"),
    (0, "OLIVETTI-MIB", "uxos-vxInstName"),
    (0, "OLIVETTI-MIB", "uxos-vxSubAddr"),
)
if mibBuilder.loadTexts:
    uxos_vxEntry.setStatus("mandatory")


class _Uxos_vxSysName_Type(DisplayString):
    """Custom type uxos_vxSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vxSysName_Type.__name__ = "DisplayString"
_Uxos_vxSysName_Object = MibScalar
uxos_vxSysName = _Uxos_vxSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1, 1, 1),
    _Uxos_vxSysName_Type()
)
uxos_vxSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vxSysName.setStatus("mandatory")


class _Uxos_vxInstName_Type(DisplayString):
    """Custom type uxos_vxInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vxInstName_Type.__name__ = "DisplayString"
_Uxos_vxInstName_Object = MibScalar
uxos_vxInstName = _Uxos_vxInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1, 1, 2),
    _Uxos_vxInstName_Type()
)
uxos_vxInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vxInstName.setStatus("mandatory")


class _Uxos_vxSubAddr_Type(DisplayString):
    """Custom type uxos_vxSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Uxos_vxSubAddr_Type.__name__ = "DisplayString"
_Uxos_vxSubAddr_Object = MibScalar
uxos_vxSubAddr = _Uxos_vxSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1, 1, 3),
    _Uxos_vxSubAddr_Type()
)
uxos_vxSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vxSubAddr.setStatus("mandatory")
_Uxos_vxipage_Type = Counter32
_Uxos_vxipage_Object = MibScalar
uxos_vxipage = _Uxos_vxipage_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1, 1, 4),
    _Uxos_vxipage_Type()
)
uxos_vxipage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vxipage.setStatus("mandatory")
_Uxos_vxinopage_Type = Counter32
_Uxos_vxinopage_Object = MibScalar
uxos_vxinopage = _Uxos_vxinopage_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1, 1, 5),
    _Uxos_vxinopage_Type()
)
uxos_vxinopage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vxinopage.setStatus("mandatory")
_Uxos_vxinodeovf_Type = Counter32
_Uxos_vxinodeovf_Object = MibScalar
uxos_vxinodeovf = _Uxos_vxinodeovf_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 6, 77, 33, 1, 1, 6),
    _Uxos_vxinodeovf_Type()
)
uxos_vxinodeovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxos_vxinodeovf.setStatus("mandatory")
_Pc_win_ObjectIdentity = ObjectIdentity
pc_win = _Pc_win_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 7)
)
_Winlms_systemrm_ObjectIdentity = ObjectIdentity
winlms_systemrm = _Winlms_systemrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 7)
)
_Winlms_system_ObjectIdentity = ObjectIdentity
winlms_system = _Winlms_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 7, 0)
)
_Winlms_systemrmTable_Object = MibTable
winlms_systemrmTable = _Winlms_systemrmTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 7, 0, 1)
)
if mibBuilder.loadTexts:
    winlms_systemrmTable.setStatus("mandatory")
_Winlms_systemrmEntry_Object = MibTableRow
winlms_systemrmEntry = _Winlms_systemrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 7, 0, 1, 1)
)
winlms_systemrmEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "winlms-systemrmSysName"),
    (0, "OLIVETTI-MIB", "winlms-systemrmInstName"),
    (0, "OLIVETTI-MIB", "winlms-systemrmSubAddr"),
)
if mibBuilder.loadTexts:
    winlms_systemrmEntry.setStatus("mandatory")


class _Winlms_systemrmSysName_Type(DisplayString):
    """Custom type winlms_systemrmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Winlms_systemrmSysName_Type.__name__ = "DisplayString"
_Winlms_systemrmSysName_Object = MibScalar
winlms_systemrmSysName = _Winlms_systemrmSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 7, 0, 1, 1, 1),
    _Winlms_systemrmSysName_Type()
)
winlms_systemrmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlms_systemrmSysName.setStatus("mandatory")


class _Winlms_systemrmInstName_Type(DisplayString):
    """Custom type winlms_systemrmInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Winlms_systemrmInstName_Type.__name__ = "DisplayString"
_Winlms_systemrmInstName_Object = MibScalar
winlms_systemrmInstName = _Winlms_systemrmInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 7, 0, 1, 1, 2),
    _Winlms_systemrmInstName_Type()
)
winlms_systemrmInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlms_systemrmInstName.setStatus("mandatory")


class _Winlms_systemrmSubAddr_Type(DisplayString):
    """Custom type winlms_systemrmSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Winlms_systemrmSubAddr_Type.__name__ = "DisplayString"
_Winlms_systemrmSubAddr_Object = MibScalar
winlms_systemrmSubAddr = _Winlms_systemrmSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 7, 0, 1, 1, 3),
    _Winlms_systemrmSubAddr_Type()
)
winlms_systemrmSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlms_systemrmSubAddr.setStatus("mandatory")
_Winlms_nms_ObjectIdentity = ObjectIdentity
winlms_nms = _Winlms_nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 12)
)
_Winlms_sdrm_ObjectIdentity = ObjectIdentity
winlms_sdrm = _Winlms_sdrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 12, 2)
)
_Winlms_sdrmTable_Object = MibTable
winlms_sdrmTable = _Winlms_sdrmTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 12, 2, 1)
)
if mibBuilder.loadTexts:
    winlms_sdrmTable.setStatus("mandatory")
_Winlms_sdrmEntry_Object = MibTableRow
winlms_sdrmEntry = _Winlms_sdrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 12, 2, 1, 1)
)
winlms_sdrmEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "winlms-sdrmSysName"),
    (0, "OLIVETTI-MIB", "winlms-sdrmInstName"),
    (0, "OLIVETTI-MIB", "winlms-sdrmSubAddr"),
)
if mibBuilder.loadTexts:
    winlms_sdrmEntry.setStatus("mandatory")


class _Winlms_sdrmSysName_Type(DisplayString):
    """Custom type winlms_sdrmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Winlms_sdrmSysName_Type.__name__ = "DisplayString"
_Winlms_sdrmSysName_Object = MibScalar
winlms_sdrmSysName = _Winlms_sdrmSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 12, 2, 1, 1, 1),
    _Winlms_sdrmSysName_Type()
)
winlms_sdrmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlms_sdrmSysName.setStatus("mandatory")


class _Winlms_sdrmInstName_Type(DisplayString):
    """Custom type winlms_sdrmInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Winlms_sdrmInstName_Type.__name__ = "DisplayString"
_Winlms_sdrmInstName_Object = MibScalar
winlms_sdrmInstName = _Winlms_sdrmInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 12, 2, 1, 1, 2),
    _Winlms_sdrmInstName_Type()
)
winlms_sdrmInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlms_sdrmInstName.setStatus("mandatory")


class _Winlms_sdrmSubAddr_Type(DisplayString):
    """Custom type winlms_sdrmSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Winlms_sdrmSubAddr_Type.__name__ = "DisplayString"
_Winlms_sdrmSubAddr_Object = MibScalar
winlms_sdrmSubAddr = _Winlms_sdrmSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 7, 12, 2, 1, 1, 3),
    _Winlms_sdrmSubAddr_Type()
)
winlms_sdrmSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlms_sdrmSubAddr.setStatus("mandatory")
_Win_nt_ObjectIdentity = ObjectIdentity
win_nt = _Win_nt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 8)
)
_Ntlms_systemrm_ObjectIdentity = ObjectIdentity
ntlms_systemrm = _Ntlms_systemrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 7)
)
_Ntlms_system_ObjectIdentity = ObjectIdentity
ntlms_system = _Ntlms_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 7, 0)
)
_Ntlms_systemrmTable_Object = MibTable
ntlms_systemrmTable = _Ntlms_systemrmTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 7, 0, 1)
)
if mibBuilder.loadTexts:
    ntlms_systemrmTable.setStatus("mandatory")
_Ntlms_systemrmEntry_Object = MibTableRow
ntlms_systemrmEntry = _Ntlms_systemrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 7, 0, 1, 1)
)
ntlms_systemrmEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "ntlms-systemrmSysName"),
    (0, "OLIVETTI-MIB", "ntlms-systemrmInstName"),
    (0, "OLIVETTI-MIB", "ntlms-systemrmSubAddr"),
)
if mibBuilder.loadTexts:
    ntlms_systemrmEntry.setStatus("mandatory")


class _Ntlms_systemrmSysName_Type(DisplayString):
    """Custom type ntlms_systemrmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ntlms_systemrmSysName_Type.__name__ = "DisplayString"
_Ntlms_systemrmSysName_Object = MibScalar
ntlms_systemrmSysName = _Ntlms_systemrmSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 7, 0, 1, 1, 1),
    _Ntlms_systemrmSysName_Type()
)
ntlms_systemrmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntlms_systemrmSysName.setStatus("mandatory")


class _Ntlms_systemrmInstName_Type(DisplayString):
    """Custom type ntlms_systemrmInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Ntlms_systemrmInstName_Type.__name__ = "DisplayString"
_Ntlms_systemrmInstName_Object = MibScalar
ntlms_systemrmInstName = _Ntlms_systemrmInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 7, 0, 1, 1, 2),
    _Ntlms_systemrmInstName_Type()
)
ntlms_systemrmInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntlms_systemrmInstName.setStatus("mandatory")


class _Ntlms_systemrmSubAddr_Type(DisplayString):
    """Custom type ntlms_systemrmSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ntlms_systemrmSubAddr_Type.__name__ = "DisplayString"
_Ntlms_systemrmSubAddr_Object = MibScalar
ntlms_systemrmSubAddr = _Ntlms_systemrmSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 7, 0, 1, 1, 3),
    _Ntlms_systemrmSubAddr_Type()
)
ntlms_systemrmSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntlms_systemrmSubAddr.setStatus("mandatory")
_Ntlms_nms_ObjectIdentity = ObjectIdentity
ntlms_nms = _Ntlms_nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 12)
)
_Ntlms_sdrm_ObjectIdentity = ObjectIdentity
ntlms_sdrm = _Ntlms_sdrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 12, 2)
)
_Ntlms_sdrmTable_Object = MibTable
ntlms_sdrmTable = _Ntlms_sdrmTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ntlms_sdrmTable.setStatus("mandatory")
_Ntlms_sdrmEntry_Object = MibTableRow
ntlms_sdrmEntry = _Ntlms_sdrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 12, 2, 1, 1)
)
ntlms_sdrmEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "ntlms-sdrmSysName"),
    (0, "OLIVETTI-MIB", "ntlms-sdrmInstName"),
    (0, "OLIVETTI-MIB", "ntlms-sdrmSubAddr"),
)
if mibBuilder.loadTexts:
    ntlms_sdrmEntry.setStatus("mandatory")


class _Ntlms_sdrmSysName_Type(DisplayString):
    """Custom type ntlms_sdrmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ntlms_sdrmSysName_Type.__name__ = "DisplayString"
_Ntlms_sdrmSysName_Object = MibScalar
ntlms_sdrmSysName = _Ntlms_sdrmSysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 12, 2, 1, 1, 1),
    _Ntlms_sdrmSysName_Type()
)
ntlms_sdrmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntlms_sdrmSysName.setStatus("mandatory")


class _Ntlms_sdrmInstName_Type(DisplayString):
    """Custom type ntlms_sdrmInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Ntlms_sdrmInstName_Type.__name__ = "DisplayString"
_Ntlms_sdrmInstName_Object = MibScalar
ntlms_sdrmInstName = _Ntlms_sdrmInstName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 12, 2, 1, 1, 2),
    _Ntlms_sdrmInstName_Type()
)
ntlms_sdrmInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntlms_sdrmInstName.setStatus("mandatory")


class _Ntlms_sdrmSubAddr_Type(DisplayString):
    """Custom type ntlms_sdrmSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ntlms_sdrmSubAddr_Type.__name__ = "DisplayString"
_Ntlms_sdrmSubAddr_Object = MibScalar
ntlms_sdrmSubAddr = _Ntlms_sdrmSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 8, 12, 2, 1, 1, 3),
    _Ntlms_sdrmSubAddr_Type()
)
ntlms_sdrmSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntlms_sdrmSubAddr.setStatus("mandatory")
_Pc_dos_ObjectIdentity = ObjectIdentity
pc_dos = _Pc_dos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 9)
)
_Lms_sys_map_ObjectIdentity = ObjectIdentity
lms_sys_map = _Lms_sys_map_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 2, 9999)
)
_LmssysmapTable_Object = MibTable
lmssysmapTable = _LmssysmapTable_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 9999, 1)
)
if mibBuilder.loadTexts:
    lmssysmapTable.setStatus("mandatory")
_LmssysmapEntry_Object = MibTableRow
lmssysmapEntry = _LmssysmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 9999, 1, 1)
)
lmssysmapEntry.setIndexNames(
    (0, "OLIVETTI-MIB", "lmsSystemName"),
)
if mibBuilder.loadTexts:
    lmssysmapEntry.setStatus("mandatory")


class _LmsSystemName_Type(DisplayString):
    """Custom type lmsSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LmsSystemName_Type.__name__ = "DisplayString"
_LmsSystemName_Object = MibTableColumn
lmsSystemName = _LmsSystemName_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 9999, 1, 1, 1),
    _LmsSystemName_Type()
)
lmsSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSystemName.setStatus("mandatory")


class _LmsSystemStatus_Type(DisplayString):
    """Custom type lmsSystemStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_LmsSystemStatus_Type.__name__ = "DisplayString"
_LmsSystemStatus_Object = MibTableColumn
lmsSystemStatus = _LmsSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 9999, 1, 1, 2),
    _LmsSystemStatus_Type()
)
lmsSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSystemStatus.setStatus("mandatory")


class _LmsSystemType_Type(DisplayString):
    """Custom type lmsSystemType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LmsSystemType_Type.__name__ = "DisplayString"
_LmsSystemType_Object = MibTableColumn
lmsSystemType = _LmsSystemType_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 9999, 1, 1, 3),
    _LmsSystemType_Type()
)
lmsSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSystemType.setStatus("mandatory")


class _LmsSystemClass_Type(DisplayString):
    """Custom type lmsSystemClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LmsSystemClass_Type.__name__ = "DisplayString"
_LmsSystemClass_Object = MibTableColumn
lmsSystemClass = _LmsSystemClass_Object(
    (1, 3, 6, 1, 4, 1, 279, 2, 9999, 1, 1, 4),
    _LmsSystemClass_Type()
)
lmsSystemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSystemClass.setStatus("mandatory")
_Lms_trap_ObjectIdentity = ObjectIdentity
lms_trap = _Lms_trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 279, 3)
)


class _Lms_SysName_Type(DisplayString):
    """Custom type lms_SysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Lms_SysName_Type.__name__ = "DisplayString"
_Lms_SysName_Object = MibScalar
lms_SysName = _Lms_SysName_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 1),
    _Lms_SysName_Type()
)
lms_SysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_SysName.setStatus("mandatory")


class _Lms_SubAddress_Type(DisplayString):
    """Custom type lms_SubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Lms_SubAddress_Type.__name__ = "DisplayString"
_Lms_SubAddress_Object = MibScalar
lms_SubAddress = _Lms_SubAddress_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 2),
    _Lms_SubAddress_Type()
)
lms_SubAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_SubAddress.setStatus("mandatory")


class _Lms_LogType_Type(DisplayString):
    """Custom type lms_LogType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Lms_LogType_Type.__name__ = "DisplayString"
_Lms_LogType_Object = MibScalar
lms_LogType = _Lms_LogType_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 3),
    _Lms_LogType_Type()
)
lms_LogType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_LogType.setStatus("mandatory")


class _Lms_FilterType_Type(DisplayString):
    """Custom type lms_FilterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Lms_FilterType_Type.__name__ = "DisplayString"
_Lms_FilterType_Object = MibScalar
lms_FilterType = _Lms_FilterType_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 4),
    _Lms_FilterType_Type()
)
lms_FilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_FilterType.setStatus("mandatory")


class _Lms_RecLevel_Type(DisplayString):
    """Custom type lms_RecLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Lms_RecLevel_Type.__name__ = "DisplayString"
_Lms_RecLevel_Object = MibScalar
lms_RecLevel = _Lms_RecLevel_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 5),
    _Lms_RecLevel_Type()
)
lms_RecLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_RecLevel.setStatus("mandatory")


class _Lms_RecCode_Type(DisplayString):
    """Custom type lms_RecCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Lms_RecCode_Type.__name__ = "DisplayString"
_Lms_RecCode_Object = MibScalar
lms_RecCode = _Lms_RecCode_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 6),
    _Lms_RecCode_Type()
)
lms_RecCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_RecCode.setStatus("mandatory")


class _Lms_ProductId_Type(DisplayString):
    """Custom type lms_ProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Lms_ProductId_Type.__name__ = "DisplayString"
_Lms_ProductId_Object = MibScalar
lms_ProductId = _Lms_ProductId_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 7),
    _Lms_ProductId_Type()
)
lms_ProductId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_ProductId.setStatus("mandatory")


class _Lms_Class_Type(DisplayString):
    """Custom type lms_Class based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Lms_Class_Type.__name__ = "DisplayString"
_Lms_Class_Object = MibScalar
lms_Class = _Lms_Class_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 8),
    _Lms_Class_Type()
)
lms_Class.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_Class.setStatus("mandatory")


class _Lms_SubClass_Type(DisplayString):
    """Custom type lms_SubClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Lms_SubClass_Type.__name__ = "DisplayString"
_Lms_SubClass_Object = MibScalar
lms_SubClass = _Lms_SubClass_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 9),
    _Lms_SubClass_Type()
)
lms_SubClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_SubClass.setStatus("mandatory")


class _Lms_ResourceName_Type(DisplayString):
    """Custom type lms_ResourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Lms_ResourceName_Type.__name__ = "DisplayString"
_Lms_ResourceName_Object = MibScalar
lms_ResourceName = _Lms_ResourceName_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 10),
    _Lms_ResourceName_Type()
)
lms_ResourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_ResourceName.setStatus("mandatory")


class _Lms_GenerationDate_Type(DisplayString):
    """Custom type lms_GenerationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_Lms_GenerationDate_Type.__name__ = "DisplayString"
_Lms_GenerationDate_Object = MibScalar
lms_GenerationDate = _Lms_GenerationDate_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 11),
    _Lms_GenerationDate_Type()
)
lms_GenerationDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_GenerationDate.setStatus("mandatory")


class _Lms_LogString_Type(DisplayString):
    """Custom type lms_LogString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5000),
    )


_Lms_LogString_Type.__name__ = "DisplayString"
_Lms_LogString_Object = MibScalar
lms_LogString = _Lms_LogString_Object(
    (1, 3, 6, 1, 4, 1, 279, 3, 12),
    _Lms_LogString_Type()
)
lms_LogString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lms_LogString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trap_lms = NotificationType(
    (1, 3, 6, 1, 4, 1, 279, 0, 138)
)
trap_lms.setObjects(
      *(("OLIVETTI-MIB", "lms_SysName"),
        ("OLIVETTI-MIB", "lms_SubAddress"),
        ("OLIVETTI-MIB", "lms_LogType"),
        ("OLIVETTI-MIB", "lms_FilterType"),
        ("OLIVETTI-MIB", "lms_RecLevel"),
        ("OLIVETTI-MIB", "lms_RecCode"),
        ("OLIVETTI-MIB", "lms_ProductId"),
        ("OLIVETTI-MIB", "lms_Class"),
        ("OLIVETTI-MIB", "lms_SubClass"),
        ("OLIVETTI-MIB", "lms_ResourceName"),
        ("OLIVETTI-MIB", "lms_GenerationDate"),
        ("OLIVETTI-MIB", "lms_LogString"))
)
if mibBuilder.loadTexts:
    trap_lms.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLIVETTI-MIB",
    **{"olivetti": olivetti,
       "trap-lms": trap_lms,
       "lms": lms,
       "pb-dos": pb_dos,
       "pblms-systemrm": pblms_systemrm,
       "pblms-system": pblms_system,
       "pblms-systemrmTable": pblms_systemrmTable,
       "pblms-systemrmEntry": pblms_systemrmEntry,
       "pblms-systemrmSysName": pblms_systemrmSysName,
       "pblms-systemrmInstName": pblms_systemrmInstName,
       "pblms-systemrmSubAddr": pblms_systemrmSubAddr,
       "lsx-unix": lsx_unix,
       "uxlms-systemrm": uxlms_systemrm,
       "uxlms-system": uxlms_system,
       "uxlms-systemrmTable": uxlms_systemrmTable,
       "uxlms-systemrmEntry": uxlms_systemrmEntry,
       "uxlms-systemrmSysName": uxlms_systemrmSysName,
       "uxlms-systemrmInstName": uxlms_systemrmInstName,
       "uxlms-systemrmSubAddr": uxlms_systemrmSubAddr,
       "uxlms-nms": uxlms_nms,
       "uxlms-sdrm": uxlms_sdrm,
       "uxlms-sdrmTable": uxlms_sdrmTable,
       "uxlms-sdrmEntry": uxlms_sdrmEntry,
       "uxlms-sdrmSysName": uxlms_sdrmSysName,
       "uxlms-sdrmInstName": uxlms_sdrmInstName,
       "uxlms-sdrmSubAddr": uxlms_sdrmSubAddr,
       "uxlmx-LM": uxlmx_LM,
       "uxlmx-SRVLM": uxlmx_SRVLM,
       "uxlmx-SRVLMTable": uxlmx_SRVLMTable,
       "uxlmx-SRVLMEntry": uxlmx_SRVLMEntry,
       "uxlmx-SRVLMSysName": uxlmx_SRVLMSysName,
       "uxlmx-SRVLMInstName": uxlmx_SRVLMInstName,
       "uxlmx-SRVLMSubAddr": uxlmx_SRVLMSubAddr,
       "uxlmx-wknumNCBs": uxlmx_wknumNCBs,
       "uxlmx-wkfiNCBs": uxlmx_wkfiNCBs,
       "uxlmx-wkfcNCBs": uxlmx_wkfcNCBs,
       "uxlmx-wksesstart": uxlmx_wksesstart,
       "uxlmx-wksessfail": uxlmx_wksessfail,
       "uxlmx-wkuses": uxlmx_wkuses,
       "uxlmx-wkusefail": uxlmx_wkusefail,
       "uxlmx-wkautorec": uxlmx_wkautorec,
       "uxlmx-svfopens": uxlmx_svfopens,
       "uxlmx-svdevopens": uxlmx_svdevopens,
       "uxlmx-svjobsqueued": uxlmx_svjobsqueued,
       "uxlmx-svsopens": uxlmx_svsopens,
       "uxlmx-svstimedout": uxlmx_svstimedout,
       "uxlmx-svserrorout": uxlmx_svserrorout,
       "uxlmx-svpwerrors": uxlmx_svpwerrors,
       "uxlmx-svpermerrors": uxlmx_svpermerrors,
       "uxlmx-svsyserrors": uxlmx_svsyserrors,
       "uxlmx-svbytessent": uxlmx_svbytessent,
       "uxlmx-svbytesrcvd": uxlmx_svbytesrcvd,
       "uxlmx-svavresponse": uxlmx_svavresponse,
       "wan": wan,
       "lapb": lapb,
       "lapbTable": lapbTable,
       "lapbEntry": lapbEntry,
       "uxlapb-lapbSysName": uxlapb_lapbSysName,
       "uxlapb-lapbInstName": uxlapb_lapbInstName,
       "uxlapb-lapbSubAddr": uxlapb_lapbSubAddr,
       "uxlapb-numOfzerotime": uxlapb_numOfzerotime,
       "uxlapb-numOfinfosent": uxlapb_numOfinfosent,
       "uxlapb-numOfinforece": uxlapb_numOfinforece,
       "uxlapb-numOfrrsent": uxlapb_numOfrrsent,
       "uxlapb-numOfrrrece": uxlapb_numOfrrrece,
       "uxlapb-numOfrnrsent": uxlapb_numOfrnrsent,
       "uxlapb-numOfrnrrece": uxlapb_numOfrnrrece,
       "uxlapb-numOfSABMitsent": uxlapb_numOfSABMitsent,
       "uxlapb-numOfSABMnitsent": uxlapb_numOfSABMnitsent,
       "uxlapb-numOfSABMitrece": uxlapb_numOfSABMitrece,
       "uxlapb-numOfSABMnitrece": uxlapb_numOfSABMnitrece,
       "uxlapb-numOfDISCitsent": uxlapb_numOfDISCitsent,
       "uxlapb-numOfDISCnitsent": uxlapb_numOfDISCnitsent,
       "uxlapb-numOfDISCitrece": uxlapb_numOfDISCitrece,
       "uxlapb-numOfDISCnitrece": uxlapb_numOfDISCnitrece,
       "uxlapb-numOfUAitsent": uxlapb_numOfUAitsent,
       "uxlapb-numOfUAnitsent": uxlapb_numOfUAnitsent,
       "uxlapb-numOfUAitrece": uxlapb_numOfUAitrece,
       "uxlapb-numOfUAnitrece": uxlapb_numOfUAnitrece,
       "uxlapb-numOfDMitsent": uxlapb_numOfDMitsent,
       "uxlapb-numOfDMnitsent": uxlapb_numOfDMnitsent,
       "uxlapb-numOfDMitrece": uxlapb_numOfDMitrece,
       "uxlapb-numOfDMnitrece": uxlapb_numOfDMnitrece,
       "uxlapb-numOffrmrsent": uxlapb_numOffrmrsent,
       "uxlapb-numOffrmrrece": uxlapb_numOffrmrrece,
       "uxlapb-numOfrejsent": uxlapb_numOfrejsent,
       "uxlapb-numOfrejrece": uxlapb_numOfrejrece,
       "uxlapb-numOfbusycondet": uxlapb_numOfbusycondet,
       "uxlapb-numOfbusyconent": uxlapb_numOfbusyconent,
       "uxlapb-numOfdataoctsent": uxlapb_numOfdataoctsent,
       "uxlapb-numOfdataoctrece": uxlapb_numOfdataoctrece,
       "uxlapb-numOfoutsequence": uxlapb_numOfoutsequence,
       "uxlapb-numOfretrframes": uxlapb_numOfretrframes,
       "uxlapb-numOfinvalidframes": uxlapb_numOfinvalidframes,
       "uxlapb-numOfphystxerrors": uxlapb_numOfphystxerrors,
       "uxlapb-numOfReserved1": uxlapb_numOfReserved1,
       "uxlapb-numOfReserved2": uxlapb_numOfReserved2,
       "uxlapb-numOfReserved3": uxlapb_numOfReserved3,
       "uxlapb-numOfReserved4": uxlapb_numOfReserved4,
       "uxlapb-numOfInformatype": uxlapb_numOfInformatype,
       "x25": x25,
       "x25Table": x25Table,
       "x25Entry": x25Entry,
       "uxx25-x25SysName": uxx25_x25SysName,
       "uxx25-x25InstName": uxx25_x25InstName,
       "uxx25-x25SubAddr": uxx25_x25SubAddr,
       "uxx25-numOfzerot": uxx25_numOfzerot,
       "uxx25-numOfrestsent": uxx25_numOfrestsent,
       "uxx25-numOfrestrece": uxx25_numOfrestrece,
       "uxx25-numOfcallsent": uxx25_numOfcallsent,
       "uxx25-numOfcallrece": uxx25_numOfcallrece,
       "uxx25-numOfclearsent": uxx25_numOfclearsent,
       "uxx25-numOfclearrece": uxx25_numOfclearrece,
       "uxx25-numOfdatasent": uxx25_numOfdatasent,
       "uxx25-numOfdatarece": uxx25_numOfdatarece,
       "uxx25-numOfoctsent": uxx25_numOfoctsent,
       "uxx25-numOfoctrece": uxx25_numOfoctrece,
       "uxx25-numOfintersent": uxx25_numOfintersent,
       "uxx25-numOfinterrece": uxx25_numOfinterrece,
       "uxx25-numOfrrxsent": uxx25_numOfrrxsent,
       "uxx25-numOfrrxrece": uxx25_numOfrrxrece,
       "uxx25-numOfrnrxsent": uxx25_numOfrnrxsent,
       "uxx25-numOfrnrxrece": uxx25_numOfrnrxrece,
       "uxx25-numOfresetsent": uxx25_numOfresetsent,
       "uxx25-numOfresetrece": uxx25_numOfresetrece,
       "uxx25-numOfrejxsent": uxx25_numOfrejxsent,
       "uxx25-numOfrejxrece": uxx25_numOfrejxrece,
       "uxx25-numOfdiagnsent": uxx25_numOfdiagnsent,
       "uxx25-numOfdiagnrece": uxx25_numOfdiagnrece,
       "uxx25-numOfregistsent": uxx25_numOfregistsent,
       "uxx25-numOfregistrece": uxx25_numOfregistrece,
       "uxx25-numOfrestretries": uxx25_numOfrestretries,
       "uxx25-numOfrestunsucfull": uxx25_numOfrestunsucfull,
       "uxx25-numOfsyntaxerrors": uxx25_numOfsyntaxerrors,
       "uxx25-numOflogicalerrors": uxx25_numOflogicalerrors,
       "uxx25-numOfcallunsucfull": uxx25_numOfcallunsucfull,
       "uxx25-numOfclearretries": uxx25_numOfclearretries,
       "uxx25-numOfclearunsucfull": uxx25_numOfclearunsucfull,
       "uxx25-numOfinterunsucfull": uxx25_numOfinterunsucfull,
       "uxx25-numOfresetretries": uxx25_numOfresetretries,
       "uxx25-numOfresetunsucfull": uxx25_numOfresetunsucfull,
       "uxx25-numOfdataretrsucfull": uxx25_numOfdataretrsucfull,
       "uxx25-numOfdataretrunsucfull": uxx25_numOfdataretrunsucfull,
       "uxx25-numOfrejretries": uxx25_numOfrejretries,
       "uxx25-numOfrejunsucfull": uxx25_numOfrejunsucfull,
       "uxx25-numOfInformat": uxx25_numOfInformat,
       "tp02": tp02,
       "tp02Table": tp02Table,
       "tp02Entry": tp02Entry,
       "uxtp02-tp02SysName": uxtp02_tp02SysName,
       "uxtp02-tp02InstName": uxtp02_tp02InstName,
       "uxtp02-tp02SubAddr": uxtp02_tp02SubAddr,
       "uxtp02-numOfzeroingtime": uxtp02_numOfzeroingtime,
       "uxtp02-numOfnumberTPDUSent": uxtp02_numOfnumberTPDUSent,
       "uxtp02-numOfnumberTPDUReceived": uxtp02_numOfnumberTPDUReceived,
       "uxtp02-numOftDataSent": uxtp02_numOftDataSent,
       "uxtp02-numOftExpeditedDataSent": uxtp02_numOftExpeditedDataSent,
       "uxtp02-numOftDataReceived": uxtp02_numOftDataReceived,
       "uxtp02-numOftExpeditedDataReceived": uxtp02_numOftExpeditedDataReceived,
       "uxtp02-numOfopenConnection": uxtp02_numOfopenConnection,
       "uxtp02-numOfctTPDUSuccessfullIncoming": uxtp02_numOfctTPDUSuccessfullIncoming,
       "uxtp02-numOfctTPDUSuccessfullOutgoing": uxtp02_numOfctTPDUSuccessfullOutgoing,
       "uxtp02-numOfctTPDUUnSuccessfullIncoming": uxtp02_numOfctTPDUUnSuccessfullIncoming,
       "uxtp02-numOfctTPDUUnSuccessfullOutgoing": uxtp02_numOfctTPDUUnSuccessfullOutgoing,
       "uxtp02-numOfctTPDUCongestion": uxtp02_numOfctTPDUCongestion,
       "uxtp02-numOfctTPDUConfProtErrorDetected": uxtp02_numOfctTPDUConfProtErrorDetected,
       "uxtp02-numOfctTPDURefusedConfProtError": uxtp02_numOfctTPDURefusedConfProtError,
       "uxtp02-numOfdetectedTPDUProtocolError": uxtp02_numOfdetectedTPDUProtocolError,
       "uxtp02-numOfrefusedTPDUProtocolError": uxtp02_numOfrefusedTPDUProtocolError,
       "tnetb-TNB": tnetb_TNB,
       "tnetb-NETB": tnetb_NETB,
       "tnetb-NETBTable": tnetb_NETBTable,
       "tnetb-NETBEntry": tnetb_NETBEntry,
       "tnetb-NETBSysName": tnetb_NETBSysName,
       "tnetb-NETBInstName": tnetb_NETBInstName,
       "tnetb-NETBSubAddr": tnetb_NETBSubAddr,
       "tnetb-NETBtxPDU": tnetb_NETBtxPDU,
       "tnetb-NETBrxPDU": tnetb_NETBrxPDU,
       "tnetb-NETBsuccessregistr": tnetb_NETBsuccessregistr,
       "tnetb-NETBunsuccessregistr": tnetb_NETBunsuccessregistr,
       "tnetb-NETBsuccessderegistr": tnetb_NETBsuccessderegistr,
       "tnetb-NETBunsuccessderegistr": tnetb_NETBunsuccessderegistr,
       "tnetb-NETBresolutednames": tnetb_NETBresolutednames,
       "tnetb-NETBunresolutednames": tnetb_NETBunresolutednames,
       "tnetb-NETBreserved": tnetb_NETBreserved,
       "tnetb-NETBrxinvalidPDU": tnetb_NETBrxinvalidPDU,
       "tnetb-TRSP": tnetb_TRSP,
       "tnetb-TRSPTable": tnetb_TRSPTable,
       "tnetb-TRSPEntry": tnetb_TRSPEntry,
       "tnetb-TRSPSysName": tnetb_TRSPSysName,
       "tnetb-TRSPInstName": tnetb_TRSPInstName,
       "tnetb-TRSPSubAddr": tnetb_TRSPSubAddr,
       "tnetb-TRSPreserved1": tnetb_TRSPreserved1,
       "tnetb-TRSPsuppconnection": tnetb_TRSPsuppconnection,
       "tnetb-TRSPreserved2": tnetb_TRSPreserved2,
       "tnetb-TRSPreserved3": tnetb_TRSPreserved3,
       "tnetb-TRSPreserved4": tnetb_TRSPreserved4,
       "tnetb-TRSPreserved5": tnetb_TRSPreserved5,
       "tnetb-TRSPtxTPDU": tnetb_TRSPtxTPDU,
       "tnetb-TRSPrxTPDU": tnetb_TRSPrxTPDU,
       "tnetb-TRSPtxretranTPDU": tnetb_TRSPtxretranTPDU,
       "tnetb-TRSPtxretranDATATPDU": tnetb_TRSPtxretranDATATPDU,
       "tnetb-TRSPactiveconnection": tnetb_TRSPactiveconnection,
       "tnetb-TRSPreserved6": tnetb_TRSPreserved6,
       "tnetb-TRSPsuccessinconnect": tnetb_TRSPsuccessinconnect,
       "tnetb-TRSPsuccessoutconnect": tnetb_TRSPsuccessoutconnect,
       "tnetb-TRSPunsuccessinconnect": tnetb_TRSPunsuccessinconnect,
       "tnetb-TRSPunsuccessoutconnect": tnetb_TRSPunsuccessoutconnect,
       "tnetb-TRSPconnectinactivity": tnetb_TRSPconnectinactivity,
       "tnetb-TRSPprotocolerror": tnetb_TRSPprotocolerror,
       "tnetb-TRSPrxinvalidTPDU": tnetb_TRSPrxinvalidTPDU,
       "tnetb-TRSPrxTSDU": tnetb_TRSPrxTSDU,
       "tnetb-TRSPtxTSDU": tnetb_TRSPtxTSDU,
       "tnetb-TRSPtxdatabyte": tnetb_TRSPtxdatabyte,
       "tnetb-TRSPrxdatabyte": tnetb_TRSPrxdatabyte,
       "tnetb-TRSPallocerror": tnetb_TRSPallocerror,
       "tnetb-TRSPtxdatagramTPDU": tnetb_TRSPtxdatagramTPDU,
       "tnetb-TRSPrxdatagrmTPDU": tnetb_TRSPrxdatagrmTPDU,
       "tnetb-TRSPoverrunTPDU": tnetb_TRSPoverrunTPDU,
       "tnetb-TRSPopenerror": tnetb_TRSPopenerror,
       "tnetb-TRSPnoendpoint": tnetb_TRSPnoendpoint,
       "tnetb-NTWK": tnetb_NTWK,
       "tnetb-NTWKTable": tnetb_NTWKTable,
       "tnetb-NTWKEntry": tnetb_NTWKEntry,
       "tnetb-NTWKSysName": tnetb_NTWKSysName,
       "tnetb-NTWKInstName": tnetb_NTWKInstName,
       "tnetb-NTWKSubAddr": tnetb_NTWKSubAddr,
       "tnetb-NTWKresourceerror": tnetb_NTWKresourceerror,
       "tnetb-NTWKrxPDU": tnetb_NTWKrxPDU,
       "tnetb-NTWKtxPDU": tnetb_NTWKtxPDU,
       "tnetb-NTWKrxbyte": tnetb_NTWKrxbyte,
       "tnetb-NTWKtxbyte": tnetb_NTWKtxbyte,
       "tnetb-NTWKtxsegmented": tnetb_NTWKtxsegmented,
       "tnetb-NTWKtxnetworkerror": tnetb_NTWKtxnetworkerror,
       "tnetb-NTWKrxnetworkerror": tnetb_NTWKrxnetworkerror,
       "tnetb-NTWKtxcongested": tnetb_NTWKtxcongested,
       "tnetb-NTWKrxreassembled": tnetb_NTWKrxreassembled,
       "tnetb-NTWKreassemblytimeout": tnetb_NTWKreassemblytimeout,
       "tnetb-NTWKtxforwarded": tnetb_NTWKtxforwarded,
       "tnetb-NTWKPDUbadformat": tnetb_NTWKPDUbadformat,
       "tnetb-NTWKPDUdestinunreach": tnetb_NTWKPDUdestinunreach,
       "tnetb-NTWKPDUunsupportedoption": tnetb_NTWKPDUunsupportedoption,
       "tnetb-NTWKlifetime": tnetb_NTWKlifetime,
       "tnetb-LLCN": tnetb_LLCN,
       "tnetb-LLCNTable": tnetb_LLCNTable,
       "tnetb-LLCNEntry": tnetb_LLCNEntry,
       "tnetb-LLCNSysName": tnetb_LLCNSysName,
       "tnetb-LLCNInstName": tnetb_LLCNInstName,
       "tnetb-LLCNSubAddr": tnetb_LLCNSubAddr,
       "tnetb-LLCNtxUI5rame": tnetb_LLCNtxUI5rame,
       "tnetb-LLCNrxUIframe": tnetb_LLCNrxUIframe,
       "tnetb-LLCNtxMACerror": tnetb_LLCNtxMACerror,
       "tnetb-LLCNrxMACerror": tnetb_LLCNrxMACerror,
       "tnetb-LLCNtxTESTframe": tnetb_LLCNtxTESTframe,
       "tnetb-LLCNrxTESTframe": tnetb_LLCNrxTESTframe,
       "tnetb-LLCNtxXIDframe": tnetb_LLCNtxXIDframe,
       "tnetb-LLCNrxXIDframe": tnetb_LLCNrxXIDframe,
       "tnetb-LLCNtxTESTresponse": tnetb_LLCNtxTESTresponse,
       "tnetb-LLCNrxTESTresponse": tnetb_LLCNrxTESTresponse,
       "tnetb-LLCNtxXIDresponse": tnetb_LLCNtxXIDresponse,
       "tnetb-LLCNrxXIDresponse": tnetb_LLCNrxXIDresponse,
       "netb-NB": netb_NB,
       "netb-NBEUI": netb_NBEUI,
       "netb-NBEUITable": netb_NBEUITable,
       "netb-NBEUIEntry": netb_NBEUIEntry,
       "netbSysName": netbSysName,
       "netbInstName": netbInstName,
       "netbSubAddr": netbSubAddr,
       "netbreserved": netbreserved,
       "netbreleaselevel": netbreleaselevel,
       "netbsoftwarelevel": netbsoftwarelevel,
       "netbadaptertype": netbadaptertype,
       "netbparamstype": netbparamstype,
       "netbreportingperiod": netbreportingperiod,
       "netbrxFRMR": netbrxFRMR,
       "netbtxFRMR": netbtxFRMR,
       "netbrxIframeserr": netbrxIframeserr,
       "netbtxaborted": netbtxaborted,
       "netbtxsuccesspack": netbtxsuccesspack,
       "netbrxsuccesspack": netbrxsuccesspack,
       "netbtxIframeserr": netbtxIframeserr,
       "netbrxnobuffer": netbrxnobuffer,
       "netbT1expired": netbT1expired,
       "netbTiexpired": netbTiexpired,
       "netbfreeNCB": netbfreeNCB,
       "netbconfiguredNCB": netbconfiguredNCB,
       "netbmaxNCB": netbmaxNCB,
       "netbtxnobuffer": netbtxnobuffer,
       "netbmaxdatagram": netbmaxdatagram,
       "netbpendingsession": netbpendingsession,
       "netbconfiguredpending": netbconfiguredpending,
       "netbmaxpending": netbmaxpending,
       "netbmaxdatapacket": netbmaxdatapacket,
       "netbnumbernames": netbnumbernames,
       "netbnumbersessions": netbnumbersessions,
       "netbDATAGRAMoutstanding": netbDATAGRAMoutstanding,
       "netbANYoustanding": netbANYoustanding,
       "elc-MAC": elc_MAC,
       "elc-ELC": elc_ELC,
       "elc-ELCTable": elc_ELCTable,
       "elc-ELCEntry": elc_ELCEntry,
       "elcSysName": elcSysName,
       "elcInstName": elcInstName,
       "elcSubAddr": elcSubAddr,
       "elctxsuccess": elctxsuccess,
       "elctxcollision": elctxcollision,
       "elcSQEtsterrors": elcSQEtsterrors,
       "elcrxsuccess": elcrxsuccess,
       "elcrxCRC": elcrxCRC,
       "elcrxalignment": elcrxalignment,
       "elcrxnobuffer": elcrxnobuffer,
       "elcrxoverrun": elcrxoverrun,
       "elcrxshframe": elcrxshframe,
       "elcrxcollision": elcrxcollision,
       "elctxattempted": elctxattempted,
       "elctxlostCS": elctxlostCS,
       "elctxlostCTS": elctxlostCTS,
       "elctxunderrun": elctxunderrun,
       "elctxmaxcollision": elctxmaxcollision,
       "elctxdeferred": elctxdeferred,
       "elctxframexceeding": elctxframexceeding,
       "elctxbytesuccess": elctxbytesuccess,
       "ethe-MAC1": ethe_MAC1,
       "ethe-ETH": ethe_ETH,
       "ethe-ETHTable": ethe_ETHTable,
       "ethe-ETHEntry": ethe_ETHEntry,
       "etheSysName": etheSysName,
       "etheInstName": etheInstName,
       "etheSubAddr": etheSubAddr,
       "ethetxsuccess": ethetxsuccess,
       "ethetxcollision": ethetxcollision,
       "etheSQEtsterrors": etheSQEtsterrors,
       "etherxsuccess": etherxsuccess,
       "etherxCRC": etherxCRC,
       "etherxalignment": etherxalignment,
       "etherxnobuffer": etherxnobuffer,
       "etherxoverrun": etherxoverrun,
       "etherxshframe": etherxshframe,
       "etherxcollision": etherxcollision,
       "ethetxattempted": ethetxattempted,
       "ethetxlostCS": ethetxlostCS,
       "ethetxlostCTS": ethetxlostCTS,
       "ethetxunderrun": ethetxunderrun,
       "ethetxmaxcollision": ethetxmaxcollision,
       "ethetxdeferred": ethetxdeferred,
       "ethetxframexceeding": ethetxframexceeding,
       "ethetxbytesuccess": ethetxbytesuccess,
       "onetware-NW": onetware_NW,
       "onetware-SRVNW": onetware_SRVNW,
       "onetware-SRVNWTable": onetware_SRVNWTable,
       "onetware-SRVNWEntry": onetware_SRVNWEntry,
       "onetwareSysName": onetwareSysName,
       "onetwareInstName": onetwareInstName,
       "onetwareSubAddr": onetwareSubAddr,
       "onetwareMaxClientConnSupported": onetwareMaxClientConnSupported,
       "onetwareClientConnInUse": onetwareClientConnInUse,
       "onetwarePeakClientConnUsed": onetwarePeakClientConnUsed,
       "onetwareMaxVolumes": onetwareMaxVolumes,
       "onetwareNWProcs": onetwareNWProcs,
       "onetwareTotalPackets": onetwareTotalPackets,
       "onetwareCreateConnectionRequests": onetwareCreateConnectionRequests,
       "onetwareCreateFileRequests": onetwareCreateFileRequests,
       "onetwareOpenRequests": onetwareOpenRequests,
       "onetwareReadRequests": onetwareReadRequests,
       "onetwareWriteRequests": onetwareWriteRequests,
       "onetwareNumOpenFiles": onetwareNumOpenFiles,
       "onetwareMaxSimultaneousOpens": onetwareMaxSimultaneousOpens,
       "onetwareLostPacketResends": onetwareLostPacketResends,
       "onetwareCacheHits": onetwareCacheHits,
       "onetwareCacheMisses": onetwareCacheMisses,
       "onetwarePrintRequests": onetwarePrintRequests,
       "onetwareMessageRequests": onetwareMessageRequests,
       "onetwareDirectoryRequests": onetwareDirectoryRequests,
       "onetwareBinderyAndMiscRequests": onetwareBinderyAndMiscRequests,
       "onetwareUnknownRequests": onetwareUnknownRequests,
       "onetwareSharedMemorySize": onetwareSharedMemorySize,
       "onetwareCurrentSharedMemoryUsage": onetwareCurrentSharedMemoryUsage,
       "onetwareMaxSharedMemoryUsed": onetwareMaxSharedMemoryUsed,
       "onetwareLogicalLockRequests": onetwareLogicalLockRequests,
       "onetwareNumLogicalLocks": onetwareNumLogicalLocks,
       "onetwareMaxSimultaneousLogLocks": onetwareMaxSimultaneousLogLocks,
       "onetwareFileLockRequests": onetwareFileLockRequests,
       "onetwareNumFileLocks": onetwareNumFileLocks,
       "onetwareMaxSimultaneousFileLocks": onetwareMaxSimultaneousFileLocks,
       "onetwarePhysLockRequests": onetwarePhysLockRequests,
       "onetwareNumPhysLocks": onetwareNumPhysLocks,
       "onetwareMaxSimultaneousPhysLocks": onetwareMaxSimultaneousPhysLocks,
       "onetwareSemaphoreRequests": onetwareSemaphoreRequests,
       "onetwareNumSemaphores": onetwareNumSemaphores,
       "onetwareMaxSimultaneousSemaphores": onetwareMaxSimultaneousSemaphores,
       "uxos-disc": uxos_disc,
       "uxos-scsi": uxos_scsi,
       "uxos-diskTable": uxos_diskTable,
       "uxos-diskEntry": uxos_diskEntry,
       "uxos-diskSysName": uxos_diskSysName,
       "uxos-diskInstName": uxos_diskInstName,
       "uxos-diskSubAddr": uxos_diskSubAddr,
       "uxos-numRW": uxos_numRW,
       "uxos-numOtherOp": uxos_numOtherOp,
       "uxos-numJobsToDr": uxos_numJobsToDr,
       "uxos-numUnlogErr": uxos_numUnlogErr,
       "uxos-totBlkTrans": uxos_totBlkTrans,
       "uxos-totBlkResp": uxos_totBlkResp,
       "uxos-cumulUse": uxos_cumulUse,
       "uxos-major": uxos_major,
       "uxos-minor": uxos_minor,
       "uxos-totNumRead": uxos_totNumRead,
       "uxos-totNumWrite": uxos_totNumWrite,
       "uxos-cumulQueLen": uxos_cumulQueLen,
       "uxos-maxQueLen": uxos_maxQueLen,
       "uxos-minQueLen": uxos_minQueLen,
       "uxos-cumulSeekDist": uxos_cumulSeekDist,
       "uxos-driveActive": uxos_driveActive,
       "uxos-drivePerf": uxos_drivePerf,
       "uxos-startOfQueue": uxos_startOfQueue,
       "uxos-lastInQueue": uxos_lastInQueue,
       "uxos-queue01": uxos_queue01,
       "uxos-queue02": uxos_queue02,
       "uxos-queue11": uxos_queue11,
       "uxos-queue12": uxos_queue12,
       "uxos-queue21": uxos_queue21,
       "uxos-queue22": uxos_queue22,
       "uxos-queue31": uxos_queue31,
       "uxos-queue32": uxos_queue32,
       "uxos-queue41": uxos_queue41,
       "uxos-queue42": uxos_queue42,
       "uxos-queue51": uxos_queue51,
       "uxos-queue52": uxos_queue52,
       "uxos-queue61": uxos_queue61,
       "uxos-queue62": uxos_queue62,
       "uxos-queue71": uxos_queue71,
       "uxos-queue72": uxos_queue72,
       "uxos-queue81": uxos_queue81,
       "uxos-queue82": uxos_queue82,
       "uxos-queue91": uxos_queue91,
       "uxos-queue92": uxos_queue92,
       "uxos-core": uxos_core,
       "uxos-cpu": uxos_cpu,
       "uxos-cpuTable": uxos_cpuTable,
       "uxos-cpuEntry": uxos_cpuEntry,
       "uxos-cpuSysName": uxos_cpuSysName,
       "uxos-cpuInstName": uxos_cpuInstName,
       "uxos-cpuSubAddr": uxos_cpuSubAddr,
       "uxos-numOfCpu": uxos_numOfCpu,
       "uxos-nproc": uxos_nproc,
       "uxos-nprocTable": uxos_nprocTable,
       "uxos-nprocEntry": uxos_nprocEntry,
       "uxos-nprocSysName": uxos_nprocSysName,
       "uxos-nprocInstName": uxos_nprocInstName,
       "uxos-nprocSubAddr": uxos_nprocSubAddr,
       "uxos-numOfProc": uxos_numOfProc,
       "uxos-ufsfreeinode": uxos_ufsfreeinode,
       "uxos-ufsfreeinodeTable": uxos_ufsfreeinodeTable,
       "uxos-ufsfreeinodeEntry": uxos_ufsfreeinodeEntry,
       "uxos-ufsfreeinodeSysName": uxos_ufsfreeinodeSysName,
       "uxos-ufsfreeinodeInstName": uxos_ufsfreeinodeInstName,
       "uxos-ufsfreeinodeSubAddr": uxos_ufsfreeinodeSubAddr,
       "uxos-numOfUfsfreeinode": uxos_numOfUfsfreeinode,
       "uxos-physmem": uxos_physmem,
       "uxos-memTable": uxos_memTable,
       "uxos-memEntry": uxos_memEntry,
       "uxos-memSysName": uxos_memSysName,
       "uxos-memInstName": uxos_memInstName,
       "uxos-memSubAddr": uxos_memSubAddr,
       "uxos-memSize": uxos_memSize,
       "uxos-filecnt": uxos_filecnt,
       "uxos-fileTable": uxos_fileTable,
       "uxos-fileEntry": uxos_fileEntry,
       "uxos-fileSysName": uxos_fileSysName,
       "uxos-fileInstName": uxos_fileInstName,
       "uxos-fileSubAddr": uxos_fileSubAddr,
       "uxos-numOfFile": uxos_numOfFile,
       "uxos-boottime": uxos_boottime,
       "uxos-bootTable": uxos_bootTable,
       "uxos-bootEntry": uxos_bootEntry,
       "uxos-bootSysName": uxos_bootSysName,
       "uxos-bootInstName": uxos_bootInstName,
       "uxos-bootSubAddr": uxos_bootSubAddr,
       "uxos-bootTime": uxos_bootTime,
       "uxos-sysinfo": uxos_sysinfo,
       "uxos-sysTable": uxos_sysTable,
       "uxos-sysEntry": uxos_sysEntry,
       "uxos-sysSysName": uxos_sysSysName,
       "uxos-sysInstName": uxos_sysInstName,
       "uxos-sysSubAddr": uxos_sysSubAddr,
       "uxos-cpuIdle": uxos_cpuIdle,
       "uxos-cpuUser": uxos_cpuUser,
       "uxos-cpuKernel": uxos_cpuKernel,
       "uxos-cpuWait": uxos_cpuWait,
       "uxos-cpuSxbrk": uxos_cpuSxbrk,
       "uxos-wIo": uxos_wIo,
       "uxos-wSwap": uxos_wSwap,
       "uxos-wPio": uxos_wPio,
       "uxos-bread": uxos_bread,
       "uxos-bwrite": uxos_bwrite,
       "uxos-lread": uxos_lread,
       "uxos-lwrite": uxos_lwrite,
       "uxos-phread": uxos_phread,
       "uxos-phwrite": uxos_phwrite,
       "uxos-swapin": uxos_swapin,
       "uxos-swapout": uxos_swapout,
       "uxos-pswapin": uxos_pswapin,
       "uxos-pswapout": uxos_pswapout,
       "uxos-pswitch": uxos_pswitch,
       "uxos-syscall": uxos_syscall,
       "uxos-sysread": uxos_sysread,
       "uxos-syswrite": uxos_syswrite,
       "uxos-sysfork": uxos_sysfork,
       "uxos-sysexec": uxos_sysexec,
       "uxos-runque": uxos_runque,
       "uxos-runocc": uxos_runocc,
       "uxos-swpque": uxos_swpque,
       "uxos-swpocc": uxos_swpocc,
       "uxos-iget": uxos_iget,
       "uxos-namei": uxos_namei,
       "uxos-dirblk": uxos_dirblk,
       "uxos-readch": uxos_readch,
       "uxos-writech": uxos_writech,
       "uxos-rcvint": uxos_rcvint,
       "uxos-xmtint": uxos_xmtint,
       "uxos-mdmint": uxos_mdmint,
       "uxos-rawch": uxos_rawch,
       "uxos-canch": uxos_canch,
       "uxos-outch": uxos_outch,
       "uxos-msg": uxos_msg,
       "uxos-sema": uxos_sema,
       "uxos-minfo": uxos_minfo,
       "uxos-minfoTable": uxos_minfoTable,
       "uxos-minfoEntry": uxos_minfoEntry,
       "uxos-minfoSysName": uxos_minfoSysName,
       "uxos-minfoInstName": uxos_minfoInstName,
       "uxos-minfoSubAddr": uxos_minfoSubAddr,
       "uxos-freememLeast": uxos_freememLeast,
       "uxos-freememMost": uxos_freememMost,
       "uxos-freeswap": uxos_freeswap,
       "uxos-sumvfault": uxos_sumvfault,
       "uxos-demand": uxos_demand,
       "uxos-swap": uxos_swap,
       "uxos-cache": uxos_cache,
       "uxos-file": uxos_file,
       "uxos-pfault": uxos_pfault,
       "uxos-cw": uxos_cw,
       "uxos-steal": uxos_steal,
       "uxos-freedpgs": uxos_freedpgs,
       "uxos-vfpg": uxos_vfpg,
       "uxos-sfpg": uxos_sfpg,
       "uxos-vspg": uxos_vspg,
       "uxos-sspg": uxos_sspg,
       "uxos-unmodsw": uxos_unmodsw,
       "uxos-unmodfl": uxos_unmodfl,
       "uxos-psoutok": uxos_psoutok,
       "uxos-psinfail": uxos_psinfail,
       "uxos-psinok": uxos_psinok,
       "uxos-rsout": uxos_rsout,
       "uxos-rsin": uxos_rsin,
       "uxos-shmem": uxos_shmem,
       "uxos-vminfo": uxos_vminfo,
       "uxos-vminfoTable": uxos_vminfoTable,
       "uxos-vminfoEntry": uxos_vminfoEntry,
       "uxos-vminfoSysName": uxos_vminfoSysName,
       "uxos-vminfoInstName": uxos_vminfoInstName,
       "uxos-vminfoSubAddr": uxos_vminfoSubAddr,
       "uxos-vPgrec": uxos_vPgrec,
       "uxos-vXsfrec": uxos_vXsfrec,
       "uxos-vXifrec": uxos_vXifrec,
       "uxos-vPgin": uxos_vPgin,
       "uxos-vPgpgin": uxos_vPgpgin,
       "uxos-vPgout": uxos_vPgout,
       "uxos-vPgpgout": uxos_vPgpgout,
       "uxos-vSwpout": uxos_vSwpout,
       "uxos-vPswpout": uxos_vPswpout,
       "uxos-vSwpin": uxos_vSwpin,
       "uxos-vPswpin": uxos_vPswpin,
       "uxos-vDfree": uxos_vDfree,
       "uxos-vScan": uxos_vScan,
       "uxos-vPfault": uxos_vPfault,
       "uxos-vVfault": uxos_vVfault,
       "uxos-vSftlock": uxos_vSftlock,
       "uxos-syserr": uxos_syserr,
       "uxos-syserrTable": uxos_syserrTable,
       "uxos-syserrEntry": uxos_syserrEntry,
       "uxos-syserrSysName": uxos_syserrSysName,
       "uxos-syserrInstName": uxos_syserrInstName,
       "uxos-syserrSubAddr": uxos_syserrSubAddr,
       "uxos-inodeovf": uxos_inodeovf,
       "uxos-ufsinodeovf": uxos_ufsinodeovf,
       "uxos-fileovf": uxos_fileovf,
       "uxos-textovf": uxos_textovf,
       "uxos-procovf": uxos_procovf,
       "uxos-kmeminfo": uxos_kmeminfo,
       "uxos-kmeminfoTable": uxos_kmeminfoTable,
       "uxos-kmeminfoEntry": uxos_kmeminfoEntry,
       "uxos-kmeminfoSysName": uxos_kmeminfoSysName,
       "uxos-kmeminfoInstName": uxos_kmeminfoInstName,
       "uxos-kmeminfoSubAddr": uxos_kmeminfoSubAddr,
       "uxos-smlMem": uxos_smlMem,
       "uxos-smlAlloc": uxos_smlAlloc,
       "uxos-smlFail": uxos_smlFail,
       "uxos-lgMem": uxos_lgMem,
       "uxos-lgAlloc": uxos_lgAlloc,
       "uxos-lgFail": uxos_lgFail,
       "uxos-ovszMem": uxos_ovszMem,
       "uxos-ovszAlloc": uxos_ovszAlloc,
       "uxos-ovszFail": uxos_ovszFail,
       "uxos-rtminfo": uxos_rtminfo,
       "uxos-rtminfoTable": uxos_rtminfoTable,
       "uxos-rtminfoEntry": uxos_rtminfoEntry,
       "uxos-rtminfoSysName": uxos_rtminfoSysName,
       "uxos-rtminfoInstName": uxos_rtminfoInstName,
       "uxos-rtminfoSubAddr": uxos_rtminfoSubAddr,
       "uxos-evPost": uxos_evPost,
       "uxos-evPoll": uxos_evPoll,
       "uxos-evTrap": uxos_evTrap,
       "uxos-var": uxos_var,
       "uxos-varTable": uxos_varTable,
       "uxos-varEntry": uxos_varEntry,
       "uxos-varSysName": uxos_varSysName,
       "uxos-varInstName": uxos_varInstName,
       "uxos-varSubAddr": uxos_varSubAddr,
       "uxos-vBuf": uxos_vBuf,
       "uxos-vCall": uxos_vCall,
       "uxos-vProc": uxos_vProc,
       "uxos-vFiller": uxos_vFiller,
       "uxos-vNglobpris": uxos_vNglobpris,
       "uxos-vMaxsyspri": uxos_vMaxsyspri,
       "uxos-vClist": uxos_vClist,
       "uxos-vMaxup": uxos_vMaxup,
       "uxos-vHbuf": uxos_vHbuf,
       "uxos-vHmask": uxos_vHmask,
       "uxos-vPbuf": uxos_vPbuf,
       "uxos-vSptmap": uxos_vSptmap,
       "uxos-vMaxpmem": uxos_vMaxpmem,
       "uxos-vAutoup": uxos_vAutoup,
       "uxos-vBufhwm": uxos_vBufhwm,
       "uxos-vScrn": uxos_vScrn,
       "uxos-vEmap": uxos_vEmap,
       "uxos-vSxt": uxos_vSxt,
       "uxos-vXsdsegs": uxos_vXsdsegs,
       "uxos-vXsdslots": uxos_vXsdslots,
       "uxos-vPhash": uxos_vPhash,
       "uxos-shlbinfo": uxos_shlbinfo,
       "uxos-shlbinfoTable": uxos_shlbinfoTable,
       "uxos-shlbinfoEntry": uxos_shlbinfoEntry,
       "uxos-shlbinfoSysName": uxos_shlbinfoSysName,
       "uxos-shlbinfoInstName": uxos_shlbinfoInstName,
       "uxos-shlbinfoSubAddr": uxos_shlbinfoSubAddr,
       "uxos-shlbs": uxos_shlbs,
       "uxos-shlblnks": uxos_shlblnks,
       "uxos-shlbovf": uxos_shlbovf,
       "uxos-shlbatts": uxos_shlbatts,
       "uxos-flckinfo": uxos_flckinfo,
       "uxos-flckinfoTable": uxos_flckinfoTable,
       "uxos-flckinfoEntry": uxos_flckinfoEntry,
       "uxos-flckinfoSysName": uxos_flckinfoSysName,
       "uxos-flckinfoInstName": uxos_flckinfoInstName,
       "uxos-flckinfoSubAddr": uxos_flckinfoSubAddr,
       "uxos-reccnt": uxos_reccnt,
       "uxos-rectot": uxos_rectot,
       "uxos-tune": uxos_tune,
       "uxos-tuneTable": uxos_tuneTable,
       "uxos-tuneEntry": uxos_tuneEntry,
       "uxos-tuneSysName": uxos_tuneSysName,
       "uxos-tuneInstName": uxos_tuneInstName,
       "uxos-tuneSubAddr": uxos_tuneSubAddr,
       "uxos-tGpgslo": uxos_tGpgslo,
       "uxos-tGpgshi": uxos_tGpgshi,
       "uxos-tPadd": uxos_tPadd,
       "uxos-tNotused": uxos_tNotused,
       "uxos-tAgeinterval": uxos_tAgeinterval,
       "uxos-tPadd11": uxos_tPadd11,
       "uxos-tPadd12": uxos_tPadd12,
       "uxos-tPadd13": uxos_tPadd13,
       "uxos-tFsflushr": uxos_tFsflushr,
       "uxos-tMinarmem": uxos_tMinarmem,
       "uxos-tMinasmem": uxos_tMinasmem,
       "uxos-tDmalimit": uxos_tDmalimit,
       "uxos-tFlckrec": uxos_tFlckrec,
       "uxos-tMinakmem": uxos_tMinakmem,
       "uxos-avenrun": uxos_avenrun,
       "uxos-avenrunTable": uxos_avenrunTable,
       "uxos-avenrunEntry": uxos_avenrunEntry,
       "uxos-avenrunSysName": uxos_avenrunSysName,
       "uxos-avenrunInstName": uxos_avenrunInstName,
       "uxos-avenrunSubAddr": uxos_avenrunSubAddr,
       "uxos-avenrun1": uxos_avenrun1,
       "uxos-avenrun2": uxos_avenrun2,
       "uxos-avenrun3": uxos_avenrun3,
       "uxos-vmcnt": uxos_vmcnt,
       "uxos-vmcntTable": uxos_vmcntTable,
       "uxos-vmcntEntry": uxos_vmcntEntry,
       "uxos-vmcntSysName": uxos_vmcntSysName,
       "uxos-vmcntInstName": uxos_vmcntInstName,
       "uxos-vmcntSubAddr": uxos_vmcntSubAddr,
       "uxos-cntvSwtch": uxos_cntvSwtch,
       "uxos-cntvTrap": uxos_cntvTrap,
       "uxos-cntvSyscall": uxos_cntvSyscall,
       "uxos-cntvIntr": uxos_cntvIntr,
       "uxos-cntvPdma": uxos_cntvPdma,
       "uxos-cntvPswpin": uxos_cntvPswpin,
       "uxos-cntvPswpout": uxos_cntvPswpout,
       "uxos-cntvPgin": uxos_cntvPgin,
       "uxos-cntvPgout": uxos_cntvPgout,
       "uxos-cntvPgpgin": uxos_cntvPgpgin,
       "uxos-cntvPgpgout": uxos_cntvPgpgout,
       "uxos-cntvIntrans": uxos_cntvIntrans,
       "uxos-cntvPgrec": uxos_cntvPgrec,
       "uxos-cntvXsfrec": uxos_cntvXsfrec,
       "uxos-cntvXifrec": uxos_cntvXifrec,
       "uxos-cntvExfod": uxos_cntvExfod,
       "uxos-cntvZfod": uxos_cntvZfod,
       "uxos-cntvVrfod": uxos_cntvVrfod,
       "uxos-cntvNexfod": uxos_cntvNexfod,
       "uxos-cntvNzfod": uxos_cntvNzfod,
       "uxos-cntvNvrfod": uxos_cntvNvrfod,
       "uxos-cntvPgfrec": uxos_cntvPgfrec,
       "uxos-cntvFaults": uxos_cntvFaults,
       "uxos-cntvScan": uxos_cntvScan,
       "uxos-cntvRev": uxos_cntvRev,
       "uxos-cntvSeqfree": uxos_cntvSeqfree,
       "uxos-cntvDfree": uxos_cntvDfree,
       "uxos-cntvFastpgrec": uxos_cntvFastpgrec,
       "uxos-cntvSwpin": uxos_cntvSwpin,
       "uxos-cntvSwpout": uxos_cntvSwpout,
       "uxos-vmrate": uxos_vmrate,
       "uxos-vmrateTable": uxos_vmrateTable,
       "uxos-vmrateEntry": uxos_vmrateEntry,
       "uxos-vmrateSysName": uxos_vmrateSysName,
       "uxos-vmrateInstName": uxos_vmrateInstName,
       "uxos-vmrateSubAddr": uxos_vmrateSubAddr,
       "uxos-ratevSwtch": uxos_ratevSwtch,
       "uxos-ratevTrap": uxos_ratevTrap,
       "uxos-ratevSyscall": uxos_ratevSyscall,
       "uxos-ratevIntr": uxos_ratevIntr,
       "uxos-ratevPdma": uxos_ratevPdma,
       "uxos-ratevPswpin": uxos_ratevPswpin,
       "uxos-ratevPswpout": uxos_ratevPswpout,
       "uxos-ratevPgin": uxos_ratevPgin,
       "uxos-ratevPgout": uxos_ratevPgout,
       "uxos-ratevPgpgin": uxos_ratevPgpgin,
       "uxos-ratevPgpgout": uxos_ratevPgpgout,
       "uxos-ratevIntrans": uxos_ratevIntrans,
       "uxos-ratevPgrec": uxos_ratevPgrec,
       "uxos-ratevXsfrec": uxos_ratevXsfrec,
       "uxos-ratevXifrec": uxos_ratevXifrec,
       "uxos-ratevExfod": uxos_ratevExfod,
       "uxos-ratevZfod": uxos_ratevZfod,
       "uxos-ratevVrfod": uxos_ratevVrfod,
       "uxos-ratevNexfod": uxos_ratevNexfod,
       "uxos-ratevNzfod": uxos_ratevNzfod,
       "uxos-ratevNvrfod": uxos_ratevNvrfod,
       "uxos-ratevPgfrec": uxos_ratevPgfrec,
       "uxos-ratevFaults": uxos_ratevFaults,
       "uxos-ratevScan": uxos_ratevScan,
       "uxos-ratevRev": uxos_ratevRev,
       "uxos-ratevSeqfree": uxos_ratevSeqfree,
       "uxos-ratevDfree": uxos_ratevDfree,
       "uxos-ratevFastpgrec": uxos_ratevFastpgrec,
       "uxos-ratevSwpin": uxos_ratevSwpin,
       "uxos-ratevSwpout": uxos_ratevSwpout,
       "uxos-vmsum": uxos_vmsum,
       "uxos-vmsumTable": uxos_vmsumTable,
       "uxos-vmsumEntry": uxos_vmsumEntry,
       "uxos-vmsumSysName": uxos_vmsumSysName,
       "uxos-vmsumInstName": uxos_vmsumInstName,
       "uxos-vmsumSubAddr": uxos_vmsumSubAddr,
       "uxos-sumvSwtch": uxos_sumvSwtch,
       "uxos-sumvTrap": uxos_sumvTrap,
       "uxos-sumvSyscall": uxos_sumvSyscall,
       "uxos-sumvIntr": uxos_sumvIntr,
       "uxos-sumvPdma": uxos_sumvPdma,
       "uxos-sumvPswpin": uxos_sumvPswpin,
       "uxos-sumvPswpout": uxos_sumvPswpout,
       "uxos-sumvPgin": uxos_sumvPgin,
       "uxos-sumvPgout": uxos_sumvPgout,
       "uxos-sumvPgpgin": uxos_sumvPgpgin,
       "uxos-sumvPgpgout": uxos_sumvPgpgout,
       "uxos-sumvIntrans": uxos_sumvIntrans,
       "uxos-sumvPgrec": uxos_sumvPgrec,
       "uxos-sumvXsfrec": uxos_sumvXsfrec,
       "uxos-sumvXifrec": uxos_sumvXifrec,
       "uxos-sumvExfod": uxos_sumvExfod,
       "uxos-sumvZfod": uxos_sumvZfod,
       "uxos-sumvVrfod": uxos_sumvVrfod,
       "uxos-sumvNexfod": uxos_sumvNexfod,
       "uxos-sumvNzfod": uxos_sumvNzfod,
       "uxos-sumvNvrfod": uxos_sumvNvrfod,
       "uxos-sumvPgfrec": uxos_sumvPgfrec,
       "uxos-sumvFaults": uxos_sumvFaults,
       "uxos-sumvScan": uxos_sumvScan,
       "uxos-sumvRev": uxos_sumvRev,
       "uxos-sumvSeqfree": uxos_sumvSeqfree,
       "uxos-sumvDfree": uxos_sumvDfree,
       "uxos-sumvFastpgrec": uxos_sumvFastpgrec,
       "uxos-sumvSwpin": uxos_sumvSwpin,
       "uxos-sumvSwpout": uxos_sumvSwpout,
       "uxos-vmtotal": uxos_vmtotal,
       "uxos-vmtotalTable": uxos_vmtotalTable,
       "uxos-vmtotalEntry": uxos_vmtotalEntry,
       "uxos-vmtotalSysName": uxos_vmtotalSysName,
       "uxos-vmtotalInstName": uxos_vmtotalInstName,
       "uxos-vmtotalSubAddr": uxos_vmtotalSubAddr,
       "uxos-tRq": uxos_tRq,
       "uxos-tDw": uxos_tDw,
       "uxos-tPw": uxos_tPw,
       "uxos-tSl": uxos_tSl,
       "uxos-tSw": uxos_tSw,
       "uxos-tVm": uxos_tVm,
       "uxos-tAvm": uxos_tAvm,
       "uxos-tRm": uxos_tRm,
       "uxos-tArm": uxos_tArm,
       "uxos-tVmtxt": uxos_tVmtxt,
       "uxos-tAvmtxt": uxos_tAvmtxt,
       "uxos-tRmtxt": uxos_tRmtxt,
       "uxos-tArmtxt": uxos_tArmtxt,
       "uxos-tFree": uxos_tFree,
       "uxos-lbolt": uxos_lbolt,
       "uxos-lboltTable": uxos_lboltTable,
       "uxos-lboltEntry": uxos_lboltEntry,
       "uxos-lboltSysName": uxos_lboltSysName,
       "uxos-lboltInstName": uxos_lboltInstName,
       "uxos-lboltSubAddr": uxos_lboltSubAddr,
       "uxos-numOfTick": uxos_numOfTick,
       "uxos-availsmem": uxos_availsmem,
       "uxos-smemTable": uxos_smemTable,
       "uxos-smemEntry": uxos_smemEntry,
       "uxos-smemSysName": uxos_smemSysName,
       "uxos-smemInstName": uxos_smemInstName,
       "uxos-smemSubAddr": uxos_smemSubAddr,
       "uxos-smemNumOfPages": uxos_smemNumOfPages,
       "uxos-availrmem": uxos_availrmem,
       "uxos-rmemTable": uxos_rmemTable,
       "uxos-rmemEntry": uxos_rmemEntry,
       "uxos-rmemSysName": uxos_rmemSysName,
       "uxos-rmemInstName": uxos_rmemInstName,
       "uxos-rmemSubAddr": uxos_rmemSubAddr,
       "uxos-rmemNumOfPages": uxos_rmemNumOfPages,
       "uxos-availkmem": uxos_availkmem,
       "uxos-kmemTable": uxos_kmemTable,
       "uxos-kmemEntry": uxos_kmemEntry,
       "uxos-kmemSysName": uxos_kmemSysName,
       "uxos-kmemInstName": uxos_kmemInstName,
       "uxos-kmemSubAddr": uxos_kmemSubAddr,
       "uxos-kmemNumOfPages": uxos_kmemNumOfPages,
       "uxos-namecache": uxos_namecache,
       "uxos-namecacheTable": uxos_namecacheTable,
       "uxos-namecacheEntry": uxos_namecacheEntry,
       "uxos-namecacheSysName": uxos_namecacheSysName,
       "uxos-namecacheInstName": uxos_namecacheInstName,
       "uxos-namecacheSubAddr": uxos_namecacheSubAddr,
       "uxos-hits": uxos_hits,
       "uxos-misses": uxos_misses,
       "uxos-enters": uxos_enters,
       "uxos-dblEnters": uxos_dblEnters,
       "uxos-longEnter": uxos_longEnter,
       "uxos-longLook": uxos_longLook,
       "uxos-lruEmpty": uxos_lruEmpty,
       "uxos-purges": uxos_purges,
       "uxos-buffercache": uxos_buffercache,
       "uxos-buffercacheTable": uxos_buffercacheTable,
       "uxos-buffercacheEntry": uxos_buffercacheEntry,
       "uxos-buffercacheSysName": uxos_buffercacheSysName,
       "uxos-buffercacheInstName": uxos_buffercacheInstName,
       "uxos-buffercacheSubAddr": uxos_buffercacheSubAddr,
       "uxos-cachehit": uxos_cachehit,
       "uxos-cachemiss": uxos_cachemiss,
       "uxos-freehit": uxos_freehit,
       "uxos-freemiss": uxos_freemiss,
       "uxos-bbusy": uxos_bbusy,
       "uxos-pfreemiss": uxos_pfreemiss,
       "uxos-prepfreemiss": uxos_prepfreemiss,
       "uxos-spare": uxos_spare,
       "uxos-aioinfo": uxos_aioinfo,
       "uxos-aioTable": uxos_aioTable,
       "uxos-aioEntry": uxos_aioEntry,
       "uxos-aioSysName": uxos_aioSysName,
       "uxos-aioInstName": uxos_aioInstName,
       "uxos-aioSubAddr": uxos_aioSubAddr,
       "uxos-aioread": uxos_aioread,
       "uxos-aiowrite": uxos_aiowrite,
       "uxos-aiolock": uxos_aiolock,
       "uxos-aiopoll": uxos_aiopoll,
       "uxos-aiohfbuf": uxos_aiohfbuf,
       "uxos-aiohab": uxos_aiohab,
       "uxos-aiomsb": uxos_aiomsb,
       "uxos-lioinfo": uxos_lioinfo,
       "uxos-lioTable": uxos_lioTable,
       "uxos-lioEntry": uxos_lioEntry,
       "uxos-lioSysName": uxos_lioSysName,
       "uxos-lioInstName": uxos_lioInstName,
       "uxos-lioSubAddr": uxos_lioSubAddr,
       "uxos-liocall": uxos_liocall,
       "uxos-lioread": uxos_lioread,
       "uxos-liowrite": uxos_liowrite,
       "uxos-liolock": uxos_liolock,
       "uxos-liopoll": uxos_liopoll,
       "uxos-liowait": uxos_liowait,
       "uxos-ipcinfo": uxos_ipcinfo,
       "uxos-ipcTable": uxos_ipcTable,
       "uxos-ipcEntry": uxos_ipcEntry,
       "uxos-ipcSysName": uxos_ipcSysName,
       "uxos-ipcInstName": uxos_ipcInstName,
       "uxos-ipcSubAddr": uxos_ipcSubAddr,
       "uxos-shm-get": uxos_shm_get,
       "uxos-shm-get-fail": uxos_shm_get_fail,
       "uxos-shm-atch": uxos_shm_atch,
       "uxos-shm-atch-fail": uxos_shm_atch_fail,
       "uxos-shm-dtch": uxos_shm_dtch,
       "uxos-shm-cntl": uxos_shm_cntl,
       "uxos-msg-get": uxos_msg_get,
       "uxos-msg-get-fail": uxos_msg_get_fail,
       "uxos-msg-snd": uxos_msg_snd,
       "uxos-msg-snd-fail": uxos_msg_snd_fail,
       "uxos-msg-snd-sleep": uxos_msg_snd_sleep,
       "uxos-msg-snd-intr": uxos_msg_snd_intr,
       "uxos-msg-snd-again": uxos_msg_snd_again,
       "uxos-msg-rcv": uxos_msg_rcv,
       "uxos-msg-rcv-fail": uxos_msg_rcv_fail,
       "uxos-msg-rcv-sleep": uxos_msg_rcv_sleep,
       "uxos-msg-rcv-intr": uxos_msg_rcv_intr,
       "uxos-msg-rcv-again": uxos_msg_rcv_again,
       "uxos-msg-cntl": uxos_msg_cntl,
       "uxos-msg-lock-sleep": uxos_msg_lock_sleep,
       "uxos-sem-get": uxos_sem_get,
       "uxos-sem-get-fail": uxos_sem_get_fail,
       "uxos-sem-op": uxos_sem_op,
       "uxos-sem-op-fail": uxos_sem_op_fail,
       "uxos-sem-op-sleep": uxos_sem_op_sleep,
       "uxos-sem-op-intr": uxos_sem_op_intr,
       "uxos-sem-op-again": uxos_sem_op_again,
       "uxos-sem-cntl": uxos_sem_cntl,
       "uxos-flockinfo": uxos_flockinfo,
       "uxos-flockTable": uxos_flockTable,
       "uxos-flockEntry": uxos_flockEntry,
       "uxos-flockSysName": uxos_flockSysName,
       "uxos-flockInstName": uxos_flockInstName,
       "uxos-flockSubAddr": uxos_flockSubAddr,
       "uxos-lock-read": uxos_lock_read,
       "uxos-lock-rd-fail": uxos_lock_rd_fail,
       "uxos-lock-rd-sleep": uxos_lock_rd_sleep,
       "uxos-lock-rd-intr": uxos_lock_rd_intr,
       "uxos-lock-rd-again": uxos_lock_rd_again,
       "uxos-lock-write": uxos_lock_write,
       "uxos-lock-wr-fail": uxos_lock_wr_fail,
       "uxos-lock-wr-sleep": uxos_lock_wr_sleep,
       "uxos-lock-wr-intr": uxos_lock_wr_intr,
       "uxos-lock-wr-again": uxos_lock_wr_again,
       "uxos-unlock": uxos_unlock,
       "uxos-segminfo": uxos_segminfo,
       "uxos-smTable": uxos_smTable,
       "uxos-smEntry": uxos_smEntry,
       "uxos-smSysName": uxos_smSysName,
       "uxos-smInstName": uxos_smInstName,
       "uxos-smSubAddr": uxos_smSubAddr,
       "uxos-fault": uxos_fault,
       "uxos-faulta": uxos_faulta,
       "uxos-getmap": uxos_getmap,
       "uxos-get-use": uxos_get_use,
       "uxos-get-reclaim": uxos_get_reclaim,
       "uxos-get-reuse": uxos_get_reuse,
       "uxos-rel-async": uxos_rel_async,
       "uxos-rel-write": uxos_rel_write,
       "uxos-rel-free": uxos_rel_free,
       "uxos-rel-abort": uxos_rel_abort,
       "uxos-rel-dontneed": uxos_rel_dontneed,
       "uxos-release": uxos_release,
       "uxos-pagecreate": uxos_pagecreate,
       "uxos-pagemiss": uxos_pagemiss,
       "uxos-pagemissatch": uxos_pagemissatch,
       "uxos-vxinfo": uxos_vxinfo,
       "uxos-vxTable": uxos_vxTable,
       "uxos-vxEntry": uxos_vxEntry,
       "uxos-vxSysName": uxos_vxSysName,
       "uxos-vxInstName": uxos_vxInstName,
       "uxos-vxSubAddr": uxos_vxSubAddr,
       "uxos-vxipage": uxos_vxipage,
       "uxos-vxinopage": uxos_vxinopage,
       "uxos-vxinodeovf": uxos_vxinodeovf,
       "pc-win": pc_win,
       "winlms-systemrm": winlms_systemrm,
       "winlms-system": winlms_system,
       "winlms-systemrmTable": winlms_systemrmTable,
       "winlms-systemrmEntry": winlms_systemrmEntry,
       "winlms-systemrmSysName": winlms_systemrmSysName,
       "winlms-systemrmInstName": winlms_systemrmInstName,
       "winlms-systemrmSubAddr": winlms_systemrmSubAddr,
       "winlms-nms": winlms_nms,
       "winlms-sdrm": winlms_sdrm,
       "winlms-sdrmTable": winlms_sdrmTable,
       "winlms-sdrmEntry": winlms_sdrmEntry,
       "winlms-sdrmSysName": winlms_sdrmSysName,
       "winlms-sdrmInstName": winlms_sdrmInstName,
       "winlms-sdrmSubAddr": winlms_sdrmSubAddr,
       "win-nt": win_nt,
       "ntlms-systemrm": ntlms_systemrm,
       "ntlms-system": ntlms_system,
       "ntlms-systemrmTable": ntlms_systemrmTable,
       "ntlms-systemrmEntry": ntlms_systemrmEntry,
       "ntlms-systemrmSysName": ntlms_systemrmSysName,
       "ntlms-systemrmInstName": ntlms_systemrmInstName,
       "ntlms-systemrmSubAddr": ntlms_systemrmSubAddr,
       "ntlms-nms": ntlms_nms,
       "ntlms-sdrm": ntlms_sdrm,
       "ntlms-sdrmTable": ntlms_sdrmTable,
       "ntlms-sdrmEntry": ntlms_sdrmEntry,
       "ntlms-sdrmSysName": ntlms_sdrmSysName,
       "ntlms-sdrmInstName": ntlms_sdrmInstName,
       "ntlms-sdrmSubAddr": ntlms_sdrmSubAddr,
       "pc-dos": pc_dos,
       "lms-sys-map": lms_sys_map,
       "lmssysmapTable": lmssysmapTable,
       "lmssysmapEntry": lmssysmapEntry,
       "lmsSystemName": lmsSystemName,
       "lmsSystemStatus": lmsSystemStatus,
       "lmsSystemType": lmsSystemType,
       "lmsSystemClass": lmsSystemClass,
       "lms-trap": lms_trap,
       "lms-SysName": lms_SysName,
       "lms-SubAddress": lms_SubAddress,
       "lms-LogType": lms_LogType,
       "lms-FilterType": lms_FilterType,
       "lms-RecLevel": lms_RecLevel,
       "lms-RecCode": lms_RecCode,
       "lms-ProductId": lms_ProductId,
       "lms-Class": lms_Class,
       "lms-SubClass": lms_SubClass,
       "lms-ResourceName": lms_ResourceName,
       "lms-GenerationDate": lms_GenerationDate,
       "lms-LogString": lms_LogString}
)
