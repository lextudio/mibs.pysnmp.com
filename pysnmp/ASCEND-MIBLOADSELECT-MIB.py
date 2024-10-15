# SNMP MIB module (ASCEND-MIBLOADSELECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBLOADSELECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:52 2024
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

_MibloadSelectProfile_ObjectIdentity = ObjectIdentity
mibloadSelectProfile = _MibloadSelectProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 92)
)
_MibloadSelectProfileTable_Object = MibTable
mibloadSelectProfileTable = _MibloadSelectProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1)
)
if mibBuilder.loadTexts:
    mibloadSelectProfileTable.setStatus("mandatory")
_MibloadSelectProfileEntry_Object = MibTableRow
mibloadSelectProfileEntry = _MibloadSelectProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1)
)
mibloadSelectProfileEntry.setIndexNames(
    (0, "ASCEND-MIBLOADSELECT-MIB", "loadSelectProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibloadSelectProfileEntry.setStatus("mandatory")
_LoadSelectProfile_Index_o_Type = Integer32
_LoadSelectProfile_Index_o_Object = MibScalar
loadSelectProfile_Index_o = _LoadSelectProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 1),
    _LoadSelectProfile_Index_o_Type()
)
loadSelectProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadSelectProfile_Index_o.setStatus("mandatory")


class _LoadSelectProfile_UnknownCards_Type(Integer32):
    """Custom type loadSelectProfile_UnknownCards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_UnknownCards_Type.__name__ = "Integer32"
_LoadSelectProfile_UnknownCards_Object = MibScalar
loadSelectProfile_UnknownCards = _LoadSelectProfile_UnknownCards_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 2),
    _LoadSelectProfile_UnknownCards_Type()
)
loadSelectProfile_UnknownCards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_UnknownCards.setStatus("mandatory")


class _LoadSelectProfile_Sr_Type(Integer32):
    """Custom type loadSelectProfile_Sr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Sr_Type.__name__ = "Integer32"
_LoadSelectProfile_Sr_Object = MibScalar
loadSelectProfile_Sr = _LoadSelectProfile_Sr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 3),
    _LoadSelectProfile_Sr_Type()
)
loadSelectProfile_Sr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Sr.setStatus("mandatory")


class _LoadSelectProfile_Sr2_Type(Integer32):
    """Custom type loadSelectProfile_Sr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Sr2_Type.__name__ = "Integer32"
_LoadSelectProfile_Sr2_Object = MibScalar
loadSelectProfile_Sr2 = _LoadSelectProfile_Sr2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 4),
    _LoadSelectProfile_Sr2_Type()
)
loadSelectProfile_Sr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Sr2.setStatus("mandatory")


class _LoadSelectProfile_Apxsr_Type(Integer32):
    """Custom type loadSelectProfile_Apxsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Apxsr_Type.__name__ = "Integer32"
_LoadSelectProfile_Apxsr_Object = MibScalar
loadSelectProfile_Apxsr = _LoadSelectProfile_Apxsr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 5),
    _LoadSelectProfile_Apxsr_Type()
)
loadSelectProfile_Apxsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Apxsr.setStatus("mandatory")


class _LoadSelectProfile_o8t1_Type(Integer32):
    """Custom type loadSelectProfile_o8t1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o8t1_Type.__name__ = "Integer32"
_LoadSelectProfile_o8t1_Object = MibScalar
loadSelectProfile_o8t1 = _LoadSelectProfile_o8t1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 6),
    _LoadSelectProfile_o8t1_Type()
)
loadSelectProfile_o8t1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o8t1.setStatus("mandatory")


class _LoadSelectProfile_o8e1_Type(Integer32):
    """Custom type loadSelectProfile_o8e1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o8e1_Type.__name__ = "Integer32"
_LoadSelectProfile_o8e1_Object = MibScalar
loadSelectProfile_o8e1 = _LoadSelectProfile_o8e1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 7),
    _LoadSelectProfile_o8e1_Type()
)
loadSelectProfile_o8e1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o8e1.setStatus("mandatory")


class _LoadSelectProfile_T3_Type(Integer32):
    """Custom type loadSelectProfile_T3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_T3_Type.__name__ = "Integer32"
_LoadSelectProfile_T3_Object = MibScalar
loadSelectProfile_T3 = _LoadSelectProfile_T3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 8),
    _LoadSelectProfile_T3_Type()
)
loadSelectProfile_T3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_T3.setStatus("mandatory")


class _LoadSelectProfile_Stm0_Type(Integer32):
    """Custom type loadSelectProfile_Stm0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Stm0_Type.__name__ = "Integer32"
_LoadSelectProfile_Stm0_Object = MibScalar
loadSelectProfile_Stm0 = _LoadSelectProfile_Stm0_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 9),
    _LoadSelectProfile_Stm0_Type()
)
loadSelectProfile_Stm0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Stm0.setStatus("mandatory")


