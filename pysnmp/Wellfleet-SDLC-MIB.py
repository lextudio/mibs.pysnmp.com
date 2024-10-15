# SNMP MIB module (Wellfleet-SDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:04 2024
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

(wfSdlcGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSdlcGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSdlc_ObjectIdentity = ObjectIdentity
wfSdlc = _WfSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 1)
)


class _WfSdlcDelete_Type(Integer32):
    """Custom type wfSdlcDelete based on Integer32"""
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


_WfSdlcDelete_Type.__name__ = "Integer32"
_WfSdlcDelete_Object = MibScalar
wfSdlcDelete = _WfSdlcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 1, 1),
    _WfSdlcDelete_Type()
)
wfSdlcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcDelete.setStatus("mandatory")


class _WfSdlcDisable_Type(Integer32):
    """Custom type wfSdlcDisable based on Integer32"""
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


_WfSdlcDisable_Type.__name__ = "Integer32"
_WfSdlcDisable_Object = MibScalar
wfSdlcDisable = _WfSdlcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 1, 2),
    _WfSdlcDisable_Type()
)
wfSdlcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcDisable.setStatus("mandatory")


class _WfSdlcState_Type(Integer32):
    """Custom type wfSdlcState based on Integer32"""
    defaultValue = 2

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
          ("notpresent", 4),
          ("up", 1))
    )


_WfSdlcState_Type.__name__ = "Integer32"
_WfSdlcState_Object = MibScalar
wfSdlcState = _WfSdlcState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 1, 3),
    _WfSdlcState_Type()
)
wfSdlcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcState.setStatus("mandatory")
_WfSdlcPortAdminTable_Object = MibTable
wfSdlcPortAdminTable = _WfSdlcPortAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    wfSdlcPortAdminTable.setStatus("mandatory")
_WfSdlcPortAdminEntry_Object = MibTableRow
wfSdlcPortAdminEntry = _WfSdlcPortAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1)
)
wfSdlcPortAdminEntry.setIndexNames(
    (0, "Wellfleet-SDLC-MIB", "wfSdlcPortAdminIndex"),
)
if mibBuilder.loadTexts:
    wfSdlcPortAdminEntry.setStatus("mandatory")


class _WfSdlcPortAdminDelete_Type(Integer32):
    """Custom type wfSdlcPortAdminDelete based on Integer32"""
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


_WfSdlcPortAdminDelete_Type.__name__ = "Integer32"
_WfSdlcPortAdminDelete_Object = MibTableColumn
wfSdlcPortAdminDelete = _WfSdlcPortAdminDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 1),
    _WfSdlcPortAdminDelete_Type()
)
wfSdlcPortAdminDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminDelete.setStatus("mandatory")


class _WfSdlcPortAdminDisable_Type(Integer32):
    """Custom type wfSdlcPortAdminDisable based on Integer32"""
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


_WfSdlcPortAdminDisable_Type.__name__ = "Integer32"
_WfSdlcPortAdminDisable_Object = MibTableColumn
wfSdlcPortAdminDisable = _WfSdlcPortAdminDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 2),
    _WfSdlcPortAdminDisable_Type()
)
wfSdlcPortAdminDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminDisable.setStatus("mandatory")
_WfSdlcPortAdminIndex_Type = Integer32
_WfSdlcPortAdminIndex_Object = MibTableColumn
wfSdlcPortAdminIndex = _WfSdlcPortAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 3),
    _WfSdlcPortAdminIndex_Type()
)
wfSdlcPortAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortAdminIndex.setStatus("mandatory")
_WfSdlcPortAdminAddress4_Type = DisplayString
_WfSdlcPortAdminAddress4_Object = MibTableColumn
wfSdlcPortAdminAddress4 = _WfSdlcPortAdminAddress4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 4),
    _WfSdlcPortAdminAddress4_Type()
)
wfSdlcPortAdminAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminAddress4.setStatus("mandatory")


class _WfSdlcPortAdminType_Type(Integer32):
    """Custom type wfSdlcPortAdminType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("switched", 2))
    )


_WfSdlcPortAdminType_Type.__name__ = "Integer32"
_WfSdlcPortAdminType_Object = MibTableColumn
wfSdlcPortAdminType = _WfSdlcPortAdminType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 5),
    _WfSdlcPortAdminType_Type()
)
wfSdlcPortAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminType.setStatus("mandatory")


class _WfSdlcPortAdminTopology_Type(Integer32):
    """Custom type wfSdlcPortAdminTopology based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 2),
          ("ptop", 1))
    )


_WfSdlcPortAdminTopology_Type.__name__ = "Integer32"
_WfSdlcPortAdminTopology_Object = MibTableColumn
wfSdlcPortAdminTopology = _WfSdlcPortAdminTopology_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 6),
    _WfSdlcPortAdminTopology_Type()
)
wfSdlcPortAdminTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminTopology.setStatus("mandatory")


class _WfSdlcPortAdminACTIVTO_Type(Integer32):
    """Custom type wfSdlcPortAdminACTIVTO based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_WfSdlcPortAdminACTIVTO_Type.__name__ = "Integer32"
_WfSdlcPortAdminACTIVTO_Object = MibTableColumn
wfSdlcPortAdminACTIVTO = _WfSdlcPortAdminACTIVTO_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 7),
    _WfSdlcPortAdminACTIVTO_Type()
)
wfSdlcPortAdminACTIVTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminACTIVTO.setStatus("mandatory")


class _WfSdlcPortAdminPAUSE_Type(Integer32):
    """Custom type wfSdlcPortAdminPAUSE based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WfSdlcPortAdminPAUSE_Type.__name__ = "Integer32"
_WfSdlcPortAdminPAUSE_Object = MibTableColumn
wfSdlcPortAdminPAUSE = _WfSdlcPortAdminPAUSE_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 8),
    _WfSdlcPortAdminPAUSE_Type()
)
wfSdlcPortAdminPAUSE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminPAUSE.setStatus("mandatory")


class _WfSdlcPortAdminCredit_Type(Integer32):
    """Custom type wfSdlcPortAdminCredit based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_WfSdlcPortAdminCredit_Type.__name__ = "Integer32"
_WfSdlcPortAdminCredit_Object = MibTableColumn
wfSdlcPortAdminCredit = _WfSdlcPortAdminCredit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 9),
    _WfSdlcPortAdminCredit_Type()
)
wfSdlcPortAdminCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminCredit.setStatus("mandatory")


class _WfSdlcPortAdminIdleTimer_Type(Integer32):
    """Custom type wfSdlcPortAdminIdleTimer based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfSdlcPortAdminIdleTimer_Type.__name__ = "Integer32"
_WfSdlcPortAdminIdleTimer_Object = MibTableColumn
wfSdlcPortAdminIdleTimer = _WfSdlcPortAdminIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 10),
    _WfSdlcPortAdminIdleTimer_Type()
)
wfSdlcPortAdminIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminIdleTimer.setStatus("mandatory")


class _WfSdlcPortAdminIdleRetry_Type(Integer32):
    """Custom type wfSdlcPortAdminIdleRetry based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSdlcPortAdminIdleRetry_Type.__name__ = "Integer32"
_WfSdlcPortAdminIdleRetry_Object = MibTableColumn
wfSdlcPortAdminIdleRetry = _WfSdlcPortAdminIdleRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 11),
    _WfSdlcPortAdminIdleRetry_Type()
)
wfSdlcPortAdminIdleRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminIdleRetry.setStatus("mandatory")


class _WfSdlcPortAdminNPRcvTimer_Type(Integer32):
    """Custom type wfSdlcPortAdminNPRcvTimer based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfSdlcPortAdminNPRcvTimer_Type.__name__ = "Integer32"
_WfSdlcPortAdminNPRcvTimer_Object = MibTableColumn
wfSdlcPortAdminNPRcvTimer = _WfSdlcPortAdminNPRcvTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 12),
    _WfSdlcPortAdminNPRcvTimer_Type()
)
wfSdlcPortAdminNPRcvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminNPRcvTimer.setStatus("mandatory")


class _WfSdlcPortAdminNPRcvRetry_Type(Integer32):
    """Custom type wfSdlcPortAdminNPRcvRetry based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSdlcPortAdminNPRcvRetry_Type.__name__ = "Integer32"
_WfSdlcPortAdminNPRcvRetry_Object = MibTableColumn
wfSdlcPortAdminNPRcvRetry = _WfSdlcPortAdminNPRcvRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 13),
    _WfSdlcPortAdminNPRcvRetry_Type()
)
wfSdlcPortAdminNPRcvRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminNPRcvRetry.setStatus("mandatory")


class _WfSdlcPortAdminWriteTimer_Type(Integer32):
    """Custom type wfSdlcPortAdminWriteTimer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfSdlcPortAdminWriteTimer_Type.__name__ = "Integer32"
_WfSdlcPortAdminWriteTimer_Object = MibTableColumn
wfSdlcPortAdminWriteTimer = _WfSdlcPortAdminWriteTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 14),
    _WfSdlcPortAdminWriteTimer_Type()
)
wfSdlcPortAdminWriteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminWriteTimer.setStatus("mandatory")


class _WfSdlcPortAdminWriteRetry_Type(Integer32):
    """Custom type wfSdlcPortAdminWriteRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSdlcPortAdminWriteRetry_Type.__name__ = "Integer32"
_WfSdlcPortAdminWriteRetry_Object = MibTableColumn
wfSdlcPortAdminWriteRetry = _WfSdlcPortAdminWriteRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 15),
    _WfSdlcPortAdminWriteRetry_Type()
)
wfSdlcPortAdminWriteRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminWriteRetry.setStatus("mandatory")


class _WfSdlcPortAdminLinkConnTimer_Type(Integer32):
    """Custom type wfSdlcPortAdminLinkConnTimer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfSdlcPortAdminLinkConnTimer_Type.__name__ = "Integer32"
_WfSdlcPortAdminLinkConnTimer_Object = MibTableColumn
wfSdlcPortAdminLinkConnTimer = _WfSdlcPortAdminLinkConnTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 16),
    _WfSdlcPortAdminLinkConnTimer_Type()
)
wfSdlcPortAdminLinkConnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminLinkConnTimer.setStatus("mandatory")


class _WfSdlcPortAdminLinkConnRetry_Type(Integer32):
    """Custom type wfSdlcPortAdminLinkConnRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSdlcPortAdminLinkConnRetry_Type.__name__ = "Integer32"
_WfSdlcPortAdminLinkConnRetry_Object = MibTableColumn
wfSdlcPortAdminLinkConnRetry = _WfSdlcPortAdminLinkConnRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 17),
    _WfSdlcPortAdminLinkConnRetry_Type()
)
wfSdlcPortAdminLinkConnRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminLinkConnRetry.setStatus("mandatory")


class _WfSdlcPortAdminPriFdplx_Type(Integer32):
    """Custom type wfSdlcPortAdminPriFdplx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfSdlcPortAdminPriFdplx_Type.__name__ = "Integer32"