class _LoadSelectProfile_Pctfit_Type(Integer32):
    """Custom type loadSelectProfile_Pctfit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Pctfit_Type.__name__ = "Integer32"
_LoadSelectProfile_Pctfit_Object = MibScalar
loadSelectProfile_Pctfit = _LoadSelectProfile_Pctfit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 10),
    _LoadSelectProfile_Pctfit_Type()
)
loadSelectProfile_Pctfit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Pctfit.setStatus("mandatory")


class _LoadSelectProfile_Pctfie_Type(Integer32):
    """Custom type loadSelectProfile_Pctfie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Pctfie_Type.__name__ = "Integer32"
_LoadSelectProfile_Pctfie_Object = MibScalar
loadSelectProfile_Pctfie = _LoadSelectProfile_Pctfie_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 11),
    _LoadSelectProfile_Pctfie_Type()
)
loadSelectProfile_Pctfie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Pctfie.setStatus("mandatory")


class _LoadSelectProfile_Clpmt_Type(Integer32):
    """Custom type loadSelectProfile_Clpmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Clpmt_Type.__name__ = "Integer32"
_LoadSelectProfile_Clpmt_Object = MibScalar
loadSelectProfile_Clpmt = _LoadSelectProfile_Clpmt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 12),
    _LoadSelectProfile_Clpmt_Type()
)
loadSelectProfile_Clpmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Clpmt.setStatus("mandatory")


class _LoadSelectProfile_Clpme_Type(Integer32):
    """Custom type loadSelectProfile_Clpme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Clpme_Type.__name__ = "Integer32"
_LoadSelectProfile_Clpme_Object = MibScalar
loadSelectProfile_Clpme = _LoadSelectProfile_Clpme_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 13),
    _LoadSelectProfile_Clpme_Type()
)
loadSelectProfile_Clpme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Clpme.setStatus("mandatory")


class _LoadSelectProfile_Ut1_Type(Integer32):
    """Custom type loadSelectProfile_Ut1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Ut1_Type.__name__ = "Integer32"
_LoadSelectProfile_Ut1_Object = MibScalar
loadSelectProfile_Ut1 = _LoadSelectProfile_Ut1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 14),
    _LoadSelectProfile_Ut1_Type()
)
loadSelectProfile_Ut1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Ut1.setStatus("mandatory")


class _LoadSelectProfile_Ue1_Type(Integer32):
    """Custom type loadSelectProfile_Ue1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Ue1_Type.__name__ = "Integer32"
_LoadSelectProfile_Ue1_Object = MibScalar
loadSelectProfile_Ue1 = _LoadSelectProfile_Ue1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 15),
    _LoadSelectProfile_Ue1_Type()
)
loadSelectProfile_Ue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Ue1.setStatus("mandatory")


class _LoadSelectProfile_Uds3_Type(Integer32):
    """Custom type loadSelectProfile_Uds3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Uds3_Type.__name__ = "Integer32"
_LoadSelectProfile_Uds3_Object = MibScalar
loadSelectProfile_Uds3 = _LoadSelectProfile_Uds3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 16),
    _LoadSelectProfile_Uds3_Type()
)
loadSelectProfile_Uds3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Uds3.setStatus("mandatory")


class _LoadSelectProfile_Ds3Atm_Type(Integer32):
    """Custom type loadSelectProfile_Ds3Atm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Ds3Atm_Type.__name__ = "Integer32"
_LoadSelectProfile_Ds3Atm_Object = MibScalar
loadSelectProfile_Ds3Atm = _LoadSelectProfile_Ds3Atm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 17),
    _LoadSelectProfile_Ds3Atm_Type()
)
loadSelectProfile_Ds3Atm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Ds3Atm.setStatus("mandatory")


class _LoadSelectProfile_Enet2_Type(Integer32):
    """Custom type loadSelectProfile_Enet2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Enet2_Type.__name__ = "Integer32"
_LoadSelectProfile_Enet2_Object = MibScalar
loadSelectProfile_Enet2 = _LoadSelectProfile_Enet2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 19),
    _LoadSelectProfile_Enet2_Type()
)
loadSelectProfile_Enet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Enet2.setStatus("mandatory")


class _LoadSelectProfile_Enet3_Type(Integer32):
    """Custom type loadSelectProfile_Enet3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Enet3_Type.__name__ = "Integer32"
_LoadSelectProfile_Enet3_Object = MibScalar
loadSelectProfile_Enet3 = _LoadSelectProfile_Enet3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 20),
    _LoadSelectProfile_Enet3_Type()
)
loadSelectProfile_Enet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Enet3.setStatus("mandatory")


class _LoadSelectProfile_Enet3nd_Type(Integer32):
    """Custom type loadSelectProfile_Enet3nd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Enet3nd_Type.__name__ = "Integer32"
_LoadSelectProfile_Enet3nd_Object = MibScalar
loadSelectProfile_Enet3nd = _LoadSelectProfile_Enet3nd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 21),
    _LoadSelectProfile_Enet3nd_Type()
)
loadSelectProfile_Enet3nd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Enet3nd.setStatus("mandatory")


class _LoadSelectProfile_EtherDual_Type(Integer32):
    """Custom type loadSelectProfile_EtherDual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_EtherDual_Type.__name__ = "Integer32"
_LoadSelectProfile_EtherDual_Object = MibScalar
loadSelectProfile_EtherDual = _LoadSelectProfile_EtherDual_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 22),
    _LoadSelectProfile_EtherDual_Type()
)
loadSelectProfile_EtherDual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_EtherDual.setStatus("mandatory")


class _LoadSelectProfile_SrsEther_Type(Integer32):
    """Custom type loadSelectProfile_SrsEther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_SrsEther_Type.__name__ = "Integer32"
_LoadSelectProfile_SrsEther_Object = MibScalar
loadSelectProfile_SrsEther = _LoadSelectProfile_SrsEther_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 23),
    _LoadSelectProfile_SrsEther_Type()
)
loadSelectProfile_SrsEther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_SrsEther.setStatus("mandatory")


class _LoadSelectProfile_MdmV34_Type(Integer32):
    """Custom type loadSelectProfile_MdmV34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_MdmV34_Type.__name__ = "Integer32"
_LoadSelectProfile_MdmV34_Object = MibScalar
loadSelectProfile_MdmV34 = _LoadSelectProfile_MdmV34_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 24),
    _LoadSelectProfile_MdmV34_Type()
)
loadSelectProfile_MdmV34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_MdmV34.setStatus("mandatory")


class _LoadSelectProfile_Mdm56k_Type(Integer32):
    """Custom type loadSelectProfile_Mdm56k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Mdm56k_Type.__name__ = "Integer32"
_LoadSelectProfile_Mdm56k_Object = MibScalar
loadSelectProfile_Mdm56k = _LoadSelectProfile_Mdm56k_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 25),
    _LoadSelectProfile_Mdm56k_Type()
)
loadSelectProfile_Mdm56k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Mdm56k.setStatus("mandatory")


class _LoadSelectProfile_Amdm_Type(Integer32):
    """Custom type loadSelectProfile_Amdm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Amdm_Type.__name__ = "Integer32"
_LoadSelectProfile_Amdm_Object = MibScalar
loadSelectProfile_Amdm = _LoadSelectProfile_Amdm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 26),
    _LoadSelectProfile_Amdm_Type()
)
loadSelectProfile_Amdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Amdm.setStatus("mandatory")


class _LoadSelectProfile_Anmdm_Type(Integer32):
    """Custom type loadSelectProfile_Anmdm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Anmdm_Type.__name__ = "Integer32"
_LoadSelectProfile_Anmdm_Object = MibScalar
loadSelectProfile_Anmdm = _LoadSelectProfile_Anmdm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 27),
    _LoadSelectProfile_Anmdm_Type()
)
loadSelectProfile_Anmdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Anmdm.setStatus("mandatory")


class _LoadSelectProfile_Csmx_Type(Integer32):
    """Custom type loadSelectProfile_Csmx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Csmx_Type.__name__ = "Integer32"
_LoadSelectProfile_Csmx_Object = MibScalar
loadSelectProfile_Csmx = _LoadSelectProfile_Csmx_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 28),
    _LoadSelectProfile_Csmx_Type()
)
loadSelectProfile_Csmx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Csmx.setStatus("mandatory")


class _LoadSelectProfile_Madd_Type(Integer32):
    """Custom type loadSelectProfile_Madd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Madd_Type.__name__ = "Integer32"
_LoadSelectProfile_Madd_Object = MibScalar
loadSelectProfile_Madd = _LoadSelectProfile_Madd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 29),
    _LoadSelectProfile_Madd_Type()
)
loadSelectProfile_Madd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Madd.setStatus("mandatory")


class _LoadSelectProfile_Csm3v_Type(Integer32):
    """Custom type loadSelectProfile_Csm3v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Csm3v_Type.__name__ = "Integer32"
_LoadSelectProfile_Csm3v_Object = MibScalar
loadSelectProfile_Csm3v = _LoadSelectProfile_Csm3v_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 30),
    _LoadSelectProfile_Csm3v_Type()
)
loadSelectProfile_Csm3v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Csm3v.setStatus("mandatory")


class _LoadSelectProfile_Madd3_Type(Integer32):
    """Custom type loadSelectProfile_Madd3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Madd3_Type.__name__ = "Integer32"
_LoadSelectProfile_Madd3_Object = MibScalar
loadSelectProfile_Madd3 = _LoadSelectProfile_Madd3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 31),
    _LoadSelectProfile_Madd3_Type()
)
loadSelectProfile_Madd3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Madd3.setStatus("mandatory")


class _LoadSelectProfile_Hdlc2_Type(Integer32):
    """Custom type loadSelectProfile_Hdlc2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Hdlc2_Type.__name__ = "Integer32"
_LoadSelectProfile_Hdlc2_Object = MibScalar
loadSelectProfile_Hdlc2 = _LoadSelectProfile_Hdlc2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 33),
    _LoadSelectProfile_Hdlc2_Type()
)
loadSelectProfile_Hdlc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Hdlc2.setStatus("mandatory")


class _LoadSelectProfile_Hdlc2ec_Type(Integer32):
    """Custom type loadSelectProfile_Hdlc2ec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Hdlc2ec_Type.__name__ = "Integer32"
_LoadSelectProfile_Hdlc2ec_Object = MibScalar
loadSelectProfile_Hdlc2ec = _LoadSelectProfile_Hdlc2ec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 34),
    _LoadSelectProfile_Hdlc2ec_Type()
)
loadSelectProfile_Hdlc2ec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Hdlc2ec.setStatus("mandatory")


class _LoadSelectProfile_Swan_Type(Integer32):
    """Custom type loadSelectProfile_Swan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Swan_Type.__name__ = "Integer32"