_WfSdlcPortAdminPriFdplx_Object = MibTableColumn
wfSdlcPortAdminPriFdplx = _WfSdlcPortAdminPriFdplx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 18),
    _WfSdlcPortAdminPriFdplx_Type()
)
wfSdlcPortAdminPriFdplx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminPriFdplx.setStatus("mandatory")


class _WfSdlcPortAdminSecFdplx_Type(Integer32):
    """Custom type wfSdlcPortAdminSecFdplx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfSdlcPortAdminSecFdplx_Type.__name__ = "Integer32"
_WfSdlcPortAdminSecFdplx_Object = MibTableColumn
wfSdlcPortAdminSecFdplx = _WfSdlcPortAdminSecFdplx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 19),
    _WfSdlcPortAdminSecFdplx_Type()
)
wfSdlcPortAdminSecFdplx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminSecFdplx.setStatus("mandatory")


class _WfSdlcPortAdminUseRej_Type(Integer32):
    """Custom type wfSdlcPortAdminUseRej based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfSdlcPortAdminUseRej_Type.__name__ = "Integer32"
_WfSdlcPortAdminUseRej_Object = MibTableColumn
wfSdlcPortAdminUseRej = _WfSdlcPortAdminUseRej_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 20),
    _WfSdlcPortAdminUseRej_Type()
)
wfSdlcPortAdminUseRej.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminUseRej.setStatus("mandatory")


class _WfSdlcPortAdminPortType_Type(Integer32):
    """Custom type wfSdlcPortAdminPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoanswer", 3),
          ("autoanswerdialout", 4),
          ("dialout", 2),
          ("leased", 1),
          ("mananswer", 6),
          ("mananswerdialout", 7),
          ("mandialout", 5))
    )


_WfSdlcPortAdminPortType_Type.__name__ = "Integer32"
_WfSdlcPortAdminPortType_Object = MibTableColumn
wfSdlcPortAdminPortType = _WfSdlcPortAdminPortType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 21),
    _WfSdlcPortAdminPortType_Type()
)
wfSdlcPortAdminPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminPortType.setStatus("mandatory")


class _WfSdlcPortAdminMaxXidSize_Type(Integer32):
    """Custom type wfSdlcPortAdminMaxXidSize based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WfSdlcPortAdminMaxXidSize_Type.__name__ = "Integer32"
_WfSdlcPortAdminMaxXidSize_Object = MibTableColumn
wfSdlcPortAdminMaxXidSize = _WfSdlcPortAdminMaxXidSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 22),
    _WfSdlcPortAdminMaxXidSize_Type()
)
wfSdlcPortAdminMaxXidSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminMaxXidSize.setStatus("mandatory")


class _WfSdlcPortAdminMaxRetryCount_Type(Integer32):
    """Custom type wfSdlcPortAdminMaxRetryCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_WfSdlcPortAdminMaxRetryCount_Type.__name__ = "Integer32"
_WfSdlcPortAdminMaxRetryCount_Object = MibTableColumn
wfSdlcPortAdminMaxRetryCount = _WfSdlcPortAdminMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 23),
    _WfSdlcPortAdminMaxRetryCount_Type()
)
wfSdlcPortAdminMaxRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminMaxRetryCount.setStatus("mandatory")


class _WfSdlcPortAdminMaxFrameSize_Type(Integer32):
    """Custom type wfSdlcPortAdminMaxFrameSize based on Integer32"""
    defaultValue = 1033

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(265,
              521,
              1033,
              2057,
              4105)
        )
    )
    namedValues = NamedValues(
        *(("pdu0265", 265),
          ("pdu0521", 521),
          ("pdu1033", 1033),
          ("pdu2057", 2057),
          ("pdu4105", 4105))
    )


_WfSdlcPortAdminMaxFrameSize_Type.__name__ = "Integer32"
_WfSdlcPortAdminMaxFrameSize_Object = MibTableColumn
wfSdlcPortAdminMaxFrameSize = _WfSdlcPortAdminMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 24),
    _WfSdlcPortAdminMaxFrameSize_Type()
)
wfSdlcPortAdminMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminMaxFrameSize.setStatus("mandatory")
_WfSdlcPortAdminDlcName8_Type = DisplayString
_WfSdlcPortAdminDlcName8_Object = MibTableColumn
wfSdlcPortAdminDlcName8 = _WfSdlcPortAdminDlcName8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 25),
    _WfSdlcPortAdminDlcName8_Type()
)
wfSdlcPortAdminDlcName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminDlcName8.setStatus("mandatory")


class _WfSdlcPortAdminCpType_Type(Integer32):
    """Custom type wfSdlcPortAdminCpType based on Integer32"""
    defaultValue = 3

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
        *(("end", 4),
          ("learn", 1),
          ("len", 2),
          ("network", 3),
          ("vrn", 5))
    )


_WfSdlcPortAdminCpType_Type.__name__ = "Integer32"
_WfSdlcPortAdminCpType_Object = MibTableColumn
wfSdlcPortAdminCpType = _WfSdlcPortAdminCpType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 26),
    _WfSdlcPortAdminCpType_Type()
)
wfSdlcPortAdminCpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminCpType.setStatus("mandatory")


class _WfSdlcPortAdminLsRole_Type(Integer32):
    """Custom type wfSdlcPortAdminLsRole based on Integer32"""
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
        *(("neg", 1),
          ("pri", 2),
          ("sec", 3))
    )


_WfSdlcPortAdminLsRole_Type.__name__ = "Integer32"
_WfSdlcPortAdminLsRole_Object = MibTableColumn
wfSdlcPortAdminLsRole = _WfSdlcPortAdminLsRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 27),
    _WfSdlcPortAdminLsRole_Type()
)
wfSdlcPortAdminLsRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminLsRole.setStatus("mandatory")


class _WfSdlcPortAdminPortNumber_Type(Integer32):
    """Custom type wfSdlcPortAdminPortNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_WfSdlcPortAdminPortNumber_Type.__name__ = "Integer32"
_WfSdlcPortAdminPortNumber_Object = MibTableColumn
wfSdlcPortAdminPortNumber = _WfSdlcPortAdminPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 28),
    _WfSdlcPortAdminPortNumber_Type()
)
wfSdlcPortAdminPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminPortNumber.setStatus("mandatory")


class _WfSdlcPortAdminLsAddress_Type(Integer32):
    """Custom type wfSdlcPortAdminLsAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfSdlcPortAdminLsAddress_Type.__name__ = "Integer32"
_WfSdlcPortAdminLsAddress_Object = MibTableColumn
wfSdlcPortAdminLsAddress = _WfSdlcPortAdminLsAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 29),
    _WfSdlcPortAdminLsAddress_Type()
)
wfSdlcPortAdminLsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminLsAddress.setStatus("mandatory")


class _WfSdlcPortAdminTotLsActLim_Type(Integer32):
    """Custom type wfSdlcPortAdminTotLsActLim based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfSdlcPortAdminTotLsActLim_Type.__name__ = "Integer32"
_WfSdlcPortAdminTotLsActLim_Object = MibTableColumn
wfSdlcPortAdminTotLsActLim = _WfSdlcPortAdminTotLsActLim_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 30),
    _WfSdlcPortAdminTotLsActLim_Type()
)
wfSdlcPortAdminTotLsActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminTotLsActLim.setStatus("mandatory")


class _WfSdlcPortAdminInLsActLim_Type(Integer32):
    """Custom type wfSdlcPortAdminInLsActLim based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfSdlcPortAdminInLsActLim_Type.__name__ = "Integer32"
_WfSdlcPortAdminInLsActLim_Object = MibTableColumn
wfSdlcPortAdminInLsActLim = _WfSdlcPortAdminInLsActLim_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 31),
    _WfSdlcPortAdminInLsActLim_Type()
)
wfSdlcPortAdminInLsActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminInLsActLim.setStatus("mandatory")


class _WfSdlcPortAdminOutLsActLim_Type(Integer32):
    """Custom type wfSdlcPortAdminOutLsActLim based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfSdlcPortAdminOutLsActLim_Type.__name__ = "Integer32"
_WfSdlcPortAdminOutLsActLim_Object = MibTableColumn
wfSdlcPortAdminOutLsActLim = _WfSdlcPortAdminOutLsActLim_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 32),
    _WfSdlcPortAdminOutLsActLim_Type()
)
wfSdlcPortAdminOutLsActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminOutLsActLim.setStatus("mandatory")


class _WfSdlcPortAdminNegLsSupp_Type(Integer32):
    """Custom type wfSdlcPortAdminNegLsSupp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfSdlcPortAdminNegLsSupp_Type.__name__ = "Integer32"
_WfSdlcPortAdminNegLsSupp_Object = MibTableColumn
wfSdlcPortAdminNegLsSupp = _WfSdlcPortAdminNegLsSupp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 33),
    _WfSdlcPortAdminNegLsSupp_Type()
)
wfSdlcPortAdminNegLsSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminNegLsSupp.setStatus("mandatory")


class _WfSdlcPortAdminRcvPoolSize_Type(Integer32):
    """Custom type wfSdlcPortAdminRcvPoolSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSdlcPortAdminRcvPoolSize_Type.__name__ = "Integer32"
_WfSdlcPortAdminRcvPoolSize_Object = MibTableColumn
wfSdlcPortAdminRcvPoolSize = _WfSdlcPortAdminRcvPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 34),
    _WfSdlcPortAdminRcvPoolSize_Type()
)
wfSdlcPortAdminRcvPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminRcvPoolSize.setStatus("mandatory")