_LoadSelectProfile_Swan_Object = MibScalar
loadSelectProfile_Swan = _LoadSelectProfile_Swan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 35),
    _LoadSelectProfile_Swan_Type()
)
loadSelectProfile_Swan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Swan.setStatus("mandatory")


class _LoadSelectProfile_Hssi_Type(Integer32):
    """Custom type loadSelectProfile_Hssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Hssi_Type.__name__ = "Integer32"
_LoadSelectProfile_Hssi_Object = MibScalar
loadSelectProfile_Hssi = _LoadSelectProfile_Hssi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 36),
    _LoadSelectProfile_Hssi_Type()
)
loadSelectProfile_Hssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Hssi.setStatus("mandatory")


class _LoadSelectProfile_Idsl_Type(Integer32):
    """Custom type loadSelectProfile_Idsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Idsl_Type.__name__ = "Integer32"
_LoadSelectProfile_Idsl_Object = MibScalar
loadSelectProfile_Idsl = _LoadSelectProfile_Idsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 37),
    _LoadSelectProfile_Idsl_Type()
)
loadSelectProfile_Idsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Idsl.setStatus("mandatory")


class _LoadSelectProfile_Capadsl_Type(Integer32):
    """Custom type loadSelectProfile_Capadsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Capadsl_Type.__name__ = "Integer32"
_LoadSelectProfile_Capadsl_Object = MibScalar
loadSelectProfile_Capadsl = _LoadSelectProfile_Capadsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 38),
    _LoadSelectProfile_Capadsl_Type()
)
loadSelectProfile_Capadsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Capadsl.setStatus("mandatory")


class _LoadSelectProfile_Dmtadsl_Type(Integer32):
    """Custom type loadSelectProfile_Dmtadsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Dmtadsl_Type.__name__ = "Integer32"
_LoadSelectProfile_Dmtadsl_Object = MibScalar
loadSelectProfile_Dmtadsl = _LoadSelectProfile_Dmtadsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 39),
    _LoadSelectProfile_Dmtadsl_Type()
)
loadSelectProfile_Dmtadsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Dmtadsl.setStatus("mandatory")


class _LoadSelectProfile_Sdsl_Type(Integer32):
    """Custom type loadSelectProfile_Sdsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Sdsl_Type.__name__ = "Integer32"
_LoadSelectProfile_Sdsl_Object = MibScalar
loadSelectProfile_Sdsl = _LoadSelectProfile_Sdsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 40),
    _LoadSelectProfile_Sdsl_Type()
)
loadSelectProfile_Sdsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Sdsl.setStatus("mandatory")


class _LoadSelectProfile_Sdsl70d_Type(Integer32):
    """Custom type loadSelectProfile_Sdsl70d based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Sdsl70d_Type.__name__ = "Integer32"
_LoadSelectProfile_Sdsl70d_Object = MibScalar
loadSelectProfile_Sdsl70d = _LoadSelectProfile_Sdsl70d_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 41),
    _LoadSelectProfile_Sdsl70d_Type()
)
loadSelectProfile_Sdsl70d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Sdsl70d.setStatus("mandatory")


class _LoadSelectProfile_Sdsl70v_Type(Integer32):
    """Custom type loadSelectProfile_Sdsl70v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Sdsl70v_Type.__name__ = "Integer32"
_LoadSelectProfile_Sdsl70v_Object = MibScalar
loadSelectProfile_Sdsl70v = _LoadSelectProfile_Sdsl70v_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 42),
    _LoadSelectProfile_Sdsl70v_Type()
)
loadSelectProfile_Sdsl70v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Sdsl70v.setStatus("mandatory")


class _LoadSelectProfile_Oc3Atm_Type(Integer32):
    """Custom type loadSelectProfile_Oc3Atm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Oc3Atm_Type.__name__ = "Integer32"
_LoadSelectProfile_Oc3Atm_Object = MibScalar
loadSelectProfile_Oc3Atm = _LoadSelectProfile_Oc3Atm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 43),
    _LoadSelectProfile_Oc3Atm_Type()
)
loadSelectProfile_Oc3Atm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Oc3Atm.setStatus("mandatory")


class _LoadSelectProfile_SdslAtm_Type(Integer32):
    """Custom type loadSelectProfile_SdslAtm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_SdslAtm_Type.__name__ = "Integer32"
_LoadSelectProfile_SdslAtm_Object = MibScalar
loadSelectProfile_SdslAtm = _LoadSelectProfile_SdslAtm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 44),
    _LoadSelectProfile_SdslAtm_Type()
)
loadSelectProfile_SdslAtm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_SdslAtm.setStatus("mandatory")


class _LoadSelectProfile_AlDmtadslAtm_Type(Integer32):
    """Custom type loadSelectProfile_AlDmtadslAtm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_AlDmtadslAtm_Type.__name__ = "Integer32"
_LoadSelectProfile_AlDmtadslAtm_Object = MibScalar
loadSelectProfile_AlDmtadslAtm = _LoadSelectProfile_AlDmtadslAtm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 45),
    _LoadSelectProfile_AlDmtadslAtm_Type()
)
loadSelectProfile_AlDmtadslAtm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_AlDmtadslAtm.setStatus("mandatory")


class _LoadSelectProfile_SdslAtmV2_Type(Integer32):
    """Custom type loadSelectProfile_SdslAtmV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_SdslAtmV2_Type.__name__ = "Integer32"
_LoadSelectProfile_SdslAtmV2_Object = MibScalar
loadSelectProfile_SdslAtmV2 = _LoadSelectProfile_SdslAtmV2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 46),
    _LoadSelectProfile_SdslAtmV2_Type()
)
loadSelectProfile_SdslAtmV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_SdslAtmV2.setStatus("mandatory")


class _LoadSelectProfile_DadslAtm24_Type(Integer32):
    """Custom type loadSelectProfile_DadslAtm24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_DadslAtm24_Type.__name__ = "Integer32"
_LoadSelectProfile_DadslAtm24_Object = MibScalar
loadSelectProfile_DadslAtm24 = _LoadSelectProfile_DadslAtm24_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 47),
    _LoadSelectProfile_DadslAtm24_Type()
)
loadSelectProfile_DadslAtm24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_DadslAtm24.setStatus("mandatory")


class _LoadSelectProfile_GliteAtm48_Type(Integer32):
    """Custom type loadSelectProfile_GliteAtm48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_GliteAtm48_Type.__name__ = "Integer32"
_LoadSelectProfile_GliteAtm48_Object = MibScalar
loadSelectProfile_GliteAtm48 = _LoadSelectProfile_GliteAtm48_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 48),
    _LoadSelectProfile_GliteAtm48_Type()
)
loadSelectProfile_GliteAtm48.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_GliteAtm48.setStatus("mandatory")


class _LoadSelectProfile_Hdsl2_Type(Integer32):
    """Custom type loadSelectProfile_Hdsl2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Hdsl2_Type.__name__ = "Integer32"
_LoadSelectProfile_Hdsl2_Object = MibScalar
loadSelectProfile_Hdsl2 = _LoadSelectProfile_Hdsl2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 49),
    _LoadSelectProfile_Hdsl2_Type()
)
loadSelectProfile_Hdsl2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Hdsl2.setStatus("mandatory")


class _LoadSelectProfile_AnnexbDmtadsl_Type(Integer32):
    """Custom type loadSelectProfile_AnnexbDmtadsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_AnnexbDmtadsl_Type.__name__ = "Integer32"
_LoadSelectProfile_AnnexbDmtadsl_Object = MibScalar
loadSelectProfile_AnnexbDmtadsl = _LoadSelectProfile_AnnexbDmtadsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 50),
    _LoadSelectProfile_AnnexbDmtadsl_Type()
)
loadSelectProfile_AnnexbDmtadsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_AnnexbDmtadsl.setStatus("mandatory")


class _LoadSelectProfile_T1000_Type(Integer32):
    """Custom type loadSelectProfile_T1000 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_T1000_Type.__name__ = "Integer32"
_LoadSelectProfile_T1000_Object = MibScalar
loadSelectProfile_T1000 = _LoadSelectProfile_T1000_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 51),
    _LoadSelectProfile_T1000_Type()
)
loadSelectProfile_T1000.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_T1000.setStatus("mandatory")


class _LoadSelectProfile_Ima_Type(Integer32):
    """Custom type loadSelectProfile_Ima based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Ima_Type.__name__ = "Integer32"
_LoadSelectProfile_Ima_Object = MibScalar
loadSelectProfile_Ima = _LoadSelectProfile_Ima_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 52),
    _LoadSelectProfile_Ima_Type()
)
loadSelectProfile_Ima.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Ima.setStatus("mandatory")


class _LoadSelectProfile_Stngr32Idsl_Type(Integer32):
    """Custom type loadSelectProfile_Stngr32Idsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Stngr32Idsl_Type.__name__ = "Integer32"
_LoadSelectProfile_Stngr32Idsl_Object = MibScalar
loadSelectProfile_Stngr32Idsl = _LoadSelectProfile_Stngr32Idsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 53),
    _LoadSelectProfile_Stngr32Idsl_Type()
)
loadSelectProfile_Stngr32Idsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Stngr32Idsl.setStatus("mandatory")


class _LoadSelectProfile_o40DmtAdsl_Type(Integer32):
    """Custom type loadSelectProfile_o40DmtAdsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o40DmtAdsl_Type.__name__ = "Integer32"
_LoadSelectProfile_o40DmtAdsl_Object = MibScalar
loadSelectProfile_o40DmtAdsl = _LoadSelectProfile_o40DmtAdsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 54),
    _LoadSelectProfile_o40DmtAdsl_Type()
)
loadSelectProfile_o40DmtAdsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o40DmtAdsl.setStatus("mandatory")


class _LoadSelectProfile_o48DmtAdsl_Type(Integer32):
    """Custom type loadSelectProfile_o48DmtAdsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o48DmtAdsl_Type.__name__ = "Integer32"