class _WfSdlcPortAdminStatsColl_Type(Integer32):
    """Custom type wfSdlcPortAdminStatsColl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfSdlcPortAdminStatsColl_Type.__name__ = "Integer32"
_WfSdlcPortAdminStatsColl_Object = MibTableColumn
wfSdlcPortAdminStatsColl = _WfSdlcPortAdminStatsColl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 35),
    _WfSdlcPortAdminStatsColl_Type()
)
wfSdlcPortAdminStatsColl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminStatsColl.setStatus("mandatory")


class _WfSdlcPortAdminDebugFlg_Type(Integer32):
    """Custom type wfSdlcPortAdminDebugFlg based on Integer32"""
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


_WfSdlcPortAdminDebugFlg_Type.__name__ = "Integer32"
_WfSdlcPortAdminDebugFlg_Object = MibTableColumn
wfSdlcPortAdminDebugFlg = _WfSdlcPortAdminDebugFlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 2, 1, 36),
    _WfSdlcPortAdminDebugFlg_Type()
)
wfSdlcPortAdminDebugFlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcPortAdminDebugFlg.setStatus("mandatory")
_WfSdlcPortOperTable_Object = MibTable
wfSdlcPortOperTable = _WfSdlcPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3)
)
if mibBuilder.loadTexts:
    wfSdlcPortOperTable.setStatus("mandatory")
_WfSdlcPortOperEntry_Object = MibTableRow
wfSdlcPortOperEntry = _WfSdlcPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1)
)
wfSdlcPortOperEntry.setIndexNames(
    (0, "Wellfleet-SDLC-MIB", "wfSdlcPortOperIndex"),
)
if mibBuilder.loadTexts:
    wfSdlcPortOperEntry.setStatus("mandatory")
_WfSdlcPortOperIndex_Type = Integer32
_WfSdlcPortOperIndex_Object = MibTableColumn
wfSdlcPortOperIndex = _WfSdlcPortOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 1),
    _WfSdlcPortOperIndex_Type()
)
wfSdlcPortOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperIndex.setStatus("mandatory")
_WfSdlcPortOperAddress4_Type = DisplayString
_WfSdlcPortOperAddress4_Object = MibTableColumn
wfSdlcPortOperAddress4 = _WfSdlcPortOperAddress4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 2),
    _WfSdlcPortOperAddress4_Type()
)
wfSdlcPortOperAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperAddress4.setStatus("mandatory")


class _WfSdlcPortOperRole_Type(Integer32):
    """Custom type wfSdlcPortOperRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("neg", 4),
          ("pri", 2),
          ("sec", 1))
    )


_WfSdlcPortOperRole_Type.__name__ = "Integer32"
_WfSdlcPortOperRole_Object = MibTableColumn
wfSdlcPortOperRole = _WfSdlcPortOperRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 3),
    _WfSdlcPortOperRole_Type()
)
wfSdlcPortOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperRole.setStatus("mandatory")


class _WfSdlcPortOperType_Type(Integer32):
    """Custom type wfSdlcPortOperType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("switched", 2))
    )


_WfSdlcPortOperType_Type.__name__ = "Integer32"
_WfSdlcPortOperType_Object = MibTableColumn
wfSdlcPortOperType = _WfSdlcPortOperType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 4),
    _WfSdlcPortOperType_Type()
)
wfSdlcPortOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperType.setStatus("mandatory")


class _WfSdlcPortOperTopology_Type(Integer32):
    """Custom type wfSdlcPortOperTopology based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 2),
          ("ptop", 1))
    )


_WfSdlcPortOperTopology_Type.__name__ = "Integer32"
_WfSdlcPortOperTopology_Object = MibTableColumn
wfSdlcPortOperTopology = _WfSdlcPortOperTopology_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 5),
    _WfSdlcPortOperTopology_Type()
)
wfSdlcPortOperTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperTopology.setStatus("mandatory")
_WfSdlcPortOperACTIVTO_Type = Integer32
_WfSdlcPortOperACTIVTO_Object = MibTableColumn
wfSdlcPortOperACTIVTO = _WfSdlcPortOperACTIVTO_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 6),
    _WfSdlcPortOperACTIVTO_Type()
)
wfSdlcPortOperACTIVTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperACTIVTO.setStatus("mandatory")
_WfSdlcPortOperPAUSE_Type = Integer32
_WfSdlcPortOperPAUSE_Object = MibTableColumn
wfSdlcPortOperPAUSE = _WfSdlcPortOperPAUSE_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 7),
    _WfSdlcPortOperPAUSE_Type()
)
wfSdlcPortOperPAUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperPAUSE.setStatus("mandatory")


class _WfSdlcPortOperSlowPollMethod_Type(Integer32):
    """Custom type wfSdlcPortOperSlowPollMethod based on Integer32"""
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
        *(("other", 3),
          ("pause", 2),
          ("servlim", 1))
    )


_WfSdlcPortOperSlowPollMethod_Type.__name__ = "Integer32"
_WfSdlcPortOperSlowPollMethod_Object = MibTableColumn
wfSdlcPortOperSlowPollMethod = _WfSdlcPortOperSlowPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 8),
    _WfSdlcPortOperSlowPollMethod_Type()
)
wfSdlcPortOperSlowPollMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperSlowPollMethod.setStatus("mandatory")
_WfSdlcPortOperSlowPollTimer_Type = TimeTicks
_WfSdlcPortOperSlowPollTimer_Object = MibTableColumn
wfSdlcPortOperSlowPollTimer = _WfSdlcPortOperSlowPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 9),
    _WfSdlcPortOperSlowPollTimer_Type()
)
wfSdlcPortOperSlowPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperSlowPollTimer.setStatus("mandatory")


class _WfSdlcPortOperAbmSuppInd_Type(Integer32):
    """Custom type wfSdlcPortOperAbmSuppInd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 2),
          ("supported", 1))
    )


_WfSdlcPortOperAbmSuppInd_Type.__name__ = "Integer32"
_WfSdlcPortOperAbmSuppInd_Object = MibTableColumn
wfSdlcPortOperAbmSuppInd = _WfSdlcPortOperAbmSuppInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 10),
    _WfSdlcPortOperAbmSuppInd_Type()
)
wfSdlcPortOperAbmSuppInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperAbmSuppInd.setStatus("mandatory")


class _WfSdlcPortOperSimRimSupp_Type(Integer32):
    """Custom type wfSdlcPortOperSimRimSupp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 2),
          ("supported", 1))
    )


_WfSdlcPortOperSimRimSupp_Type.__name__ = "Integer32"
_WfSdlcPortOperSimRimSupp_Object = MibTableColumn
wfSdlcPortOperSimRimSupp = _WfSdlcPortOperSimRimSupp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 11),
    _WfSdlcPortOperSimRimSupp_Type()
)
wfSdlcPortOperSimRimSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperSimRimSupp.setStatus("mandatory")


class _WfSdlcPortOperSecInitNonactSupp_Type(Integer32):
    """Custom type wfSdlcPortOperSecInitNonactSupp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 2),
          ("supported", 1))
    )


_WfSdlcPortOperSecInitNonactSupp_Type.__name__ = "Integer32"
_WfSdlcPortOperSecInitNonactSupp_Object = MibTableColumn
wfSdlcPortOperSecInitNonactSupp = _WfSdlcPortOperSecInitNonactSupp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 3, 1, 12),
    _WfSdlcPortOperSecInitNonactSupp_Type()
)
wfSdlcPortOperSecInitNonactSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortOperSecInitNonactSupp.setStatus("mandatory")
_WfSdlcPortStatsTable_Object = MibTable
wfSdlcPortStatsTable = _WfSdlcPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 4)
)
if mibBuilder.loadTexts:
    wfSdlcPortStatsTable.setStatus("mandatory")
_WfSdlcPortStatsEntry_Object = MibTableRow
wfSdlcPortStatsEntry = _WfSdlcPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 4, 1)
)
wfSdlcPortStatsEntry.setIndexNames(
    (0, "Wellfleet-SDLC-MIB", "wfSdlcPortStatsIndex"),
)
if mibBuilder.loadTexts:
    wfSdlcPortStatsEntry.setStatus("mandatory")
_WfSdlcPortStatsIndex_Type = Integer32
_WfSdlcPortStatsIndex_Object = MibTableColumn
wfSdlcPortStatsIndex = _WfSdlcPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 4, 1, 1),
    _WfSdlcPortStatsIndex_Type()
)
wfSdlcPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortStatsIndex.setStatus("mandatory")
_WfSdlcPortStatsDwarfFrames_Type = Integer32
_WfSdlcPortStatsDwarfFrames_Object = MibTableColumn
wfSdlcPortStatsDwarfFrames = _WfSdlcPortStatsDwarfFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 4, 1, 2),
    _WfSdlcPortStatsDwarfFrames_Type()
)
wfSdlcPortStatsDwarfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcPortStatsDwarfFrames.setStatus("mandatory")
_WfSdlcLSAdminTable_Object = MibTable
wfSdlcLSAdminTable = _WfSdlcLSAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5)
)
if mibBuilder.loadTexts:
    wfSdlcLSAdminTable.setStatus("mandatory")
_WfSdlcLSAdminEntry_Object = MibTableRow
wfSdlcLSAdminEntry = _WfSdlcLSAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1)
)
wfSdlcLSAdminEntry.setIndexNames(
    (0, "Wellfleet-SDLC-MIB", "wfSdlcLSAdminIfIndex"),
    (0, "Wellfleet-SDLC-MIB", "wfSdlcLSAdminAddress"),
)
if mibBuilder.loadTexts:
    wfSdlcLSAdminEntry.setStatus("mandatory")


class _WfSdlcLSAdminDelete_Type(Integer32):
    """Custom type wfSdlcLSAdminDelete based on Integer32"""
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


_WfSdlcLSAdminDelete_Type.__name__ = "Integer32"
_WfSdlcLSAdminDelete_Object = MibTableColumn
wfSdlcLSAdminDelete = _WfSdlcLSAdminDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 1),
    _WfSdlcLSAdminDelete_Type()
)
wfSdlcLSAdminDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminDelete.setStatus("mandatory")


class _WfSdlcLSAdminDisable_Type(Integer32):
    """Custom type wfSdlcLSAdminDisable based on Integer32"""
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


_WfSdlcLSAdminDisable_Type.__name__ = "Integer32"
_WfSdlcLSAdminDisable_Object = MibTableColumn
wfSdlcLSAdminDisable = _WfSdlcLSAdminDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 2),
    _WfSdlcLSAdminDisable_Type()
)
wfSdlcLSAdminDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminDisable.setStatus("mandatory")
_WfSdlcLSAdminIfIndex_Type = Integer32
_WfSdlcLSAdminIfIndex_Object = MibTableColumn
wfSdlcLSAdminIfIndex = _WfSdlcLSAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 3),
    _WfSdlcLSAdminIfIndex_Type()
)
wfSdlcLSAdminIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSAdminIfIndex.setStatus("mandatory")
_WfSdlcLSAdminAddress_Type = Integer32
_WfSdlcLSAdminAddress_Object = MibTableColumn
wfSdlcLSAdminAddress = _WfSdlcLSAdminAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 4),
    _WfSdlcLSAdminAddress_Type()
)
wfSdlcLSAdminAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSAdminAddress.setStatus("mandatory")
_WfSdlcLSAdminGroupAddress_Type = Integer32
_WfSdlcLSAdminGroupAddress_Object = MibTableColumn
wfSdlcLSAdminGroupAddress = _WfSdlcLSAdminGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 5),
    _WfSdlcLSAdminGroupAddress_Type()
)
wfSdlcLSAdminGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminGroupAddress.setStatus("mandatory")


class _WfSdlcLSAdminRole_Type(Integer32):
    """Custom type wfSdlcLSAdminRole based on Integer32"""
    defaultValue = 2

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
        *(("msec", 4),
          ("negot", 1),
          ("primary", 2),
          ("sec", 3))
    )


_WfSdlcLSAdminRole_Type.__name__ = "Integer32"
_WfSdlcLSAdminRole_Object = MibTableColumn
wfSdlcLSAdminRole = _WfSdlcLSAdminRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 6),
    _WfSdlcLSAdminRole_Type()
)
wfSdlcLSAdminRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminRole.setStatus("mandatory")


class _WfSdlcLSAdminMAXDATA_Type(Integer32):
    """Custom type wfSdlcLSAdminMAXDATA based on Integer32"""
    defaultValue = 1033

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(265,
              521,
              1033,
              2057,
              4105)
        )
    )
    namedValues = NamedValues(
        *(("pdu0265", 265),
          ("pdu0521", 521),
          ("pdu1033", 1033),
          ("pdu2057", 2057),
          ("pdu4105", 4105))
    )


_WfSdlcLSAdminMAXDATA_Type.__name__ = "Integer32"
_WfSdlcLSAdminMAXDATA_Object = MibTableColumn
wfSdlcLSAdminMAXDATA = _WfSdlcLSAdminMAXDATA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 7),
    _WfSdlcLSAdminMAXDATA_Type()
)
wfSdlcLSAdminMAXDATA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminMAXDATA.setStatus("mandatory")


class _WfSdlcLSAdminREPLYTO_Type(Integer32):
    """Custom type wfSdlcLSAdminREPLYTO based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WfSdlcLSAdminREPLYTO_Type.__name__ = "Integer32"