_LoadSelectProfile_o48DmtAdsl_Object = MibScalar
loadSelectProfile_o48DmtAdsl = _LoadSelectProfile_o48DmtAdsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 55),
    _LoadSelectProfile_o48DmtAdsl_Type()
)
loadSelectProfile_o48DmtAdsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o48DmtAdsl.setStatus("mandatory")


class _LoadSelectProfile_Ds3Atm2_Type(Integer32):
    """Custom type loadSelectProfile_Ds3Atm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Ds3Atm2_Type.__name__ = "Integer32"
_LoadSelectProfile_Ds3Atm2_Object = MibScalar
loadSelectProfile_Ds3Atm2 = _LoadSelectProfile_Ds3Atm2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 56),
    _LoadSelectProfile_Ds3Atm2_Type()
)
loadSelectProfile_Ds3Atm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Ds3Atm2.setStatus("mandatory")


class _LoadSelectProfile_E3Atm_Type(Integer32):
    """Custom type loadSelectProfile_E3Atm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_E3Atm_Type.__name__ = "Integer32"
_LoadSelectProfile_E3Atm_Object = MibScalar
loadSelectProfile_E3Atm = _LoadSelectProfile_E3Atm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 57),
    _LoadSelectProfile_E3Atm_Type()
)
loadSelectProfile_E3Atm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_E3Atm.setStatus("mandatory")


class _LoadSelectProfile_Oc3Atm2_Type(Integer32):
    """Custom type loadSelectProfile_Oc3Atm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Oc3Atm2_Type.__name__ = "Integer32"
_LoadSelectProfile_Oc3Atm2_Object = MibScalar
loadSelectProfile_Oc3Atm2 = _LoadSelectProfile_Oc3Atm2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 58),
    _LoadSelectProfile_Oc3Atm2_Type()
)
loadSelectProfile_Oc3Atm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Oc3Atm2.setStatus("mandatory")


class _LoadSelectProfile_Vpn_Type(Integer32):
    """Custom type loadSelectProfile_Vpn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Vpn_Type.__name__ = "Integer32"
_LoadSelectProfile_Vpn_Object = MibScalar
loadSelectProfile_Vpn = _LoadSelectProfile_Vpn_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 59),
    _LoadSelectProfile_Vpn_Type()
)
loadSelectProfile_Vpn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Vpn.setStatus("mandatory")


class _LoadSelectProfile_Swan2_Type(Integer32):
    """Custom type loadSelectProfile_Swan2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Swan2_Type.__name__ = "Integer32"
_LoadSelectProfile_Swan2_Object = MibScalar
loadSelectProfile_Swan2 = _LoadSelectProfile_Swan2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 60),
    _LoadSelectProfile_Swan2_Type()
)
loadSelectProfile_Swan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Swan2.setStatus("mandatory")


class _LoadSelectProfile_Action_o_Type(Integer32):
    """Custom type loadSelectProfile_Action_o based on Integer32"""
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


_LoadSelectProfile_Action_o_Type.__name__ = "Integer32"
_LoadSelectProfile_Action_o_Object = MibScalar
loadSelectProfile_Action_o = _LoadSelectProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 61),
    _LoadSelectProfile_Action_o_Type()
)
loadSelectProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Action_o.setStatus("mandatory")


class _LoadSelectProfile_o72Shdsl_Type(Integer32):
    """Custom type loadSelectProfile_o72Shdsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o72Shdsl_Type.__name__ = "Integer32"
_LoadSelectProfile_o72Shdsl_Object = MibScalar
loadSelectProfile_o72Shdsl = _LoadSelectProfile_o72Shdsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 62),
    _LoadSelectProfile_o72Shdsl_Type()
)
loadSelectProfile_o72Shdsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o72Shdsl.setStatus("mandatory")


class _LoadSelectProfile_o24t1_Type(Integer32):
    """Custom type loadSelectProfile_o24t1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o24t1_Type.__name__ = "Integer32"
_LoadSelectProfile_o24t1_Object = MibScalar
loadSelectProfile_o24t1 = _LoadSelectProfile_o24t1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 64),
    _LoadSelectProfile_o24t1_Type()
)
loadSelectProfile_o24t1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o24t1.setStatus("mandatory")


class _LoadSelectProfile_o24e1_Type(Integer32):
    """Custom type loadSelectProfile_o24e1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o24e1_Type.__name__ = "Integer32"
_LoadSelectProfile_o24e1_Object = MibScalar
loadSelectProfile_o24e1 = _LoadSelectProfile_o24e1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 65),
    _LoadSelectProfile_o24e1_Type()
)
loadSelectProfile_o24e1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o24e1.setStatus("mandatory")


class _LoadSelectProfile_AtmHse_Type(Integer32):
    """Custom type loadSelectProfile_AtmHse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_AtmHse_Type.__name__ = "Integer32"
_LoadSelectProfile_AtmHse_Object = MibScalar
loadSelectProfile_AtmHse = _LoadSelectProfile_AtmHse_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 68),
    _LoadSelectProfile_AtmHse_Type()
)
loadSelectProfile_AtmHse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_AtmHse.setStatus("mandatory")


class _LoadSelectProfile_EnetHse_Type(Integer32):
    """Custom type loadSelectProfile_EnetHse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_EnetHse_Type.__name__ = "Integer32"