_WfSdlcLSAdminREPLYTO_Object = MibTableColumn
wfSdlcLSAdminREPLYTO = _WfSdlcLSAdminREPLYTO_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 8),
    _WfSdlcLSAdminREPLYTO_Type()
)
wfSdlcLSAdminREPLYTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminREPLYTO.setStatus("mandatory")


class _WfSdlcLSAdminMAXIN_Type(Integer32):
    """Custom type wfSdlcLSAdminMAXIN based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfSdlcLSAdminMAXIN_Type.__name__ = "Integer32"
_WfSdlcLSAdminMAXIN_Object = MibTableColumn
wfSdlcLSAdminMAXIN = _WfSdlcLSAdminMAXIN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 9),
    _WfSdlcLSAdminMAXIN_Type()
)
wfSdlcLSAdminMAXIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminMAXIN.setStatus("mandatory")


class _WfSdlcLSAdminMAXOUT_Type(Integer32):
    """Custom type wfSdlcLSAdminMAXOUT based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfSdlcLSAdminMAXOUT_Type.__name__ = "Integer32"
_WfSdlcLSAdminMAXOUT_Object = MibTableColumn
wfSdlcLSAdminMAXOUT = _WfSdlcLSAdminMAXOUT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 10),
    _WfSdlcLSAdminMAXOUT_Type()
)
wfSdlcLSAdminMAXOUT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminMAXOUT.setStatus("mandatory")


class _WfSdlcLSAdminMODULO_Type(Integer32):
    """Custom type wfSdlcLSAdminMODULO based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("default", 8),
          ("extended", 128))
    )


_WfSdlcLSAdminMODULO_Type.__name__ = "Integer32"
_WfSdlcLSAdminMODULO_Object = MibTableColumn
wfSdlcLSAdminMODULO = _WfSdlcLSAdminMODULO_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 11),
    _WfSdlcLSAdminMODULO_Type()
)
wfSdlcLSAdminMODULO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminMODULO.setStatus("mandatory")


class _WfSdlcLSAdminRETRIESm_Type(Integer32):
    """Custom type wfSdlcLSAdminRETRIESm based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WfSdlcLSAdminRETRIESm_Type.__name__ = "Integer32"
_WfSdlcLSAdminRETRIESm_Object = MibTableColumn
wfSdlcLSAdminRETRIESm = _WfSdlcLSAdminRETRIESm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 12),
    _WfSdlcLSAdminRETRIESm_Type()
)
wfSdlcLSAdminRETRIESm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminRETRIESm.setStatus("mandatory")


class _WfSdlcLSAdminRETRIESt_Type(Integer32):
    """Custom type wfSdlcLSAdminRETRIESt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfSdlcLSAdminRETRIESt_Type.__name__ = "Integer32"
_WfSdlcLSAdminRETRIESt_Object = MibTableColumn
wfSdlcLSAdminRETRIESt = _WfSdlcLSAdminRETRIESt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 13),
    _WfSdlcLSAdminRETRIESt_Type()
)
wfSdlcLSAdminRETRIESt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminRETRIESt.setStatus("mandatory")


class _WfSdlcLSAdminRETRIESn_Type(Integer32):
    """Custom type wfSdlcLSAdminRETRIESn based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfSdlcLSAdminRETRIESn_Type.__name__ = "Integer32"
_WfSdlcLSAdminRETRIESn_Object = MibTableColumn
wfSdlcLSAdminRETRIESn = _WfSdlcLSAdminRETRIESn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 14),
    _WfSdlcLSAdminRETRIESn_Type()
)
wfSdlcLSAdminRETRIESn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminRETRIESn.setStatus("mandatory")


class _WfSdlcLSAdminRNRLIMIT_Type(Integer32):
    """Custom type wfSdlcLSAdminRNRLIMIT based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_WfSdlcLSAdminRNRLIMIT_Type.__name__ = "Integer32"
_WfSdlcLSAdminRNRLIMIT_Object = MibTableColumn
wfSdlcLSAdminRNRLIMIT = _WfSdlcLSAdminRNRLIMIT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 15),
    _WfSdlcLSAdminRNRLIMIT_Type()
)
wfSdlcLSAdminRNRLIMIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminRNRLIMIT.setStatus("mandatory")


class _WfSdlcLSAdminContTimer_Type(Integer32):
    """Custom type wfSdlcLSAdminContTimer based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminContTimer_Type.__name__ = "Integer32"
_WfSdlcLSAdminContTimer_Object = MibTableColumn
wfSdlcLSAdminContTimer = _WfSdlcLSAdminContTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 16),
    _WfSdlcLSAdminContTimer_Type()
)
wfSdlcLSAdminContTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminContTimer.setStatus("mandatory")


class _WfSdlcLSAdminContTimerRetry_Type(Integer32):
    """Custom type wfSdlcLSAdminContTimerRetry based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminContTimerRetry_Type.__name__ = "Integer32"
_WfSdlcLSAdminContTimerRetry_Object = MibTableColumn
wfSdlcLSAdminContTimerRetry = _WfSdlcLSAdminContTimerRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 17),
    _WfSdlcLSAdminContTimerRetry_Type()
)
wfSdlcLSAdminContTimerRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminContTimerRetry.setStatus("mandatory")


class _WfSdlcLSAdminContTimer2_Type(Integer32):
    """Custom type wfSdlcLSAdminContTimer2 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminContTimer2_Type.__name__ = "Integer32"
_WfSdlcLSAdminContTimer2_Object = MibTableColumn
wfSdlcLSAdminContTimer2 = _WfSdlcLSAdminContTimer2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 18),
    _WfSdlcLSAdminContTimer2_Type()
)
wfSdlcLSAdminContTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminContTimer2.setStatus("mandatory")


class _WfSdlcLSAdminContTimer2Retry_Type(Integer32):
    """Custom type wfSdlcLSAdminContTimer2Retry based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminContTimer2Retry_Type.__name__ = "Integer32"
_WfSdlcLSAdminContTimer2Retry_Object = MibTableColumn
wfSdlcLSAdminContTimer2Retry = _WfSdlcLSAdminContTimer2Retry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 19),
    _WfSdlcLSAdminContTimer2Retry_Type()
)
wfSdlcLSAdminContTimer2Retry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminContTimer2Retry.setStatus("mandatory")


class _WfSdlcLSAdminDiscTimer_Type(Integer32):
    """Custom type wfSdlcLSAdminDiscTimer based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminDiscTimer_Type.__name__ = "Integer32"
_WfSdlcLSAdminDiscTimer_Object = MibTableColumn
wfSdlcLSAdminDiscTimer = _WfSdlcLSAdminDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 20),
    _WfSdlcLSAdminDiscTimer_Type()
)
wfSdlcLSAdminDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminDiscTimer.setStatus("mandatory")


class _WfSdlcLSAdminDiscTimerRetry_Type(Integer32):
    """Custom type wfSdlcLSAdminDiscTimerRetry based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminDiscTimerRetry_Type.__name__ = "Integer32"
_WfSdlcLSAdminDiscTimerRetry_Object = MibTableColumn
wfSdlcLSAdminDiscTimerRetry = _WfSdlcLSAdminDiscTimerRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 21),
    _WfSdlcLSAdminDiscTimerRetry_Type()
)
wfSdlcLSAdminDiscTimerRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminDiscTimerRetry.setStatus("mandatory")


class _WfSdlcLSAdminNvePollTimer_Type(Integer32):
    """Custom type wfSdlcLSAdminNvePollTimer based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminNvePollTimer_Type.__name__ = "Integer32"
_WfSdlcLSAdminNvePollTimer_Object = MibTableColumn
wfSdlcLSAdminNvePollTimer = _WfSdlcLSAdminNvePollTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 22),
    _WfSdlcLSAdminNvePollTimer_Type()
)
wfSdlcLSAdminNvePollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminNvePollTimer.setStatus("mandatory")


class _WfSdlcLSAdminNvePollTimerRetry_Type(Integer32):
    """Custom type wfSdlcLSAdminNvePollTimerRetry based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfSdlcLSAdminNvePollTimerRetry_Type.__name__ = "Integer32"
_WfSdlcLSAdminNvePollTimerRetry_Object = MibTableColumn
wfSdlcLSAdminNvePollTimerRetry = _WfSdlcLSAdminNvePollTimerRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 23),
    _WfSdlcLSAdminNvePollTimerRetry_Type()
)
wfSdlcLSAdminNvePollTimerRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminNvePollTimerRetry.setStatus("mandatory")


class _WfSdlcLSAdminNvePollTimer2_Type(Integer32):
    """Custom type wfSdlcLSAdminNvePollTimer2 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminNvePollTimer2_Type.__name__ = "Integer32"
_WfSdlcLSAdminNvePollTimer2_Object = MibTableColumn
wfSdlcLSAdminNvePollTimer2 = _WfSdlcLSAdminNvePollTimer2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 24),
    _WfSdlcLSAdminNvePollTimer2_Type()
)
wfSdlcLSAdminNvePollTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminNvePollTimer2.setStatus("mandatory")


class _WfSdlcLSAdminNvePollTimer2Retry_Type(Integer32):
    """Custom type wfSdlcLSAdminNvePollTimer2Retry based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfSdlcLSAdminNvePollTimer2Retry_Type.__name__ = "Integer32"
_WfSdlcLSAdminNvePollTimer2Retry_Object = MibTableColumn
wfSdlcLSAdminNvePollTimer2Retry = _WfSdlcLSAdminNvePollTimer2Retry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 25),
    _WfSdlcLSAdminNvePollTimer2Retry_Type()
)
wfSdlcLSAdminNvePollTimer2Retry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminNvePollTimer2Retry.setStatus("mandatory")


class _WfSdlcLSAdminNoRespTimerRetry_Type(Integer32):
    """Custom type wfSdlcLSAdminNoRespTimerRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminNoRespTimerRetry_Type.__name__ = "Integer32"
_WfSdlcLSAdminNoRespTimerRetry_Object = MibTableColumn
wfSdlcLSAdminNoRespTimerRetry = _WfSdlcLSAdminNoRespTimerRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 26),
    _WfSdlcLSAdminNoRespTimerRetry_Type()
)
wfSdlcLSAdminNoRespTimerRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminNoRespTimerRetry.setStatus("mandatory")


class _WfSdlcLSAdminRemBusyTimerRetry_Type(Integer32):
    """Custom type wfSdlcLSAdminRemBusyTimerRetry based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_WfSdlcLSAdminRemBusyTimerRetry_Type.__name__ = "Integer32"
_WfSdlcLSAdminRemBusyTimerRetry_Object = MibTableColumn
wfSdlcLSAdminRemBusyTimerRetry = _WfSdlcLSAdminRemBusyTimerRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 27),
    _WfSdlcLSAdminRemBusyTimerRetry_Type()
)
wfSdlcLSAdminRemBusyTimerRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminRemBusyTimerRetry.setStatus("mandatory")


class _WfSdlcLSAdminRRTimer_Type(Integer32):
    """Custom type wfSdlcLSAdminRRTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_WfSdlcLSAdminRRTimer_Type.__name__ = "Integer32"
_WfSdlcLSAdminRRTimer_Object = MibTableColumn
wfSdlcLSAdminRRTimer = _WfSdlcLSAdminRRTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 28),
    _WfSdlcLSAdminRRTimer_Type()
)
wfSdlcLSAdminRRTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminRRTimer.setStatus("mandatory")
_WfSdlcLSAdminGpAddName_Type = DisplayString
_WfSdlcLSAdminGpAddName_Object = MibTableColumn
wfSdlcLSAdminGpAddName = _WfSdlcLSAdminGpAddName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 29),
    _WfSdlcLSAdminGpAddName_Type()
)
wfSdlcLSAdminGpAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminGpAddName.setStatus("mandatory")


class _WfSdlcLSAdminPollFrame_Type(Integer32):
    """Custom type wfSdlcLSAdminPollFrame based on Integer32"""
    defaultValue = 191

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(83,
              147,
              191,
              223,
              243)
        )
    )
    namedValues = NamedValues(
        *(("disc", 83),
          ("snrm", 147),
          ("snrme", 223),
          ("test", 243),
          ("xid", 191))
    )


_WfSdlcLSAdminPollFrame_Type.__name__ = "Integer32"
_WfSdlcLSAdminPollFrame_Object = MibTableColumn
wfSdlcLSAdminPollFrame = _WfSdlcLSAdminPollFrame_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 30),
    _WfSdlcLSAdminPollFrame_Type()
)
wfSdlcLSAdminPollFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminPollFrame.setStatus("mandatory")


class _WfSdlcLSAdminPollOnIframe_Type(Integer32):
    """Custom type wfSdlcLSAdminPollOnIframe based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfSdlcLSAdminPollOnIframe_Type.__name__ = "Integer32"
_WfSdlcLSAdminPollOnIframe_Object = MibTableColumn
wfSdlcLSAdminPollOnIframe = _WfSdlcLSAdminPollOnIframe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 31),
    _WfSdlcLSAdminPollOnIframe_Type()
)
wfSdlcLSAdminPollOnIframe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminPollOnIframe.setStatus("mandatory")
_WfSdlcLSAdminLinkStationName_Type = DisplayString
_WfSdlcLSAdminLinkStationName_Object = MibTableColumn
wfSdlcLSAdminLinkStationName = _WfSdlcLSAdminLinkStationName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 32),
    _WfSdlcLSAdminLinkStationName_Type()
)
wfSdlcLSAdminLinkStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminLinkStationName.setStatus("mandatory")


class _WfSdlcLSAdminAdjNodeType_Type(Integer32):
    """Custom type wfSdlcLSAdminAdjNodeType based on Integer32"""
    defaultValue = 3

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
        *(("end", 4),
          ("learn", 1),
          ("len", 2),
          ("network", 3),
          ("vrn", 5))
    )


_WfSdlcLSAdminAdjNodeType_Type.__name__ = "Integer32"
_WfSdlcLSAdminAdjNodeType_Object = MibTableColumn
wfSdlcLSAdminAdjNodeType = _WfSdlcLSAdminAdjNodeType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 33),
    _WfSdlcLSAdminAdjNodeType_Type()
)
wfSdlcLSAdminAdjNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminAdjNodeType.setStatus("mandatory")


class _WfSdlcLSAdminSimRim_Type(Integer32):
    """Custom type wfSdlcLSAdminSimRim based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfSdlcLSAdminSimRim_Type.__name__ = "Integer32"
_WfSdlcLSAdminSimRim_Object = MibTableColumn
wfSdlcLSAdminSimRim = _WfSdlcLSAdminSimRim_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 5, 1, 34),
    _WfSdlcLSAdminSimRim_Type()
)
wfSdlcLSAdminSimRim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSdlcLSAdminSimRim.setStatus("mandatory")
_WfSdlcLSOperTable_Object = MibTable
wfSdlcLSOperTable = _WfSdlcLSOperTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6)
)
if mibBuilder.loadTexts:
    wfSdlcLSOperTable.setStatus("mandatory")
_WfSdlcLSOperEntry_Object = MibTableRow
wfSdlcLSOperEntry = _WfSdlcLSOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1)
)
wfSdlcLSOperEntry.setIndexNames(
    (0, "Wellfleet-SDLC-MIB", "wfSdlcLSOperIfIndex"),
    (0, "Wellfleet-SDLC-MIB", "wfSdlcLSOperAddress"),
)
if mibBuilder.loadTexts:
    wfSdlcLSOperEntry.setStatus("mandatory")
_WfSdlcLSOperIfIndex_Type = Integer32
_WfSdlcLSOperIfIndex_Object = MibTableColumn
wfSdlcLSOperIfIndex = _WfSdlcLSOperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 1),
    _WfSdlcLSOperIfIndex_Type()
)
wfSdlcLSOperIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperIfIndex.setStatus("mandatory")
_WfSdlcLSOperAddress_Type = Integer32
_WfSdlcLSOperAddress_Object = MibTableColumn
wfSdlcLSOperAddress = _WfSdlcLSOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 2),
    _WfSdlcLSOperAddress_Type()
)
wfSdlcLSOperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperAddress.setStatus("mandatory")


class _WfSdlcLSOperRole_Type(Integer32):
    """Custom type wfSdlcLSOperRole based on Integer32"""
    defaultValue = 3

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
        *(("msec", 4),
          ("negot", 1),
          ("primary", 2),
          ("sec", 3))
    )


_WfSdlcLSOperRole_Type.__name__ = "Integer32"
_WfSdlcLSOperRole_Object = MibTableColumn
wfSdlcLSOperRole = _WfSdlcLSOperRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 3),
    _WfSdlcLSOperRole_Type()
)
wfSdlcLSOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperRole.setStatus("mandatory")


class _WfSdlcLSOperState_Type(Integer32):
    """Custom type wfSdlcLSOperState based on Integer32"""
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
        *(("conpend", 2),
          ("contact", 3),
          ("discont", 1),
          ("dispend", 4))
    )


_WfSdlcLSOperState_Type.__name__ = "Integer32"
_WfSdlcLSOperState_Object = MibTableColumn
wfSdlcLSOperState = _WfSdlcLSOperState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 4),
    _WfSdlcLSOperState_Type()
)
wfSdlcLSOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperState.setStatus("mandatory")


class _WfSdlcLSOperMAXDATA_Type(Integer32):
    """Custom type wfSdlcLSOperMAXDATA based on Integer32"""
    defaultValue = 1033

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(265,
              521,
              1033,
              2057,
              4105)
        )
    )
    namedValues = NamedValues(
        *(("pdu0265", 265),
          ("pdu0521", 521),
          ("pdu1033", 1033),
          ("pdu2057", 2057),
          ("pdu4105", 4105))
    )