_LoadSelectProfile_EnetHse_Object = MibScalar
loadSelectProfile_EnetHse = _LoadSelectProfile_EnetHse_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 69),
    _LoadSelectProfile_EnetHse_Type()
)
loadSelectProfile_EnetHse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_EnetHse.setStatus("mandatory")


class _LoadSelectProfile_o32DmtAslam_Type(Integer32):
    """Custom type loadSelectProfile_o32DmtAslam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o32DmtAslam_Type.__name__ = "Integer32"
_LoadSelectProfile_o32DmtAslam_Object = MibScalar
loadSelectProfile_o32DmtAslam = _LoadSelectProfile_o32DmtAslam_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 70),
    _LoadSelectProfile_o32DmtAslam_Type()
)
loadSelectProfile_o32DmtAslam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o32DmtAslam.setStatus("mandatory")


class _LoadSelectProfile_Vdsl_Type(Integer32):
    """Custom type loadSelectProfile_Vdsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Vdsl_Type.__name__ = "Integer32"
_LoadSelectProfile_Vdsl_Object = MibScalar
loadSelectProfile_Vdsl = _LoadSelectProfile_Vdsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 71),
    _LoadSelectProfile_Vdsl_Type()
)
loadSelectProfile_Vdsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Vdsl.setStatus("mandatory")


class _LoadSelectProfile_Cln_Type(Integer32):
    """Custom type loadSelectProfile_Cln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Cln_Type.__name__ = "Integer32"
_LoadSelectProfile_Cln_Object = MibScalar
loadSelectProfile_Cln = _LoadSelectProfile_Cln_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 72),
    _LoadSelectProfile_Cln_Type()
)
loadSelectProfile_Cln.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Cln.setStatus("mandatory")


class _LoadSelectProfile_Alpmt_Type(Integer32):
    """Custom type loadSelectProfile_Alpmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Alpmt_Type.__name__ = "Integer32"
_LoadSelectProfile_Alpmt_Object = MibScalar
loadSelectProfile_Alpmt = _LoadSelectProfile_Alpmt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 75),
    _LoadSelectProfile_Alpmt_Type()
)
loadSelectProfile_Alpmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Alpmt.setStatus("mandatory")


class _LoadSelectProfile_Alpme_Type(Integer32):
    """Custom type loadSelectProfile_Alpme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Alpme_Type.__name__ = "Integer32"
_LoadSelectProfile_Alpme_Object = MibScalar
loadSelectProfile_Alpme = _LoadSelectProfile_Alpme_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 76),
    _LoadSelectProfile_Alpme_Type()
)
loadSelectProfile_Alpme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Alpme.setStatus("mandatory")


class _LoadSelectProfile_o72CtDmtAdsl_Type(Integer32):
    """Custom type loadSelectProfile_o72CtDmtAdsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_o72CtDmtAdsl_Type.__name__ = "Integer32"
_LoadSelectProfile_o72CtDmtAdsl_Object = MibScalar
loadSelectProfile_o72CtDmtAdsl = _LoadSelectProfile_o72CtDmtAdsl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 77),
    _LoadSelectProfile_o72CtDmtAdsl_Type()
)
loadSelectProfile_o72CtDmtAdsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_o72CtDmtAdsl.setStatus("mandatory")