_WfSdlcLSOperMAXDATA_Type.__name__ = "Integer32"
_WfSdlcLSOperMAXDATA_Object = MibTableColumn
wfSdlcLSOperMAXDATA = _WfSdlcLSOperMAXDATA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 5),
    _WfSdlcLSOperMAXDATA_Type()
)
wfSdlcLSOperMAXDATA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperMAXDATA.setStatus("mandatory")
_WfSdlcLSOperREPLYTO_Type = Integer32
_WfSdlcLSOperREPLYTO_Object = MibTableColumn
wfSdlcLSOperREPLYTO = _WfSdlcLSOperREPLYTO_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 6),
    _WfSdlcLSOperREPLYTO_Type()
)
wfSdlcLSOperREPLYTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperREPLYTO.setStatus("mandatory")
_WfSdlcLSOperMAXIN_Type = Integer32
_WfSdlcLSOperMAXIN_Object = MibTableColumn
wfSdlcLSOperMAXIN = _WfSdlcLSOperMAXIN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 7),
    _WfSdlcLSOperMAXIN_Type()
)
wfSdlcLSOperMAXIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperMAXIN.setStatus("mandatory")
_WfSdlcLSOperMAXOUT_Type = Integer32
_WfSdlcLSOperMAXOUT_Object = MibTableColumn
wfSdlcLSOperMAXOUT = _WfSdlcLSOperMAXOUT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 8),
    _WfSdlcLSOperMAXOUT_Type()
)
wfSdlcLSOperMAXOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperMAXOUT.setStatus("mandatory")
_WfSdlcLSOperMODULO_Type = Integer32
_WfSdlcLSOperMODULO_Object = MibTableColumn
wfSdlcLSOperMODULO = _WfSdlcLSOperMODULO_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 9),
    _WfSdlcLSOperMODULO_Type()
)
wfSdlcLSOperMODULO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperMODULO.setStatus("mandatory")
_WfSdlcLSOperRETRIESm_Type = Integer32
_WfSdlcLSOperRETRIESm_Object = MibTableColumn
wfSdlcLSOperRETRIESm = _WfSdlcLSOperRETRIESm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 10),
    _WfSdlcLSOperRETRIESm_Type()
)
wfSdlcLSOperRETRIESm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperRETRIESm.setStatus("mandatory")
_WfSdlcLSOperRETRIESt_Type = Integer32
_WfSdlcLSOperRETRIESt_Object = MibTableColumn
wfSdlcLSOperRETRIESt = _WfSdlcLSOperRETRIESt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 11),
    _WfSdlcLSOperRETRIESt_Type()
)
wfSdlcLSOperRETRIESt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperRETRIESt.setStatus("mandatory")
_WfSdlcLSOperRETRIESn_Type = Integer32
_WfSdlcLSOperRETRIESn_Object = MibTableColumn
wfSdlcLSOperRETRIESn = _WfSdlcLSOperRETRIESn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 12),
    _WfSdlcLSOperRETRIESn_Type()
)
wfSdlcLSOperRETRIESn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperRETRIESn.setStatus("mandatory")
_WfSdlcLSOperRNRLIMIT_Type = Integer32
_WfSdlcLSOperRNRLIMIT_Object = MibTableColumn
wfSdlcLSOperRNRLIMIT = _WfSdlcLSOperRNRLIMIT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 13),
    _WfSdlcLSOperRNRLIMIT_Type()
)
wfSdlcLSOperRNRLIMIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperRNRLIMIT.setStatus("mandatory")


class _WfSdlcLSOperDATMODE_Type(Integer32):
    """Custom type wfSdlcLSOperDATMODE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_WfSdlcLSOperDATMODE_Type.__name__ = "Integer32"
_WfSdlcLSOperDATMODE_Object = MibTableColumn
wfSdlcLSOperDATMODE = _WfSdlcLSOperDATMODE_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 14),
    _WfSdlcLSOperDATMODE_Type()
)
wfSdlcLSOperDATMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperDATMODE.setStatus("mandatory")
_WfSdlcLSOperCreateTime_Type = TimeTicks
_WfSdlcLSOperCreateTime_Object = MibTableColumn
wfSdlcLSOperCreateTime = _WfSdlcLSOperCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 15),
    _WfSdlcLSOperCreateTime_Type()
)
wfSdlcLSOperCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperCreateTime.setStatus("mandatory")


class _WfSdlcLSOperLastFailCause_Type(Integer32):
    """Custom type wfSdlcLSOperLastFailCause based on Integer32"""
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
        *(("noactiv", 6),
          ("noresp", 4),
          ("protoerr", 5),
          ("retriesexp", 8),
          ("rnrlimit", 7),
          ("rxfrmr", 2),
          ("txfrmr", 3),
          ("undefined", 1))
    )


_WfSdlcLSOperLastFailCause_Type.__name__ = "Integer32"
_WfSdlcLSOperLastFailCause_Object = MibTableColumn
wfSdlcLSOperLastFailCause = _WfSdlcLSOperLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 16),
    _WfSdlcLSOperLastFailCause_Type()
)
wfSdlcLSOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperLastFailCause.setStatus("mandatory")
_WfSdlcLSOperLastFailCtrlIn2_Type = OctetString
_WfSdlcLSOperLastFailCtrlIn2_Object = MibTableColumn
wfSdlcLSOperLastFailCtrlIn2 = _WfSdlcLSOperLastFailCtrlIn2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 17),
    _WfSdlcLSOperLastFailCtrlIn2_Type()
)
wfSdlcLSOperLastFailCtrlIn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperLastFailCtrlIn2.setStatus("mandatory")
_WfSdlcLSOperLastFailCtrlOut2_Type = OctetString
_WfSdlcLSOperLastFailCtrlOut2_Object = MibTableColumn
wfSdlcLSOperLastFailCtrlOut2 = _WfSdlcLSOperLastFailCtrlOut2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 18),
    _WfSdlcLSOperLastFailCtrlOut2_Type()
)
wfSdlcLSOperLastFailCtrlOut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperLastFailCtrlOut2.setStatus("mandatory")
_WfSdlcLSOperLastFailFRMRInfo5_Type = OctetString
_WfSdlcLSOperLastFailFRMRInfo5_Object = MibTableColumn
wfSdlcLSOperLastFailFRMRInfo5 = _WfSdlcLSOperLastFailFRMRInfo5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 19),
    _WfSdlcLSOperLastFailFRMRInfo5_Type()
)
wfSdlcLSOperLastFailFRMRInfo5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperLastFailFRMRInfo5.setStatus("mandatory")
_WfSdlcLSOperLastFailREPLYTOs_Type = Counter32
_WfSdlcLSOperLastFailREPLYTOs_Object = MibTableColumn
wfSdlcLSOperLastFailREPLYTOs = _WfSdlcLSOperLastFailREPLYTOs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 20),
    _WfSdlcLSOperLastFailREPLYTOs_Type()
)
wfSdlcLSOperLastFailREPLYTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperLastFailREPLYTOs.setStatus("mandatory")
_WfSdlcLSOperGroupAddress_Type = Integer32
_WfSdlcLSOperGroupAddress_Object = MibTableColumn
wfSdlcLSOperGroupAddress = _WfSdlcLSOperGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 6, 1, 21),
    _WfSdlcLSOperGroupAddress_Type()
)
wfSdlcLSOperGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSOperGroupAddress.setStatus("mandatory")
_WfSdlcLSStatsTable_Object = MibTable
wfSdlcLSStatsTable = _WfSdlcLSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7)
)
if mibBuilder.loadTexts:
    wfSdlcLSStatsTable.setStatus("mandatory")
_WfSdlcLSStatsEntry_Object = MibTableRow
wfSdlcLSStatsEntry = _WfSdlcLSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1)
)
wfSdlcLSStatsEntry.setIndexNames(
    (0, "Wellfleet-SDLC-MIB", "wfSdlcLSStatsIfIndex"),
    (0, "Wellfleet-SDLC-MIB", "wfSdlcLSStatsAddress"),
)
if mibBuilder.loadTexts:
    wfSdlcLSStatsEntry.setStatus("mandatory")
_WfSdlcLSStatsIfIndex_Type = Integer32
_WfSdlcLSStatsIfIndex_Object = MibTableColumn
wfSdlcLSStatsIfIndex = _WfSdlcLSStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 1),
    _WfSdlcLSStatsIfIndex_Type()
)
wfSdlcLSStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsIfIndex.setStatus("mandatory")
_WfSdlcLSStatsAddress_Type = Integer32
_WfSdlcLSStatsAddress_Object = MibTableColumn
wfSdlcLSStatsAddress = _WfSdlcLSStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 2),
    _WfSdlcLSStatsAddress_Type()
)
wfSdlcLSStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsAddress.setStatus("mandatory")
_WfSdlcLSStatsBLUsIns_Type = Counter32
_WfSdlcLSStatsBLUsIns_Object = MibTableColumn
wfSdlcLSStatsBLUsIns = _WfSdlcLSStatsBLUsIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 3),
    _WfSdlcLSStatsBLUsIns_Type()
)
wfSdlcLSStatsBLUsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsBLUsIns.setStatus("mandatory")
_WfSdlcLSStatsBLUsOuts_Type = Counter32
_WfSdlcLSStatsBLUsOuts_Object = MibTableColumn
wfSdlcLSStatsBLUsOuts = _WfSdlcLSStatsBLUsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 4),
    _WfSdlcLSStatsBLUsOuts_Type()
)
wfSdlcLSStatsBLUsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsBLUsOuts.setStatus("mandatory")
_WfSdlcLSStatsOctetsIns_Type = Counter32
_WfSdlcLSStatsOctetsIns_Object = MibTableColumn
wfSdlcLSStatsOctetsIns = _WfSdlcLSStatsOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 5),
    _WfSdlcLSStatsOctetsIns_Type()
)
wfSdlcLSStatsOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsOctetsIns.setStatus("mandatory")
_WfSdlcLSStatsOctetsOuts_Type = Counter32
_WfSdlcLSStatsOctetsOuts_Object = MibTableColumn
wfSdlcLSStatsOctetsOuts = _WfSdlcLSStatsOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 6),
    _WfSdlcLSStatsOctetsOuts_Type()
)
wfSdlcLSStatsOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsOctetsOuts.setStatus("mandatory")
_WfSdlcLSStatsPollsOuts_Type = Counter32
_WfSdlcLSStatsPollsOuts_Object = MibTableColumn
wfSdlcLSStatsPollsOuts = _WfSdlcLSStatsPollsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 7),
    _WfSdlcLSStatsPollsOuts_Type()
)
wfSdlcLSStatsPollsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsPollsOuts.setStatus("mandatory")
_WfSdlcLSStatsPollRspOuts_Type = Counter32
_WfSdlcLSStatsPollRspOuts_Object = MibTableColumn
wfSdlcLSStatsPollRspOuts = _WfSdlcLSStatsPollRspOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 8),
    _WfSdlcLSStatsPollRspOuts_Type()
)
wfSdlcLSStatsPollRspOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsPollRspOuts.setStatus("mandatory")
_WfSdlcLSStatsLocalBusies_Type = Counter32
_WfSdlcLSStatsLocalBusies_Object = MibTableColumn
wfSdlcLSStatsLocalBusies = _WfSdlcLSStatsLocalBusies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 9),
    _WfSdlcLSStatsLocalBusies_Type()
)
wfSdlcLSStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsLocalBusies.setStatus("mandatory")
_WfSdlcLSStatsRemoteBusies_Type = Counter32
_WfSdlcLSStatsRemoteBusies_Object = MibTableColumn
wfSdlcLSStatsRemoteBusies = _WfSdlcLSStatsRemoteBusies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 10),
    _WfSdlcLSStatsRemoteBusies_Type()
)
wfSdlcLSStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsRemoteBusies.setStatus("mandatory")
_WfSdlcLSStatsIFramesIns_Type = Counter32
_WfSdlcLSStatsIFramesIns_Object = MibTableColumn
wfSdlcLSStatsIFramesIns = _WfSdlcLSStatsIFramesIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 11),
    _WfSdlcLSStatsIFramesIns_Type()
)
wfSdlcLSStatsIFramesIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsIFramesIns.setStatus("mandatory")
_WfSdlcLSStatsIFramesOuts_Type = Counter32
_WfSdlcLSStatsIFramesOuts_Object = MibTableColumn
wfSdlcLSStatsIFramesOuts = _WfSdlcLSStatsIFramesOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 12),
    _WfSdlcLSStatsIFramesOuts_Type()
)
wfSdlcLSStatsIFramesOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsIFramesOuts.setStatus("mandatory")
_WfSdlcLSStatsRetransmits_Type = Counter32
_WfSdlcLSStatsRetransmits_Object = MibTableColumn
wfSdlcLSStatsRetransmits = _WfSdlcLSStatsRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 13),
    _WfSdlcLSStatsRetransmits_Type()
)
wfSdlcLSStatsRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsRetransmits.setStatus("mandatory")
_WfSdlcLSStatsIOctetsIns_Type = Counter32
_WfSdlcLSStatsIOctetsIns_Object = MibTableColumn
wfSdlcLSStatsIOctetsIns = _WfSdlcLSStatsIOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 14),
    _WfSdlcLSStatsIOctetsIns_Type()
)
wfSdlcLSStatsIOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsIOctetsIns.setStatus("mandatory")
_WfSdlcLSStatsIOctetsOuts_Type = Counter32
_WfSdlcLSStatsIOctetsOuts_Object = MibTableColumn
wfSdlcLSStatsIOctetsOuts = _WfSdlcLSStatsIOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 15),
    _WfSdlcLSStatsIOctetsOuts_Type()
)
wfSdlcLSStatsIOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsIOctetsOuts.setStatus("mandatory")
_WfSdlcLSStatsUIFramesIns_Type = Counter32
_WfSdlcLSStatsUIFramesIns_Object = MibTableColumn
wfSdlcLSStatsUIFramesIns = _WfSdlcLSStatsUIFramesIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 16),
    _WfSdlcLSStatsUIFramesIns_Type()
)
wfSdlcLSStatsUIFramesIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsUIFramesIns.setStatus("mandatory")
_WfSdlcLSStatsUIFramesOuts_Type = Counter32
_WfSdlcLSStatsUIFramesOuts_Object = MibTableColumn
wfSdlcLSStatsUIFramesOuts = _WfSdlcLSStatsUIFramesOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 17),
    _WfSdlcLSStatsUIFramesOuts_Type()
)
wfSdlcLSStatsUIFramesOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsUIFramesOuts.setStatus("mandatory")
_WfSdlcLSStatsXIDsIns_Type = Counter32
_WfSdlcLSStatsXIDsIns_Object = MibTableColumn
wfSdlcLSStatsXIDsIns = _WfSdlcLSStatsXIDsIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 18),
    _WfSdlcLSStatsXIDsIns_Type()
)
wfSdlcLSStatsXIDsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsXIDsIns.setStatus("mandatory")
_WfSdlcLSStatsXIDsOuts_Type = Counter32
_WfSdlcLSStatsXIDsOuts_Object = MibTableColumn
wfSdlcLSStatsXIDsOuts = _WfSdlcLSStatsXIDsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 19),
    _WfSdlcLSStatsXIDsOuts_Type()
)
wfSdlcLSStatsXIDsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsXIDsOuts.setStatus("mandatory")
_WfSdlcLSStatsTESTsIns_Type = Counter32
_WfSdlcLSStatsTESTsIns_Object = MibTableColumn
wfSdlcLSStatsTESTsIns = _WfSdlcLSStatsTESTsIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 20),
    _WfSdlcLSStatsTESTsIns_Type()
)
wfSdlcLSStatsTESTsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsTESTsIns.setStatus("mandatory")
_WfSdlcLSStatsTESTsOuts_Type = Counter32
_WfSdlcLSStatsTESTsOuts_Object = MibTableColumn
wfSdlcLSStatsTESTsOuts = _WfSdlcLSStatsTESTsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 21),
    _WfSdlcLSStatsTESTsOuts_Type()
)
wfSdlcLSStatsTESTsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsTESTsOuts.setStatus("mandatory")
_WfSdlcLSStatsREJsIns_Type = Counter32
_WfSdlcLSStatsREJsIns_Object = MibTableColumn
wfSdlcLSStatsREJsIns = _WfSdlcLSStatsREJsIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 22),
    _WfSdlcLSStatsREJsIns_Type()
)
wfSdlcLSStatsREJsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsREJsIns.setStatus("mandatory")
_WfSdlcLSStatsREJsOuts_Type = Counter32
_WfSdlcLSStatsREJsOuts_Object = MibTableColumn
wfSdlcLSStatsREJsOuts = _WfSdlcLSStatsREJsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 23),
    _WfSdlcLSStatsREJsOuts_Type()
)
wfSdlcLSStatsREJsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsREJsOuts.setStatus("mandatory")
_WfSdlcLSStatsFRMRsIns_Type = Counter32
_WfSdlcLSStatsFRMRsIns_Object = MibTableColumn
wfSdlcLSStatsFRMRsIns = _WfSdlcLSStatsFRMRsIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 24),
    _WfSdlcLSStatsFRMRsIns_Type()
)
wfSdlcLSStatsFRMRsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsFRMRsIns.setStatus("mandatory")
_WfSdlcLSStatsFRMRsOuts_Type = Counter32
_WfSdlcLSStatsFRMRsOuts_Object = MibTableColumn
wfSdlcLSStatsFRMRsOuts = _WfSdlcLSStatsFRMRsOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 25),
    _WfSdlcLSStatsFRMRsOuts_Type()
)
wfSdlcLSStatsFRMRsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsFRMRsOuts.setStatus("mandatory")
_WfSdlcLSStatsSimsIn_Type = Counter32
_WfSdlcLSStatsSimsIn_Object = MibTableColumn
wfSdlcLSStatsSimsIn = _WfSdlcLSStatsSimsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 26),
    _WfSdlcLSStatsSimsIn_Type()
)
wfSdlcLSStatsSimsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsSimsIn.setStatus("mandatory")
_WfSdlcLSStatsSimsOut_Type = Counter32
_WfSdlcLSStatsSimsOut_Object = MibTableColumn
wfSdlcLSStatsSimsOut = _WfSdlcLSStatsSimsOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 27),
    _WfSdlcLSStatsSimsOut_Type()
)
wfSdlcLSStatsSimsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsSimsOut.setStatus("mandatory")
_WfSdlcLSStatsRimsIn_Type = Counter32
_WfSdlcLSStatsRimsIn_Object = MibTableColumn
wfSdlcLSStatsRimsIn = _WfSdlcLSStatsRimsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 28),
    _WfSdlcLSStatsRimsIn_Type()
)
wfSdlcLSStatsRimsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsRimsIn.setStatus("mandatory")
_WfSdlcLSStatsRimsOut_Type = Counter32
_WfSdlcLSStatsRimsOut_Object = MibTableColumn
wfSdlcLSStatsRimsOut = _WfSdlcLSStatsRimsOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7, 7, 1, 29),
    _WfSdlcLSStatsRimsOut_Type()
)
wfSdlcLSStatsRimsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSdlcLSStatsRimsOut.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SDLC-MIB",
    **{"wfSdlc": wfSdlc,
       "wfSdlcDelete": wfSdlcDelete,
       "wfSdlcDisable": wfSdlcDisable,
       "wfSdlcState": wfSdlcState,
       "wfSdlcPortAdminTable": wfSdlcPortAdminTable,
       "wfSdlcPortAdminEntry": wfSdlcPortAdminEntry,
       "wfSdlcPortAdminDelete": wfSdlcPortAdminDelete,
       "wfSdlcPortAdminDisable": wfSdlcPortAdminDisable,
       "wfSdlcPortAdminIndex": wfSdlcPortAdminIndex,
       "wfSdlcPortAdminAddress4": wfSdlcPortAdminAddress4,
       "wfSdlcPortAdminType": wfSdlcPortAdminType,
       "wfSdlcPortAdminTopology": wfSdlcPortAdminTopology,
       "wfSdlcPortAdminACTIVTO": wfSdlcPortAdminACTIVTO,
       "wfSdlcPortAdminPAUSE": wfSdlcPortAdminPAUSE,
       "wfSdlcPortAdminCredit": wfSdlcPortAdminCredit,
       "wfSdlcPortAdminIdleTimer": wfSdlcPortAdminIdleTimer,
       "wfSdlcPortAdminIdleRetry": wfSdlcPortAdminIdleRetry,
       "wfSdlcPortAdminNPRcvTimer": wfSdlcPortAdminNPRcvTimer,
       "wfSdlcPortAdminNPRcvRetry": wfSdlcPortAdminNPRcvRetry,
       "wfSdlcPortAdminWriteTimer": wfSdlcPortAdminWriteTimer,
       "wfSdlcPortAdminWriteRetry": wfSdlcPortAdminWriteRetry,
       "wfSdlcPortAdminLinkConnTimer": wfSdlcPortAdminLinkConnTimer,
       "wfSdlcPortAdminLinkConnRetry": wfSdlcPortAdminLinkConnRetry,
       "wfSdlcPortAdminPriFdplx": wfSdlcPortAdminPriFdplx,
       "wfSdlcPortAdminSecFdplx": wfSdlcPortAdminSecFdplx,
       "wfSdlcPortAdminUseRej": wfSdlcPortAdminUseRej,
       "wfSdlcPortAdminPortType": wfSdlcPortAdminPortType,
       "wfSdlcPortAdminMaxXidSize": wfSdlcPortAdminMaxXidSize,
       "wfSdlcPortAdminMaxRetryCount": wfSdlcPortAdminMaxRetryCount,
       "wfSdlcPortAdminMaxFrameSize": wfSdlcPortAdminMaxFrameSize,
       "wfSdlcPortAdminDlcName8": wfSdlcPortAdminDlcName8,
       "wfSdlcPortAdminCpType": wfSdlcPortAdminCpType,
       "wfSdlcPortAdminLsRole": wfSdlcPortAdminLsRole,
       "wfSdlcPortAdminPortNumber": wfSdlcPortAdminPortNumber,
       "wfSdlcPortAdminLsAddress": wfSdlcPortAdminLsAddress,
       "wfSdlcPortAdminTotLsActLim": wfSdlcPortAdminTotLsActLim,
       "wfSdlcPortAdminInLsActLim": wfSdlcPortAdminInLsActLim,
       "wfSdlcPortAdminOutLsActLim": wfSdlcPortAdminOutLsActLim,
       "wfSdlcPortAdminNegLsSupp": wfSdlcPortAdminNegLsSupp,
       "wfSdlcPortAdminRcvPoolSize": wfSdlcPortAdminRcvPoolSize,
       "wfSdlcPortAdminStatsColl": wfSdlcPortAdminStatsColl,
       "wfSdlcPortAdminDebugFlg": wfSdlcPortAdminDebugFlg,
       "wfSdlcPortOperTable": wfSdlcPortOperTable,
       "wfSdlcPortOperEntry": wfSdlcPortOperEntry,
       "wfSdlcPortOperIndex": wfSdlcPortOperIndex,
       "wfSdlcPortOperAddress4": wfSdlcPortOperAddress4,
       "wfSdlcPortOperRole": wfSdlcPortOperRole,
       "wfSdlcPortOperType": wfSdlcPortOperType,
       "wfSdlcPortOperTopology": wfSdlcPortOperTopology,
       "wfSdlcPortOperACTIVTO": wfSdlcPortOperACTIVTO,
       "wfSdlcPortOperPAUSE": wfSdlcPortOperPAUSE,
       "wfSdlcPortOperSlowPollMethod": wfSdlcPortOperSlowPollMethod,
       "wfSdlcPortOperSlowPollTimer": wfSdlcPortOperSlowPollTimer,
       "wfSdlcPortOperAbmSuppInd": wfSdlcPortOperAbmSuppInd,
       "wfSdlcPortOperSimRimSupp": wfSdlcPortOperSimRimSupp,
       "wfSdlcPortOperSecInitNonactSupp": wfSdlcPortOperSecInitNonactSupp,
       "wfSdlcPortStatsTable": wfSdlcPortStatsTable,
       "wfSdlcPortStatsEntry": wfSdlcPortStatsEntry,
       "wfSdlcPortStatsIndex": wfSdlcPortStatsIndex,
       "wfSdlcPortStatsDwarfFrames": wfSdlcPortStatsDwarfFrames,
       "wfSdlcLSAdminTable": wfSdlcLSAdminTable,
       "wfSdlcLSAdminEntry": wfSdlcLSAdminEntry,
       "wfSdlcLSAdminDelete": wfSdlcLSAdminDelete,
       "wfSdlcLSAdminDisable": wfSdlcLSAdminDisable,
       "wfSdlcLSAdminIfIndex": wfSdlcLSAdminIfIndex,
       "wfSdlcLSAdminAddress": wfSdlcLSAdminAddress,
       "wfSdlcLSAdminGroupAddress": wfSdlcLSAdminGroupAddress,
       "wfSdlcLSAdminRole": wfSdlcLSAdminRole,
       "wfSdlcLSAdminMAXDATA": wfSdlcLSAdminMAXDATA,
       "wfSdlcLSAdminREPLYTO": wfSdlcLSAdminREPLYTO,
       "wfSdlcLSAdminMAXIN": wfSdlcLSAdminMAXIN,
       "wfSdlcLSAdminMAXOUT": wfSdlcLSAdminMAXOUT,
       "wfSdlcLSAdminMODULO": wfSdlcLSAdminMODULO,
       "wfSdlcLSAdminRETRIESm": wfSdlcLSAdminRETRIESm,
       "wfSdlcLSAdminRETRIESt": wfSdlcLSAdminRETRIESt,
       "wfSdlcLSAdminRETRIESn": wfSdlcLSAdminRETRIESn,
       "wfSdlcLSAdminRNRLIMIT": wfSdlcLSAdminRNRLIMIT,
       "wfSdlcLSAdminContTimer": wfSdlcLSAdminContTimer,
       "wfSdlcLSAdminContTimerRetry": wfSdlcLSAdminContTimerRetry,
       "wfSdlcLSAdminContTimer2": wfSdlcLSAdminContTimer2,
       "wfSdlcLSAdminContTimer2Retry": wfSdlcLSAdminContTimer2Retry,
       "wfSdlcLSAdminDiscTimer": wfSdlcLSAdminDiscTimer,
       "wfSdlcLSAdminDiscTimerRetry": wfSdlcLSAdminDiscTimerRetry,
       "wfSdlcLSAdminNvePollTimer": wfSdlcLSAdminNvePollTimer,
       "wfSdlcLSAdminNvePollTimerRetry": wfSdlcLSAdminNvePollTimerRetry,
       "wfSdlcLSAdminNvePollTimer2": wfSdlcLSAdminNvePollTimer2,
       "wfSdlcLSAdminNvePollTimer2Retry": wfSdlcLSAdminNvePollTimer2Retry,
       "wfSdlcLSAdminNoRespTimerRetry": wfSdlcLSAdminNoRespTimerRetry,
       "wfSdlcLSAdminRemBusyTimerRetry": wfSdlcLSAdminRemBusyTimerRetry,
       "wfSdlcLSAdminRRTimer": wfSdlcLSAdminRRTimer,
       "wfSdlcLSAdminGpAddName": wfSdlcLSAdminGpAddName,
       "wfSdlcLSAdminPollFrame": wfSdlcLSAdminPollFrame,
       "wfSdlcLSAdminPollOnIframe": wfSdlcLSAdminPollOnIframe,
       "wfSdlcLSAdminLinkStationName": wfSdlcLSAdminLinkStationName,
       "wfSdlcLSAdminAdjNodeType": wfSdlcLSAdminAdjNodeType,
       "wfSdlcLSAdminSimRim": wfSdlcLSAdminSimRim,
       "wfSdlcLSOperTable": wfSdlcLSOperTable,
       "wfSdlcLSOperEntry": wfSdlcLSOperEntry,
       "wfSdlcLSOperIfIndex": wfSdlcLSOperIfIndex,
       "wfSdlcLSOperAddress": wfSdlcLSOperAddress,
       "wfSdlcLSOperRole": wfSdlcLSOperRole,
       "wfSdlcLSOperState": wfSdlcLSOperState,
       "wfSdlcLSOperMAXDATA": wfSdlcLSOperMAXDATA,
       "wfSdlcLSOperREPLYTO": wfSdlcLSOperREPLYTO,
       "wfSdlcLSOperMAXIN": wfSdlcLSOperMAXIN,
       "wfSdlcLSOperMAXOUT": wfSdlcLSOperMAXOUT,
       "wfSdlcLSOperMODULO": wfSdlcLSOperMODULO,
       "wfSdlcLSOperRETRIESm": wfSdlcLSOperRETRIESm,
       "wfSdlcLSOperRETRIESt": wfSdlcLSOperRETRIESt,
       "wfSdlcLSOperRETRIESn": wfSdlcLSOperRETRIESn,
       "wfSdlcLSOperRNRLIMIT": wfSdlcLSOperRNRLIMIT,
       "wfSdlcLSOperDATMODE": wfSdlcLSOperDATMODE,
       "wfSdlcLSOperCreateTime": wfSdlcLSOperCreateTime,
       "wfSdlcLSOperLastFailCause": wfSdlcLSOperLastFailCause,
       "wfSdlcLSOperLastFailCtrlIn2": wfSdlcLSOperLastFailCtrlIn2,
       "wfSdlcLSOperLastFailCtrlOut2": wfSdlcLSOperLastFailCtrlOut2,
       "wfSdlcLSOperLastFailFRMRInfo5": wfSdlcLSOperLastFailFRMRInfo5,
       "wfSdlcLSOperLastFailREPLYTOs": wfSdlcLSOperLastFailREPLYTOs,
       "wfSdlcLSOperGroupAddress": wfSdlcLSOperGroupAddress,
       "wfSdlcLSStatsTable": wfSdlcLSStatsTable,
       "wfSdlcLSStatsEntry": wfSdlcLSStatsEntry,
       "wfSdlcLSStatsIfIndex": wfSdlcLSStatsIfIndex,
       "wfSdlcLSStatsAddress": wfSdlcLSStatsAddress,
       "wfSdlcLSStatsBLUsIns": wfSdlcLSStatsBLUsIns,
       "wfSdlcLSStatsBLUsOuts": wfSdlcLSStatsBLUsOuts,
       "wfSdlcLSStatsOctetsIns": wfSdlcLSStatsOctetsIns,
       "wfSdlcLSStatsOctetsOuts": wfSdlcLSStatsOctetsOuts,
       "wfSdlcLSStatsPollsOuts": wfSdlcLSStatsPollsOuts,
       "wfSdlcLSStatsPollRspOuts": wfSdlcLSStatsPollRspOuts,
       "wfSdlcLSStatsLocalBusies": wfSdlcLSStatsLocalBusies,
       "wfSdlcLSStatsRemoteBusies": wfSdlcLSStatsRemoteBusies,
       "wfSdlcLSStatsIFramesIns": wfSdlcLSStatsIFramesIns,
       "wfSdlcLSStatsIFramesOuts": wfSdlcLSStatsIFramesOuts,
       "wfSdlcLSStatsRetransmits": wfSdlcLSStatsRetransmits,
       "wfSdlcLSStatsIOctetsIns": wfSdlcLSStatsIOctetsIns,
       "wfSdlcLSStatsIOctetsOuts": wfSdlcLSStatsIOctetsOuts,
       "wfSdlcLSStatsUIFramesIns": wfSdlcLSStatsUIFramesIns,
       "wfSdlcLSStatsUIFramesOuts": wfSdlcLSStatsUIFramesOuts,
       "wfSdlcLSStatsXIDsIns": wfSdlcLSStatsXIDsIns,
       "wfSdlcLSStatsXIDsOuts": wfSdlcLSStatsXIDsOuts,
       "wfSdlcLSStatsTESTsIns": wfSdlcLSStatsTESTsIns,
       "wfSdlcLSStatsTESTsOuts": wfSdlcLSStatsTESTsOuts,
       "wfSdlcLSStatsREJsIns": wfSdlcLSStatsREJsIns,
       "wfSdlcLSStatsREJsOuts": wfSdlcLSStatsREJsOuts,
       "wfSdlcLSStatsFRMRsIns": wfSdlcLSStatsFRMRsIns,
       "wfSdlcLSStatsFRMRsOuts": wfSdlcLSStatsFRMRsOuts,
       "wfSdlcLSStatsSimsIn": wfSdlcLSStatsSimsIn,
       "wfSdlcLSStatsSimsOut": wfSdlcLSStatsSimsOut,
       "wfSdlcLSStatsRimsIn": wfSdlcLSStatsRimsIn,
       "wfSdlcLSStatsRimsOut": wfSdlcLSStatsRimsOut}
)