class _LoadSelectProfile_Apxenet_Type(Integer32):
    """Custom type loadSelectProfile_Apxenet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("load", 2),
          ("skip", 3))
    )


_LoadSelectProfile_Apxenet_Type.__name__ = "Integer32"
_LoadSelectProfile_Apxenet_Object = MibScalar
loadSelectProfile_Apxenet = _LoadSelectProfile_Apxenet_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 82),
    _LoadSelectProfile_Apxenet_Type()
)
loadSelectProfile_Apxenet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadSelectProfile_Apxenet.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBLOADSELECT-MIB",
    **{"DisplayString": DisplayString,
       "mibloadSelectProfile": mibloadSelectProfile,
       "mibloadSelectProfileTable": mibloadSelectProfileTable,
       "mibloadSelectProfileEntry": mibloadSelectProfileEntry,
       "loadSelectProfile-Index-o": loadSelectProfile_Index_o,
       "loadSelectProfile-UnknownCards": loadSelectProfile_UnknownCards,
       "loadSelectProfile-Sr": loadSelectProfile_Sr,
       "loadSelectProfile-Sr2": loadSelectProfile_Sr2,
       "loadSelectProfile-Apxsr": loadSelectProfile_Apxsr,
       "loadSelectProfile-o8t1": loadSelectProfile_o8t1,
       "loadSelectProfile-o8e1": loadSelectProfile_o8e1,
       "loadSelectProfile-T3": loadSelectProfile_T3,
       "loadSelectProfile-Stm0": loadSelectProfile_Stm0,
       "loadSelectProfile-Pctfit": loadSelectProfile_Pctfit,
       "loadSelectProfile-Pctfie": loadSelectProfile_Pctfie,
       "loadSelectProfile-Clpmt": loadSelectProfile_Clpmt,
       "loadSelectProfile-Clpme": loadSelectProfile_Clpme,
       "loadSelectProfile-Ut1": loadSelectProfile_Ut1,
       "loadSelectProfile-Ue1": loadSelectProfile_Ue1,
       "loadSelectProfile-Uds3": loadSelectProfile_Uds3,
       "loadSelectProfile-Ds3Atm": loadSelectProfile_Ds3Atm,
       "loadSelectProfile-Enet2": loadSelectProfile_Enet2,
       "loadSelectProfile-Enet3": loadSelectProfile_Enet3,
       "loadSelectProfile-Enet3nd": loadSelectProfile_Enet3nd,
       "loadSelectProfile-EtherDual": loadSelectProfile_EtherDual,
       "loadSelectProfile-SrsEther": loadSelectProfile_SrsEther,
       "loadSelectProfile-MdmV34": loadSelectProfile_MdmV34,
       "loadSelectProfile-Mdm56k": loadSelectProfile_Mdm56k,
       "loadSelectProfile-Amdm": loadSelectProfile_Amdm,
       "loadSelectProfile-Anmdm": loadSelectProfile_Anmdm,
       "loadSelectProfile-Csmx": loadSelectProfile_Csmx,
       "loadSelectProfile-Madd": loadSelectProfile_Madd,
       "loadSelectProfile-Csm3v": loadSelectProfile_Csm3v,
       "loadSelectProfile-Madd3": loadSelectProfile_Madd3,
       "loadSelectProfile-Hdlc2": loadSelectProfile_Hdlc2,
       "loadSelectProfile-Hdlc2ec": loadSelectProfile_Hdlc2ec,
       "loadSelectProfile-Swan": loadSelectProfile_Swan,
       "loadSelectProfile-Hssi": loadSelectProfile_Hssi,
       "loadSelectProfile-Idsl": loadSelectProfile_Idsl,
       "loadSelectProfile-Capadsl": loadSelectProfile_Capadsl,
       "loadSelectProfile-Dmtadsl": loadSelectProfile_Dmtadsl,
       "loadSelectProfile-Sdsl": loadSelectProfile_Sdsl,
       "loadSelectProfile-Sdsl70d": loadSelectProfile_Sdsl70d,
       "loadSelectProfile-Sdsl70v": loadSelectProfile_Sdsl70v,
       "loadSelectProfile-Oc3Atm": loadSelectProfile_Oc3Atm,
       "loadSelectProfile-SdslAtm": loadSelectProfile_SdslAtm,
       "loadSelectProfile-AlDmtadslAtm": loadSelectProfile_AlDmtadslAtm,
       "loadSelectProfile-SdslAtmV2": loadSelectProfile_SdslAtmV2,
       "loadSelectProfile-DadslAtm24": loadSelectProfile_DadslAtm24,
       "loadSelectProfile-GliteAtm48": loadSelectProfile_GliteAtm48,
       "loadSelectProfile-Hdsl2": loadSelectProfile_Hdsl2,
       "loadSelectProfile-AnnexbDmtadsl": loadSelectProfile_AnnexbDmtadsl,
       "loadSelectProfile-T1000": loadSelectProfile_T1000,
       "loadSelectProfile-Ima": loadSelectProfile_Ima,
       "loadSelectProfile-Stngr32Idsl": loadSelectProfile_Stngr32Idsl,
       "loadSelectProfile-o40DmtAdsl": loadSelectProfile_o40DmtAdsl,
       "loadSelectProfile-o48DmtAdsl": loadSelectProfile_o48DmtAdsl,
       "loadSelectProfile-Ds3Atm2": loadSelectProfile_Ds3Atm2,
       "loadSelectProfile-E3Atm": loadSelectProfile_E3Atm,
       "loadSelectProfile-Oc3Atm2": loadSelectProfile_Oc3Atm2,
       "loadSelectProfile-Vpn": loadSelectProfile_Vpn,
       "loadSelectProfile-Swan2": loadSelectProfile_Swan2,
       "loadSelectProfile-Action-o": loadSelectProfile_Action_o,
       "loadSelectProfile-o72Shdsl": loadSelectProfile_o72Shdsl,
       "loadSelectProfile-o24t1": loadSelectProfile_o24t1,
       "loadSelectProfile-o24e1": loadSelectProfile_o24e1,
       "loadSelectProfile-AtmHse": loadSelectProfile_AtmHse,
       "loadSelectProfile-EnetHse": loadSelectProfile_EnetHse,
       "loadSelectProfile-o32DmtAslam": loadSelectProfile_o32DmtAslam,
       "loadSelectProfile-Vdsl": loadSelectProfile_Vdsl,
       "loadSelectProfile-Cln": loadSelectProfile_Cln,
       "loadSelectProfile-Alpmt": loadSelectProfile_Alpmt,
       "loadSelectProfile-Alpme": loadSelectProfile_Alpme,
       "loadSelectProfile-o72CtDmtAdsl": loadSelectProfile_o72CtDmtAdsl,
       "loadSelectProfile-Apxenet": loadSelectProfile_Apxenet}
)
